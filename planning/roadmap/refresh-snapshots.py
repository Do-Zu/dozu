"""Read-only tracking refresh; preserve all live labels and project values."""
import collections
import datetime
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
def gh(*args):
    return json.loads(subprocess.check_output(['gh', *args], text=True, encoding='utf-8'))
def read(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))
def write(path,obj):
    path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

issues = gh('api','repos/Do-Zu/dozu/issues?state=all&per_page=100')
board = gh('project','item-list','6','--owner','Do-Zu','--format','json','--limit','100')
write(HERE/'issues-current.json',issues)
write(HERE/'project-current.json',board)
manifest = read(ROOT/'planning/issues.json')
snapshot = read(ROOT/'planning/tracking-snapshot.json')
snapshot['capturedAtUtc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
byid = {}
for draft in manifest['issues']:
    found = [i for i in issues if '<!-- dozu-roadmap:'+draft['id']+' -->' in (i.get('body') or '')]
    assert len(found)==1,draft['id']
    byid[draft['id']]=found[0]
rows=[]
for draft in manifest['issues']:
    i=byid[draft['id']]
    def label(prefix):
        values=[x['name'][len(prefix):] for x in i['labels'] if x['name'].startswith(prefix)]
        assert len(values)==1,(i['number'],prefix)
        return values[0]
    waiting=[byid[d]['html_url'] for d in draft['dependsOn'] if not (byid[d]['state']=='closed' and byid[d]['state_reason']=='completed')]
    rows.append(dict(id=draft['id'],number=i['number'],url=i['html_url'],title=i['title'],
        type=draft['label'],status=label('status:'),priority=label('priority:'),complexity=label('complexity:'),
        state=i['state'],stateReason=i['state_reason'],assignees=[a['login'] for a in i['assignees']],
        waitingOn=waiting,blockReason=draft.get('blockReason','')))
snapshot['issues']=rows
snapshot['completedTaskCount']=sum(x['type']=='task' and x['status']=='done' and x['stateReason']=='completed' for x in rows)
snapshot['totalTaskCount']=sum(x['type']=='task' for x in rows)
snapshot['statusCounts']=[dict(status=k,count=v) for k,v in sorted(collections.Counter(x['status'] for x in rows).items())]
snapshot['trackingWarnings']=[dict(number=x['number'],message='Live state reason is completed but status label is closed; preserved external values. No runtime acceptance is inferred.') for x in rows if x['stateReason']=='completed' and x['status']=='closed']
write(ROOT/'planning/tracking-snapshot.json',snapshot)
md='# Task dashboard\n\nSnapshot UTC: '+snapshot['capturedAtUtc']+'. Read-only live refresh; labels and project fields are preserved.\n\n'
md+=f"Completed tasks (including audit): {snapshot['completedTaskCount']}/{snapshot['totalTaskCount']}. Original manifest: 44 issues; project: {len(board['items'])} items. Counts do not establish product/runtime parity.\n\n"
for warning in snapshot['trackingWarnings']:
    md+=f"Tracking warning #{warning['number']}: {warning['message']}\n\n"
md+='| Issue | Status | Priority | Complexity | Owner | Unfinished prerequisites |\n| --- | --- | --- | --- | --- | --- |\n'
for x in rows:
    md+=f"| [#{x['number']}]({x['url']}) {x['title']} | {x['status']} | {x['priority']} | {x['complexity']} | {', '.join(x['assignees']) or 'Unassigned'} | {', '.join(x['waitingOn']) or 'None'} |\n"
(ROOT/'planning/task-dashboard.md').write_text(md,encoding='utf-8')
summary=read(ROOT/'planning/project-board-verification.json')
summary.update(capturedAtUtc=snapshot['capturedAtUtc'],totalProjectItems=len(board['items']),
    boardStatuses=[dict(status=k,count=v) for k,v in sorted(collections.Counter(x.get('status','Unset') for x in board['items']).items())],
    assignedItems=sum(bool(x.get('assignees')) for x in board['items']),
    verificationScope='Read-only live snapshot after delegated #5/#6 work; no unrelated board fields changed by refresh.',
    completedIssueNumbers=[x['number'] for x in rows if x['stateReason']=='completed'],
    closedNotPlannedIssueNumbers=[x['number'] for x in rows if x['stateReason']=='not_planned'],
    trackingWarnings=snapshot['trackingWarnings'])
write(ROOT/'planning/project-board-verification.json',summary)
print(json.dumps(dict(completedTaskCount=snapshot['completedTaskCount'],
    foundation=[x for x in rows if x['number'] in (5,6)],warnings=snapshot['trackingWarnings']),indent=2))
