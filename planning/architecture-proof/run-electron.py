"""Run a downloaded pinned Electron executable with explicit sanitized child env."""
import json
from pathlib import Path
import subprocess
import sys
import shutil
from build import OUT,ROOT,RUN,ENV

mode = sys.argv[1]
run_dir = RUN / ('electron-'+mode)
run_dir.mkdir(parents=True,exist_ok=True)
env=ENV.copy()
env.update({'FRONTEND_BASE_URL':'http://127.0.0.1:43000','BACKEND_BASE_URL':'http://127.0.0.1:43333'}) if mode=='api-local-urls' else None
if mode.startswith('api'):
    cwd=RUN/'dozu-api-service'
    entry=cwd/'dist/index.js'
else:
    cwd=RUN/'dozu-ui-service/.next/standalone'
    entry=cwd/'server.js'
    env.update({'HOSTNAME':'localhost','PORT':'43000'})
    if mode=='web-contained':
        env['PROOF_ENFORCE_RUNTIME_ROOT']=str(cwd)
    # Next standalone does not include these automatically. Copy all original
    # assets without deleting any emitted feature chunks/pages.
    shutil.copytree(RUN/'dozu-ui-service/public',cwd/'public',dirs_exist_ok=True)
    shutil.copytree(RUN/'dozu-ui-service/.next/static',cwd/'.next/static',dirs_exist_ok=True)
if not entry.exists():raise RuntimeError(f'Missing actual service entry: {entry}')
config={'mode':mode,'runDir':str(run_dir),'cwd':str(cwd),'entry':str(entry),'env':env,'log':str(OUT/f'electron-{mode}-child.log'),'result':str(OUT/f'electron-{mode}.json')}
Path(config['log']).write_text('',encoding='utf-8')
config_path=run_dir/'config.json';config_path.write_text(json.dumps(config),encoding='utf-8')
with (OUT/f'electron-{mode}-main.log').open('wb') as log:
    proc=subprocess.Popen([str(OUT/'.downloads/electron/electron.exe'),str(OUT/'electron-main.cjs'),str(config_path)],env=ENV,cwd=run_dir,stdout=log,stderr=subprocess.STDOUT)
    try:code=proc.wait(timeout=90)
    except subprocess.TimeoutExpired:
        # Exact process tree started by this harness only.
        subprocess.run(['taskkill','/PID',str(proc.pid),'/T','/F'],capture_output=True)
        Path(config['result']).write_text(json.dumps({'mode':mode,'error':'outer 90-second timeout; exact launched process tree terminated','entry':str(entry)}),encoding='utf-8')
        raise
result=json.loads(Path(config['result']).read_text(encoding='utf-8'))
print(json.dumps({'electronExitCode':code,**{k:v for k,v in result.items() if k not in {'metricSamples','metricsBeforeStop'}}}),flush=True)
