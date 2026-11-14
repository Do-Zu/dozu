"""Apply only the explicit user-approved foundation closure and verify its boundaries."""
import json
from pathlib import Path
import subprocess

HERE=Path(__file__).resolve().parent
REPO='Do-Zu/dozu'
PROJECT='PVT_kwDODsVOHc4Bq0ro'
before=json.loads((HERE/'issues-before.json').read_text(encoding='utf-8'))
plan=json.loads((HERE/'plan.json').read_text(encoding='utf-8'))
fields=json.loads((HERE/'project-fields.json').read_text(encoding='utf-8'))['fields']
def gh(*args):
    r=subprocess.run(['gh',*args],capture_output=True,text=True,encoding='utf-8')
    if r.returncode:raise RuntimeError(r.stderr)
    return r.stdout.strip()
def save(name,value):
    (HERE/name).write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8')
def issue(number):
    return json.loads(gh('issue','view',str(number),'--repo',REPO,'--json',
        'number,id,title,body,state,labels,assignees,projectItems'))
def labels(value):return sorted(x['name'] for x in value['labels'])
def edit_body(number,title=None):
    current=issue(number)
    wanted=(HERE/f'issue-{number}.md').read_text(encoding='utf-8')
    if current['body'] not in [before[str(number)]['body'],wanted]:
        raise RuntimeError(f'Concurrent body edit on #{number}; refusing to overwrite')
    assert current['assignees']==before[str(number)]['assignees']
    args=['issue','edit',str(number),'--repo',REPO,'--body-file',str(HERE/f'issue-{number}.md')]
    if title:args+=['--title',title]
    gh(*args)
def set_label(number,status):
    current=issue(number)
    previous=[x for x in labels(current) if x.startswith('status:')]
    args=['issue','edit',str(number),'--repo',REPO,'--add-label',f'status:{status}']
    for label in previous:
        if label!=f'status:{status}':args+=['--remove-label',label]
    gh(*args)
def set_field(item,name,value):
    definition=next(x for x in fields if x['name']==name)
    args=['project','item-edit','--id',item['id'],'--project-id',PROJECT,'--field-id',definition['id']]
    if definition.get('options'):
        args+=['--single-select-option-id',next(o['id'] for o in definition['options'] if o['name']==value)]
    else:args+=['--text',value]
    gh(*args)
def items():
    return json.loads(gh('project','item-list','6','--owner','Do-Zu','--limit','100','--format','json'))['items']

assert gh('api',f'repos/{REPO}/commits/dev','--jq','.sha')=='8e7b7d134ec450ecd0244ab8deaee3d67b9379bb'
initial_items=items()
save('project-live-before-publish.json',{'items':initial_items})
edit_body(7,plan['issue7Title'])
for number in [48,49]:
    parent=json.loads(gh('api',f'repos/{REPO}/issues/{number}/parent'))
    assert parent['number'] in [1,7],(number,parent['number'])
    if parent['number']!=1:
        numeric_id=gh('api',f'repos/{REPO}/issues/{number}','--jq','.id')
        gh('api','--method','POST',f'repos/{REPO}/issues/1/sub_issues',
           '-F',f'sub_issue_id={numeric_id}','-F','replace_parent=true')
    edit_body(number)
    print(f'#{number} remains open under roadmap #1',flush=True)
edit_body(38)

# Record the scope/evidence before transitioning the issue to completed.
marker='<!-- dozu-scoped-foundation-completion:2026-11-13 -->'
pages=json.loads(gh('api',f'repos/{REPO}/issues/7/comments?per_page=100','--paginate','--slurp'))
existing=next((c for page in pages for c in page if marker in c['body']),None)
if existing:comment_url=existing['html_url']
else:
    file=HERE/'published-comment.md'
    file.write_text(marker+'\n'+(HERE/'completion-comment.md').read_text(encoding='utf-8'),encoding='utf-8')
    comment_url=gh('issue','comment','7','--repo',REPO,'--body-file',str(file))
