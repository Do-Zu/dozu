"""Create a sanitized pinned snapshot; never import ancestry or local config.

Only writes missing target files (or identical files), so later workspace work
cannot be accidentally overwritten by rerunning the importer.
"""
import hashlib
import json
import re
import subprocess
from pathlib import Path

from preflight import ROOT, OUT, RULES, git

def sha(data):
    return hashlib.sha256(data).hexdigest()

def write_new(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        assert path.read_bytes() == data, f'Refusing to overwrite changed target: {path}'
    else:
        path.write_bytes(data)

def sanitize(repo, path, data):
    changes = []
    if repo == 'dozu-ui-service' and path == 'src/app/[locale]/auth/testBackEnd/page.tsx':
        # Keep the complete existing route and its profile action. Authentication
        # must come from the existing user session, never a bundled bearer token.
        s = data.decode('utf-8')
        s = s.replace("import Axios from '@/api/axios';\n", '')
        for line in ("import { updateAccessToken } from '@/stores/features/auth/authSlice';\n",
                     "import { useAppDispatch } from '@/stores/hooks';\n",
                     "import { useEffect } from 'react';\n"):
            s = s.replace(line, '')
        s, count = re.subn(r'  const dispatch = useAppDispatch\(\);\n  useEffect\(\(\) => \{.*?\n  \}, \[\]\);\n', '', s, flags=re.S)
        assert count == 1
        s = s.replace("Axios.get('/auth/profile')", "getRequest<unknown, unknown>('/auth/profile')")
        data = s.encode('utf-8')
        changes.append('Remove embedded JWT/session overwrite; retained profile action uses existing API wrapper/session. No route removed.')
    if repo == 'dozu-api-service' and path == 'containers/database/postgres/README.md':
        s = data.decode('utf-8')
        s, count = re.subn(RULES['credential-url'].decode(), '', s)
        assert count == 1
        # Replace the complete remaining URL/example with a variable reference.
        s = re.sub(r'(?m)^localhost:5434/dozu$', '${DATABASE_URL}', s)
        s = re.sub(r'(?m)^- \*\*Password\*\*: .*$', '- **Password**: set a local development password in your untracked environment', s)
        data = s.encode('utf-8')
        changes.append('Replace documented development password and credential URL with untracked local configuration reference; runtime unchanged.')
    return data, changes

def main():
    preflight = json.loads((OUT / 'preflight.json').read_text(encoding='utf-8'))
    result = {'strategy': 'sanitized HEAD snapshot; original history stays in original repositories',
              'historyImported': False, 'publicRedistributionCleared': False, 'repositories': []}
    for repo in preflight['repositories']:
        source = repo['source']
        assert git(source, 'rev-parse', 'HEAD').decode().strip() == repo['commit']
        assert not git(source, 'status', '--porcelain', '--untracked-files=no')
        payload = b''.join(f['gitBlob'].encode() + b'\n' for f in repo['files'])
        raw = subprocess.check_output(['git', '-C', str(ROOT / source), 'cat-file', '--batch'], input=payload)
        cursor = 0
        records, changes = [], []
        for f in repo['files']:
            end = raw.index(b'\n', cursor)
            oid, kind, size = raw[cursor:end].split()
            assert oid.decode() == f['gitBlob'] and kind == b'blob'
            cursor = end + 1
            original = raw[cursor:cursor + int(size)]
            cursor += int(size) + 1
            assert sha(original) == f['sha256']
            data, notes = sanitize(source, f['path'], original)
            for rule, pattern in RULES.items():
                assert not re.search(pattern, data), (source, f['path'], rule)
            destination = ROOT / repo['target'] / f['path']
            assert destination.resolve().is_relative_to((ROOT / repo['target']).resolve())
            write_new(destination, data)
            records.append(dict(path=f['path'], sourceBlob=f['gitBlob'], sourceSha256=f['sha256'],
                                importedSha256=sha(data), mode=f['mode'], bytes=len(data), sanitized=bool(notes)))
            if notes:
                changes.append(dict(path=f['path'], notes=notes, sourceSha256=f['sha256'], importedSha256=sha(data)))
        # History metadata only: no messages, historical file contents or env blobs.
        log = git(source, 'log', '--format=%H%x09%P%x09%aN%x09%aE%x09%aI%x09%cN%x09%cE%x09%cI', repo['commit']).decode('utf-8')
        authors = []
        for line in log.splitlines():
            fields = line.split('\t')
            assert len(fields) == 8
            authors.append(dict(zip(('commit','parents','author','authorEmail','authoredAt','committer','committerEmail','committedAt'), fields)))
        result['repositories'].append(dict(source=source, target=repo['target'], commit=repo['commit'],
            branch=repo['branch'], files=records, excluded=repo['excluded'], sanitation=changes,
            historyMetadata=authors, licensePaths=repo['licensePaths']))
        assert not git(source, 'status', '--porcelain', '--untracked-files=no')
    (OUT / 'import-manifest.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('Sanitized snapshots written:', [(r['target'], len(r['files'])) for r in result['repositories']])

if __name__ == '__main__':
    main()
