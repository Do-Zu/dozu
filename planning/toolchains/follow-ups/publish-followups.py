"""Publish the two user-requested missing follow-ups without replacing existing ownership/fields."""
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
REPO = 'Do-Zu/dozu'
PROJECT = 'PVT_kwDODsVOHc4Bq0ro'

def gh(*args):
    result = subprocess.run(['gh', *args], capture_output=True, text=True, encoding='utf-8')
    if result.returncode:
        raise RuntimeError(result.stderr)
    return result.stdout.strip()

def save(name, value):
    (HERE/name).write_text(json.dumps(value, indent=2)+'\n', encoding='utf-8')

before = json.loads((HERE/'issue-7-before.json').read_text(encoding='utf-8'))
live = json.loads(gh('issue','view','7','--repo',REPO,'--json','number,title,body,state,labels,assignees'))
addendum = (HERE/'issue-7-addendum.md').read_text(encoding='utf-8')
marker = '<!-- dozu-toolchains-followup-ledger:start -->'
if marker not in live['body']:
    if live['body'] != before['body']:
        raise RuntimeError('Issue #7 changed since review; preserve and review concurrent changes before editing')
    gh('issue','edit','7','--repo',REPO,'--body-file',str(HERE/'issue-7-updated.md'))
    print('Linked remaining acceptance work on #7', flush=True)

children = json.loads(gh('api',f'repos/{REPO}/issues/7/sub_issues'))
child_ids = {i['id'] for i in children}
specs = [(48,'framework-security','L',[6]),(49,'native-script-portability','M',[6,48])]
fields = json.loads((HERE/'project-fields.json').read_text(encoding='utf-8'))['fields']
items_before = json.loads(gh('project','item-list','6','--owner','Do-Zu','--limit','100','--format','json'))['items']
save('project-items-before.json',[i for i in items_before if i.get('content',{}).get('number') in [7,48,49]])

for number, key, complexity, dependencies in specs:
    issue = json.loads(gh('api',f'repos/{REPO}/issues/{number}'))
    if f'<!-- dozu-toolchains-followup:{key} -->' not in issue['body']:
        raise RuntimeError(f'Unexpected issue #{number}; refusing to modify it')
    if issue['id'] not in child_ids:
        gh('api','--method','POST',f'repos/{REPO}/issues/7/sub_issues','-F',f'sub_issue_id={issue["id"]}')
    matching = next((i for i in items_before if i.get('content',{}).get('number') == number),None)
    if matching:
        # Respect any existing populated custom fields; fill missing values only.
        item = matching
    else:
        item = json.loads(gh('project','item-add','6','--owner','Do-Zu','--url',issue['html_url'],'--format','json'))
    desired = {'Status':'Todo','Priority':'P0','Complexity':complexity,'Phase':'1 Foundation',
               'Depends on':'\n'.join(f'https://github.com/{REPO}/issues/{n}' for n in dependencies),
               'Blocker':'None'}
    for name, value in desired.items():
        if matching and matching.get(name.lower()):
            continue
        definition = next(f for f in fields if f['name'] == name)
        args = ['project','item-edit','--id',item['id'],'--project-id',PROJECT,'--field-id',definition['id']]
        if definition.get('options'):
            args += ['--single-select-option-id',next(o['id'] for o in definition['options'] if o['name'] == value)]
        else:
            args += ['--text',value]
        gh(*args)
    print(f'Linked #{number} as child and added Project item', flush=True)

after = json.loads(gh('issue','view','7','--repo',REPO,'--json','number,title,body,state,labels,assignees,projectItems'))
assert after['state'] == 'OPEN'
assert after['assignees'] == before['assignees']
assert sorted(x['name'] for x in after['labels']) == sorted(x['name'] for x in before['labels'])
assert after['body'].startswith(before['body'].rstrip())
assert before['body'].count('- [ ]') == 5 and after['body'].count('- [ ]') == 5
save('issue-7-final.json',after)
save('subissues-final.json',json.loads(gh('api',f'repos/{REPO}/issues/7/sub_issues')))
items_after = json.loads(gh('project','item-list','6','--owner','Do-Zu','--limit','100','--format','json'))['items']
selected = [i for i in items_after if i.get('content',{}).get('number') in [7,48,49]]
save('project-items-final.json',selected)
old_parent = next(i for i in items_before if i.get('content',{}).get('number') == 7)
new_parent = next(i for i in items_after if i.get('content',{}).get('number') == 7)
for field in ['id','status','priority','complexity','phase','depends on','blocker']:
    assert old_parent.get(field) == new_parent.get(field),field
assert new_parent['status'] == 'In Progress'
for number in [48,49]:
    current = json.loads(gh('issue','view',str(number),'--repo',REPO,'--json','number,title,body,state,labels,assignees,projectItems'))
    save(f'issue-{number}-final.json',current)
    assert current['state'] == 'OPEN' and current['assignees'] == []
    project = next(i for i in selected if i.get('content',{}).get('number') == number)
    assert project['status'] == 'Todo' and project['priority'] == 'P0'
save('verification.json',{'issue7Open':True,'fullAcceptanceCriteriaUnchecked':5,
    'existingAssignmentLabelsAndCustomFieldsPreserved':True,'newIssues':[48,49],
    'newIssuesOpenUnassignedAndOnProject':True,'parentChildLinksVerified':True})
print('Verified open parent, preserved fields, both child issues and Project items',flush=True)
