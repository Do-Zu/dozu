"""Record the user's 2026-11-10 requirements decisions and prepare narrow tracking edits."""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
if (HERE / 'decision-issue-2-body.md').exists():
    raise SystemExit('One-time decision import already applied. Read live state before editing further.')
platform = '''# Agreed v1 desktop support contract — Task #2

Approved by the user on 2026-11-10. This is the initial v1 support contract and engineering target set, not evidence of compatibility or measured performance. If the selected framework or bundled backend cannot meet a target, provide benchmark evidence and an explicit recommendation before changing the agreement.

## OS, architecture and distribution

| Platform | Required v1 baseline | CPU | Installer |
| --- | --- | --- | --- |
| Windows | Windows 10 22H2, legacy compatibility; Windows 11, primary | x86-64 | NSIS .exe primary; .msi optional for enterprise |
| macOS | macOS 13 Ventura or later | Intel x86-64 and Apple Silicon ARM64 | Signed and notarized .dmg for each architecture |
| Linux | Ubuntu 22.04 LTS and Debian 12 minimum tested baselines; Ubuntu 24.04 LTS or newer recommended | x86-64 | .deb for Ubuntu/Debian; additional .AppImage where compatible |

32-bit systems are unsupported. Windows ARM64 and Linux ARM64 may be added only after native dependency validation; they are not current required v1 targets. Later recommended releases still require compatibility evidence; the wording above does not assert tests have run.

## Hardware

| Configuration | CPU | System RAM | Free disk | Display / storage |
| --- | --- | --- | --- | --- |
| Minimum | 64-bit dual-core | 4 GB | 2 GB for installation and initial data | 1366 × 768; integrated graphics; HDD-compatible, SSD preferred |
| Recommended | 64-bit quad-core or better | 8 GB or more | 5 GB | 1920 × 1080; SSD |
| High performance | 6–8+ cores | 16 GB or more | Dataset/workload-dependent; no additional number specified | NVMe SSD; larger datasets and concurrent background workloads |

A dedicated GPU is not required for normal functionality. Provide a low-resource mode for 4 GB machines using efficient process management, lazy initialization, bounded caching and reduced background concurrency. Preserve functionality; do not achieve budgets by silently removing pages or required processing.

## Performance and disk targets

| Production-build metric | Minimum-spec device | Recommended device |
| --- | --- | --- |
| Cold launch to interactive UI | ≤ 10 s | ≤ 5 s |
| Warm launch to interactive UI | ≤ 5 s | ≤ 3 s |
| Local backend ready | ≤ 8 s | ≤ 4 s |
| Normal application memory, including backend and database | ≤ 700 MB | ≤ 1 GB |

Installer target: **≤ 250 MB**. Installed application target, including bundled backend: **≤ 750 MB**. Require **at least 2 GB free before installation**, covering installation and initial data. User-generated data and imported media may grow beyond the application footprint. Account for runtime/model/assets in the application footprint; do not hide them in a first-run download or call them user data to satisfy the budget.

Use production builds and documented repeatable workloads on minimum supported configurations. Document OS/CPU/RAM/storage, dataset/media sizes, model revision, cache state, concurrency, network state and measurement method. Report all resident app-owned processes, including Electron, Next, API, database and any running embedding/converter/transcription processes. Keep interactive-UI and backend-ready timings separate; an interactive shell is not proof the database/model is ready. Measure background and processing peaks as well as the agreed normal workload. No numerical CPU cap, conversion/embedding peak-memory cap or peak upgrade-space budget was supplied; measure and report them rather than inventing an agreement.

## Local runtime and data lifecycle

Backend and primary data storage run locally. Internet is permitted for genuine Google authentication, email, YouTube and other external services; classroom v1 is LAN, and payments are explicitly deferred/blocked under #41. No externally hosted application backend is required for core local functionality. Bundle/provision required dependencies through installation; no manual Node, Python, database, Docker, WSL or developer tooling. Retain the earlier self-contained baseline model/runtime requirement.

PostgreSQL/pgvector remains the source-supported candidate. The user permits considering SQLite **only after compatibility with the existing backend/business requirements is validated**. This does not authorize a database replacement: #4/#29 must prove migrations, PostgreSQL-specific SQL/JSONB, vector(384)/cosine/HNSW behavior and repository contracts before recommending an alternative.

Upgrades preserve data. Uninstall retains the earlier explicit keep-data/delete-all-app-owned-data choice, with reliable removal of app-owned databases, caches, logs and local data while protecting unrelated files. All managed data stays on the device unless the feature explicitly requires external communication. LAN participants access the user-owned host's authoritative data; no cloud database/sync is introduced.

## Evidence gates

#4/#38 must prove each agreed native OS/CPU combination and resource budget; #21/#32 include all media/conversion/transcription/model/font/browser resources discovered by audit. Electron + Next + Express + PostgreSQL + Python/model and conversion resources have not yet been shown to fit these budgets. No target is relaxed based on that uncertainty.

#22/#23/#25/#33/#35/#36 validate clean installation, startup/readiness, memory/core functionality, dependency compatibility, low-resource mode, restart/recovery, upgrades/backup/restore and uninstall on the minimum configurations. Release compliance requires actual evidence. Signing/distribution remain #24/#26. A benchmark failure requires evidence and an explicit recommendation before changing this contract.
'''
(BASE / 'platform-support.md').write_text(platform, encoding='utf-8')
decisions = {
    'date': '2026-11-10', 'authority': 'User reply in Task #2 session',
    'platformSupport': 'Agreed v1 support contract; platform-support.md',
    'payments': {'decision': 'Defer and block payment execution during local migration', 'trackingIssue': 41, 'merchantOwnership': 'Deferred; not selected', 'deleteExistingPages': False, 'runtimeImplementation': 'Not performed by requirements work'},
    'classroom': {'decision': 'Other devices on the same LAN', 'trackingIssue': 43, 'authority': 'User-owned host with local backend/database', 'remoteInternetTunnel': 'Not a v1 requirement', 'implementation': 'Unverified'},
    'database': 'SQLite may be evaluated with compatibility proof; no replacement selected',
    'criteriaComplete': 5, 'releaseValidation': 'Pending downstream evidence'
}
(HERE / 'user-decisions.json').write_text(json.dumps(decisions,indent=2)+'\n',encoding='utf-8')
record = (BASE / 'integration-decisions.md').read_text(encoding='utf-8')
record = record.replace('Real Google/YouTube/email/payments/AI and other existing internet features remain in scope.', 'Real Google/YouTube/email/AI and other existing internet features remain in scope; payment execution is explicitly deferred/blocked under #41 by the user on 2026-11-10.')
record = re.sub(r'^\| INT-06 .*$', '| INT-06 | Payment execution during local migration | **User decision 2026-11-10: defer/skip and keep one explicit blocker, existing [#41](https://github.com/Do-Zu/dozu/issues/41).** Merchant ownership is deferred, not implicitly selected. Preserve existing payment/history/admin page inventory and show a clear unavailable state when implemented; no live checkout/charge or simulated success. Page deletion is not authorized. Re-enable only after an explicit ownership/provider decision and genuine proof. |', record, flags=re.M)
record = re.sub(r'^\| INT-07 .*$', '| INT-07 | Classroom v1 participants | **User decision 2026-11-10: other devices on the same LAN.** [#43](https://github.com/Do-Zu/dozu/issues/43) implements an opt-in user-owned local host serving teacher/student clients. Keep default core services loopback-only and expose only the reviewed classroom access surface when LAN mode is enabled. Identity/roles, TLS/auth/ACL, discovery/connection, firewall, reconnect/revocation, data visibility and host availability need implementation proof. Remote internet/tunnel collaboration is not a v1 requirement. No cloud database/sync. |', record, flags=re.M)
record = record[:record.index('User input requested for INT-06')]+'''The user answered on 2026-11-10: platform agreement is recorded in [platform-support.md](platform-support.md), payments are deferred/blocked under #41, and classrooms use other devices on the same LAN. This resolves #2's requirements decisions. It does not resolve deferred merchant ownership or certify live provider/LAN behavior. #43's topology-choice blocker is resolved; ordinary implementation prerequisites remain. #27 remains the integration proof tracker.

Payment callback/reconciliation design is deferred with #41. Mail/OAuth return paths, genuine provider behavior and LAN identity/TLS/auth/availability remain #14/#27/#42/#43 implementation evidence gates. Do not introduce a central callback server or share application data through cloud sync.
'''
(BASE / 'integration-decisions.md').write_text(record,encoding='utf-8')
req=(BASE/'requirements.md').read_text(encoding='utf-8')
req=req.replace('No reduced release scope is adopted.', 'All page inventory remains; the user explicitly deferred/blocked payment execution under #41 on 2026-11-10. Classroom v1 supports other devices on the same LAN; remote internet participants are not a v1 requirement.')
start=req.index('Windows, macOS and Linux remain the intended platform families.')
end=req.index('| Issue #2 criterion',start)
req=req[:start]+'''The user agreed the initial [v1 platform/hardware/installer/performance contract](platform-support.md) on 2026-11-10. It includes Windows 10 22H2 legacy/Windows 11 primary x86-64, macOS 13+ Intel/ARM64, Ubuntu 22.04 LTS/Debian 12 x86-64, and specified budgets and low-resource mode. These are requirements awaiting benchmark validation. SQLite may be evaluated only with backend/business compatibility proof; PostgreSQL/pgvector is not silently replaced.

[INTEGRATIONS decisions](integration-decisions.md): payment execution is explicitly deferred/blocked under existing #41; preserve page/history inventory without fake success, and do not delete payment pages. Classroom v1 connects other devices on the same LAN to a user-owned authoritative host. #43's topology blocker is resolved; networking/auth/TLS and provider flows still require implementation proof under #27. No central Dozu backend/cloud DB/sync is introduced.

'''+req[end:]
req=req.replace('Pending user agreement in platform-support.md.', 'Agreed by user on 2026-11-10; platform-support.md. Benchmarks pending.')
req=req.replace('Constraint/option record added under #27; merchant/topology and concrete callback solution remain pending.', 'User decisions recorded under #27: defer/block payments #41; LAN classroom #43. Callback/provider/LAN implementation proofs remain downstream.')
req+='\nTask #2 is complete as requirements work (5/5 criteria). This does not certify release compliance or complete any implementation issue.\n'
(BASE/'requirements.md').write_text(req,encoding='utf-8')

