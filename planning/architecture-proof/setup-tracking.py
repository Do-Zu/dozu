"""Idempotently add native proof subissues, preserving unrelated Project values."""
import json
from pathlib import Path
import subprocess

OUT = Path(__file__).resolve().parent
REPO = 'Do-Zu/dozu'
PROJECT = 'PVT_kwDODsVOHc4Bq0ro'
FIELDS = json.loads((OUT / 'project-fields-before.json').read_text(encoding='utf-8-sig'))['fields']

def gh(*args):
    result = subprocess.run(['gh', *args], capture_output=True, text=True, encoding='utf-8')
    if result.returncode:
        raise RuntimeError(result.stderr)
    return result.stdout.strip()

def field(item, name, value):
    definition = next(f for f in FIELDS if f['name'] == name)
    args = ['project', 'item-edit', '--id', item, '--project-id', PROJECT, '--field-id', definition['id']]
    if 'options' in definition:
        args += ['--single-select-option-id', next(o['id'] for o in definition['options'] if o['name'] == value)]
    else:
        args += ['--text', value]
    gh(*args)

specs = [
    ('windows', 'Windows 10/11 x64 NSIS', 'Windows 10 22H2 and Windows 11 x64', 'NSIS .exe'),
    ('macos', 'macOS 13+ Intel and Apple Silicon DMGs', 'macOS 13+ on both Intel x64 and Apple Silicon ARM64', 'signed/notarized .dmg per architecture'),
    ('linux', 'Ubuntu 22.04 and Debian 12 x64 packages', 'Ubuntu 22.04 and Debian 12 x64', '.deb plus .AppImage where compatible'),
]
existing = json.loads(gh('issue', 'list', '--repo', REPO, '--state', 'all', '--limit', '200', '--json', 'number,title,body'))
items = json.loads(gh('project', 'item-list', '6', '--owner', 'Do-Zu', '--limit', '200', '--format', 'json'))['items']
children = []
for key, name, baseline, installer in specs:
    marker = f'<!-- dozu-proof-native:{key} -->'
    match = next((i for i in existing if marker in i['body']), None)
    if not match:
        body = f'''{marker}
Parent: https://github.com/{REPO}/issues/4

## Outcome
Run the complete candidate locally on **{baseline}**, using **{installer}**. Native execution is required; cross-compilation and a passing requirements/audit ticket are insufficient.

## Sequence
Execute after the shared #4 P1–P5 component experiments establish a runnable candidate. This depends on those experiments, not on closing parent #4. It is a proof subtask, not a duplicate implementation ticket. Coordinate #22/#23/#24/#38 for the release implementation.

## Acceptance criteria
- [ ] Record native host OS/build, CPU/architecture, RAM/storage, production artifacts/checksums, toolchain/native ABI and dynamic library versions.
- [ ] Install on each stated baseline without system Node/Python/PostgreSQL/Docker/WSL or first-run runtime/model downloads; pgvector is deferred from v1.
- [ ] Run retained full Next standalone, Express, per-user PostgreSQL and real CPU text-embedding service for PDF/YouTube references; account for retained conversion/browser/font assets. Speech-to-text/Whisper/tiny speech model are deferred per planning/v1-scope-2026-11-11.md; include FFmpeg only for a proved retained non-STT need.
- [ ] Exercise dynamic routes/en+vi, shared Electron/browser local writes, files, sockets/streams, PDF/editor/media and a genuine configured system-browser provider flow. Preserve all 84 workflows; payments remain deferred under #41.
- [ ] Measure complete installer ≤250 MB/application ≤750 MB; all app-owned process normal memory ≤700 MB minimum/1 GB recommended; cold/warm interactive UI ≤10/5s minimum and ≤5/3s recommended; backend ready ≤8/4s. Record processing peaks and model/cache/network/concurrency state separately.
- [ ] Verify loopback/session boundaries, restart persistence, crash cleanup, upgrade/backup/restore, uninstall keep/delete and minimum-device/low-resource behavior, with logs.
- [ ] Publish native evidence into #4 P6/P7 and its ADR. Unrun hosts/checks remain unpassed; never relax the approved contract implicitly.

## Tracking
Priority P0; complexity L (native packaging/integration across runtime dependencies). Status waiting on #4 P1–P5 shared component experiments. No assignee is inferred. See local planning/architecture-proof/README.md for exact experiment order. Mac/Linux native hosts are not available in the current Windows workspace.
'''
        path = OUT / f'issue-native-{key}.md'
        path.write_text(body, encoding='utf-8')
        url = gh('issue', 'create', '--repo', REPO, '--title', f'[Proof] Validate native {name} local stack', '--body-file', str(path), '--label', 'task,status:waiting,priority:P0,complexity:L')
        number = int(url.rsplit('/', 1)[-1])
    else:
        number = match['number']
        url = f'https://github.com/{REPO}/issues/{number}'
    issue = json.loads(gh('api', f'repos/{REPO}/issues/{number}'))
    subissues = json.loads(gh('api', f'repos/{REPO}/issues/4/sub_issues'))
    if not any(i['number'] == number for i in subissues):
        gh('api', '--method', 'POST', f'repos/{REPO}/issues/4/sub_issues', '-F', f'sub_issue_id={issue["id"]}')
    old_item = next((i for i in items if i.get('content', {}).get('number') == number), None)
    if old_item:
        item = old_item['id']
    else:
        item = json.loads(gh('project', 'item-add', '6', '--owner', 'Do-Zu', '--url', url, '--format', 'json'))['id']
        for name_, value in [('Status','Todo'), ('Priority','P0'), ('Complexity','L'), ('Phase','0 Requirements'), ('Depends on',f'https://github.com/{REPO}/issues/4 (P1–P5 component experiments; not parent closure)'), ('Blocker','None; awaiting shared component experiments')]:
            field(item, name_, value)
    children.append({'platform':key,'number':number,'url':url,'itemId':item})
    (OUT / 'native-subissues.json').write_text(json.dumps(children, indent=2), encoding='utf-8')
    print(f'{key}: {url}', flush=True)

