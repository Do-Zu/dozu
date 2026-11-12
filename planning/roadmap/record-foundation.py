"""Prepare #5/#6 handoff updates without changing unrelated live issue text."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
manifest_path = ROOT / 'planning/issues.json'
manifest = json.loads(manifest_path.read_text(encoding='utf-8-sig'))
source = next(x for x in manifest['issues'] if x['id'] == 'IMPORT')
source['body'] = source['body'].replace('- [ ]', '- [x]', 5)
evidence = (ROOT / 'planning/source-import/issue-5.md').read_text(encoding='utf-8').split('## Source import acceptance evidence',1)[1]
if '## Source import acceptance evidence' not in source['body']:
    source['body'] += '\n\n## Source import acceptance evidence' + evidence
source['initialStatus'] = 'done'
workspace_draft = next(x for x in manifest['issues'] if x['id'] == 'WORKSPACE')
if workspace_draft['initialStatus'] not in ('done', 'closed'):
    workspace_draft['initialStatus'] = 'in-progress'
note = '''<!-- dozu-foundation-handoff-2026-11-12:start -->
## Foundation handoff — 2026-11-12

#5 is closed completed after parent review and an independent rerun of its import-baseline verifier: 1,899 files; all 84 pages and 20 layouts retained; 20 archived SQL migration hashes match the audit. Original repositories/history remain unchanged. This completes local structural import only; public redistribution/license clearance, runtime parity and release proof are separate. Evidence: local `planning/source-import/report.md` and the acceptance record on #5.

#6 is now In Progress, implementing and validating the reproducible workspace/build graph against that verified source baseline. Configuration/lockfile generation alone does not pass its clean install/build, peer, tracing and portable-output criteria. #1 remains In Progress with remaining delivery acceptance open.
<!-- dozu-foundation-handoff-2026-11-12:end -->
'''
parent = next(x for x in manifest['issues'] if x['id'] == 'ROADMAP')
if '<!-- dozu-foundation-handoff-2026-11-12:start -->' not in parent['body']:
    parent['body'] += '\n\n' + note
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
live = (HERE / 'issue-1-live.md').read_text(encoding='utf-8-sig')
assert live.count('- [ ] #5 -') == 1
live = live.replace('- [ ] #5 -','- [x] #5 -',1)
if '<!-- dozu-foundation-handoff-2026-11-12:start -->' not in live:
    live += '\n\n' + note
(HERE / 'issue-1-foundation.md').write_text(live,encoding='utf-8')
print('Prepared #5 completion and #6 active handoff; no remote mutation.')
