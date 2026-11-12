"""Verify source snapshot coverage, sanitation, retained assets and originals."""
import hashlib
import json
import re
import runpy
import subprocess
import sys
from pathlib import Path

from preflight import ROOT, OUT, RULES, excluded, git

def sha(data):
    return hashlib.sha256(data).hexdigest()

manifest = json.loads((OUT / 'import-manifest.json').read_text(encoding='utf-8'))
baseline_only = '--baseline-only' in sys.argv[1:]
sanitize = runpy.run_path(str(OUT / 'import-snapshot.py'))['sanitize']
report = {'sourceHistoryUnchanged': True, 'originalTrackedTreesClean': True,
          'mode': 'reconstruct immutable import baseline from pinned original blobs' if baseline_only else 'compare live imported tree against immutable baseline',
          'secretScanScope': 'All imported HEAD bytes, known provider/private-key/JWT/credential-URL patterns; no historical blobs or dotenv read. Heuristics are not a complete secret guarantee.',
          'allImportedKnownPatternFindings': [], 'additionalQuotedAssignmentReview': [],
          'repositories': []}
quoted = re.compile(rb'''(?i)(?:api[_-]?key|access[_-]?token|auth[_-]?token|password|secret)\s*[:=]\s*['"][^'"\r\n]{16,}['"]''')
for repo in manifest['repositories']:
    source, target = repo['source'], ROOT / repo['target']
    assert git(source, 'rev-parse', 'HEAD').decode().strip() == repo['commit']
    assert not git(source, 'status', '--porcelain', '--untracked-files=no')
    tree = git(source, 'ls-tree', '-rz', '--full-tree', repo['commit'])
    source_paths, source_modes = set(), {}
    for entry in tree.split(b'\0'):
        if not entry:
            continue
        meta, path = entry.split(b'\t', 1)
        path = path.decode('utf-8')
        source_paths.add(path)
        source_modes[path] = meta.decode().split()[0]
    imported = {f['path'] for f in repo['files']}
    omitted = {f['path'] for f in repo['excluded']}
    assert source_paths == imported | omitted and not imported & omitted
    assert all(excluded(p) for p in omitted)
    if not baseline_only:
        actual = {p.relative_to(target).as_posix() for p in target.rglob('*') if p.is_file()}
        assert actual == imported, (source, sorted(actual ^ imported))
    else:
        payload = b''.join(f['sourceBlob'].encode() + b'\n' for f in repo['files'])
        raw = subprocess.check_output(['git', '-C', str(ROOT / source), 'cat-file', '--batch'], input=payload)
        cursor = 0
    for f in repo['files']:
        if baseline_only:
            end = raw.index(b'\n', cursor)
            oid, kind, size = raw[cursor:end].split()
            assert oid.decode() == f['sourceBlob'] and kind == b'blob'
            cursor = end + 1
            original = raw[cursor:cursor + int(size)]
            cursor += int(size) + 1
            assert sha(original) == f['sourceSha256']
            data, _ = sanitize(source, f['path'], original)
        else:
            data = (target / f['path']).read_bytes()
        assert sha(data) == f['importedSha256'], f['path']
        assert source_modes[f['path']] == f['mode']
        assert f['sanitized'] or f['sourceSha256'] == f['importedSha256']
        assert not excluded(f['path']), f['path']
        for rule, pattern in RULES.items():
            if re.search(pattern, data):
                report['allImportedKnownPatternFindings'].append(dict(path=f"{repo['target']}/{f['path']}", rule=rule))
        if quoted.search(data):
            report['additionalQuotedAssignmentReview'].append(f"{repo['target']}/{f['path']}")
    if source == 'dozu-ui-service':
        pages = {p for p in source_paths if p.startswith('src/app/') and p.endswith('/page.tsx')}
        layouts = {p for p in source_paths if p.startswith('src/app/') and p.endswith('/layout.tsx')}
        assert pages <= imported and len(pages) == 84
        assert layouts <= imported and len(layouts) == 20
    else:
        pages, layouts = set(), set()
    report['repositories'].append(dict(source=source, target=repo['target'], trackedFiles=len(source_paths),
        importedFiles=len(imported), excludedFiles=len(omitted), completePathCoverage=True,
        pageCount=len(pages), layoutCount=len(layouts), exactByteParityExceptSanitation=True,
        sourceModesPreservedInManifest=True, executablePaths=[p for p,m in source_modes.items() if m=='100755'],
        guidancePaths=[p for p in imported if p=='AGENTS.md' or '/skills/' in p or p.startswith('.github/')],
        sanitationPaths=[f['path'] for f in repo['files'] if f['sanitized']]))
assert not report['allImportedKnownPatternFindings']
# Preserve the ignored migration series as historical input outside active apps.
db = json.loads((ROOT / 'planning/audit/database-inventory.json').read_text(encoding='utf-8'))
migrations = []
for migration in db['migrations']:
    path = ROOT / migration['source']
    assert path.resolve().is_relative_to((ROOT / 'dozu-api-service/drizzle').resolve())
    data = path.read_bytes()
    assert sha(data) == migration['sha256']
    for rule, pattern in RULES.items():
        assert not re.search(pattern, data), (path.name, rule)
    archived = OUT / 'legacy-migrations' / path.name
    archived.parent.mkdir(exist_ok=True)
    if archived.exists():
        assert archived.read_bytes() == data
    else:
        archived.write_bytes(data)
    migrations.append(dict(source=migration['source'], archive=archived.relative_to(ROOT).as_posix(), sha256=sha(data)))
assert len(migrations) == 20
report['legacyMigrations'] = migrations
report['legacyMigrationsActive'] = False
report['publicRedistributionCleared'] = False
(OUT / ('verification-baseline.json' if baseline_only else 'verification.json')).write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k not in ('repositories','legacyMigrations')}, indent=2))
print('Verified', sum(r['importedFiles'] for r in report['repositories']), 'files; 84 pages, 20 layouts; 20 archived SQL hashes match audit.')