marker = '<!-- dozu-proof-checklist:start -->'
parent = json.loads(gh('issue','view','4','--repo',REPO,'--json','body'))['body']
if marker not in parent:
    checklist = '''

<!-- dozu-proof-checklist:start -->
## Executable architecture proof (started 2026-11-10)

Shared component experiments execute in order; native platforms have explicit subissues. Evidence lives in local `planning/architecture-proof/` with sanitized logs/manifests/scripts. These unchecked gates do not change the acceptance criteria above.

- [ ] P1 — Measure pinned runtime/text-model/browser/font/conversion assets for retained workflows, hashes, complete footprint and installer feasibility; exclude deferred speech-only assets/pgvector; report missing assets, no first-run downloads.
- [ ] P2 — Sanitized production build and Electron utilityProcess or pinned bundled Node startup of retained Next standalone + Express; dynamic en/vi routes, streams/sockets and process cleanup; fix only measured necessary build/runtime blockers.
- [ ] P3 — Disposable native PostgreSQL without pgvector: review 20 migration hashes/vector-dependent steps, prove relational seeds/SQL CRUD/persistence and evaluate a compatible extension-free path for retained references. Preserve migration/data history.
- [ ] P4 — Pinned offline CPU Python/model with fresh user paths, API consumer contract including known batch 500, startup/steady/processing memory and model/cache manifest.
- [ ] P5 — Native DOC/DOCX/TXT→PDF, URL→PDF/browser assets and retained PDF/editor/media/font/library fixtures. Exclude Whisper/tiny speech model; FFmpeg requires a retained non-STT consumer. Apply planning/v1-scope-2026-11-11.md.
- [ ] P6 — Native packaged matrix on every approved OS/CPU baseline, clean installation without developer dependencies (subissues below). Cross-builds are not evidence.
- [ ] P7 — Complete-process cold/warm UI/backend timing, normal/peak RAM+CPU/size; loopback/auth/secret review, restart/upgrade/backup/uninstall keep/delete evidence and conditional ADR/options. Approved budgets stay unchanged.

### Native execution subissues
'''
    for child in children:
        checklist += f'- [ ] #{child["number"]} — {child["platform"]}: {child["url"]}\n'
    checklist += '\nCurrent workspace is Windows only; macOS/Linux native acceptance remains unpassed. Shared experiments can progress here. No assignee is invented. P1–P5 are component checks; P6/P7 must still validate full packaged behavior on supported hardware.\n<!-- dozu-proof-checklist:end -->\n'
    path = OUT / 'issue-4-with-checklist.md'
    path.write_text(parent + checklist, encoding='utf-8')
    gh('issue','edit','4','--repo',REPO,'--body-file',str(path))
print('Parent checklist and native subissue links recorded.', flush=True)