set_label(7,'done')
if issue(7)['state']!='CLOSED':gh('issue','close','7','--repo',REPO,'--reason','completed')
parent_item=next(i for i in initial_items if i.get('content',{}).get('number')==7)
set_field(parent_item,'Status','Done')
set_field(parent_item,'Depends on','https://github.com/Do-Zu/dozu/issues/6')
print('#7 completed for the revised tooling foundation; Project Done',flush=True)

# Only this now-satisfied direct prerequisite is promoted. No bulk sync of contradictory #4 metadata.
assert issue(6)['state']=='CLOSED' and issue(7)['state']=='CLOSED'
set_label(38,'ready')
runtime_item=next(i for i in initial_items if i.get('content',{}).get('number')==38)
set_field(runtime_item,'Status','Todo')
edit_body(1)
print('#38 Ready; roadmap delivery list updated',flush=True)

after={str(n):issue(n) for n in [1,4,6,7,38,45,48,49]}
save('issues-final.json',after)
for number in [1,4,6,7,38,45,48,49]:
    old=before[str(number)];new=after[str(number)]
    assert old['assignees']==new['assignees'],('assignee',number)
    if number not in [7,38]:assert labels(old)==labels(new),('labels',number)
    if number not in [7]:assert old['state']==new['state'],('state',number)
    if number in [4,6,45]:assert old['body']==new['body'],('proof body',number)
    if number in [38,48,49]:
        assert old['body'].count('- [ ]')==new['body'].count('- [ ]'),('unpassed criteria',number)
        assert new['state']=='OPEN'
assert after['7']['state']=='CLOSED' and 'status:done' in labels(after['7'])
assert after['7']['body'].count('- [x]')==5 and '- [ ]' not in after['7']['body']
assert '- [x] #7 - '+plan['issue7Title'] in after['1']['body']
assert after['1']['state']=='OPEN'
parents={str(n):json.loads(gh('api',f'repos/{REPO}/issues/{n}/parent')) for n in [48,49]}
assert all(p['number']==1 for p in parents.values())
remaining=json.loads(gh('api',f'repos/{REPO}/issues/7/sub_issues'))
assert not remaining,'Completed foundation must not retain unfinished child tasks'
save('followup-parents-final.json',parents)
final_items=items()
save('project-final.json',{'items':final_items})
for number in [1,7,38,48,49]:
    old=next(i for i in initial_items if i.get('content',{}).get('number')==number)
    new=next(i for i in final_items if i.get('content',{}).get('number')==number)
    for field in ['id','priority','complexity','phase','blocker','assignees']:
        assert old.get(field)==new.get(field),(number,field)
    if number!=7:assert old.get('depends on')==new.get('depends on'),(number,'dependencies')
    if number not in [7,38]:assert old.get('status')==new.get('status'),(number,'status')
assert next(i for i in final_items if i.get('content',{}).get('number')==7)['status']=='Done'
assert next(i for i in final_items if i.get('content',{}).get('number')==7)['depends on']=='https://github.com/Do-Zu/dozu/issues/6'
assert 'status:ready' in labels(after['38'])
save('verification.json',{'scopeSplitExplicitlyAuthorized':True,'foundationIssue':7,'state':'closed',
    'stateReason':gh('api',f'repos/{REPO}/issues/7','--jq','.state_reason'),
    'revisedFoundationCriteriaCompleted':5,'originalBroaderCriteriaArchivedNotPassed':5,
    'openFollowupsMovedToRoadmap':[48,49],'noUnfinishedSubissuesRemainOn7':True,
    'existingRuntimeReleaseCriteriaPreservedUnpassed':True,'nextReadyIssue':38,
    'project7Status':'Done','project38Status':'Todo','assigneesAndUnrelatedFieldsPreserved':True,
    'proofIssues4And45Unchanged':True,'remoteSourceSha':'8e7b7d134ec450ecd0244ab8deaee3d67b9379bb',
    'completionComment':comment_url})
print('Verified completed foundation, open roadmap gates, preserved proof history and next Ready step',flush=True)