contract = '''## User-approved v1 decisions — 2026-11-10

The user has supplied the v1 support contract. This supersedes the earlier pending-decision note. These are requirements and engineering targets, not measured results.

'''+platform[platform.index('## OS, architecture'):]+'''

Payment decision: explicitly defer/skip payment execution and retain existing issue #41 as the single blocker. Merchant ownership is deferred, not selected. Preserve page/history inventory and a clear disabled/unavailable payment state when implemented; no live charges, fake success or payment-page deletion. This is an explicit scope exception to earlier all-feature wording.

Classroom decision: other devices on the same LAN use a user-owned authoritative local host. Preserve teacher/student workflows with explicit LAN access/auth/TLS/availability proof under #43. Remote internet/tunnel participants are not a v1 requirement. No central Dozu backend/cloud database/sync.

All five #2 criteria are now evidenced as requirements. Implementation, installer/platform compatibility, performance/resource benchmarks, provider flows, data lifecycle and LAN runtime proof remain open under downstream issues. Source trees remain unchanged.
'''
payment_block='User explicitly deferred/skipped payment execution during the local migration on 2026-11-10. Keep payments blocked under #41 until the user explicitly reopens the feature and chooses merchant ownership/provider flow; no live charges or simulated success. Existing payment/history/admin page inventory is retained.'
integrations='''## Agreed requirements decisions — 2026-11-10

Supersedes the previous unresolved topology/requirements note. User-approved platform, installer, low-resource mode and performance contract is in #2 and local `planning/platform-support.md`.

- Payments: user explicitly defers/skips execution for the local migration. Reuse #41 as the single blocker. Merchant ownership and payment callback/reconciliation are deferred. Keep page/history inventory; do not delete pages, charge, ship merchant secrets or simulate success. Reopening requires an explicit user decision and genuine provider proof.
- Classrooms: user selects other devices on the same LAN. One user-owned host remains authoritative; opt-in LAN access serves participants. Identity/roles, TLS/auth/ACL, host discovery/connection, firewall, availability/reconnect/revocation and persisted events need proof under #43. Core loopback binding must not be widened indiscriminately. Internet/tunnel classrooms are not a v1 requirement; no cloud DB/sync.
- Existing no-central-backend and no-shared-publisher-secret constraints remain. Google/mail return paths and genuine provider/LAN proof remain work here and in #14/#42/#43/#44. The payment-specific proof criteria below apply only if #41 is explicitly reopened; they do not block requirements completion or other migration work.

This records product choices only; no implementation checkbox here is marked complete.
'''
manifest=json.loads((BASE/'issues.json').read_text(encoding='utf-8'))
drafts={i['id']:i for i in manifest['issues']}
for n,key in [(2,'DECISION-SCOPE'),(27,'INTEGRATIONS'),(41,'PAYMENTS'),(43,'CLASSROOM'),(1,'ROADMAP')]:
    old=json.loads((HERE/f'decision-before-{n}.json').read_text(encoding='utf-8'))
    remote=old['body']; draft=drafts[key]
    if n==2:
        remote=re.sub(r'^Blocked because:.*\n?', '', remote, flags=re.M)
        remote=remote.replace('- [ ] Agree OS', '- [x] Agree OS').replace('- [ ] Record public callback','- [x] Record public callback')
        remote=re.sub(r'\*\*Agreement still required:\*\*.*?(?=\n\n<details>)', 'The user has now provided the support contract and integration choices; see the approved decision section below.',remote,flags=re.S)
        remote=re.sub(r'\n\*\*Blocking decision/impediment:\*\*[^\n]*','',remote)
        draft['body']=re.sub(r'^Blocked because:.*\n?', '', draft['body'],flags=re.M)
        draft['body']=draft['body'].replace('- [ ] Agree OS','- [x] Agree OS').replace('- [ ] Record public callback','- [x] Record public callback')
        draft['body']=re.sub(r'\*\*Agreement still required:\*\*.*?(?=\n\n<details>)','The user has now provided the support contract and integration choices; see the approved decision section below.',draft['body'],flags=re.S)
        draft['blockReason']=''; addition=contract
    elif n==27:
        addition=integrations
    elif n==41:
        addition='## Explicit payment deferral — 2026-11-10\n\nBlocked because: '+payment_block+'\n\nThis user decision defers payment execution rather than authorizing page deletion. Future implementation must expose an honest blocked state and preserve local history/admin inventory. No payment functionality has been disabled in application code by this requirements task. Existing technical criteria are retained for an explicitly reopened payment feature, not a mandatory v1 payment release gate.'
        draft['blockReason']=payment_block
        remote=re.sub(r'\*\*Blocking decision/impediment:\*\*[^\n]*','**Blocking decision/impediment:** '+payment_block,remote)
    elif n==43:
        oldcrit='For remote participants, decide and prove opt-in authenticated LAN/reachable user host/tunnel access, ownership, NAT/TLS and authorization; loopback alone cannot connect independent installations.'
        newcrit='Prove opt-in authenticated access from other devices on the same LAN to a user-owned authoritative host, with explicit TLS/auth/ACL, firewall and connection/discovery design; loopback alone cannot serve LAN clients. Remote internet/tunnel access is not a v1 requirement.'
        remote=remote.replace(oldcrit,newcrit);draft['body']=draft['body'].replace(oldcrit,newcrit)
        remote=re.sub(r'\n\*\*Blocking decision/impediment:\*\*[^\n]*','',remote)
        draft['blockReason']=''
        draft['complexityReason']='LAN classroom access across multiple devices, authorization/TLS, host availability and persisted realtime behavior; split implementation before execution.'
        addition='## Topology selected by user — 2026-11-10\n\nOther devices on the same LAN connect to a user-owned authoritative local host. The prior topology-choice blocker is resolved. Ordinary prerequisites #27/#14/#30 remain; status is waiting, not complete. Remote internet/tunnel classroom access is not a v1 requirement. No central Dozu service/cloud DB/sync. Preserve local teacher/student/admin workflows; prove opt-in LAN exposure, roles/auth/TLS/ACL, firewall/discovery, host availability, identity/revocation, reconnect and real persisted events. No implementation checkbox is completed by this decision.'
    else:
        remote=remote.replace('- [ ] #2 -','- [x] #2 -')
        addition='## v1 requirements agreed — 2026-11-10\n\n#2 records the user-approved OS/CPU/installer/hardware/resource contract and low-resource mode. Classrooms support other devices on the same LAN (#43), with the user-owned host authoritative. Payment execution is explicitly deferred/skipped and tracked by the existing blocked #41; it is an explicit exception to prior all-feature payment release wording, not authorization to delete payment/history/admin pages. Remaining payment implementation criteria apply only upon explicit reopening. No central backend/cloud DB/sync is introduced. Budgets are targets awaiting proof; provide benchmark evidence and an explicit recommendation before changing them. Requirements completion does not complete implementation or release compliance.'
    draft['body']=draft['body'].rstrip()+'\n\n'+addition
    remote=remote.rstrip()+'\n\n'+addition+'\n'
    (HERE/f'decision-issue-{n}-body.md').write_text(remote,encoding='utf-8')
(BASE/'issues.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
(HERE/'payment-blocker.txt').write_text(payment_block,encoding='utf-8')
(HERE/'handoff.md').write_text('User-approved Task #2 contract is now recorded in #2: Windows 10 22H2 legacy/Windows 11 primary x86-64, macOS 13+ Intel/ARM64, Ubuntu 22.04/Debian 12 x86-64; NSIS exe/dmg/deb (MSI optional, AppImage where compatible). Minimum 4 GB RAM/2 GB free/dual-core; low-resource mode required. Targets: 250 MB installer, 750 MB installed; minimum cold UI 10s/warm 5s/backend 8s/normal app memory 700 MB; recommended 5s/3s/4s/1 GB. Account for all runtimes/models/assets/processes. Benchmark in production on agreed minimum configurations; report evidence and an explicit recommendation before changing targets. SQLite is evaluation-only pending backend/vector/SQL/migration compatibility proof. LAN classrooms selected; payment execution explicitly deferred under #41. Read #2 for the full hardware/display/data lifecycle contract. This is a requirements handoff, not benchmark/packaging evidence.\n',encoding='utf-8')
print('Recorded user decisions; prepared only #1/#2/#27/#41/#43 body updates.')
