"""Inventory pinned source blobs without reading dotenv or importing Git history.

Findings contain paths/rule names only. This is a bounded heuristic scan, not
redistribution clearance or a complete history secret audit.
"""
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
SOURCES = {'dozu-ui-service': 'apps/web', 'dozu-api-service': 'apps/api',
           'dozu-embedding-service': 'services/embedding'}
RULES = {
    'private-key': rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
    'github-token': rb'\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,})',
    'aws-access-key': rb'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b',
    'google-api-key': rb'\bAIza[A-Za-z0-9_-]{30,}',
    'jwt-literal': rb'\beyJ[A-Za-z0-9_-]{15,}\.[A-Za-z0-9_-]{15,}\.[A-Za-z0-9_-]{15,}',
    'credential-url': rb'[a-z]+://[^\s/:@]+:[^\s/@]+@',
}

def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(ROOT / repo), *args])

def excluded(path):
    p = Path(path)
    if any(x in {'.git', 'node_modules', '.venv', 'venv', '__pycache__', '.next',
                 'dist', 'build', 'logs', '.cache'} for x in p.parts):
        return 'local/generated directory'
    if p.parts[0] == 'uploads':
        return 'root runtime uploads directory'
    if p.name.startswith('.env') or p.name in {'.npmrc', '.pypirc', 'token-githubs.txt'}:
        return 'credential/config path (contents unread)'
    if p.suffix.lower() in {'.pem', '.key', '.p12', '.pfx', '.db', '.sqlite', '.dump', '.log', '.pyc'}:
        return 'credential/data/generated file'
    return None

def main():
    result = {'historyImported': False, 'sourceModified': False,
              'scope': 'HEAD tracked blobs only; no dotenv contents, ignored data or historical objects read',
              'repositories': []}
    for repo, target in SOURCES.items():
        head = git(repo, 'rev-parse', 'HEAD').decode().strip()
        records, exclusions, findings = [], [], []
        before = git(repo, 'status', '--porcelain', '--untracked-files=no')
        entries = []
        for entry in git(repo, 'ls-tree', '-rz', '--full-tree', head).split(b'\0'):
            if not entry:
                continue
            meta, rawpath = entry.split(b'\t', 1)
            mode, kind, oid = meta.decode().split()
            path = rawpath.decode('utf-8')
            reason = excluded(path)
            if reason:
                exclusions.append({'path': path, 'reason': reason})
                continue
            if kind != 'blob' or mode not in {'100644', '100755'}:
                findings.append({'path': path, 'rule': 'non-regular entry requires review'})
                continue
            entries.append((path, mode, oid))
        payload = b''.join(oid.encode() + b'\n' for _, _, oid in entries)
        raw = subprocess.check_output(['git', '-C', str(ROOT / repo), 'cat-file', '--batch'], input=payload)
        cursor = 0
        for path, mode, oid in entries:
            end = raw.index(b'\n', cursor)
            returned_oid, kind, size = raw[cursor:end].split()
            assert returned_oid.decode() == oid and kind == b'blob'
            cursor = end + 1
            data = raw[cursor:cursor + int(size)]
            cursor += int(size) + 1
            records.append({'path': path, 'gitBlob': oid, 'mode': mode,
                            'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()})
            for rule, pattern in RULES.items():
                if re.search(pattern, data):
                    findings.append({'path': path, 'rule': rule})
        assert before == git(repo, 'status', '--porcelain', '--untracked-files=no')
        result['repositories'].append({'source': repo, 'target': target, 'commit': head,
            'branch': git(repo, 'branch', '--show-current').decode().strip(),
            'trackedTreeClean': not bool(before), 'files': records,
            'excluded': exclusions, 'reviewFindings': findings,
            'licensePaths': [x['path'] for x in records if Path(x['path']).name.lower().startswith(('license', 'notice', 'copying'))]})
    (OUT / 'preflight.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    for repo in result['repositories']:
        print(repo['source'], repo['commit'], 'eligible', len(repo['files']),
              'excluded', len(repo['excluded']), 'review findings', len(repo['reviewFindings']))
        for finding in repo['reviewFindings']:
            print(' review:', finding['path'], finding['rule'])

if __name__ == '__main__':
    main()
