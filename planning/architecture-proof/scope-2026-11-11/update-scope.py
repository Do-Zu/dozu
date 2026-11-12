"""Apply the explicit v1 scope amendment without changing status/assignees/board fields."""
import json
from pathlib import Path
import re
import subprocess
import sys

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[2]
REPO='Do-Zu/dozu'
START='<!-- dozu-v1-scope-2026-11-11:start -->'
END='<!-- dozu-v1-scope-2026-11-11:end -->'
NOTE=f'''{START}
## User-approved v1 scope amendment — 2026-11-11

- Remove local speech-to-text from this version: no whisper.cpp server, tiny speech model, speech startup/readiness gate or speech-only assets. Retain independent media playback and genuine existing YouTube transcript text retrieval. Preserve source/page inventory; no fake transcript or new cloud STT fallback.
- Keep PostgreSQL; **defer pgvector**. A private relational cluster, reviewed migrations/seeds, persistence and data-safe upgrades remain required. Current vector(384), `<=>` and HNSW consumers need explicit reviewed adaptation; do not blindly run vector-dependent migrations, discard data or replace PostgreSQL.
- The measured 479.729 MB MiniLM snapshot is a separate **text-embedding model**, used by retained PDF/YouTube reference search and ingestion. The user's condition for dropping its experiment is not met: keep smaller-runtime/quantization proof scoped to these consumers. No working smaller runtime or pgvector-free ranking implementation is claimed.
- Ordinary PostgreSQL array/JSONB vector storage plus bounded application-side cosine ranking is an evaluation candidate only. Prove owner/topic filtering, 384-value shape, ranking/topK/ties, persistence/migration, quality and realistic scale/resource budgets before adopting it. Semantic reference retrieval has not been deferred by this decision.
- Exclude FFmpeg only when its sole consumer is deferred speech-to-text; separately prove any retained non-STT need. Keep required document/URL/PDF/editor/media/font/browser resources. OS/CPU/installers, 250 MB installer/750 MB installed and memory/startup targets remain unchanged. Payments remain deferred under #41; classrooms remain LAN.

Source trace: `PdfFileEmbeddingStrategy.ts`, `YoutubeEmbeddingStrategy.ts`, `BaseEmbeddingStrategy.queryTopSimilarity()`, `inputSet.service.ts`, UI topic `components/reference/Reference.tsx`, and separate `features/whisper/api/whisper.service.ts`. Full record: local `planning/v1-scope-2026-11-11.md`. Earlier audits/measurements are historical evidence. Planning updates are not implemented feature removal or passing acceptance.
{END}'''

def gh(*args):
    p=subprocess.run(['gh',*args],capture_output=True,text=True,encoding='utf-8')
    if p.returncode:raise RuntimeError(p.stderr)
    return p.stdout.strip()

def amend(number,title,body):
    body=body.replace('\r','')
    if START in body:
        if END not in body:raise RuntimeError('Incomplete existing scope marker; review before editing')
        body=re.sub(re.escape(START)+r'.*?'+re.escape(END),'',body,flags=re.S).rstrip()
    # #2 is completed historical requirements work: append the new decision,
    # preserving its original checked acceptance/evidence and closed state.
    if number!=2:
        body=body.replace('PostgreSQL/pgvector','PostgreSQL')
        body=body.replace('Bundle and initialize per-user PostgreSQL with pgvector','Bundle and initialize per-user PostgreSQL (pgvector deferred)')
        body=body.replace('All pages/features remain in release scope.','All existing pages remain in scope; explicit v1 capability deferrals in the 2026-11-11 amendment below apply.')
        body=body.replace('all conversion/browser/whisper.cpp/tiny-model/FFmpeg/font assets','all retained conversion/browser/text-embedding/font assets; exclude Whisper/tiny speech model and speech-only assets')
        body=body.replace('runtime/model/browser/font/conversion/transcription assets','runtime/text-model/browser/font/conversion assets required by retained workflows')
        body=body.replace('local converters/rendering/transcription resources','local document converters/rendering resources for retained workflows')
        body=body.replace('converter/media/browser/transcription dependencies','retained converter/media/browser/text-embedding dependencies')
        body=body.replace('app/API/DB/pgvector/Python/model compatibility','app/API/PostgreSQL/text-embedding runtime/model compatibility')
    if number==4:
        body=re.sub(r'^- \[ \] P3 .+$','- [ ] P3 — Disposable native PostgreSQL without pgvector: review 20 migration hashes and vector-dependent steps; prove relational seeds/SQL CRUD/restart persistence and evaluate extension-free retained reference storage/ranking. Preserve migration/data history.',body,flags=re.M)
        body=re.sub(r'^- \[ \] P5 .+$','- [ ] P5 — Native DOC/DOCX/TXT→PDF, URL→PDF/browser assets and retained media/fonts/libraries/fixtures. Exclude Whisper/tiny speech model; FFmpeg requires a retained non-STT consumer.',body,flags=re.M)
    if number==8:
        title='[Task] Bundle local text-embedding runtime for PDF and YouTube references'
        body=body.replace('current embedding service','current text-embedding service for PDF/YouTube reference retrieval')
        body=body.replace('text/PDF/transcript contracts','text/PDF/existing-transcript-text contracts (speech-to-text is deferred)')
    if number==29:
        title='[Task] Bundle and initialize per-user PostgreSQL (pgvector deferred)'
        body=body.replace('Preserve PostgreSQL/Drizzle/vector behavior','Preserve PostgreSQL/Drizzle relational behavior and a reviewed compatibility path for retained text references')
        body=body.replace('Bundle PostgreSQL, matching pgvector and dynamic libraries/tools for each target OS/CPU.','Bundle PostgreSQL and required dynamic libraries/tools for each target OS/CPU; no v1 pgvector dependency.')
        body=body.replace('Apply extension/schema migrations and seed required roles/settings atomically with versioned recovery.','Apply a reviewed extension-free desktop schema/bootstrap path and seed required roles/settings atomically with versioned recovery; preserve all historical migration hashes and vector data for migration.')
        body=body.replace('Verify JSONB, vector(384), cosine queries/HNSW and existing repository behavior on clean installations.','Verify PostgreSQL JSONB/relational repository behavior on clean installations without vector types/operators/HNSW; prove an extension-free compatibility path for retained PDF/YouTube reference storage/query and its performance before adoption.')
    return title,body.rstrip()+'\n\n'+NOTE+'\n'

