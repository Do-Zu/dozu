"""Inventory only imported tracked code/tooling, never original checkouts or local configuration."""
import collections
import hashlib
import json
from pathlib import Path
import re
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
tracked = subprocess.check_output(['git', 'ls-files', 'apps', 'services', 'tooling'], cwd=ROOT,
                                  text=True, encoding='utf-8').splitlines()
rules = {'cwd-dependent': r'process\.cwd\(', 'shell-execution': r'execSync|execFileSync|spawn\(',
         'windows-env-assignment': r'\bset NODE_ENV=',
         'mutable-file-operation': r'writeFile|mkdir|createWriteStream',
         'linux-only-speech-executable': r'vendor/whisper/whisper-cli',
         'model-download-or-unpinned-revision': r'from_pretrained|SentenceTransformer\('}
findings = []
for name in tracked:
    file = ROOT / name
    if file.suffix not in {'.ts', '.js', '.cjs', '.mjs', '.py', '.sh', '.ps1'}:
        continue
    raw = file.read_bytes()
    source = raw.decode('utf-16' if raw.startswith((b'\xff\xfe', b'\xfe\xff')) else 'utf-8-sig')
    for number, line in enumerate(source.splitlines(), 1):
        for category, pattern in rules.items():
            if re.search(pattern, line):
                findings.append({'file': name, 'line': number, 'category': category})
scripts = {str(f.relative_to(ROOT)).replace('\\', '/'): json.loads(f.read_text(encoding='utf-8'))['scripts']
           for f in [ROOT / 'package.json', ROOT / 'apps/api/package.json', ROOT / 'apps/web/package.json']}
report = {'scope': 'Imported apps, services and tooling; tracked source files only',
          'scripts': scripts, 'findings': findings,
          'classification': {
              'portable-build': 'cross-env, rimraf, local pinned CLI executables, Node path joins',
              'desktop-data': 'DOZU_DATA_DIR absolute inherited setting; website cwd default retained',
              'legacy-developer-only': 'Lambda AWS CLI/Node20 deployment commands, Docker Compose and zip utilities are not desktop dependencies',
              'legacy-invalid': 'db:migrate:docker still uses obsolete push:pg with missing dist/db/schema.js; never used by root build/package',
              'deferred-speech': 'whisper CLI paths/scripts retained as source history; no v1 packaging/startup certification',
              'unpassed': 'Embedding Python image/requirements/model revision and resource cache remain unpinned; no immutable native runtime manifest exists'},
          'lockSha256': hashlib.sha256((ROOT / 'pnpm-lock.yaml').read_bytes()).hexdigest()}
(HERE / 'inventory.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')

def lint_diagnostics(file):
    current = ''
    counts = collections.Counter()
    for line in file.read_text(encoding='utf-8').splitlines():
        if re.match(r'^[A-Z]:', line):
            current = line.replace('\\', '/')
        match = re.match(r'\s*\d+:\d+\s+(error|warning)\s+(.*?)\s{2,}(\S+)\s*$', line)
        if match:
            counts[(current, *match.groups())] += 1
    return counts
before = lint_diagnostics(HERE.parent / 'workspace/api-lint.log')
after = lint_diagnostics(HERE / 'api-lint.log')
lint = {'addedDiagnostics': list((after - before).elements()),
        'removedDiagnostics': list((before - after).elements()),
        'note': 'Ignores diagnostic line shifts; full lint still fails with 100 errors/143 warnings'}
(HERE / 'lint-comparison.json').write_text(json.dumps(lint, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'inventoryFindings': len(findings), 'lint': lint}))
