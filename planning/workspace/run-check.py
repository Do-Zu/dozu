"""Run workspace tooling with no provider credentials or user registry config."""
import datetime
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
allowed = {'SYSTEMROOT', 'WINDIR', 'SYSTEMDRIVE', 'COMSPEC', 'PATH', 'PATHEXT',
           'TEMP', 'TMP', 'PROCESSOR_ARCHITECTURE', 'NUMBER_OF_PROCESSORS'}
env = {k:v for k,v in os.environ.items() if k.upper() in allowed}
config = HERE / '.runs/empty.npmrc'
config.parent.mkdir(parents=True, exist_ok=True)
config.write_text('', encoding='utf-8')
global_config = config.with_name('empty-global.npmrc')
global_config.write_text('', encoding='utf-8')
env.update(NPM_CONFIG_USERCONFIG=str(config), NPM_CONFIG_GLOBALCONFIG=str(global_config),
           NPM_CONFIG_REGISTRY='https://registry.npmjs.org/',
           NPM_CONFIG_STORE_DIR=str(HERE / '.pnpm-store'),
           PNPM_HOME=str(HERE / '.runs/pnpm-home'),
           HUSKY='0', CI='true', NEXT_TELEMETRY_DISABLED='1', TURBO_TELEMETRY_DISABLED='1',
           NEXT_PUBLIC_API_URL='http://127.0.0.1:3333',
           NEXT_PUBLIC_API_STREAM_SSE_URL='http://127.0.0.1:3333',
           NEXT_PUBLIC_GOOGLE_REDIRECT_URI='http://127.0.0.1:3000/en/auth/login',
           NEXT_PUBLIC_OAUTH_CLIENT_ID='workspace-unconfigured')
name, *args = sys.argv[1:]
if not name or not args:
    raise SystemExit('Usage: run-check.py CHECK_NAME PNPM_ARGUMENTS...')
if name.startswith('api-test'):
    env.update(NODE_ENV='test', DATABASE_URL='postgresql://workspace:workspace@127.0.0.1:1/workspace',
               REDIS_HOST='127.0.0.1', REDIS_PORT='1', AWS_EC2_METADATA_DISABLED='true')
pnpm = shutil.which('pnpm.cmd') or shutil.which('pnpm')
start = time.monotonic()
result = subprocess.run([pnpm, *args], cwd=ROOT, env=env, stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT, text=True, encoding='utf-8', errors='replace')
(HERE / (name + '.log')).write_text(result.stdout, encoding='utf-8')
entry = {'name':name, 'command':['pnpm',*args], 'exitCode':result.returncode,
         'seconds':round(time.monotonic()-start,3),
         'capturedAtUtc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
         'environment':'OS allowlist plus declared credential-free loopback build settings',
         'log':name+'.log'}
(HERE / (name+'.json')).write_text(json.dumps(entry,indent=2)+'\n',encoding='utf-8')
print(json.dumps(entry))
print(result.stdout[-7000:])
raise SystemExit(result.returncode)
