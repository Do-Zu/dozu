"""Audit the decision evidence without mistaking it for application migration."""
import ast
import hashlib
import json
from pathlib import Path
import subprocess

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]


def sha(path):
    with path.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()


def read(path):return json.loads(path.read_text(encoding='utf-8-sig'))


def main():
    before=read(HERE/'postgres-before.json');after=read(HERE/'postgres-after.json')
    native=read(HERE/'postgres-native-probe.json')
    assert before['passed']==4 and after['passed']==8
    assert not before['redisUsed'] and not after['redisUsed']
    assert native['result']=='passed' and native['ownedClusterStopped']
    assert all(p['exitCode']==0 for p in native['phases'])
    assert [p['name'] for p in native['phases']]==['initdb','start','before','stop-for-restart','restart','after','final-stop']
    assert not list((HERE/'.runs').glob('postgres-ascii-*/data/postmaster.pid')), 'Owned test cluster still running'
    lock=read(HERE/'evaluation-package-lock.json')
    assert lock['packages']['node_modules/bullmq']['version']=='6.7.6'
    assert lock['packages']['node_modules/pg']['version']=='8.14.1'
    assert read(ROOT/'apps/api/package.json')['dependencies']['bullmq']=='5.49.1'
    scope=read(ROOT/'resources/manifests/scope.json')
    target=read(ROOT/'resources/manifests/targets/win32-x64.json')
    assert not scope['desktopStateStrategy']['applicationMigrationImplemented']
    assert not scope['desktopStateStrategy']['redisRuntimeRequired']
    assert target['desktopStateStrategy']==scope['desktopStateStrategy']
    assert not target['releaseEligible'] and 'DESKTOP-STATE-PG' in target['gates']
    assert 'WINDOWS-REDIS' not in target['gates']
    assert not read(ROOT/'planning/runtime-manifests/validation.json')['releaseEligible']
    assert read(HERE/'postgres-unicode-path-probe.json')['result']=='failed'
    assert read(HERE/'garnet-runtime-probe.json')['compatibilityVerdict'].startswith('untested')
    for p in HERE.glob('*.py'):ast.parse(p.read_text(encoding='utf-8'))
    subprocess.run(['node','--check',str(HERE/'probe_postgres.cjs')],check=True)
    files=[p for p in HERE.iterdir() if p.is_file() and p.name!='evidence.json']
    files.extend([ROOT/'planning/v1-scope-2026-11-14-desktop-state.md',ROOT/'resources/manifests/scope.json',ROOT/'resources/manifests/targets/win32-x64.json'])
    evidence={'researchDecisionVerified':True,'selected':'desktop PostgreSQL durable jobs/state plus bounded disposable process cache',
        'actualPostgresChecksPassed':before['passed']+after['passed'],'ownedClusterStopped':True,
        'redisFreeApplicationClaim':False,'cleanNativeTargetClaim':False,'issue38Complete':False,
        'nextImplementation':'#30 desktop/website queue-profile boundary after #29 reviewed bootstrap/migrations; see work packages in decision.md',
        'files':[{'path':p.relative_to(ROOT).as_posix(),'sha256':sha(p)} for p in sorted(files)]}
    (HERE/'evidence.json').write_text(json.dumps(evidence,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in evidence.items() if k!='files'}))


if __name__=='__main__':main()
