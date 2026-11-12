"""Record direct installed/locked versions and secret-path history metadata only."""
import json
from pathlib import Path
import subprocess
import hashlib

ROOT = Path(__file__).resolve().parents[2]
results = []
for name in ['dozu-ui-service','dozu-api-service']:
    repo = ROOT / name
    manifest = json.loads((repo/'package.json').read_text(encoding='utf-8'))
    lock = json.loads((repo/'package-lock.json').read_text(encoding='utf-8'))
    entries = []
    for group in ['dependencies','devDependencies']:
        for package, spec in manifest.get(group, {}).items():
            installed_path = repo/'node_modules'/package/'package.json'
            installed = json.loads(installed_path.read_text(encoding='utf-8')).get('version') if installed_path.exists() else None
            expected = lock.get('packages',{}).get('node_modules/'+package,{}).get('version')
            entries.append({'package':package,'group':group,'declared':spec,'locked':expected,'installed':installed,'matchesLock':installed==expected})
    history_count = subprocess.check_output(['git','-C',str(repo),'rev-list','--all','--count','--','.env','.env.*'], text=True).strip()
    results.append({'repo':name,'manifestLicense':manifest.get('license'),'lockSha256':hashlib.sha256((repo/'package-lock.json').read_bytes()).hexdigest(),'directDependencies':entries,'commitsTouchingEnvPaths':int(history_count),'note':'History metadata only; credential content/diffs not opened. Direct dependency agreement is not complete transitive or clean-install reproducibility proof.'})
(ROOT/'planning/audit/runtime-dependencies.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
print(json.dumps([{'repo':r['repo'],'directDependencies':len(r['directDependencies']),'mismatches':[p['package'] for p in r['directDependencies'] if not p['matchesLock']],'commitsTouchingEnvPaths':r['commitsTouchingEnvPaths']} for r in results],indent=2))
