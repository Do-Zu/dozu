"""Check the root website start wrapper with package reads only and no filesystem writes."""
import html
import json
import os
from pathlib import Path
import re
import shutil
import socket
import subprocess
import time
import urllib.request
import urllib.parse
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
node = shutil.which('node')
destination = ROOT / 'apps/web/.package'
wrapper = ROOT / 'tooling/start-web.cjs'
flags = ['--permission', '--allow-fs-read=' + str(destination), '--allow-fs-read=' + str(wrapper)]
env = {k:v for k,v in os.environ.items() if k.upper() in
       {'PATH','SYSTEMROOT','WINDIR','COMSPEC','PATHEXT','TEMP','TMP'}}
env.update(NODE_ENV='production', NEXT_TELEMETRY_DISABLED='1')
guard = "const a=require('node:assert/strict'),fs=require('node:fs'); a.throws(()=>fs.readFileSync(process.argv[1]),{code:'ERR_ACCESS_DENIED'});a.throws(()=>fs.writeFileSync(process.argv[2],'x'),{code:'ERR_ACCESS_DENIED'});"
subprocess.run([node,*flags,'-e',guard,str(ROOT/'package.json'),str(destination/'forbidden.txt')],
               cwd=HERE,env=env,capture_output=True,check=True)
checks=[]
start=time.monotonic()
with socket.socket() as sock:
    sock.bind(('127.0.0.1',0))
    env['PORT'] = str(sock.getsockname()[1])
base_url = 'http://localhost:' + env['PORT']
checks = []
log_path = HERE / 'website-server.log'
start = time.monotonic()
with log_path.open('w',encoding='utf-8') as log:
    process = subprocess.Popen([node,*flags,str(wrapper)], cwd=destination,
                               env=env, stdout=log, stderr=subprocess.STDOUT)
    try:
        deadline = time.monotonic()+45
        while True:
            try:
                with urllib.request.urlopen(base_url+'/en/welcome',timeout=5) as response:
                    english = response.read().decode('utf-8')
                    assert response.status == 200
                break
            except Exception:
                if process.poll() is not None or time.monotonic()>deadline:
                    raise
                time.sleep(0.25)
        ready = round(time.monotonic()-start,3)
        for locale in ('en','vi'):
            expected = json.loads((ROOT/f'apps/web/messages/{locale}/welcome.json').read_text(encoding='utf-8'))['welcome']['title']
            with urllib.request.urlopen(base_url+f'/{locale}/welcome',timeout=10) as response:
                body = response.read().decode('utf-8')
                assert response.status == 200 and expected in html.unescape(body)
                checks.append({'path':f'/{locale}/welcome','status':response.status,'localeTitlePresent':True})
        for locale in ('en','vi'):
            expected = json.loads((ROOT/f'apps/web/messages/{locale}/emailAvailability.json').read_text(encoding='utf-8'))['EmailAvailability']['recoveryUnavailable']
            with urllib.request.urlopen(base_url+f'/{locale}/auth/forgotPassword',timeout=10) as response:
                body = response.read().decode('utf-8')
                assert response.status == 200 and expected in html.unescape(body)
                assert 'id="email"' not in body
                checks.append({'path':f'/{locale}/auth/forgotPassword','status':200,'unavailableMessage':True,'emailFormAbsent':True})
        for path in ('/en/auth/login','/vi/auth/login','/en/payment','/icon.png'):
            with urllib.request.urlopen(base_url+path,timeout=10) as response:
                data = response.read()
                assert response.status==200 and len(data)>0
                checks.append({'path':path,'status':response.status,'bytes':len(data)})
        assets = list(dict.fromkeys(re.findall(r'(/_next/static/[^"\s<>]+?\.(?:js|css|woff2))',english)))
        assert assets
        # Font resources can be referenced by CSS rather than preloaded in HTML.
        stylesheet = ''
        stylesheet_url = ''
        for extension in ('.js','.css'):
            selected = next((p for p in assets if p.endswith(extension)),None)
            assert selected, extension
            with urllib.request.urlopen(base_url+html.unescape(selected),timeout=10) as response:
                data=response.read()
                assert response.status==200 and len(data)>0
                checks.append({'assetType':extension,'status':response.status,'bytes':len(data)})
                if extension == '.css':
                    stylesheet = data.decode('utf-8')
                    stylesheet_url = base_url+html.unescape(selected)
        font = re.search(r'url\([\x22\x27]?([^\x22\x27)]+\.(?:woff2?|ttf|otf))',stylesheet)
        if not font:
            for css_path in (p for p in assets if p.endswith('.css')):
                stylesheet_url = base_url+html.unescape(css_path)
                with urllib.request.urlopen(stylesheet_url,timeout=10) as response:
                    assert response.status == 200
                    stylesheet=response.read().decode('utf-8')
                font=re.search(r'url\([\x22\x27]?([^\x22\x27)]+\.(?:woff2?|ttf|otf))',stylesheet)
                if font:
                    break
        assert font, 'bundled font reference in emitted CSS'
        font_url = urllib.parse.urljoin(stylesheet_url,font[1])
        assert urllib.parse.urlsplit(font_url).netloc == urllib.parse.urlsplit(base_url).netloc
        with urllib.request.urlopen(font_url,timeout=10) as response:
            data=response.read()
            assert response.status==200 and len(data)>0
            checks.append({'assetType':'bundled-font','status':response.status,'bytes':len(data)})
    finally:
        process.terminate()
        try:
            process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait(timeout=5)
result={'rootWrapper':'tooling/start-web.cjs','originalWorkspaceReadDenied':True,
        'allFilesystemWritesDenied':True,'defaultHost':'localhost',
        'readySecondsDeveloperHost':ready,'checks':checks,'ownedProcessStopped':process.poll() is not None,
        'limitations':'Sampled website server/assets only; no API/database/embedding/provider, OS ACL or full feature acceptance.'}
(HERE/'website-proof.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
