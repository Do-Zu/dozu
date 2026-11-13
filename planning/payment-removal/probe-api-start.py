"""Bounded real entrypoint probe; no real credentials, dotenv, DB or Redis instance."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
API = ROOT / 'apps/api'
(HERE / '.runs').mkdir(exist_ok=True)
data = Path(tempfile.mkdtemp(prefix='api data ', dir=HERE / '.runs'))
# Keep Puppeteer's config discovery inside the disposable fixture; never read host configuration.
(data/'.puppeteerrc.json').write_text(json.dumps({'skipDownload': True, 'cacheDirectory': str(data/'browser-cache')}),encoding='utf-8')
env = {key:value for key,value in os.environ.items() if key.upper() in
       {'PATH','SYSTEMROOT','WINDIR','COMSPEC','PATHEXT','TEMP','TMP'}}
env.update(NODE_ENV='production', DOZU_DATA_DIR=str(data), HOST='localhost', PORT='0',
           ALLOWED_ORIGINS='http://localhost', AWS_EC2_METADATA_DISABLED='true',
           DATABASE_URL='postgresql://fixture:fixture@127.0.0.1:1/fixture',
           REDIS_HOST='127.0.0.1', REDIS_PORT='1', REDIS_PUBSUB_HOST='127.0.0.1', REDIS_PUBSUB_PORT='1',
           REDIS_RECOMMENDATION_HOST='127.0.0.1', REDIS_RECOMMENDATION_PORT='1')
reads = [API/'dist',ROOT/'node_modules',API/'node_modules',API/'package.json',ROOT/'package.json',data]
command = [shutil.which('node'),'--permission',*[f'--allow-fs-read={p}' for p in reads],
           f'--allow-fs-write={data}',str(API/'dist/index.js')]
timed_out = False
try:
    result = subprocess.run(command,cwd=data,env=env,capture_output=True,timeout=10)
    log = result.stdout + result.stderr
    exit_code = result.returncode
except subprocess.TimeoutExpired as error:
    timed_out = True
    log = (error.stdout or b'') + (error.stderr or b'')
    exit_code = None
(HERE/'production-startup.log').write_bytes(log)
assert b'BACKEND_BASE_URL is missing' not in log
assert b'nodeMailerTransporter' not in log
assert b'PayOSManager' not in log
assert b'PaymentBase configuration' not in log
report = {'exitCode':exit_code,'timedOut':timed_out,'emailStartupBlockerAbsent':True,'payosStartupBlockerAbsent':True,
          'backendReady':False,'boundary':'Scrubbed real entrypoint; deliberately unavailable loopback DB/Redis; no SMTP/provider credentials or real dotenv reads; owned process bounded/stopped.'}
(HERE/'production-startup.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report))
