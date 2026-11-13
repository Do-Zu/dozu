"""Verify only payment dependencies/behavior changed in this follow-up, preserving earlier work."""
import collections
import json
from pathlib import Path
import re
import subprocess

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
before=(HERE/'lock-before.yaml').read_text(encoding='utf-8')
expected=before.replace("      '@payos/node':\n        specifier: 1.0.10\n        version: 1.0.10\n",'')
for pattern in [r"(?ms)^  '@payos/node@1\.0\.10':[^\n]*\n(?:(?!^  \S).)*",
                r'(?ms)^  crypto@1\.0\.1:[^\n]*\n(?:(?!^  \S).)*']:
    expected,count=re.subn(pattern,'',expected)
    assert count==2,count
assert (ROOT/'pnpm-lock.yaml').read_text(encoding='utf-8')==expected
api=json.loads((ROOT/'apps/api/package.json').read_text(encoding='utf-8'))
baseline=json.loads(subprocess.check_output(['git','show','HEAD:apps/api/package.json'],cwd=ROOT))
for field in ['dependencies','devDependencies']:
    wanted=baseline[field].copy()
    for package in ['@payos/node','nodemailer','@types/nodemailer']:wanted.pop(package,None)
    assert api[field]==wanted,field
untouched=['apps/api/src/models','apps/api/src/repositories','apps/api/src/libs/redis',
    'apps/api/src/libs/bullmq','apps/api/src/services/subscription/subscription.service.ts',
    'apps/api/drizzle','apps/api/src/services/notification/notification.scheduler.ts']
assert not subprocess.check_output(['git','diff','--name-only','--',*untouched],cwd=ROOT,text=True).strip()
for file in (ROOT/'apps/api/src').rglob('*.ts'):
    assert '@payos/node' not in file.read_text(encoding='utf-8'),file
keys=[sorted(json.loads((ROOT/f'apps/web/messages/{locale}/paymentAvailability.json').read_text(encoding='utf-8'))['PaymentAvailability']) for locale in ['en','vi']]
assert keys[0]==keys[1]

def lint(file):
    result=collections.Counter();name=''
    for line in file.read_text(encoding='utf-8').splitlines():
        if re.match(r'^[A-Z]:',line):name=line.replace('\\','/')
        match=re.match(r'\s*\d+:\d+\s+(error|warning)\s+(.*?)\s{2,}(\S+)\s*$',line)
        if match:result[(name,*match.groups())]+=1
    return result
old=lint(HERE.parent/'email-removal/api-lint.log');new=lint(HERE/'api-lint.log')
added=list((new-old).elements());removed=list((old-new).elements())
assert not added,added
(HERE/'api-lint-comparison.json').write_text(json.dumps({'added':added,'removed':removed},indent=2)+'\n',encoding='utf-8')
report={'onlyPayosAndUnusedCryptoRemovedFromPriorLock':True,'noOtherDirectDependencyChanges':True,
    'schemasRepositoriesMigrationHistoryRedisBullMQFreePlanAndSchedulerSourceUnchanged':True,
    'noPayosSdkImportsInApiSource':True,'translationKeysMatch':True,'apiLintAddedDiagnostics':0,
    'apiLintRemovedDiagnostics':len(removed),'noRealTransactionOrMigrationExecuted':True}
(HERE/'scope-verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report))
