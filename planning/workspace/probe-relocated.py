"""Launch a copied standalone website with filesystem access limited to the copy."""
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
source = ROOT / 'apps/web/.package'
# A unique destination avoids deleting an existing artifact or following output links.
destination = HERE / '.runs' / ('relocated-web-' + str(time.time_ns()))
node = shutil.which('node')
copy_and_check = r"""
const fs=require('fs'),p=require('path');
const source=p.resolve(process.argv[1]),dest=p.resolve(process.argv[2]);
if(fs.existsSync(dest)) throw Error('Relocation output must be new');
fs.cpSync(source,dest,{recursive:true,verbatimSymlinks:true});
const links=[];
function walk(dir){for(const e of fs.readdirSync(dir,{withFileTypes:true})){
 const f=p.join(dir,e.name);
 if(e.isSymbolicLink()){
  const target=fs.realpathSync(f),r=p.relative(dest,target);
  if(p.isAbsolute(fs.readlinkSync(f))||r==='..'||r.startsWith('..'+p.sep)||p.isAbsolute(r))throw Error('Link escapes copied artifact');
  links.push(p.relative(dest,f));
 }else if(e.isDirectory())walk(f);
}}
walk(dest);console.log(JSON.stringify(links));
"""
copied = subprocess.run([node,'-e',copy_and_check,str(source),str(destination)],
                        capture_output=True,text=True,check=True)
links = json.loads(copied.stdout)
flags = ['--permission', '--allow-fs-read=' + str(destination), '--allow-fs-write=' + str(destination)]
env = {k:v for k,v in os.environ.items() if k.upper() in
       {'PATH','SYSTEMROOT','WINDIR','SYSTEMDRIVE','COMSPEC','PATHEXT','TEMP','TMP'}}
# Next 14 normalizes middleware self-proxy URLs to localhost. Match its bind
# hostname rather than mixing an IPv4-only bind with dual-stack localhost.
env.update(NODE_ENV='production', HOSTNAME='localhost', NEXT_TELEMETRY_DISABLED='1')
guard = "try { require('fs').readFileSync(process.argv[1]); process.exit(9); } catch(e) { if(e.code!=='ERR_ACCESS_DENIED') throw e; console.log('original-workspace-denied'); }"
deny = subprocess.run([node, *flags, '-e', guard, str(ROOT/'package.json')],
                      cwd=destination, env=env, capture_output=True, text=True)
assert deny.returncode == 0 and 'original-workspace-denied' in deny.stdout, deny.stderr
with socket.socket() as sock:
    sock.bind(('127.0.0.1',0))
    env['PORT'] = str(sock.getsockname()[1])
base_url = 'http://localhost:' + env['PORT']
checks = []
log_path = HERE / 'relocated-server.log'
start = time.monotonic()
with log_path.open('w',encoding='utf-8') as log:
    process = subprocess.Popen([node,*flags,'apps/web/server.js'], cwd=destination,
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
result={'copiedArtifact':str(destination.relative_to(ROOT)), 'relativeContainedLinks':len(links),
        'originalWorkspaceReadDenied':True,'nodePermissionsRestrictedToCopy':True,
        'readySecondsDeveloperHost':ready,'checks':checks,'ownedProcessStopped':process.poll() is not None,
        'limitations':'Website server/assets only; no API/database/embedding/provider or complete feature parity acceptance.'}
(HERE/'relocated-proof.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