def prepare():
    original=json.loads((OUT/'issues-before.json').read_text(encoding='utf-8-sig'))
    targets={1,2,4,8,21,23,25,27,29,32,38,45,46,47}
    # Propagate the renamed #29 reference only where it already appears.
    targets|={i['number'] for i in original if i['state']=='OPEN' and 'Bundle and initialize per-user PostgreSQL with pgvector' in i['body']}
    updates=[]
    for issue in sorted(original,key=lambda i:i['number']):
        if issue['number'] not in targets:continue
        title,body=amend(issue['number'],issue['title'],issue['body'])
        path=OUT/f'issue-{issue["number"]}.md';path.write_text(body,encoding='utf-8',newline='\n')
        updates.append({'number':issue['number'],'title':title,'bodyFile':path.name})
    (OUT/'updates.json').write_text(json.dumps(updates,indent=2),encoding='utf-8')
    # Keep publisher input in agreement. Never import current generated tracking
    # blocks/dependency sections into its source body; apply the same scoped edit.
    path=ROOT/'planning/issues.json';manifest=json.loads(path.read_text(encoding='utf-8-sig'))
    # Existing manifest ordering is the published 1–44 mapping; verify identity
    # against the current fetched issue title before applying by position.
    numbers={i['number']:i for i in original}
    for index,draft in enumerate(manifest['issues'],1):
        if index not in targets:continue
        assert draft['title']==numbers[index]['title'] or index in {8,29},f'Unexpected mapping for issue {index}'
        draft['title'],draft['body']=amend(index,draft['title'],draft['body'])
        if index==4:draft['complexityReason']=draft['complexityReason'].replace('PostgreSQL/pgvector','PostgreSQL')
        if index==29:draft['complexityReason']=draft['complexityReason'].replace('PostgreSQL/pgvector','PostgreSQL')
    manifest['scopeAmendment']='v1-scope-2026-11-11.md'
    path.write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({'preparedIssues':[u['number'] for u in updates],'statesLabelsAssignees':'unchanged','projectCustomFields':'unchanged'}),flush=True)

def publish():
    updates=json.loads((OUT/'updates.json').read_text(encoding='utf-8'))
    original={i['number']:i for i in json.loads((OUT/'issues-before.json').read_text(encoding='utf-8-sig'))}
    for update in updates:
        n=update['number']
        live=json.loads(gh('issue','view',str(n),'--repo',REPO,'--json','title,body,state,labels,assignees'))
        # Work from current text to preserve edits made after the initial read.
        title,body=amend(n,live['title'],live['body'])
        path=OUT/update['bodyFile'];path.write_text(body,encoding='utf-8',newline='\n')
        gh('issue','edit',str(n),'--repo',REPO,'--title',title,'--body-file',str(path))
        print(f'Updated #{n}; tracking ownership/state not mutated',flush=True)

if __name__=='__main__':
    publish() if len(sys.argv)>1 and sys.argv[1]=='publish' else prepare()
