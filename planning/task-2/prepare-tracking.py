"""Prepare narrow issue-body edits; never publish unrelated manifest changes."""
import json
from pathlib import Path
from urllib.parse import quote

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
if (HERE / 'user-decisions.json').exists():
    raise SystemExit('Historical helper disabled: user decisions supersede these snapshots.')
manifest = json.loads((BASE / 'issues.json').read_text(encoding='utf-8-sig'))
pages = json.loads((BASE / 'feature-preservation.json').read_text(encoding='utf-8'))['pages']
blocker = 'User decisions are required for minimum OS/CPU/Linux support, installer formats and resource budgets, plus merchant ownership (#41) and classroom topology (#43) recorded under #27. No agreement has been supplied. Requirements and the source-backed feature matrix are complete; runtime parity is unverified.'
section2 = '''## Requirements evidence — 2026-11-10

The local-first architecture and complete feature scope are mandatory. The Task #3 source commits remain unchanged. Local evidence: `planning/requirements.md`, `planning/feature-preservation.md/json`, `planning/platform-support.md`, `planning/integration-decisions.md`, and the immutable `planning/audit/` ledgers. These files are in the current checkout and have not been pushed. The page scope is reproduced below for GitHub review.

Source coverage verified against tracked UI commit `5e1ceb263a29e2fde2359c36f43d0118a8d622f0`: **84 pages, 20 layouts, 164 shared TSX components**. The expanded audit covers 584 non-entry TSX (including the 164), 132 hook/provider/context sources and 550 navigation/config sites. All route-scoped code remains in scope. Family counts: public/diagnostic 5, classroom 26, administration 18, accounts 7, generation/Feynman 2, study workspace 15, personal learning 8, billing 1, teacher approval 2.

Required surfaces: retained website build, packaged Electron and localhost browser sharing the local Express/database/files stack. Each applicable workflow must preserve en/vi, layouts/themes, authorized and denied access, mutations/local persistence/restart, loading/empty/validation/error/retry states, provider missing/offline/failure/real-success behavior, and files/streams/sockets/media. These are implementation acceptance requirements, **not passing runtime results**. Existing placeholders, missing navigation destinations and baseline failures remain tracked gaps; no page or feature is removed.

**Agreement still required:** minimum Windows/macOS versions, CPU targets, Linux distro/release baseline, installer formats, RAM/disk/installer-size/cold-and-warm-start/CPU budgets; merchant ownership (#41); and classroom participant topology (#43). Windows/macOS/Linux remain intended families. Developer host versions are not support commitments. The #27 record distinguishes established constraints from proposed provider/callback flows. No numeric defaults, ownership or topology are invented. Do not close #2 until the remaining choices are agreed and recorded. Runtime proof stays in downstream implementation issues.
'''
inline = ['<details>', '<summary>All 84 required pages — en/vi; roles below are source intent, not authorization proof</summary>', '', '| ID / family | Route and source | Role intent | Existing required workflow |', '| --- | --- | --- | --- |']
for p in pages:
    source = p['source'].split('/',1)[1]
    url = 'https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/' + quote(source, safe='/')
    role = p['rolesAndWorkflows'].split(';',1)[0]
    inline.append(f'| {p["id"]} / {p["family"]} | [`{p["route"]}`]({url}) | {role} | {p["workflow"]} |')
inline += ['', '</details>']
section2 += '\n' + '\n'.join(inline)
section27 = '''## Requirements-stage decision record — 2026-11-10 (Task #2)

Local record: `planning/integration-decisions.md` (not pushed). Existing source/provider evidence is in completed audit #3. No live provider flow is certified by this update.

- Established constraints: every installation owns its local backend/database/files/jobs; Electron and browser share them; no required central Dozu backend/cloud database/sync. Real internet-enabled integrations and all existing pages remain in scope.
- Credential ownership: no shared publisher merchant/SMTP/vendor secret in installers/config/renderer responses. Use user-owned credentials or supported delegation. Optional providers initialize lazily and cannot crash unrelated local use.
- Proposed adaptations requiring proof: Google native/system-browser authorization with a loopback return; user-owned/delegated mail with a desktop return path; direct configured AI calls from local Express; authoritative local uploads/content and real YouTube/transcript/media ingestion.
- Callback design: prefer genuine authenticated outbound reconciliation when it preserves provider semantics; any required public endpoint/tunnel is explicit, user-owned, opt-in, scoped/authenticated and documented for TLS, delivery, availability, replay and idempotency. The actual payment/email solution still requires ownership/provider proof. No implicit central callback service.
- **Unresolved #41:** each user operates their own merchant account versus customers paying Dozu for an entitlement. Dozu merchant secrets cannot be distributed to customers. Preserve checkout/history/admin functionality while deciding the real reconciliation/entitlement authority.
- **Unresolved #43:** same-computer sessions, LAN participants, or remote participants reaching a user-owned host. Record identity/roles, TLS/auth/ACL, reachability, uptime and reconnect/conflict handling. Separate installations do not automatically share state.

The user has been asked for these ownership/topology choices in the Task #2 session. They remain unresolved until answered. #2's remaining criterion concerns agreed product requirements; this item's genuine provider/callback proofs remain separate implementation work. No new dependency edge or completion claim is introduced.
'''
for key, section in [('DECISION-SCOPE', section2), ('INTEGRATIONS', section27)]:
    draft = next(i for i in manifest['issues'] if i['id'] == key)
    old = json.loads((HERE / ('issue2-before.json' if key=='DECISION-SCOPE' else 'issue27-before.json')).read_text(encoding='utf-8'))
    if key == 'DECISION-SCOPE':
        draft['body'] = draft['body'].split('\n\nBlocked because: ')[0]
        draft['body'] = draft['body'].replace('- [ ] Record local frontend', '- [x] Record local frontend').replace('- [ ] Build a per-route', '- [x] Build a per-route').replace('- [ ] Include all admin', '- [x] Include all admin')
        body = old['body'].replace('- [ ] Record local frontend', '- [x] Record local frontend').replace('- [ ] Build a per-route', '- [x] Build a per-route').replace('- [ ] Include all admin', '- [x] Include all admin')
        draft['blockReason'] = blocker
        addition = '\n\nBlocked because: ' + blocker + '\n\n' + section
    else:
        draft['body'] = draft['body'].split('\n\n## Requirements-stage decision record — 2026-11-10 (Task #2)')[0]
        body = old['body']
        addition = '\n\n' + section
    draft['body'] += addition
    (HERE / ('issue-2-body.md' if key=='DECISION-SCOPE' else 'issue-27-body.md')).write_text(body.rstrip() + addition + '\n', encoding='utf-8')
(BASE / 'issues.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
(HERE / 'blocker.txt').write_text(blocker, encoding='utf-8')
print('Prepared #2: 3/5 criteria; #27: decision record only. No network changes.')
