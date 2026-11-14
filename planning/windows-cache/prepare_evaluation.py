"""Isolated build-host evaluator dependencies; never changes app lockfiles."""
import json
import os
from pathlib import Path
import subprocess

HERE=Path(__file__).resolve().parent
stage=HERE/'.runs/queue-evaluation'
stage.mkdir(parents=True,exist_ok=True)
(stage/'package.json').write_text(json.dumps({'name':'dozu-queue-research','version':'0.0.0','private':True,
    'dependencies':{'bullmq':'6.7.6','pg':'8.14.1'}})+'\n',encoding='utf-8')
recorded_lock=HERE/'evaluation-package-lock.json'
if recorded_lock.exists(): (stage/'package-lock.json').write_bytes(recorded_lock.read_bytes())
for name in ['user.npmrc','global.npmrc']: (stage/name).write_text('',encoding='utf-8')
env={k:v for k,v in os.environ.items() if k.upper() in {'SYSTEMROOT','WINDIR','TEMP','TMP','COMSPEC','PATH'}}
env['NPM_CONFIG_CACHE']=str(HERE/'.downloads/npm-cache')
node=Path('C:/nvm4w/nodejs/node.exe')
npm=node.parent/'node_modules/npm/bin/npm-cli.js'
p=subprocess.run([str(node),str(npm),'ci' if recorded_lock.exists() else 'install','--ignore-scripts','--no-audit','--no-fund',
    '--userconfig',str(stage/'user.npmrc'),'--globalconfig',str(stage/'global.npmrc')],
    cwd=stage,env=env,capture_output=True,text=True,timeout=180)
(HERE/'.runs/npm-evaluation.log').write_text(p.stdout+p.stderr,encoding='utf-8')
p.check_returncode()
(HERE/'evaluation-package-lock.json').write_bytes((stage/'package-lock.json').read_bytes())
print(json.dumps({'isolatedDependenciesInstalled':True,'lifecycleScripts':False,'applicationLockfilesChanged':False}))
