"""Explicit research/build-host acquisition only. No global installs or app changes."""
import hashlib
import json
from pathlib import Path
import shutil
import urllib.request

HERE = Path(__file__).resolve().parent


def fetch(url):
    with urllib.request.urlopen(url, timeout=30) as r: return r.read()


def sha(p):
    with p.open('rb') as f: return hashlib.file_digest(f, 'sha256').hexdigest()


def main():
    cache = HERE/'.downloads'
    cache.mkdir(exist_ok=True)
    url = 'https://github.com/microsoft/garnet/releases/download/v2.2.12/win-x64-based-readytorun.zip'
    expected = '3edef0529508bd479c46d943569627189673bdfb3359b1697b19cbf7f93085c1'
    target = cache/'garnet-2.2.12-win-x64.zip'
    if not target.exists():
        with urllib.request.urlopen(url,timeout=30) as r, target.open('wb') as f: shutil.copyfileobj(r,f)
    assert sha(target)==expected
    rows = {'garnet': {'version':'2.2.12','source':url,'sha256':expected,'bytes':target.stat().st_size,
            'upstreamCommit':'3412254f6662a496571ef251bdbfe3db66904601',
            'checksumEvidence':'https://api.github.com/repos/microsoft/garnet/releases/tags/v2.2.12',
            'status':'evaluation-only-not-selected-runtime'}}
    for package, version in [('bullmq','6.7.6'),('pg-boss','12.38.2'),('lru-cache','11.5.3')]:
        data = json.loads(fetch('https://registry.npmjs.org/'+package+'/'+version))
        rows[package] = {'version':data['version'],'engines':data.get('engines'), 'dist':data['dist'],
                         'dependencies':data.get('dependencies'), 'repository':data.get('repository'), 'license':data.get('license')}
        (cache/(package+'-metadata.json')).write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    for name, path in [('garnet-license','LICENSE'),('garnet-security','SECURITY.md')]:
        url = 'https://raw.githubusercontent.com/microsoft/garnet/3412254f6662a496571ef251bdbfe3db66904601/'+path
        content = fetch(url)
        (cache/(name+'.txt')).write_bytes(content)
        rows[name]={'source':url,'sha256':hashlib.sha256(content).hexdigest(),'bytes':len(content)}
    (HERE/'candidate-metadata.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v.get('version') for k,v in rows.items()}))


if __name__=='__main__': main()
