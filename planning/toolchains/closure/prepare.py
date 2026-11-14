"""Read current tracking and prepare the user-authorized foundation scope split."""
import json
from pathlib import Path
import subprocess

HERE=Path(__file__).resolve().parent
REPO='Do-Zu/dozu'
def gh(*args):
    r=subprocess.run(['gh',*args],capture_output=True,text=True,encoding='utf-8')
    if r.returncode:raise RuntimeError(r.stderr)
    return r.stdout.strip()
def save(name,value):
    (HERE/name).write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8')

issues={}
for n in [1,4,6,7,38,45,48,49]:
    issues[n]=json.loads(gh('issue','view',str(n),'--repo',REPO,'--json',
        'number,id,title,body,state,labels,assignees,projectItems'))
save('issues-before.json',issues)
save('remote-dev.json',{'sha':gh('api',f'repos/{REPO}/commits/dev','--jq','.sha')})
assert issues[7]['state']=='OPEN' and issues[6]['state']=='CLOSED'
assert issues[7]['body'].count('- [ ]')==5
assert (HERE/'issue-7.md').read_text(encoding='utf-8').count('- [x]')==5
save('original-acceptance.json',{'issue':7,'title':issues[7]['title'],
    'criteria':[line for line in issues[7]['body'].splitlines() if line.startswith('- [ ]')]})

for n in [48,49]:
    body=issues[n]['body']
    body=body.replace('Parent: #7. Roadmap: #1.', 'Parent: #1. Follow-up from completed tooling foundation: #7.')
    body=body.replace('This child supplies evidence back to #7 and avoids a parent/child dependency cycle.',
        'This independent roadmap follow-up supplies release evidence to #1; it is outside the completed #7 foundation scope.')
    body=body.replace('This issue is a child of #7 and must not wait for #7 closure.',
        'This is an independent roadmap #1 follow-up from completed foundation #7; it does not reopen that foundation scope.')
    body+='\n\n<!-- dozu-foundation-split-2026-11-13 -->\nThe user explicitly authorized closing #7 for its delivered JavaScript tooling foundation and moving later desktop acceptance to independent issues. This issue stays open and is parented to roadmap #1. Its original acceptance boxes and metadata are preserved. This work remains a required desktop release gate; #7 closure is not evidence it passed. Redis remains retained, while outgoing email, local STT and payment execution are excluded by explicit user scope amendments.\n'
    (HERE/f'issue-{n}.md').write_text(body,encoding='utf-8')

title='[Task] Pin portable JavaScript build toolchains and developer entry points'
body=issues[1]['body']
old='- [ ] #7 - '+issues[7]['title']
assert body.count(old)==1
body=body.replace(old,'- [x] #7 - '+title)
note='''<!-- dozu-foundation-closure-2026-11-13:start -->
## Tooling foundation completed; desktop acceptance retained — 2026-11-13
The user explicitly authorized a scope split so migration can proceed. #7 is completed for the committed/measured JavaScript tooling foundation at verified dev SHA 8e7b7d134ec450ecd0244ab8deaee3d67b9379bb. Its original wider criteria are archived and transferred; they were not marked passing. This does not certify a shipped runtime, full API readiness, migrations, read-only native installation, clean-machine setup, budgets or platform parity.

Independent required follow-ups now parented to this roadmap:
- [ ] #48 — Supported framework/security upgrade and independent regression proof.
- [ ] #49 — Native portable-script/build matrix on all approved OS/CPU hosts.

Existing #38/#8/#32 own shipped runtime/ABI/resources; #40/#28/#29/#34/#15 own startup/migrations/installed paths; #23/#33/#22/#46/#47 own installers/native release evidence; #14/#16 own real account/study integration; #10 owns full CI/lint/test validation. These remain open. #38 becomes Ready after #7's foundation completion and is the next executable desktop migration step, not a completed runtime proof. Final runtime versions still need the #48 security review.

The closed #4/#45 metadata is not used as passing support evidence and those issues are unchanged. #7's narrowed foundation depends on completed #6, eliminating the prior circular expectation of downstream runtime acceptance before build-tooling completion. Redis stays retained; email/STT/payment execution are excluded; PostgreSQL without pgvector, retained PDF/YouTube text embeddings, website/UI and LAN scope remain authoritative. No owner is invented and no unrelated status/field is changed.
<!-- dozu-foundation-closure-2026-11-13:end -->'''
(HERE/'roadmap-note.md').write_text(note+'\n',encoding='utf-8')
(HERE/'issue-1.md').write_text(body.rstrip()+'\n\n'+note+'\n',encoding='utf-8')

runtime_note='''<!-- dozu-toolchain-foundation-ready-2026-11-13 -->
## Next executable desktop step after #7
The user authorized completing #7 as the committed, measured JavaScript tooling foundation. Its original broader release proof is transferred to its independent roadmap owners; this issue's #7 foundation prerequisite is now satisfied. Mark this issue Ready/Todo, not Done. #48/#49 remain open under #1 and no #7-to-#38 reverse dependency is introduced.

Start by inventorying and pinning candidate per-target artifacts, strategy, checksums, licenses and required native libraries. Include the retained Redis runtime where required; do not implement the older #30 removal proposal. No SMTP/PayOS/STT-only resources are required. Preserve PostgreSQL without pgvector, required PDF/YouTube text embeddings, all other website/UI features and LAN scope. Final shipped versions must pass #48's security review; candidate manifests do not certify complete native compatibility. #8/#29/#32/#23 and native #22/#46/#47 still own their integration/release gates.

Existing state/evidence: dev 8e7b7d134ec450ecd0244ab8deaee3d67b9379bb; Node build baseline 22.22.0/module ABI 127/Node-API 10; Windows SWC load only; no selected production Electron/Node/Python/PostgreSQL manifest yet. The API probe's ten-second bound against unavailable DB/Redis is not readiness evidence. No existing criterion on this issue is checked by #7 closure.
'''
(HERE/'issue-38.md').write_text(issues[38]['body'].rstrip()+'\n\n'+runtime_note,encoding='utf-8')
save('plan.json',{'issue7Title':title,'issue7DependencyNumbers':[6],
    'completedScope':'measured JavaScript tooling foundation','transferredNotPassed':[48,49,38,8,32,40,28,29,34,15,23,33,22,46,47,14,16,10],
    'newParents':{'48':1,'49':1},'nextReadyIssue':38,'originalProofIssuesUnchanged':[4,45]})
print('Prepared five completed foundation criteria, archived originals, independent roadmap follow-ups and #38 handoff')
