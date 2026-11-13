"""Record this user-approved scope change without closing tickets or changing metadata."""
import json
from pathlib import Path
import subprocess

HERE=Path(__file__).resolve().parent
REPO='Do-Zu/dozu'
def gh(*args):
    result=subprocess.run(['gh',*args],capture_output=True,text=True,encoding='utf-8')
    if result.returncode:raise RuntimeError(result.stderr)
    return result.stdout.strip()
def snapshot(number):
    return json.loads(gh('issue','view',str(number),'--repo',REPO,'--json',
                         'number,title,body,state,labels,assignees,projectItems'))
def save(name,value):
    (HERE/name).write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8')

before={n:snapshot(n) for n in [7,40,41]}
save('tracking-before.json',before)
marker='<!-- dozu-v1-payments-excluded-2026-11-13:start -->'
if marker not in before[41]['body']:
    text=before[41]['body'].rstrip()+'\n\n'+(HERE/'issue-41-scope-note.md').read_text(encoding='utf-8')
    bodyfile=HERE/'issue-41-published.md'
    bodyfile.write_text(text,encoding='utf-8')
    gh('issue','edit','41','--repo',REPO,'--body-file',str(bodyfile))

urls={}
for number,filename in [(7,'github-progress.md'),(40,'startup-handoff.md')]:
    comment_marker=f'<!-- dozu-payments-removal-checkpoint:{number}:2026-11-13 -->'
    pages=json.loads(gh('api',f'repos/{REPO}/issues/{number}/comments?per_page=100','--paginate','--slurp'))
    existing=next((c for page in pages for c in page if comment_marker in c['body']),None)
    if existing:
        urls[number]=existing['html_url']
    else:
        comment=HERE/f'comment-{number}.md'
        comment.write_text(comment_marker+'\n'+(HERE/filename).read_text(encoding='utf-8'),encoding='utf-8')
        urls[number]=gh('issue','comment',str(number),'--repo',REPO,'--body-file',str(comment))
    print(urls[number],flush=True)

after={n:snapshot(n) for n in [7,40,41]}
for number in before:
    for key in ['title','state','labels','assignees','projectItems']:
        assert before[number][key]==after[number][key],(number,key)
    assert before[number]['body'].count('- [ ]')==after[number]['body'].count('- [ ]'),number
assert marker in after[41]['body']
assert after[7]['state']=='OPEN'
save('tracking-after.json',after)
save('tracking-verification.json',{'statesLabelsAssignmentsAndProjectFieldsPreserved':True,
     'allExistingAcceptanceBoxesPreserved':True,'paymentExclusionRecordedOn41':True,
     'issue7StillOpen':True,'commentUrls':urls})
print('Verified scope note, startup handoffs and unchanged tracking metadata',flush=True)
