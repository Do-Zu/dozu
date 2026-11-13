# Dozu local-first desktop planning

**Payment scope — 2026-11-13:** [PayOS/payment execution excluded from desktop](v1-scope-2026-11-13-payments.md). The SDK/eager gateway blocker is removed; checkout is explicitly unavailable, historical reads/data are retained, and Redis remains. [Implementation evidence](payment-removal/README.md) does not establish full API/native readiness or complete #7/#41.

**Completion review — 2026-11-13:** #7 remains In Progress with original acceptance unpassed. New [#48 framework/security upgrade](https://github.com/Do-Zu/dozu/issues/48) and [#49 native script validation](https://github.com/Do-Zu/dozu/issues/49) track missing work; every other gap maps to existing delivery issues. See the [completion ledger](toolchains/follow-ups/README.md). Creating follow-ups does not certify native runtimes/installers or complete #7.

**Scope follow-up — 2026-11-13:** [Email delivery removed; Redis retained](v1-scope-2026-11-13-email.md). The user clarified that Redis removal is skipped; alternatives are suggestions only. [Implementation and checks](email-removal/README.md) record email-free account flows and local backend URL defaults. Older email-delivery requirements are superseded by this amendment.

**Toolchain work — 2026-11-13:** #7 and its Project item are In Progress. [Portable-script implementation and evidence](toolchains/README.md) records the JavaScript build pins, API path/build fixes and explicit unpassed runtime/native gates. Live #4's closed/completed state and checked headline boxes conflict with its user-directed NOT PLANNED closure; this work preserves #4 and does not infer completed platform/resource/lifecycle acceptance from it.

**Latest foundation result — 2026-11-12:** #5 source import and #6 JavaScript workspace/build graph are completed after review. Both child issues and Project Status are Done; #1 remains In Progress. Source import and workspace evidence do not establish full-stack/installer/platform acceptance. See [workspace evidence](workspace/README.md).

**Current tracker state — 2026-11-12:** #4 is closed **not planned**, with acceptance unpassed; descriptions of it as in progress below are historical. #1 coordinates the remaining proof through existing delivery children; #5 source-import review has started. See [delivery reconciliation](roadmap/README.md). The 2026-11-11 amendment supersedes older speech/pgvector wording.

The authoritative architecture is **local-first with optional internet connectivity**.

[Windows welcome-page desktop preview](desktop-preview/README.md) is the current user-test milestone under #4/#45 (2026-11-11). It is a portable one-page test build; PostgreSQL/full backend/model/native-platform acceptance remain open. See its `artifact.json`, included START-HERE.md and FEEDBACK.md for the exact build and checks.

**Latest v1 scope decision — 2026-11-11:** [local speech-to-text removed; PostgreSQL retained; pgvector deferred](v1-scope-2026-11-11.md). The large model measured in #4 is for retained PDF/YouTube text reference retrieval, so the smaller text-embedding runtime experiment remains relevant. Earlier requirements/measurement documents must be read with this amendment.

Issue #4 started on 2026-11-10. The original roadmap has 44 issues; its native proof subissues [#45 Windows](https://github.com/Do-Zu/dozu/issues/45), [#46 macOS](https://github.com/Do-Zu/dozu/issues/46), and [#47 Linux](https://github.com/Do-Zu/dozu/issues/47) are additional. [First Windows proof evidence](architecture-proof/report.md) records a measured installed-size failure for the unoptimized candidate. #4 remains in progress with all acceptance criteria unchecked. Historical publication/board counts below are not a fresh live snapshot.

