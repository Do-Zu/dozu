"""Verify narrowly scoped remote changes, then preserve the checklist locally."""
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from inventory import OUT,ROOT

def read(name):return json.loads((OUT/name).read_text(encoding='utf-8-sig'))
before=read('issue-4-before.json');after=read('issue-4-after.json')
items_before={i['id']:i for i in read('project-items-before.json')['items']}
items_after={i['id']:i for i in read('project-items-after.json')['items']}
children=read('native-subissues.json')
assert after['state']=='OPEN'
assert [l['name'] for l in after['labels'] if l['name'].startswith('status:')]==['status:in-progress']
assert after['assignees']==before['assignees']==[]
assert 'In Progress' in [p.get('status',{}).get('name') for p in after['projectItems']]
parent=next(i for i in items_after.values() if i.get('content',{}).get('number')==4)
assert parent['status']=='In Progress' and parent['priority']=='P0' and parent['complexity']=='XL'
assert read('project-fields-before.json')==read('project-fields-after.json')
changes=[]
for key,item in items_before.items():
    assert key in items_after,'Existing Project item removed'
    if item.get('content',{}).get('number')!=4 and item!=items_after[key]:
        changes.append({'number':item.get('content',{}).get('number'),'fields':{k:{'before':item.get(k),'after':items_after[key].get(k)} for k in set(item)|set(items_after[key]) if item.get(k)!=items_after[key].get(k)}})
# Readback observed concurrent Assignee additions on #2/#3. These were not
# mutated by this task. Preserve them and report the observation, never restore
# old values simply to make a snapshot comparison pass.
assert all(set(change['fields'])=={'assignees'} for change in changes),f'Additional unrelated changes to inspect and preserve: {changes}'
assert {i['number'] for i in read('subissues-after.json')}=={i['number'] for i in children}
for child in children:
    item=items_after[child['itemId']]
    assert item['status']=='Todo' and item['priority']=='P0' and item['complexity']=='L'
    assert 'status:waiting' in item['labels']
    assert len([l for l in item['labels'] if l.startswith('status:')])==1
    assert not item.get('assignees')
    assert 'not parent closure' in item['depends on']
acceptance=lambda body:body.replace('\r','').split('## Acceptance criteria',1)[1].split('## Architecture constraints',1)[0]
assert acceptance(before['body'])==acceptance(after['body'])
assert '- [x]' not in acceptance(after['body'])
marker='<!-- dozu-proof-checklist:start -->'
checklist=after['body'].replace('\r','').split(marker,1)[1].split('<!-- dozu-proof-checklist:end -->',1)[0]
assert '- [x]' not in checklist
manifest_path=ROOT/'planning/issues.json'
manifest=json.loads(manifest_path.read_text(encoding='utf-8-sig'))
draft=next(i for i in manifest['issues'] if i['id']=='DECISION-STACK')
if marker not in draft['body']:
    draft['body']+='\n\n'+marker+checklist+'<!-- dozu-proof-checklist:end -->'
    manifest_path.write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

# Preserve the original roadmap snapshot's timestamp/counts. Explicitly name
# this scoped refresh, instead of claiming unrelated issues were refreshed.
snapshot_path=ROOT/'planning/tracking-snapshot.json'
snapshot=json.loads(snapshot_path.read_text(encoding='utf-8-sig'))
next(i for i in snapshot['issues'] if i['number']==4)['status']='in-progress'
now=datetime.now(timezone.utc).isoformat()
snapshot['scopedProofRefresh']={'utc':now,'issues':[4,*[i['number'] for i in children]],'baseSnapshotUnchanged':'Original 44-item roadmap timestamp/counts remain; unrelated issues not refreshed. Three native proof subissues below are additional. No assignee inferred per user instruction.'}
snapshot['proofSubissues']=[dict(i,status='waiting',priority='P0',complexity='L',assignees=[],parent=4,waitingOnExperiments='P1–P5, not parent closure') for i in children]
snapshot_path.write_text(json.dumps(snapshot,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
dashboard=ROOT/'planning/task-dashboard.md'
text=dashboard.read_text(encoding='utf-8-sig')
lines=text.splitlines()
for index,line in enumerate(lines):
    if line.startswith('| [#4]('):
        lines[index]=line.replace('| ticket | ready |','| ticket | in-progress |')
text='\n'.join(lines)+'\n'
note='<!-- dozu-proof-snapshot:start -->'
if note in text:text=text.split(note,1)[0].rstrip()+'\n'
text+=f'''\n{note}
## Scoped #4 update — 2026-11-10

#4 is in progress / Project In Progress, without an inferred assignee. The original snapshot and 40-task roadmap count above remain historical; only #4 and the three new proof subissues were refreshed at {now}. They do not change the feature implementation completion count.

| Additional native proof | Status / Project | Prerequisite |
| --- | --- | --- |
| [#45 Windows](https://github.com/Do-Zu/dozu/issues/45) | waiting / Todo | #4 P1–P5 shared component experiments, not parent closure |
| [#46 macOS x64/ARM64](https://github.com/Do-Zu/dozu/issues/46) | waiting / Todo | Same; native hosts unavailable here |
| [#47 Linux x64](https://github.com/Do-Zu/dozu/issues/47) | waiting / Todo | Same; native hosts unavailable here |

[First proof findings and measured footprint failure](architecture-proof/report.md). All #4 acceptance gates remain unchecked. Local issues.json preserves the linked checklist for a later publisher run; the separate native subissues are intentionally not folded into its original 44-item delivery manifest.
<!-- dozu-proof-snapshot:end -->
'''
dashboard.write_text(text,encoding='utf-8')
verification={'utc':now,'issue4OpenInProgress':True,'project4InProgress':True,'originalAcceptanceUnchangedAndUnchecked':True,'issue4AssigneesUnchangedEmpty':True,'nativeSubissues':children,'newItems':len(items_after)-len(items_before),'concurrentUnrelatedChangesObservedAndPreserved':changes,'unrelatedExistingCustomFieldsChanged':[],'originalProjectFieldsUnchanged':True,'progressCommentUrl':after['comments'][-1]['url'],'localSnapshotRefreshScope':[4,45,46,47]}
(OUT/'tracking-verification.json').write_text(json.dumps(verification,indent=2),encoding='utf-8')
print(json.dumps(verification,indent=2),flush=True)
