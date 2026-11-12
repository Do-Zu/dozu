"""Derive concise evidence, exact footprint bounds, and immutable result hashes."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
from inventory import OUT,ROOT,MODEL,SITE,digest

def read(name):return json.loads((OUT/name).read_text(encoding='utf-8-sig'))
inv=read('inventory.json')
web=read('electron-web-contained.json')
emb=read('embedding-runtime-serial.json')
paths=[MODEL/'model.safetensors',SITE/'torch/lib/torch_cpu.dll',OUT/'.downloads/electron/electron.exe']
bound=[{'path':str(p),'bytes':p.stat().st_size,'sha256':digest(p)} for p in paths]
result={'threeFileInstalledBound':{'method':'Exactly the unquantized model weight, actually loaded torch_cpu.dll, and executed Electron executable from this Windows candidate. Does not include model tokenizer, Python, other DLLs, Next/API, PostgreSQL, files/jobs or any processing assets. Pruning other files cannot make these three files fit; changing model/runtime is a different candidate to validate. Logical bytes, not compressed filesystem bytes.','files':bound,'bytes':sum(p['bytes'] for p in bound),'MB':sum(p['bytes'] for p in bound)/1e6,'MiB':sum(p['bytes'] for p in bound)/2**20,'approvedInstalledMB':750,'passes':False},'modelCompression':read('model-compression.json'),'electronArchive':read('electron-acquisition.json'),'containedNext':{'packages':len(read('next-packaged-closure.json')['packages']),'standaloneBytes':read('next-packaged-closure.json')['standalone']['bytes'],'routes':web['checks'],'externalModuleResolutionBlocked':True,'httpReadySeconds':web.get('httpReadySeconds'),'hiddenRendererLoadSeconds':web.get('loadedHiddenRendererSeconds'),'processes':web.get('metricsBeforeStop'),'workingSetBytesAtSnapshot':sum(p['memory']['workingSetSize']*1024 for p in web.get('metricsBeforeStop',[])),'measurementStart':'Inside Electron main script, after Electron executable startup began; not OS launch-to-interactive timing.','knownGaps':['sharp missing; image optimization unpassed','dynamic topic route logs location is not defined despite HTTP 200','CSP warning observed','no API/DB/model in this process group; no full normal-workload measurement']},'embedding':{k:v for k,v in emb.items() if k not in {'nativeLoadedModulePaths','memorySamples'}},'loadedNativeModules':{'count':len(emb['nativeLoadedModulePaths']),'torchCpuObserved':any(p.lower().endswith('torch_cpu.dll') for p in emb['nativeLoadedModulePaths']),'optionalSpacyObserved':any('site-packages\\spacy\\' in p.lower() for p in emb['nativeLoadedModulePaths']),'caveat':'Existing venv includes spaCy/thinc; YouTube module eagerly imports optional spaCy. en_core_web_sm not present; refinement falls back. Current memory is not a minimal clean requirements closure; no optional capability silently removed.'},'database':read('database-availability.json'),'sourceStatus':{},'acceptance':'All parent #4 criteria and P1–P7 completion gates remain unpassed; native macOS/Linux and supported Windows baselines/installer/minimum hardware have not been executed.'}
for name in ['dozu-ui-service','dozu-api-service','dozu-embedding-service']:
    status=subprocess.check_output(['git','-C',str(ROOT/name),'status','--porcelain'],text=True)
    result['sourceStatus'][name]={'trackedOrUntrackedChanges':status,'commit':subprocess.check_output(['git','-C',str(ROOT/name),'rev-parse','HEAD'],text=True).strip()}
snapshot=OUT/'.runs/electron-web-contained/welcome.png'
if snapshot.exists():shutil.copyfile(snapshot,OUT/'next-welcome.png')
(OUT/'results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
manifest=[]
for p in sorted(OUT.iterdir()):
    if p.is_file() and p.name not in {'evidence-manifest.json'}:
        manifest.append({'path':p.name,'bytes':p.stat().st_size,'sha256':digest(p)})
(OUT/'evidence-manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(json.dumps({'installedThreeFileMB':result['threeFileInstalledBound']['MB'],'standaloneMB':result['containedNext']['standaloneBytes']/1e6,'electronNextWorkingSetMB':result['containedNext']['workingSetBytesAtSnapshot']/1e6,'embeddingWorkingSetMB':emb['idleMemoryAfterRequests']['workingSetBytes']/1e6,'embeddingReadySeconds':emb['backendReadySeconds'],'sourceStatus':result['sourceStatus']},indent=2),flush=True)
