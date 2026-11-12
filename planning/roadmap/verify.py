"""Verify narrow remote changes and refresh local read-only tracking snapshots."""
import collections
import datetime
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
def read(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))
def write(path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

before = {x['number']: x for x in read(HERE / 'issues-before.json')}
after = {x['number']: x for x in read(HERE / 'issues-after.json')}
external_body_changes = []
assert set(before) == set(after)
expected_status = {1: 'in-progress', 4: 'closed', 5: 'in-progress'}
for n, old in before.items():
    new = after[n]
    for key in ('assignees', 'state', 'state_reason', 'milestone', 'title'):
        assert old[key] == new[key], (n, key)
    oldlabels = {x['name'] for x in old['labels']}
    newlabels = {x['name'] for x in new['labels']}
    if n in expected_status:
        assert newlabels == {x for x in oldlabels if not x.startswith('status:')} | {'status:' + expected_status[n]}
    else:
        assert oldlabels == newlabels, n
    if n == 1:
        assert new['body'].replace('\r\n', '\n') == (HERE / 'issue-1.md').read_text(encoding='utf-8')
    else:
        if old['body'] != new['body']:
            external_body_changes.append(n)
            assert n == 4 and old['body'].replace('- [ ]', '- [x]', 8) == new['body'], n

board_before = read(HERE / 'project-before.json')
board_after = read(HERE / 'project-after.json')
assert read(HERE / 'fields-before.json') == read(HERE / 'fields-after.json')
olditems = {x['id']: x for x in board_before['items']}
newitems = {x['id']: x for x in board_after['items']}
assert olditems.keys() == newitems.keys()
for itemid, old in olditems.items():
    new = newitems[itemid]
    number = old['content'].get('number')
    assert {k:v for k,v in old.items() if k not in ('status','labels','content')} == {k:v for k,v in new.items() if k not in ('status','labels','content')}, number
    assert new.get('status') == ('In Progress' if number in (1,5) else old.get('status')), number
    assert {k:v for k,v in old['content'].items() if k != 'body'} == {k:v for k,v in new['content'].items() if k != 'body'}
    assert new['content']['body'] == after[number]['body']
    assert set(new.get('labels', [])) == {x['name'] for x in after[number]['labels']}

manifest = read(ROOT / 'planning/issues.json')
byid = {}
for draft in manifest['issues']:
    matches = [x for x in after.values() if '<!-- dozu-roadmap:' + draft['id'] + ' -->' in (x['body'] or '')]
    assert len(matches) == 1, draft['id']
    byid[draft['id']] = matches[0]
snapshot = read(ROOT / 'planning/tracking-snapshot.json')
snapshot['capturedAtUtc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
rows = []
for draft in manifest['issues']:
    issue = byid[draft['id']]
    labels = [x['name'] for x in issue['labels']]
    def label(prefix):
        found = [x.removeprefix(prefix) for x in labels if x.startswith(prefix)]
        assert len(found) == 1
        return found[0]
    status = label('status:')
    if issue['state'] == 'closed':
        assert status == ('done' if issue['state_reason'] == 'completed' else 'closed')
    waiting = [byid[d]['html_url'] for d in draft['dependsOn'] if not (byid[d]['state'] == 'closed' and byid[d]['state_reason'] == 'completed')]
    rows.append(dict(id=draft['id'], number=issue['number'], url=issue['html_url'],
        type=draft['label'], title=issue['title'], status=status, priority=label('priority:'),
        complexity=label('complexity:'), assignees=[x['login'] for x in issue['assignees']],
        waitingOn=waiting, blockReason=draft.get('blockReason', '')))
snapshot['issues'] = rows
snapshot['completedTaskCount'] = sum(x['type'] == 'task' and x['status'] == 'done' for x in rows)
snapshot['totalTaskCount'] = sum(x['type'] == 'task' for x in rows)
snapshot['statusCounts'] = [dict(status=k,count=v) for k,v in sorted(collections.Counter(x['status'] for x in rows).items())]
write(ROOT / 'planning/tracking-snapshot.json', snapshot)
md = '# Task dashboard\n\nSnapshot UTC: ' + snapshot['capturedAtUtc'] + '. Read back from live GitHub; no remote fields changed by this verifier.\n\n'
md += 'Completed tasks (including audit): ' + str(snapshot['completedTaskCount']) + '/' + str(snapshot['totalTaskCount']) + '. #4 is closed not planned and is excluded from completion. Original 44-item manifest; board has 47 items including native proof children.\n\n'
md += '| Issue | Status | Priority | Complexity | Owner | Unfinished prerequisites |\n| --- | --- | --- | --- | --- | --- |\n'
for x in rows:
    md += f"| [#{x['number']}]({x['url']}) {x['title']} | {x['status']} | {x['priority']} | {x['complexity']} | {', '.join(x['assignees']) or 'Unassigned'} | {', '.join(x['waitingOn']) or 'None'} |\n"
(ROOT / 'planning/task-dashboard.md').write_text(md, encoding='utf-8')
proof = dict(capturedAtUtc=snapshot['capturedAtUtc'], issueChangesVerified=[1,4,5],
    parentBodyVerified=True, allAssignmentsPreserved=True, allIssueStatesPreserved=True,
    unrelatedIssueLabelsPreserved=True, allBoardItemsAndFieldsPreserved=True,
    externalIssueBodyChanges=external_body_changes,
    externalChangeNote='During execution #4 acceptance and P1-P3 boxes were checked externally. This task only changed its status label. No completion evidence was supplied by that edit; state remains closed/not_planned and no requirement is counted complete.',
    boardStatusChangesOnly=[1,5], boardItemCount=len(newitems),
    completedIssues=[n for n,i in after.items() if i['state']=='closed' and i['state_reason']=='completed'],
    missingLocalEvidence=[p for p in ['planning/architecture-proof/postgres-only/report.md',
        'planning/architecture-proof/backend-local/report.md','planning/desktop-preview/README.md'] if not (ROOT/p).exists()])
write(HERE / 'verification.json', proof)
print(json.dumps(proof, indent=2))
