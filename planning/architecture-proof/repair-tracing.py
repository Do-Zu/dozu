"""Re-home traced dependency files from junction-backed build into standalone."""
import json
from pathlib import Path
import shutil
import os
from inventory import OUT,ROOT,tree

ui=OUT/'.runs/dozu-ui-service'
standalone=ui/'.next/standalone'
source_modules=ROOT/'dozu-ui-service/node_modules'
# The default copier preserved the development dependency link itself.
# Remove only this exact link (non-recursive), never its target.
linked=standalone/'node_modules'
if linked.is_symlink() or linked.is_junction():
    if linked.absolute().parent != standalone.absolute():
        raise RuntimeError('Unexpected link location')
    os.rmdir(linked)
    linked.mkdir()
copied={};excluded=[];missing=[]
for manifest in (ui/'.next').rglob('*.nft.json'):
    if standalone in manifest.parents:
        continue
    for rel in json.loads(manifest.read_text(encoding='utf-8'))['files']:
        source=(manifest.parent/rel).resolve()
        if source == source_modules:
            # Original directory-link entry; its traced files are copied below.
            continue
        if source_modules in source.parents:
            dest=standalone/'node_modules'/source.relative_to(source_modules)
        elif ui in source.parents:
            dest=standalone/source.relative_to(ui)
        else:
            excluded.append(str(source));continue
        if source.name.startswith('.env') or source.name in {'.npmrc','.netrc','.pypirc'}:
            raise RuntimeError('Credential configuration in trace: refuse to package')
        if not dest.resolve().is_relative_to(standalone.resolve()):
            raise RuntimeError('Trace destination escapes standalone')
        if not source.is_file():
            missing.append(str(source));continue
        dest.parent.mkdir(parents=True,exist_ok=True)
        if source != dest:
            shutil.copyfile(source,dest)
        copied[dest.relative_to(standalone).as_posix()]=source.stat().st_size
        if source_modules in source.parents:
            parts=source.relative_to(source_modules).parts
            package_parts=parts[:2] if parts[0].startswith('@') else parts[:1]
            metadata=source_modules.joinpath(*package_parts)/'package.json'
            if metadata.is_file():
                metadata_dest=standalone/'node_modules'/metadata.relative_to(source_modules)
                metadata_dest.parent.mkdir(parents=True,exist_ok=True)
                shutil.copyfile(metadata,metadata_dest)
                copied[metadata_dest.relative_to(standalone).as_posix()]=metadata.stat().st_size
asset=tree(standalone)
result={'method':'Next build uses a node_modules junction, whose .nft paths point outside tracing root. Explicitly copy all traced files from approved source dependency root to standalone/node_modules, preserving package-relative layout; copy proof-root traced files relative to proof UI. No unknown roots or env/auth config copied. Runtime guard then rejects module resolution outside standalone. This is proof harness packaging, not a source config change.','copiedFileCount':len(copied),'excludedOutsideApprovedRoots':sorted(set(excluded)),'missingFiles':sorted(set(missing)),'standalone':asset}
(OUT/'next-standalone-manifest.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='standalone'}),flush=True)
print('Standalone including public/static:',asset['MB'],'MB',asset['fileCount'],'files',flush=True)
if excluded or missing:raise SystemExit(1)
