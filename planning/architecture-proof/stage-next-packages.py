"""Conservative runtime package closure when junction-backed NFT output is incomplete."""
import json
from pathlib import Path
import shutil
from inventory import ROOT,OUT,tree

source=ROOT/'dozu-ui-service/node_modules'
target=OUT/'.runs/dozu-ui-service/.next/standalone/node_modules'
queue=[source/n for n in ['next','react','react-dom']]
seen=set();missing=[];packages=[]
def find(name,package):
    for parent in [package,*package.parents]:
        candidate=parent/'node_modules'/name
        if (candidate/'package.json').is_file():return candidate
    raise RuntimeError(f'Missing installed dependency {name}')
while queue:
    package=queue.pop()
    if package in seen:continue
    seen.add(package)
    if not package.is_relative_to(source):raise RuntimeError('Package outside approved source dependency root')
    metadata=json.loads((package/'package.json').read_text(encoding='utf-8'))
    dest=target/package.relative_to(source)
    shutil.copytree(package,dest,dirs_exist_ok=True,ignore=shutil.ignore_patterns('node_modules','.git','.env*','.npmrc','.netrc'))
    packages.append({'name':metadata['name'],'version':metadata['version'],'relativePath':package.relative_to(source).as_posix()})
    for name in metadata.get('dependencies',{}):queue.append(find(name,package))
ui=OUT/'.runs/dozu-ui-service'
shutil.copytree(ui/'public',target.parent/'public',dirs_exist_ok=True)
shutil.copytree(ui/'.next/static',target.parent/'.next/static',dirs_exist_ok=True)
result={'method':'Conservative complete package directories for Next + React + React DOM, recursively resolving declared production dependencies from installed source packages. Optional build-only per-platform SWC packages not included by this step; sharp absent in source remains an explicit runtime capability gap. Includes unused files; not a minimal trace or complete application proof. External-module runtime guard validates sampled routes only.','packages':sorted(packages,key=lambda p:p['name']),'standalone':tree(target.parent)}
(OUT/'next-packaged-closure.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print('Runtime packages',len(packages),'standalone MB',result['standalone']['MB'],flush=True)
