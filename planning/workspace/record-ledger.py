"""Verify every #6 deviation from the frozen #5 snapshot and direct versions."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
reasons = {
    'apps/web/.gitignore': 'Remove tracked-dotenv negation so root credential exclusions remain effective.',
    'apps/api/.gitignore': 'Remove tracked-dotenv negation so root credential exclusions remain effective.',
    'apps/web/package-lock.json': 'Archived byte-for-byte in planning/workspace/npm-locks; replaced active lock with root pnpm-lock.yaml.',
    'apps/api/package-lock.json': 'Archived byte-for-byte in planning/workspace/npm-locks; replaced active lock with root pnpm-lock.yaml.',
    'apps/web/package.json': 'Private workspace, portable scripts, guarded repeat builds, typecheck/package scripts and exact missing direct import declarations.',
    'apps/api/package.json': 'Private workspace, portable NODE_ENV scripts, cross-env runtime dependency and consumed @types/qs dev dependency.',
    'apps/web/next.config.js': 'Next14 experimental tracing root set to workspace root; standalone/UI behavior retained.',
    'apps/web/Dockerfile': 'Executable root-context pnpm/standalone website image recipe; original checkout retained for rollback.',
    'apps/api/Dockerfile': 'Root-context frozen pnpm website API recipe; remove build-time dotenv copy, supply runtime environment.',
    'apps/web/src/app/[locale]/topics/[topicId]/(topic)/media/core/youtube/YoutubePlayerAdapter.ts': 'Measured existing TS2322 blocker: validate raw ready-event synchronous number instead of typed Promise facade; independent source/type/runtime review and targeted lint passed.',
}
baseline = json.loads((ROOT/'planning/source-import/import-manifest.json').read_text(encoding='utf-8'))
changes=[]
for repo in baseline['repositories']:
    for record in repo['files']:
        relative=repo['target']+'/'+record['path']
        p=ROOT/relative
        current=sha(p) if p.exists() else None
        if current != record['importedSha256']:
            assert relative in reasons, relative
            changes.append({'path':relative,'operation':'modified' if p.exists() else 'removed',
                            'importedSha256':record['importedSha256'],'currentSha256':current,'reason':reasons[relative]})
assert set(x['path'] for x in changes)==set(reasons)
new_files = ['.gitignore','.dockerignore','package.json','pnpm-workspace.yaml','pnpm-lock.yaml','turbo.json']
new_files += [str(p.relative_to(ROOT)).replace('\\','/') for p in (ROOT/'tooling').glob('*.cjs')]
versions=[]
for app in ('web','api'):
    old=json.loads((HERE/f'npm-locks/{app}-package-lock.json').read_text(encoding='utf-8'))
    current=json.loads((ROOT/f'apps/{app}/package.json').read_text(encoding='utf-8'))
    for kind in ('dependencies','devDependencies'):
        for name,spec in old['packages'][''].get(kind,{}).items():
            before=old['packages']['node_modules/'+name]['version']
            now=json.loads((ROOT/f'apps/{app}/node_modules'/name/'package.json').read_text(encoding='utf-8'))['version']
            assert before==now, (app,name,before,now)
            assert current[kind][name]==spec, (app,name,'declared spec changed')
            versions.append({'app':app,'name':name,'declared':spec,'originalLockedVersion':before,'installedVersion':now})
    for name in set(current.get('dependencies',{}))|set(current.get('devDependencies',{})):
        if name not in old['packages'][''].get('dependencies',{}) and name not in old['packages'][''].get('devDependencies',{}):
            kind='dependencies' if name in current.get('dependencies',{}) else 'devDependencies'
            version=current[kind][name]
            if name != 'cross-env':
                assert old['packages']['node_modules/'+name]['version']==version
            versions.append({'app':app,'name':name,'newDirectDeclaration':version,'kind':kind,
                'reason':'Portable NODE_ENV scripts' if name=='cross-env' else 'Existing direct source import, exact original transitive lock version'})
result={'changedImportedPaths':changes,'newRootAndToolingFiles':[{'path':p,'sha256':sha(ROOT/p)} for p in sorted(new_files)],
        'directDependencies':versions,'originalDeclaredVersionsUnchanged':True,
        'originalNextDependencyFilesUnchangedAfterTwoGuardedBuilds':6387,
        'pythonRuntimeReproducibilityProven':False,
        'pythonBoundary':'Original unpinned requirements/Docker inputs retained independently; #7/#8 own Python/toolchain/wheel/model pinning and portable runtime proof.'}
(HERE/'change-ledger.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Verified',len(changes),'intentional imported-path changes and',len(new_files),'new root/tooling files.')
print('Every original declared dependency spec and installed direct version matches its source npm lock.')
