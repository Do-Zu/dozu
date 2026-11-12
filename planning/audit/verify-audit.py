"""Independent audit coverage, provenance and document-reference validation."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
def read(name): return json.loads((HERE/name).read_text(encoding='utf-8'))
sources = read('source-inventory.json')
by_source = {s['source']:s for s in sources}
ui = read('ui-workflows.json')
matrix = read('feature-parity.json')['pages']
api = read('backend-endpoints.json')
database = read('database-inventory.json')
old = json.loads((ROOT/'planning/route-inventory.json').read_text(encoding='utf-8'))
errors = []
def check(condition, message):
    if not condition: errors.append(message)

for p in read('source-provenance.json'):
    repo = ROOT / p['repo']
    head = subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD'],text=True).strip()
    dirty = subprocess.check_output(['git','-C',str(repo),'status','--porcelain=v1'],text=True).strip()
    check(head==p['commit'], 'Source commit changed: '+p['repo'])
    check(dirty==p['dirty']=='', 'Source dirty tree changed: '+p['repo'])

for s in sources:
    file=ROOT/s['source']
    check(hashlib.sha256(file.read_bytes()).hexdigest()==s['sha256'], 'Source hash mismatch: '+s['source'])
    check(not Path(s['source']).name.startswith('.env'), 'Secret path in source payload')

pages={s['source'] for s in sources if s['source'].startswith('dozu-ui-service/src/app/') and s['source'].endswith('/page.tsx')}
check(pages=={p['source'] for p in ui['pages']}=={p['source'] for p in matrix}=={p['source'] for p in old['pages']},'Page coverage mismatch')
check(len(pages)==84 and len(ui['layouts'])==20,'Original page/layout counts changed')
check(len([s for s in sources if s['source'].startswith('dozu-ui-service/src/components/') and s['source'].endswith('.tsx')])==164,'Shared component count changed')
all_nonentry={s['source'] for s in sources if s['source'].startswith('dozu-ui-service/src/') and s['source'].endswith('.tsx') and not s['source'].endswith(('/page.tsx','/layout.tsx'))}
check(all_nonentry=={s['source'] for s in ui['components']},'Missing TSX component')
check(all(m['workflow'] and m['followUpIssues'] and m['runtimeParity']=='UNVERIFIED' and m['locales']==['en','vi'] for m in matrix),'Matrix missing workflow/uncertainty/locale')
for p in ui['pages']:
    check('dozu-ui-service/src/app/layout.tsx' in p['layouts'],'Root layout missing for '+p['route'])
    check('dozu-ui-service/src/app/[locale]/layout.tsx' in p['layouts'],'Locale layout missing for '+p['route'])
    for s in p['ownReach']+p['withLayoutReach']:
        check(s in by_source,'Invalid source closure: '+s)

seen={(e['source'],e['line']) for e in api['endpoints']}
unmounted=set(api['unreachableRouteFiles'])
unmapped=[]
for s in sources:
    if not s['source'].startswith('dozu-api-service/src/routes/'): continue
    for c in s['calls']:
        if c['kind']=='route' and c['callee'].split('.')[-1] in ['get','post','put','patch','delete','all'] and (s['source'],c['line']) not in seen:
            unmapped.append({'source':s['source'],'line':c['line'],'method':c['callee'],'path':c['path']})
            check(s['source'] in unmounted,'Unexplained unmapped endpoint '+str(unmapped[-1]))
check(len(api['endpoints'])==len({(e['method'],e['path']) for e in api['endpoints']})==330,'Endpoint duplicate/count mismatch')
webhook=next(e for e in api['endpoints'] if e['path']=='/api/payment/payos/webhook')
check(not any('authMiddleware' in m['middleware'] for m in webhook['middlewareChain']),'Wrong middleware order for public signed webhook')
check(len(database['migrations'])==len(database['journal']['entries'])==20,'Migration count mismatch')
check(all(not m['tracked'] for m in database['migrations']),'Migration tracked-state mismatch')
check(all((ROOT/m['source']).exists() for m in database['migrations']),'Missing local migration artifact')

references=0
for doc in HERE.glob('*.md'):
    for target in re.findall(r'\]\((<[^>]+>|[^)]+)\)',doc.read_text(encoding='utf-8')):
        target=unquote(target.strip('<>').split('#')[0])
        if not target or re.match(r'^[a-z]+://',target): continue
        references+=1
        check((doc.parent/target).exists(),f'Broken document link {doc.name}: {target}')

checks=read('baselines/results.json')
check({c['check'] for c in checks}>={'ui-lint','ui-build','api-typecheck','api-lint','api-jest','embedding-startup'},'Missing required baseline')
check(next(c for c in checks if c['check']=='api-typecheck')['exitCode']==0,'Corrected API typecheck no longer passes')
for c in checks+read('baselines/jest-suites.json'):
    check((HERE/c['log']).exists(),'Missing baseline log '+c['log'])
contract=read('baselines/embedding-contract.json')
check(contract['dimension']==384 and abs(contract['norm']-1)<.001,'Real embedding vector contract invalid')
check(len(contract['checks'])==10,'Missing real HTTP contract outcomes')
failures=[c for c in contract['checks'] if c['status']!=c['expected']]
check(len(failures)==1 and failures[0]['path']=='/segments/embedding' and failures[0]['status']==500,'Undocumented embedding contract change')

result={'auditDate':'2026-11-09','result':'PASS' if not errors else 'FAIL','sourceCommitsAndTreesUnchanged':not any('Source' in e for e in errors),'sourceFilesHashed':len(sources),'pageRows':len(matrix),'layouts':len(ui['layouts']),'nonEntryTsx':len(ui['components']),'hookProviderContextFiles':len(ui['hooksAndProviders']),'navigationSites':len(ui['navigation']),'mountedApiContracts':len(api['endpoints']),'unmountedDeclarationsExplained':unmapped,'localMigrationArtifacts':len(database['migrations']),'documentLinksChecked':references,'embeddingObservedFailures':failures,'errors':errors,'note':'PASS validates audit coverage/references and expected recorded baselines. It does not mean application tests or desktop parity pass.'}
(HERE/'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
raise SystemExit(bool(errors))
