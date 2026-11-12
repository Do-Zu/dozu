"""Prepare narrow roadmap reconciliation from saved live snapshots."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
rows = json.loads((HERE / 'issues-before.json').read_text(encoding='utf-8-sig'))
by_number = {x['number']: x for x in rows}
assert all(by_number[n]['state'] == 'closed' and by_number[n]['state_reason'] == 'completed' for n in (2, 3))
assert by_number[4]['state'] == 'closed' and by_number[4]['state_reason'] == 'not_planned'
section = '''<!-- dozu-roadmap-checkpoint-2026-11-12:start -->
## Delivery reconciliation — 2026-11-12

#1 is actively coordinating delivery through child tasks. Only #2 requirements and #3 source audit are completed. All product acceptance criteria above remain open.

#4 was closed **not planned** at the user's Windows integration checkpoint; its unchecked checklist entry is historical, not a requirement to reopen or complete the canceled ticket. The latest [closure record](https://github.com/Do-Zu/dozu/issues/4#issuecomment-6825382086) reports 21 disposable-candidate Windows smoke checks, including real local first-owner setup/login/topic/Vietnamese-note persistence. It does not establish complete runtime parity. No full-stack installable ZIP was built and verified; the delivered welcome-page preview is narrower. The 983 MB original model/torch/Electron lower bound and 410.6 MB compression subset are component evidence, not installer measurements.

### Remaining proof obligations (replacement tracking)
Execute and attach fresh evidence through these existing delivery children, retaining #4 artifacts as historical inputs. This checklist replaces #4 as the roadmap's active proof ledger; no gate is waived by its closure.

- [ ] #8/#21/#29: retained 384-dimensional PDF/YouTube text ingestion, production repository/ranking, owner/topic isolation, persistence, migration safety, English/Vietnamese quality and realistic scale. PostgreSQL arrays/JSONB plus cosine remain a candidate.
- [ ] #11–#17/#39/#40: reviewed adoption of candidate fixes, full retained Next UI and website, real local bootstrap/seeds, shared browser/backend behavior and complete workflows; 84-page source inventory is not runtime parity.
- [ ] #7/#23/#32/#38: complete pinned runtime/model/browser/font/conversion resources, genuine installer and installed footprint; 250 MB/750 MB targets and all startup/memory targets remain unchanged.
- [ ] #22/#45/#46/#47: native Windows 10/11 x64, macOS 13+ Intel/ARM64, Ubuntu 22.04/Debian 12 x64 evidence on required configurations. Windows developer-host smoke checks do not pass this matrix.
- [ ] #25/#28/#31/#33–#37: lifecycle, clean-machine setup, process readiness/recovery, security/credentials, backup/restore/upgrades, and uninstall keep/delete evidence.
- [ ] #18–#21/#27/#30/#42–#44: local state/files/jobs/cache plus genuine external integrations and authoritative same-LAN classroom host. Payment execution stays deferred/blocked under #41; payment/history/admin pages stay inventoried.

The 2026-11-11 amendment remains authoritative: local speech-to-text and speech-only assets are excluded; media playback and genuine YouTube transcript text retrieval remain; PostgreSQL stays and pgvector is deferred. No required Dozu-hosted service/cloud synchronization or new scope reduction is introduced.

### Next executable child
#5 source import depends only on completed #3 and starts now; #6 workspace/build graph waits for #5 acceptance. First step: tracked-source provenance, exclusion ledger, bounded secret preflight and history/attribution/license review, preserving all three originals. No owner is invented; #1's existing assignment and #5's current assignment are preserved. Unsanitized source history must not be pushed. Existing #4 prerequisite links on #7/#12/#15/#34 and native proof tasks remain unresolved architecture gates pending a reviewed dependency transition; cancellation does not satisfy them or make them ready.
<!-- dozu-roadmap-checkpoint-2026-11-12:end -->
'''
manifest_path = ROOT / 'planning/issues.json'
manifest = json.loads(manifest_path.read_text(encoding='utf-8-sig'))
parent = next(x for x in manifest['issues'] if x['id'] == 'ROADMAP')
if '<!-- dozu-roadmap-checkpoint-2026-11-12:start -->' not in parent['body']:
    parent['body'] += '\n\n' + section
parent['initialStatus'] = 'in-progress'
import_draft = next(x for x in manifest['issues'] if x['id'] == 'IMPORT')
if import_draft['initialStatus'] not in ('done', 'closed'):
    import_draft['initialStatus'] = 'in-progress'
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
body = by_number[1]['body']
if '<!-- dozu-roadmap-checkpoint-2026-11-12:start -->' not in body:
    body += '\n\n' + section
(HERE / 'issue-1.md').write_text(body, encoding='utf-8')
(HERE / 'README.md').write_text('# Active delivery reconciliation\n\n' + section + '\nLocal snapshot preparation: `python planning/roadmap/reconcile.py`. Live issue/project snapshots are stored alongside this report. The original 44-item dashboard and the 47-item board are distinct inventories.\n', encoding='utf-8')
for relative in ('planning/README.md', 'planning/architecture-proof/README.md'):
    path = ROOT / relative
    content = path.read_text(encoding='utf-8-sig')
    notice = '**Current tracker state — 2026-11-12:** #4 is closed **not planned**, with acceptance unpassed; descriptions of it as in progress below are historical. #1 coordinates the remaining proof through existing delivery children; #5 source-import review has started. See [delivery reconciliation](' + ('roadmap/README.md' if relative == 'planning/README.md' else '../roadmap/README.md') + '). The 2026-11-11 amendment supersedes older speech/pgvector wording.\n\n'
    if '**Current tracker state — 2026-11-12:**' not in content:
        first, rest = content.split('\n', 1)
        path.write_text(first + '\n\n' + notice + rest.lstrip('\n'), encoding='utf-8')
print('Prepared roadmap body, manifest and current-state notices; no GitHub writes.')
