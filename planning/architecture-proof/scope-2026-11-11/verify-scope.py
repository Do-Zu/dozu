"""Verify approved scope changes and preservation of live issue/Project metadata."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[2]
def read(name):return json.loads((OUT/name).read_text(encoding='utf-8-sig'))
before={i['number']:i for i in read('issues-before.json')}
after={i['number']:i for i in read('issues-after.json')}
targets={u['number'] for u in read('updates.json')}
assert before.keys()==after.keys()
for number,old in before.items():
    new=after[number]
    for key in ['state','assignees','closedAt']:
        assert old[key]==new[key],f'{number} {key} changed; review concurrent edits without reverting'
    assert sorted(l['name'] for l in old['labels'])==sorted(l['name'] for l in new['labels'])
    if number in targets:
        assert '<!-- dozu-v1-scope-2026-11-11:start -->' in new['body']
        assert old['body'].count('- [x]')==new['body'].count('- [x]')
    else:
        assert old['title']==new['title'] and old['body']==new['body']
assert after[4]['state']=='OPEN' and 'status:in-progress' in [l['name'] for l in after[4]['labels']]
assert after[2]['state']=='CLOSED' and after[3]['state']=='CLOSED'
assert 'pgvector deferred' in after[29]['title']
assert 'text-embedding' in after[8]['title']
for number in [4,8,21,23,25,29,32,38,45,46,47]:
    acceptance=after[number]['body'].split('## Acceptance criteria',1)[1].split('## Architecture constraints',1)[0] if '## Architecture constraints' in after[number]['body'] else after[number]['body'].split('## Acceptance criteria',1)[1].split('## Tracking',1)[0]
    assert '- [x]' not in acceptance
board_before={i['id']:i for i in read('project-items-before.json')['items']}
board_after={i['id']:i for i in read('project-items-after.json')['items']}
assert board_before.keys()==board_after.keys()
for key,item in board_before.items():
    # Issue bodies/titles intentionally propagate to built-in Project fields.
    old={k:v for k,v in item.items() if k not in {'title','content'}}
    new={k:v for k,v in board_after[key].items() if k not in {'title','content'}}
    assert old==new,f'Project metadata changed for {key}; inspect without overwriting'
assert read('project-fields-before.json')==read('project-fields-after.json')
source=[]
for name in ['dozu-ui-service','dozu-api-service','dozu-embedding-service']:
    status=subprocess.check_output(['git','-C',str(ROOT/name),'status','--porcelain'],text=True)
    source.append({'name':name,'status':status})
    assert not status,'Source changes observed; inspect before claiming unchanged'
hashes=[]
paths=[ROOT/'planning/v1-scope-2026-11-11.md',ROOT/'planning/platform-support.md',ROOT/'planning/requirements.md',ROOT/'planning/feature-preservation.json',ROOT/'planning/issues.json',*OUT.glob('*.md')]
for path in paths:
    hashes.append({'path':str(path.relative_to(ROOT)),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
result={'utc':datetime.now(timezone.utc).isoformat(),'affectedIssues':sorted(targets),'issueStatesLabelsAssigneesPreserved':True,'allProjectCustomFieldsAndDefinitionsPreserved':True,'originalAuditIssue3Unchanged':True,'noAcceptanceMarkedComplete':True,'sourceTrees':source,'pageInventory':84,'speechToText':'DEFERRED_V1','database':'POSTGRESQL_RETAINED','pgvector':'DEFERRED_V1','textEmbedding':'RETAINED_FOR_PDF_YOUTUBE_REFERENCES','implementationState':'Planning/acceptance scope updated; no runtime removal, schema migration or optimized model implemented','hashes':hashes}
(OUT/'verification.json').write_text(json.dumps(result,indent=2),encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in result.items() if k!='hashes'},indent=2))
