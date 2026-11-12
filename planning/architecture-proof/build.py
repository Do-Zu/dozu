"""Sanitized production build copies. No source/history import or real env loading."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
RUN = OUT / '.runs'
SAFE = {'PATH','SYSTEMROOT','WINDIR','COMSPEC','PATHEXT','TEMP','TMP','PROCESSOR_ARCHITECTURE','NUMBER_OF_PROCESSORS','APPDATA','LOCALAPPDATA','USERPROFILE','PROGRAMFILES','PROGRAMFILES(X86)','PROGRAMDATA','SYSTEMDRIVE'}
ENV = {k:v for k,v in os.environ.items() if k.upper() in SAFE}
ENV.update({'CI':'1','NODE_ENV':'production','NEXT_TELEMETRY_DISABLED':'1','NEXT_PUBLIC_API_URL':'http://127.0.0.1:43333','NEXT_PUBLIC_API_STREAM_SSE_URL':'http://127.0.0.1:43333','NEXT_PUBLIC_WEBSOCKET_URL':'http://127.0.0.1:43333','DATABASE_URL':'postgresql://proof:proof@127.0.0.1:1/proof','REDIS_HOST':'127.0.0.1','REDIS_PORT':'1','HOST':'127.0.0.1','PORT':'43333','ALLOWED_ORIGINS':'http://127.0.0.1:43000','TRUST_PROXY':'false','PYTHONDONTWRITEBYTECODE':'1'})
ENV.update({'REDIS_PUBSUB_HOST':'127.0.0.1','REDIS_PUBSUB_PORT':'1','REDIS_RECOMMENDATION_HOST':'127.0.0.1','REDIS_RECOMMENDATION_PORT':'1'})

def prepare(name):
    source = ROOT / name
    target = RUN / name
    target.mkdir(parents=True,exist_ok=True)
    paths = subprocess.check_output(['git','-C',str(source),'ls-files','-z']).decode().split('\0')
    excluded = {'.git','node_modules','.venv','dist','dist-stage','dist-lambda','logs','outputs','uploads','.next'}
    hashes = []
    import hashlib
    for rel in paths:
        if not rel or Path(rel).parts[0] in excluded or Path(rel).name.startswith('.env') or Path(rel).name in {'.npmrc','.pypirc','.netrc'} or 'token-github' in rel.lower():
            continue
        p = source / rel
        if p.is_file():
            dest = target / rel
            dest.parent.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(p,dest)
            hashes.append({'path':rel,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
    modules = target/'node_modules'
    if (source/'node_modules').exists() and not modules.exists():
        # Fixed workspace paths; no user-controlled shell interpolation.
        subprocess.run(['powershell','-NoProfile','-Command',f"New-Item -ItemType Junction -Path '{modules}' -Target '{source/'node_modules'}' | Out-Null"],check=True)
    (OUT/f'{name}-inputs.json').write_text(json.dumps({'commit':subprocess.check_output(['git','-C',str(source),'rev-parse','HEAD'],text=True).strip(),'files':hashes},indent=2),encoding='utf-8')
    return target

def run(label,args,cwd,timeout=600):
    started = time.perf_counter()
    try:
        p = subprocess.run(args,cwd=cwd,env=ENV,capture_output=True,timeout=timeout)
        code, log = p.returncode,p.stdout+p.stderr
    except subprocess.TimeoutExpired as exc:
        code,log = 'timeout',(exc.stdout or b'')+(exc.stderr or b'')
    (OUT/f'{label}.log').write_bytes(log)
    result = {'check':label,'args':args,'cwd':str(cwd.relative_to(ROOT)),'seconds':round(time.perf_counter()-started,3),'exitCode':code,'log':f'{label}.log','inputs':'sanitized tracked copies; existing node_modules junction; no npm install/real dotenv; development dependencies remain available for build only'}
    (OUT/f'{label}.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result),flush=True)
    print(log.decode('utf-8',errors='replace')[-5000:],flush=True)
    return code

if __name__ == '__main__':
    mode = sys.argv[1]
    name = 'dozu-ui-service' if mode == 'ui' else 'dozu-api-service'
    cwd = prepare(name)
    node = shutil.which('node')
    args = [node,str(cwd/'node_modules/next/dist/bin/next'),'build'] if mode=='ui' else [node,str(cwd/'node_modules/typescript/bin/tsc'),'--incremental','false','--noEmitOnError']
    sys.exit(run(f'{mode}-build-baseline',args,cwd))
