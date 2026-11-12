"""Read-only asset inventory. Never reads dotenv, auth configuration or user data."""
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
from datetime import datetime, timezone

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
MODEL = Path.home() / '.cache/huggingface/hub/models--sentence-transformers--paraphrase-multilingual-MiniLM-L12-v2/snapshots/86741b4e3f5cb7765a600d3a3d55a0f6a6cb443d'
SITE = ROOT / 'dozu-embedding-service/.venv/Lib/site-packages'

def digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()

def entry(path, root, hashed=False):
    size = path.stat().st_size
    result = {'path': path.relative_to(root).as_posix(), 'bytes': size, 'MB': round(size / 1e6, 3), 'MiB': round(size / 2**20, 3)}
    if hashed:
        result['sha256'] = digest(path)
    return result

def tree(path, hash_all=False):
    if not path.exists():
        return {'root':str(path),'available':False,'bytes':None}
    files = []
    for base, dirs, names in os.walk(path):
        dirs[:] = [d for d in dirs if d not in {'__pycache__','.git'}]
        for name in names:
            p = Path(base) / name
            if not name.startswith('.env') and p.is_file():
                files.append(entry(p, path, hash_all))
    files.sort(key=lambda x: x['bytes'], reverse=True)
    size = sum(f['bytes'] for f in files)
    return {'root':str(path),'available':True,'bytes':size,'MB':round(size/1e6,3),'MiB':round(size/2**20,3),'fileCount':len(files),'files':files}

def main():
    assets = {'modelSnapshot':tree(MODEL,True)}
    for package in ['torch','transformers','sentence_transformers','numpy','scipy','sklearn','tokenizers','safetensors']:
        assets[package] = tree(SITE / package)
    for name, path in [('pythonEnvironment',ROOT/'dozu-embedding-service/.venv'),('uiPublic',ROOT/'dozu-ui-service/public'),('uiFonts',ROOT/'dozu-ui-service/src/fonts'),('puppeteerCache',Path.home()/'.cache/puppeteer'),('electron',OUT/'.downloads/electron')]:
        assets[name] = tree(path)
    disk = shutil.disk_usage(ROOT)
    result = {'utc':datetime.now(timezone.utc).isoformat(),'host':{'platform':platform.platform(),'machine':platform.machine(),'logicalCpuCount':os.cpu_count(),'orchestratorPython':sys.version,'diskBytes':{'total':disk.total,'free':disk.free}},'method':'Logical file bytes, recursive read-only inventory; excludes __pycache__; no developer tree is represented as a production closure. Model formats/unused cache versions must be selected before aggregating.', 'assets':assets}
    node = Path(shutil.which('node'))
    result['node'] = entry(node,node.parent,True) | {'source':str(node),'version':subprocess.check_output([str(node),'--version'],text=True).strip()}
    ffmpeg = shutil.which('ffmpeg')
    if ffmpeg:
        path = Path(ffmpeg)
        result['ffmpeg'] = entry(path,path.parent,True) | {'source':str(path),'versionLine':subprocess.check_output([str(path),'-version'],text=True).splitlines()[0]}
    result['currentScopeRecord'] = 'planning/v1-scope-2026-11-11.md'
    result['missingNativeResources'] = ['PostgreSQL portable distribution (not found on PATH/standard install path); pgvector is deferred','Gotenberg/LibreOffice native adapter and fonts','portable text-embedding runtime production distribution','signed per-platform installer and ownership/license manifests']
    result['deferredNativeResources'] = ['whisper.cpp server and tiny speech model','speech-only FFmpeg; retained non-STT need must be separately proven','pgvector extension']
    (OUT/'inventory.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    for name, asset in assets.items():
        print(name, asset.get('MB'), 'MB', asset.get('fileCount'), 'files',flush=True)
        if name in {'torch','modelSnapshot','puppeteerCache'}:
            print(json.dumps(asset.get('files',[])[:8]),flush=True)

if __name__ == '__main__':
    main()