- [Latest requirements](requirements.md)
- [Task #2 full preservation requirements and 84-page matrix](feature-preservation.md)
- [Agreed v1 platform and performance contract](platform-support.md)
- [INTEGRATIONS decisions: LAN classrooms, payments deferred](integration-decisions.md)
- [Completed application baseline audit (#3)](audit/README.md)
- [84-page feature-parity matrix and audit findings](audit/feature-parity.md)
- [Architecture, stack and integration feasibility plan](monorepo-desktop-plan.md)
- [44 GitHub issues with dependencies](backlog.md)
- [Complete route preservation inventory](route-inventory.md)
- [Machine-readable inventory](route-inventory.json)
- [Issue manifest](issues.json)
- [Published issue URL mapping](published-issues.json)
- [Idempotent GitHub publisher](publish-github-backlog.ps1)
- [How to read status, ownership, priority and complexity](work-tracking.md)
- [Task dashboard snapshot](task-dashboard.md)
- [Refresh live tracking labels and the snapshot](sync-issue-tracking.ps1)
- [Your Project board](https://github.com/orgs/Do-Zu/projects/6)
- [Populate missing board items/fields](populate-project-board.ps1)

## Architecture
Electron hosts the complete existing Next.js application and manages local Express, PostgreSQL/pgvector, files/jobs/cache, and FastAPI/embedding services. A browser uses that same localhost backend. Application data is local; real third-party Google/YouTube/email/payment/AI integrations may use the internet. No required central Dozu backend, cloud database or synchronization.

Preserve all pages/layouts/components/navigation/roles/features, and retain the website build. The source inventory currently has 84 page entrypoints, 20 layouts and 164 shared TSX files; route-scoped code is additional. This is an inventory, not a passing parity test.

## GitHub status
All 44 issues are published and verified: revised titles, bodies, dependency links, labels, and the roadmap's 43-child checklist match the local manifest.
- [Roadmap #1](https://github.com/Do-Zu/dozu/issues/1)
- [Authoritative scope #2](https://github.com/Do-Zu/dozu/issues/2)
- [Electron/local runtime proof #4](https://github.com/Do-Zu/dozu/issues/4)
- [Started #4: first Windows evidence, footprint failure and proposed ADR](architecture-proof/report.md)
- [Integration limitations and solutions #27](https://github.com/Do-Zu/dozu/issues/27)
- [Uninstall keep/delete option #36](https://github.com/Do-Zu/dozu/issues/36)

The original 26 issue URLs are retained and revised; 18 items were added. Labels: **4 tickets**, **40 tasks**. Every issue has acceptance criteria, phase/priority and actual GitHub dependency links. No issue is marked implemented merely because its plan was revised.

Your existing [Project #6](https://github.com/orgs/Do-Zu/projects/6) now contains all 44 issues, each verified with Status, Priority, Complexity, Phase, Depends on and Blocker. Initial board counts: 42 Todo, 2 Block, 0 In Progress, 0 Done. The five original columns (including Need Clarify) are retained; owners and dates are not invented. See project-board-guide.md and project-board-verification.json. These counts are snapshots, not a live automation.

## Integration limitations
A desktop binary cannot keep a shared publisher merchant/SMTP/vendor secret confidential from its owner. Use native/public OAuth, user-scoped credentials and supported provider delegation. Inbound webhooks cannot target localhost: verify provider-authenticated status reconciliation or an explicit scoped public endpoint/tunnel when needed. Remote classroom participants require an explicitly reachable local host; separate local installations do not share state automatically.

User decisions recorded on 2026-11-10: payment execution is explicitly deferred under blocked #41; classroom v1 serves other devices on the same LAN from a user-owned authoritative host. The v1 support/resource contract is in platform-support.md. Genuine provider/LAN/installer/benchmark proof remains pending; no simulated success or implicit central service.

## Validate or republish
From D:\product\dozu in PowerShell:
```powershell
.\planning\publish-github-backlog.ps1 -ValidateOnly
.\planning\publish-github-backlog.ps1
```

Use a GitHub CLI login that can create issues and labels in Do-Zu/dozu. The publisher creates missing labels/issues, updates generated titles/bodies, adds actual links and the parent checklist, preserves unrelated labels/issues, and reads each issue back for verification. Stable markers prevent duplicate issue creation. Update issues.json before republishing; generated-body edits made only on GitHub will be replaced.

Tracking is independent of task/ticket type. The user-created Project #6 is the main management board. Issue labels and board fields start consistently; built-in Labels/Assignees reflect the issues, while custom board Status/Priority/Complexity are independent fields. No automatic two-way synchronization was configured. The issue tracker preserves live issue labels and derives ready/waiting from completed dependencies. The project population script preserves existing board edits by default; use -RefreshFromIssues only when deliberately replacing board values from issue labels. See work-tracking.md for the rules.

## Verification and implementation status
Manifest structure, labels, unique IDs and an acyclic dependency graph passed offline validation. Publisher syntax was checked. The publication process verifies all remote titles/bodies/labels. Application source trees remain unchanged; no working desktop installer, database runtime or complete feature parity is claimed by this planning revision.

The #3 baseline audit is now complete: source/workflow inventories, independent failing/passing baselines, integration constraints and follow-up evidence are in [audit/README.md](audit/README.md). It found ignored local migration history, current UI build/lint/Jest failures, an embedding batch response bug, and additional conversion/transcription resources that #4 must prove. This completes audit work only; implementation and runtime parity remain unverified. Historical board/publication counts above describe their original snapshots.


Task #2 requirements are agreed and completed on 2026-11-10. [The v1 support/resource contract](platform-support.md) and [integration decisions](integration-decisions.md) record the user reply. Payment execution stays blocked under #41; classroom #43 uses LAN and waits on implementation prerequisites. Installer/resource/runtime compliance is unverified.
