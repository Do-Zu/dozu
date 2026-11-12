# Local-first desktop backlog

Main board: [Dozu Project #6](https://github.com/orgs/Do-Zu/projects/6). [Roadmap #1](https://github.com/Do-Zu/dozu/issues/1). [Tracking rules](work-tracking.md).

44 published issues: 4 tickets and 40 tasks. All existing UI inventory remains; payment execution is explicitly deferred under #41 and classroom v1 is LAN per the 2026-11-10 user decision. See platform-support.md and integration-decisions.md. Values below are planning snapshots; use the live board/issue metadata for current status and ownership. Complexity estimates are provisional, not delivery dates; XL items need executable breakdown.

| Issue | Type | Status snapshot | Priority | Complexity | Phase | Prerequisites |
| --- | --- | --- | --- | --- | --- | --- |
| [#1](https://github.com/Do-Zu/dozu/issues/1) [Ticket] Deliver self-contained local-first desktop and monorepo | ticket | backlog | P0 | XL | All | None |
| [#2](https://github.com/Do-Zu/dozu/issues/2) [Ticket] Record local-first requirements and full feature-preservation matrix | ticket | done | P0 | M | 0 Requirements | None |
| [#3](https://github.com/Do-Zu/dozu/issues/3) [Task] Audit complete UI/backend and local-first integration baselines | task | done | P0 | L | 0 Requirements | None |
| [#4](https://github.com/Do-Zu/dozu/issues/4) [Ticket] Prove Electron can package the complete local Next.js and service stack | ticket | ready | P0 | XL | 0 Requirements | [#3](https://github.com/Do-Zu/dozu/issues/3), [#2](https://github.com/Do-Zu/dozu/issues/2) |
| [#5](https://github.com/Do-Zu/dozu/issues/5) [Task] Import current frontend/backend/embedding sources with provenance | task | ready | P0 | M | 1 Foundation | [#3](https://github.com/Do-Zu/dozu/issues/3) |
| [#6](https://github.com/Do-Zu/dozu/issues/6) [Task] Establish reproducible monorepo workspaces and build graph | task | waiting | P0 | M | 1 Foundation | [#5](https://github.com/Do-Zu/dozu/issues/5) |
| [#7](https://github.com/Do-Zu/dozu/issues/7) [Task] Pin portable toolchains and runtime-compatible builds | task | waiting | P0 | M | 1 Foundation | [#6](https://github.com/Do-Zu/dozu/issues/6), [#4](https://github.com/Do-Zu/dozu/issues/4) |
| [#8](https://github.com/Do-Zu/dozu/issues/8) [Task] Bundle local FastAPI, Python and baseline embedding model | task | waiting | P0 | L | 1 Foundation | [#5](https://github.com/Do-Zu/dozu/issues/5), [#38](https://github.com/Do-Zu/dozu/issues/38), [#34](https://github.com/Do-Zu/dozu/issues/34) |
| [#9](https://github.com/Do-Zu/dozu/issues/9) [Task] Provide local-stack development and packaging diagnostics | task | waiting | P2 | M | 1 Foundation | [#7](https://github.com/Do-Zu/dozu/issues/7), [#29](https://github.com/Do-Zu/dozu/issues/29), [#40](https://github.com/Do-Zu/dozu/issues/40), [#8](https://github.com/Do-Zu/dozu/issues/8) |
| [#10](https://github.com/Do-Zu/dozu/issues/10) [Task] Build local desktop artifacts while retaining website CI/deployment | task | waiting | P1 | L | 1 Foundation | [#7](https://github.com/Do-Zu/dozu/issues/7), [#8](https://github.com/Do-Zu/dozu/issues/8), [#40](https://github.com/Do-Zu/dozu/issues/40) |
| [#11](https://github.com/Do-Zu/dozu/issues/11) [Task] Route every frontend transport to the runtime-discovered local API | task | waiting | P1 | L | 2 Local services | [#6](https://github.com/Do-Zu/dozu/issues/6), [#40](https://github.com/Do-Zu/dozu/issues/40) |
| [#12](https://github.com/Do-Zu/dozu/issues/12) [Task] Add narrow desktop host adapters around the retained Next.js UI | task | waiting | P1 | L | 2 Local services | [#11](https://github.com/Do-Zu/dozu/issues/11), [#4](https://github.com/Do-Zu/dozu/issues/4), [#34](https://github.com/Do-Zu/dozu/issues/34) |
| [#13](https://github.com/Do-Zu/dozu/issues/13) [Task] Preserve the full Next.js UI, navigation, themes and en/vi assets | task | waiting | P1 | L | 2 Local services | [#6](https://github.com/Do-Zu/dozu/issues/6), [#32](https://github.com/Do-Zu/dozu/issues/32) |
| [#14](https://github.com/Do-Zu/dozu/issues/14) [Task] Preserve local accounts and adapt genuine Google OAuth for desktop | task | waiting | P1 | L | 2 Local services | [#40](https://github.com/Do-Zu/dozu/issues/40), [#11](https://github.com/Do-Zu/dozu/issues/11), [#12](https://github.com/Do-Zu/dozu/issues/12), [#31](https://github.com/Do-Zu/dozu/issues/31), [#27](https://github.com/Do-Zu/dozu/issues/27) |
| [#15](https://github.com/Do-Zu/dozu/issues/15) [Task] Integrate Electron with the complete managed local application | task | waiting | P1 | L | 3 Full application | [#4](https://github.com/Do-Zu/dozu/issues/4), [#13](https://github.com/Do-Zu/dozu/issues/13), [#12](https://github.com/Do-Zu/dozu/issues/12), [#28](https://github.com/Do-Zu/dozu/issues/28) |
| [#16](https://github.com/Do-Zu/dozu/issues/16) [Task] Prove an end-to-end local study workflow without reducing release scope | task | waiting | P1 | M | 3 Full application | [#15](https://github.com/Do-Zu/dozu/issues/15), [#14](https://github.com/Do-Zu/dozu/issues/14), [#18](https://github.com/Do-Zu/dozu/issues/18) |
| [#17](https://github.com/Do-Zu/dozu/issues/17) [Task] Preserve every existing page, role and feature in the local desktop | task | waiting | P1 | XL | 3 Full application | [#16](https://github.com/Do-Zu/dozu/issues/16), [#27](https://github.com/Do-Zu/dozu/issues/27), [#41](https://github.com/Do-Zu/dozu/issues/41), [#42](https://github.com/Do-Zu/dozu/issues/42), [#43](https://github.com/Do-Zu/dozu/issues/43), [#44](https://github.com/Do-Zu/dozu/issues/44) |
| [#18](https://github.com/Do-Zu/dozu/issues/18) [Task] Replace required cloud storage with local files and localhost URLs | task | waiting | P1 | L | 2 Local services | [#29](https://github.com/Do-Zu/dozu/issues/29), [#40](https://github.com/Do-Zu/dozu/issues/40), [#34](https://github.com/Do-Zu/dozu/issues/34) |
| [#19](https://github.com/Do-Zu/dozu/issues/19) [Task] Preserve local realtime and streaming with network failure recovery | task | waiting | P1 | L | 3 Full application | [#14](https://github.com/Do-Zu/dozu/issues/14), [#16](https://github.com/Do-Zu/dozu/issues/16), [#30](https://github.com/Do-Zu/dozu/issues/30) |
| [#20](https://github.com/Do-Zu/dozu/issues/20) [Task] Preserve schedules and native notifications from local state | task | waiting | P2 | M | 3 Full application | [#15](https://github.com/Do-Zu/dozu/issues/15), [#30](https://github.com/Do-Zu/dozu/issues/30), [#2](https://github.com/Do-Zu/dozu/issues/2) |
| [#21](https://github.com/Do-Zu/dozu/issues/21) [Task] Preserve PDF/editor/media and real YouTube/URL integrations locally | task | waiting | P1 | L | 3 Full application | [#16](https://github.com/Do-Zu/dozu/issues/16), [#18](https://github.com/Do-Zu/dozu/issues/18), [#27](https://github.com/Do-Zu/dozu/issues/27) |
| [#22](https://github.com/Do-Zu/dozu/issues/22) [Task] Verify complete local-first desktop parity across all supported OSes | task | waiting | P1 | XL | 4 Release | [#17](https://github.com/Do-Zu/dozu/issues/17), [#18](https://github.com/Do-Zu/dozu/issues/18), [#19](https://github.com/Do-Zu/dozu/issues/19), [#21](https://github.com/Do-Zu/dozu/issues/21), [#20](https://github.com/Do-Zu/dozu/issues/20), [#39](https://github.com/Do-Zu/dozu/issues/39), [#37](https://github.com/Do-Zu/dozu/issues/37) |
| [#23](https://github.com/Do-Zu/dozu/issues/23) [Task] Build self-contained installers with all required local services | task | waiting | P1 | XL | 4 Release | [#15](https://github.com/Do-Zu/dozu/issues/15), [#7](https://github.com/Do-Zu/dozu/issues/7), [#38](https://github.com/Do-Zu/dozu/issues/38), [#33](https://github.com/Do-Zu/dozu/issues/33) |
| [#24](https://github.com/Do-Zu/dozu/issues/24) [Task] Sign local-first desktop releases and notarize macOS artifacts | task | waiting | P1 | L | 4 Release | [#23](https://github.com/Do-Zu/dozu/issues/23) |
| [#25](https://github.com/Do-Zu/dozu/issues/25) [Task] Upgrade the bundled local stack with data-safe migrations | task | waiting | P1 | L | 4 Release | [#23](https://github.com/Do-Zu/dozu/issues/23), [#24](https://github.com/Do-Zu/dozu/issues/24), [#35](https://github.com/Do-Zu/dozu/issues/35) |
| [#26](https://github.com/Do-Zu/dozu/issues/26) [Task] Validate local-first beta, distribution and data-lifecycle support | task | waiting | P1 | L | 4 Release | [#22](https://github.com/Do-Zu/dozu/issues/22), [#24](https://github.com/Do-Zu/dozu/issues/24), [#25](https://github.com/Do-Zu/dozu/issues/25), [#10](https://github.com/Do-Zu/dozu/issues/10), [#36](https://github.com/Do-Zu/dozu/issues/36) |
| [#27](https://github.com/Do-Zu/dozu/issues/27) [Ticket] Resolve desktop integration callbacks, secrets and shared-state limits | ticket | ready | P0 | L | 0 Requirements | [#3](https://github.com/Do-Zu/dozu/issues/3), [#2](https://github.com/Do-Zu/dozu/issues/2) |
| [#28](https://github.com/Do-Zu/dozu/issues/28) [Task] Supervise local backend, database and embedding process lifecycle | task | waiting | P0 | L | 1 Foundation | [#29](https://github.com/Do-Zu/dozu/issues/29), [#40](https://github.com/Do-Zu/dozu/issues/40), [#8](https://github.com/Do-Zu/dozu/issues/8), [#12](https://github.com/Do-Zu/dozu/issues/12) |
| [#29](https://github.com/Do-Zu/dozu/issues/29) [Task] Bundle and initialize per-user PostgreSQL with pgvector | task | waiting | P0 | L | 1 Foundation | [#5](https://github.com/Do-Zu/dozu/issues/5), [#34](https://github.com/Do-Zu/dozu/issues/34), [#38](https://github.com/Do-Zu/dozu/issues/38) |
| [#30](https://github.com/Do-Zu/dozu/issues/30) [Task] Replace desktop Redis/BullMQ consumers with durable local adapters | task | waiting | P0 | XL | 2 Local services | [#29](https://github.com/Do-Zu/dozu/issues/29), [#3](https://github.com/Do-Zu/dozu/issues/3) |
| [#31](https://github.com/Do-Zu/dozu/issues/31) [Task] Store user-scoped provider credentials securely on the device | task | waiting | P1 | L | 2 Local services | [#34](https://github.com/Do-Zu/dozu/issues/34), [#27](https://github.com/Do-Zu/dozu/issues/27) |
| [#32](https://github.com/Do-Zu/dozu/issues/32) [Task] Bundle frontend assets and required local processing resources | task | waiting | P1 | M | 1 Foundation | [#5](https://github.com/Do-Zu/dozu/issues/5), [#3](https://github.com/Do-Zu/dozu/issues/3) |
| [#33](https://github.com/Do-Zu/dozu/issues/33) [Task] Validate automatic first-run setup on clean user machines | task | waiting | P1 | L | 3 Full application | [#15](https://github.com/Do-Zu/dozu/issues/15), [#29](https://github.com/Do-Zu/dozu/issues/29), [#40](https://github.com/Do-Zu/dozu/issues/40), [#8](https://github.com/Do-Zu/dozu/issues/8), [#32](https://github.com/Do-Zu/dozu/issues/32) |
| [#34](https://github.com/Do-Zu/dozu/issues/34) [Task] Define app-owned local data paths and ownership manifest | task | waiting | P0 | M | 1 Foundation | [#4](https://github.com/Do-Zu/dozu/issues/4) |
| [#35](https://github.com/Do-Zu/dozu/issues/35) [Task] Back up and restore local database, files and application settings | task | waiting | P1 | L | 4 Release | [#29](https://github.com/Do-Zu/dozu/issues/29), [#18](https://github.com/Do-Zu/dozu/issues/18), [#34](https://github.com/Do-Zu/dozu/issues/34), [#31](https://github.com/Do-Zu/dozu/issues/31) |
| [#36](https://github.com/Do-Zu/dozu/issues/36) [Task] Offer keep-data or permanent app-data deletion on every OS | task | waiting | P1 | L | 4 Release | [#23](https://github.com/Do-Zu/dozu/issues/23), [#34](https://github.com/Do-Zu/dozu/issues/34), [#31](https://github.com/Do-Zu/dozu/issues/31) |
| [#37](https://github.com/Do-Zu/dozu/issues/37) [Task] Verify local data authority and deliberate third-party network use | task | waiting | P1 | L | 4 Release | [#16](https://github.com/Do-Zu/dozu/issues/16), [#18](https://github.com/Do-Zu/dozu/issues/18), [#44](https://github.com/Do-Zu/dozu/issues/44), [#41](https://github.com/Do-Zu/dozu/issues/41), [#42](https://github.com/Do-Zu/dozu/issues/42), [#43](https://github.com/Do-Zu/dozu/issues/43) |
| [#38](https://github.com/Do-Zu/dozu/issues/38) [Task] Assemble verified per-platform runtimes, binaries and licenses | task | waiting | P0 | L | 1 Foundation | [#7](https://github.com/Do-Zu/dozu/issues/7) |
| [#39](https://github.com/Do-Zu/dozu/issues/39) [Task] Serve browser and Electron interfaces through the same localhost stack | task | waiting | P1 | M | 3 Full application | [#15](https://github.com/Do-Zu/dozu/issues/15), [#14](https://github.com/Do-Zu/dozu/issues/14), [#11](https://github.com/Do-Zu/dozu/issues/11) |
| [#40](https://github.com/Do-Zu/dozu/issues/40) [Task] Add a local backend profile with automatic seeds and lazy integrations | task | waiting | P0 | L | 2 Local services | [#29](https://github.com/Do-Zu/dozu/issues/29), [#30](https://github.com/Do-Zu/dozu/issues/30) |
| [#41](https://github.com/Do-Zu/dozu/issues/41) [Task] Preserve real payments with secure desktop reconciliation | task | blocked | P1 | XL | 2 Local services | [#27](https://github.com/Do-Zu/dozu/issues/27), [#31](https://github.com/Do-Zu/dozu/issues/31), [#40](https://github.com/Do-Zu/dozu/issues/40) |
| [#42](https://github.com/Do-Zu/dozu/issues/42) [Task] Preserve genuine email delivery and desktop return-link flows | task | waiting | P1 | L | 2 Local services | [#27](https://github.com/Do-Zu/dozu/issues/27), [#31](https://github.com/Do-Zu/dozu/issues/31), [#14](https://github.com/Do-Zu/dozu/issues/14), [#30](https://github.com/Do-Zu/dozu/issues/30) |
| [#43](https://github.com/Do-Zu/dozu/issues/43) [Task] Preserve classroom workflows with an explicit reachable-host design | task | waiting | P1 | XL | 2 Local services | [#27](https://github.com/Do-Zu/dozu/issues/27), [#14](https://github.com/Do-Zu/dozu/issues/14), [#30](https://github.com/Do-Zu/dozu/issues/30) |
| [#44](https://github.com/Do-Zu/dozu/issues/44) [Task] Preserve external AI integrations from the local backend | task | waiting | P1 | L | 2 Local services | [#27](https://github.com/Do-Zu/dozu/issues/27), [#31](https://github.com/Do-Zu/dozu/issues/31), [#40](https://github.com/Do-Zu/dozu/issues/40), [#8](https://github.com/Do-Zu/dozu/issues/8) |

## ROADMAP: [Ticket] Deliver self-contained local-first desktop and monorepo

[GitHub #1](https://github.com/Do-Zu/dozu/issues/1) | Type: ticket | Phase: All

Planning priority: P0 - Architecture/foundation work that unblocks the implementation path.

Planning complexity: XL - Umbrella delivery spanning the full product; execute through child tasks, not as one work item.

Dependencies: None

## Outcome
Package the complete existing website, backend and local data stack for Windows, macOS and Linux. Internet-enabled third-party features remain genuine integrations. Each user's computer is the primary source of truth.

## Acceptance criteria
- [ ] Next.js frontend, Express/business logic, PostgreSQL/pgvector, local files/jobs and FastAPI run on the user's machine without manual runtime/database setup.
- [ ] Preserve ALL pages, layouts, components, navigation, roles, locales and features; retain the website build and a localhost browser interface using the same local backend.
- [ ] Google/YouTube/email/payments/AI/classroom integration limitations have verified desktop-compatible designs; no online feature is silently removed or replaced with a simulation.
- [ ] Application data, accounts, progress, settings, jobs and uploads remain local; no required central Dozu service, cloud database or synchronization.
- [ ] Clean-machine installation, restart/crash recovery, upgrade/backup/restore, complete feature parity and uninstall keep/delete options pass on every supported platform.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## Authoritative requirement update
The user's latest clarification requires a self-hosted, local-first desktop with optional internet connectivity. It supersedes both earlier remote-backend and fully air-gapped assumptions. Third-party APIs are allowed; the application backend and authoritative storage remain local.

## Recommended stack
Electron + TypeScript supervising the existing Next.js standalone app, existing Express API, bundled PostgreSQL/pgvector, durable local jobs/cache adapters, and bundled FastAPI/embedding model. Preserve external AI provider interfaces with scoped user-owned credentials. pnpm workspaces/Turborepo + uv for development/build tooling.

## Repository
```text
apps/web                 complete current Next.js app
apps/api                 existing Express, local/website runtime profiles
apps/desktop             Electron shell, supervisor, installer hooks
services/embedding       bundled FastAPI service
packages/local-runtime   local bootstrap/jobs/files/cache/provider adapters
packages/runtime-contracts
resources/manifests      binaries/models/assets/license/checksum manifests
infra/                   dev tooling + retained website deployment
docs/                    architecture/integrations/release evidence
```

## Runtime
Electron/local browser → local Next.js → localhost Express → local PostgreSQL/pgvector/files/jobs/FastAPI. Express may call third-party Google, YouTube, SMTP, payments and configured AI providers when requested. Backend code is shared; every desktop installation owns its own backend instance and database.

## Release sequence
Requirements/integration audit → monorepo and packaged runtime proof → local providers and real integration adaptation → complete UI/feature parity → signed installers, data lifecycle and release evidence. The early proof is not a reduced-feature release.

## Specific limits to resolve
Desktop apps cannot protect a shared publisher merchant/API/SMTP secret. Use native public clients, user-owned credentials or supported provider delegation. Webhooks cannot target 127.0.0.1; verify authenticated outbound reconciliation or an opt-in scoped public callback/tunnel when required. Separate classroom installations do not share state without an explicit reachable host; no cloud sync is proposed.

## References
- [Next.js standalone output/assets](https://nextjs.org/docs/app/api-reference/config/next-config-js/output)
- [Electron process supervision](https://www.electronjs.org/docs/latest/api/utility-process)
- [Google desktop OAuth](https://developers.google.com/identity/protocols/oauth2/native-app)
- [PayOS API](https://payos.vn/docs/api/)
- [Electron security](https://www.electronjs.org/docs/latest/tutorial/security)

## DECISION-SCOPE: [Ticket] Record local-first requirements and full feature-preservation matrix

[GitHub #2](https://github.com/Do-Zu/dozu/issues/2) | Type: ticket | Phase: 0 Requirements

Planning priority: P0 - Architecture/foundation work that unblocks the implementation path.

Planning complexity: M - Requirements and a complete role/route matrix; bounded documentation with product decisions.

Dependencies: None

## Outcome
Record the now-fixed local-first architecture, full UI scope and supported platform matrix. Internet-enabled integrations remain in scope; do not reopen online-first versus offline-only as the architecture choice.

## Acceptance criteria
- [ ] Record local frontend/backend/database/files, optional internet APIs, no required central application server/cloud DB/sync and self-contained install as mandatory.
- [ ] Build a per-route/role/locale/feature matrix from all 84 current page entrypoints, 20 layouts, 164 shared TSX components and route-scoped code; update counts if sources change.
- [ ] Include all admin, teacher/student, payment/history, auth, generation, media, games, study, schedule/settings and navigation flows; no silent omissions.
- [ ] Agree OS minimum versions, CPU architectures, Linux distro baseline, installer types and resource budgets.
- [ ] Record public callback/shared-secret/classroom topology decisions under INTEGRATIONS; preserve actual external functionality wherever feasible.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## BASELINE: [Task] Audit complete UI/backend and local-first integration baselines

[GitHub #3](https://github.com/Do-Zu/dozu/issues/3) | Type: task | Phase: 0 Requirements

Planning priority: P0 - Architecture/foundation work that unblocks the implementation path.

Planning complexity: L - Cross-repository behavior audit, integration inventory and independent build/contract baselines.

Dependencies: None

## Outcome
Capture existing behavior and source provenance before migration, including external-provider dependencies and every UI workflow.

## Acceptance criteria
- [ ] Record source commits, licenses, dirty trees, DB/extensions/migrations, workers, provider initialization, external endpoints and deployment paths without exposing credentials.
- [ ] Run website lint/build, API typecheck/lint/Jest and embedding health/contract baselines in appropriate isolated environments; document pre-existing failures.
- [ ] Inventory every route/layout/component/provider/hook, role, locale and interaction; static route discovery alone is not full parity evidence.
- [ ] Trace Google/SMTP/payment/webhook/YouTube/LLM/R2/Cloudinary/Lambda/Redis consumers and identify what must stay local versus deliberate third-party API calls.
- [ ] Record runtime downloads, compiled API URLs, cloud credential assumptions and the safe source/history import strategy.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## DECISION-STACK: [Ticket] Prove Electron can package the complete local Next.js and service stack

[GitHub #4](https://github.com/Do-Zu/dozu/issues/4) | Type: ticket | Phase: 0 Requirements

Planning priority: P0 - Architecture/foundation work that unblocks the implementation path.

Planning complexity: XL - Multi-OS packaging experiment with Node, PostgreSQL/pgvector and Python compatibility unknowns; split the proof into platform work.

Dependencies: [#3](https://github.com/Do-Zu/dozu/issues/3), [#2](https://github.com/Do-Zu/dozu/issues/2)

## Outcome
Recommend Electron with the existing Next.js standalone server, Express and local data/services. Validate packaged behavior instead of creating a second React/Vite UI.

## Acceptance criteria
- [ ] Run a native packaged proof on Windows/macOS/Linux with full Next server semantics, local Express, PostgreSQL/pgvector and FastAPI/model.
- [ ] Verify Electron utilityProcess compatibility or bundle a pinned standalone Node runtime; no system Node/Python/database/Docker/WSL requirement.
- [ ] Exercise dynamic routes, locales/server messages, local data writes, files, sockets/streams, PDF/editor/media and a system-browser provider flow.
- [ ] Measure bundle size, RAM/startup, supported CPU/OS and native ABI/dynamic library compatibility; record evidence and resource budgets.
- [ ] Record architecture ADR; the proof is an early gate, not permission to reduce the first-release feature scope.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## IMPORT: [Task] Import current frontend/backend/embedding sources with provenance

[GitHub #5](https://github.com/Do-Zu/dozu/issues/5) | Type: task | Phase: 1 Foundation

Planning priority: P0 - Architecture/foundation work that unblocks the implementation path.

Planning complexity: M - Mostly structural source/history movement with provenance and secret checks.

Dependencies: [#3](https://github.com/Do-Zu/dozu/issues/3)

## Outcome
Move reviewed sources into apps/web, apps/api and services/embedding while retaining all UI and backend behavior.

## Acceptance criteria
- [ ] Preserve agreed history/attribution/licenses, source-ref mapping and applicable AGENTS guidance; keep original checkouts intact.
- [ ] Exclude credentials, local DBs/uploads/caches, nested .git, virtualenvs and node_modules from the public source import.
- [ ] Verify source inventory/secret scan and document required path-only changes separately from behavior changes.
- [ ] Keep Next route/component boundaries and server features; do not replace the UI with a selected subset.
- [ ] Retain website build/deployment capability and record source/deployment rollback.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## WORKSPACE: [Task] Establish reproducible monorepo workspaces and build graph

[GitHub #6](https://github.com/Do-Zu/dozu/issues/6) | Type: task | Phase: 1 Foundation

Planning priority: P0 - Architecture/foundation work that unblocks the implementation path.

Planning complexity: M - Workspace/lockfile/task-graph setup with Next tracing and peer-dependency validation.

Dependencies: [#5](https://github.com/Do-Zu/dozu/issues/5)

## Outcome
Use pnpm/Turborepo for TypeScript builds and explicit Python tooling without rewriting the application architecture.

## Acceptance criteria
- [ ] Create private workspace definitions, one pnpm lockfile and real internal dependencies only where consumed.
- [ ] Verify React singleton/peers, Next output tracing across monorepo boundaries and portable build outputs.
- [ ] Declare lint/typecheck/test/build/package dependencies and environment inputs; persistent dev tasks and migrations are uncached.
- [ ] Keep desktop binaries/models/runtime manifests and Python lockfiles in appropriate independent build pipelines.
- [ ] Verify clean install/build and document current npm lockfile migration.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## TOOLCHAINS: [Task] Pin portable toolchains and runtime-compatible builds

[GitHub #7](https://github.com/Do-Zu/dozu/issues/7) | Type: task | Phase: 1 Foundation

Planning priority: P0 - Architecture/foundation work that unblocks the implementation path.

Planning complexity: M - Portable scripts and version/ABI compatibility across three build environments.

Dependencies: [#6](https://github.com/Do-Zu/dozu/issues/6), [#4](https://github.com/Do-Zu/dozu/issues/4)

## Outcome
Replace Windows-only script assumptions and select supported toolchains compatible with the bundled Node/Electron/Python/native database stack.

## Acceptance criteria
- [ ] Make scripts/environment/path handling portable across all three OSes.
- [ ] Pin build toolchain/runtime versions and verify Electron/native-module ABI or standalone Node compatibility.
- [ ] Separate necessary framework/security upgrades from source movement with independent validation.
- [ ] Validate API aliases, production startup, migration paths, installed-resource paths and read-only installation behavior.
- [ ] Provide root development and packaging commands; end users require no developer tools.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## PYTHON: [Task] Bundle local FastAPI, Python and baseline embedding model

[GitHub #8](https://github.com/Do-Zu/dozu/issues/8) | Type: task | Phase: 1 Foundation

Planning priority: P0 - Architecture/foundation work that unblocks the implementation path.

Planning complexity: L - Python and native ML dependency/model packaging across operating systems.

Dependencies: [#5](https://github.com/Do-Zu/dozu/issues/5), [#38](https://github.com/Do-Zu/dozu/issues/38), [#34](https://github.com/Do-Zu/dozu/issues/34)

## Outcome
Package the current embedding service as a managed local process with its full CPU-capable runtime/model resources.

## Acceptance criteria
- [ ] Lock complete Python dependencies and package native libraries per target OS/architecture; no user pip/Python setup.
- [ ] Bundle pinned model/tokenizer/config resources and preserve the existing 384-dimensional vector contract.
- [ ] Load baseline resources from verified local paths without Hub fallback downloads blocking local startup.
- [ ] Verify text/PDF/transcript contracts and CPU operation; optional acceleration must not require manual setup.
- [ ] Expose loopback readiness/shutdown and route user files through authenticated local paths or URLs.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## DEV-INFRA: [Task] Provide local-stack development and packaging diagnostics

[GitHub #9](https://github.com/Do-Zu/dozu/issues/9) | Type: task | Phase: 1 Foundation

Planning priority: P2 - Required supporting work scheduled after the core foundations; not removed from release scope.

Planning complexity: M - Development orchestration and diagnostic documentation after local service contracts exist.

Dependencies: [#7](https://github.com/Do-Zu/dozu/issues/7), [#29](https://github.com/Do-Zu/dozu/issues/29), [#40](https://github.com/Do-Zu/dozu/issues/40), [#8](https://github.com/Do-Zu/dozu/issues/8)

## Outcome
Provide developer commands and diagnostics matching the managed desktop runtime while retaining website development.

## Acceptance criteria
- [ ] Run Next/Express/DB/embedding/jobs with explicit readiness and generated local configuration.
- [ ] Document development-only tooling separately from the installer: Docker may help development but is never a desktop runtime prerequisite.
- [ ] Provide placeholder-only environment templates and optional integration configuration instructions.
- [ ] Verify local browser and Electron point to the same API/DB/files with no compiled hosted Dozu endpoint.
- [ ] Document non-destructive stop/reset, logs, port conflicts and platform-specific native dependency troubleshooting.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## CI-DEPLOY: [Task] Build local desktop artifacts while retaining website CI/deployment

[GitHub #10](https://github.com/Do-Zu/dozu/issues/10) | Type: task | Phase: 1 Foundation

Planning priority: P1 - Required product, integration or release work after its prerequisites.

Planning complexity: L - Native CI and retained website deployment paths, artifacts and security checks.

Dependencies: [#7](https://github.com/Do-Zu/dozu/issues/7), [#8](https://github.com/Do-Zu/dozu/issues/8), [#40](https://github.com/Do-Zu/dozu/issues/40)

## Outcome
Update CI for the monorepo and self-contained desktop without removing the website build/deployment profile.

## Acceptance criteria
- [ ] Run website lint/build, API typecheck/lint/Jest and local embedding/provider contract checks with locked dependencies.
- [ ] Include transitive shared changes in filters and validate tracing/native resource inclusion.
- [ ] Retain website deployment contexts/migration ownership independently; desktop never requires that deployment.
- [ ] Scan public sources/artifacts for credentials and unintended provider defaults; protect release environments.
- [ ] Create representative native test artifacts and record rollback paths for website and desktop build changes.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## API-CLIENT: [Task] Route every frontend transport to the runtime-discovered local API

[GitHub #11](https://github.com/Do-Zu/dozu/issues/11) | Type: task | Phase: 2 Local services

Planning priority: P1 - Required product, integration or release work after its prerequisites.

Planning complexity: L - Several HTTP/auth/upload/socket/stream transports and runtime-origin behavior.

Dependencies: [#6](https://github.com/Do-Zu/dozu/issues/6), [#40](https://github.com/Do-Zu/dozu/issues/40)

## Outcome
Preserve typed wrappers and service behavior while removing baked-in hosted URLs from desktop HTTP, uploads, auth, Socket.IO and streams.

## Acceptance criteria
- [ ] Inventory Axios, direct fetch, refresh, upload/download, sockets and stream clients; use one localhost runtime configuration or same-origin proxy.
- [ ] Preserve headers/envelopes, validation, feature gating, multipart, retries and error handling.
- [ ] Keep existing website configuration profile without letting it leak into desktop builds.
- [ ] Verify random-port/port-conflict startup and local browser access without exposing privileged launch credentials in URLs.
- [ ] Prove frontend domain mutations/readback hit the installed local API/database.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## PLATFORM: [Task] Add narrow desktop host adapters around the retained Next.js UI

[GitHub #12](https://github.com/Do-Zu/dozu/issues/12) | Type: task | Phase: 2 Local services

Planning priority: P1 - Required product, integration or release work after its prerequisites.

Planning complexity: L - Security-sensitive preload/IPC interfaces and browser/Electron compatibility.

Dependencies: [#11](https://github.com/Do-Zu/dozu/issues/11), [#4](https://github.com/Do-Zu/dozu/issues/4), [#34](https://github.com/Do-Zu/dozu/issues/34)

## Outcome
Provide native capabilities without duplicating existing routes/navigation or coupling website components to Electron.

## Acceptance criteria
- [ ] Add typed interfaces only where needed for native files, notifications, lifecycle, secure settings and external system-browser actions.
- [ ] Keep Next.js routing/rendering/navigation and all current pages; retain browser-compatible behavior.
- [ ] Use a constrained preload/IPC boundary with validation, context isolation, sandboxing and renderer Node integration disabled.
- [ ] Handle native permission denial and missing optional provider credentials with translated feature-specific errors.
- [ ] Verify adapter behavior, navigation/session boundaries and safe external link handling.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## UI-I18N: [Task] Preserve the full Next.js UI, navigation, themes and en/vi assets

[GitHub #13](https://github.com/Do-Zu/dozu/issues/13) | Type: task | Phase: 2 Local services

Planning priority: P1 - Required product, integration or release work after its prerequisites.

Planning complexity: L - Full route/server-feature/assets preservation with role/locale regression coverage.

Dependencies: [#6](https://github.com/Do-Zu/dozu/issues/6), [#32](https://github.com/Do-Zu/dozu/issues/32)

## Outcome
Package the existing frontend as one Next.js app for browser and desktop rather than extracting a second frontend.

## Acceptance criteria
- [ ] Preserve all route/layout/component trees, server message loader, locale middleware, roles, theme/fonts and navigation.
- [ ] Configure standalone resource tracing and include public/.next/static/fonts/workers/translation files.
- [ ] Keep route-scoped code scoped; extract shared UI only when actually useful.
- [ ] Compare role/locale/theme visual/navigation baselines and check dynamic URLs, reload and deep links.
- [ ] Record every parity gap against the complete inventory; do not hide pages to pass smoke tests.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## AUTH: [Task] Preserve local accounts and adapt genuine Google OAuth for desktop

[GitHub #14](https://github.com/Do-Zu/dozu/issues/14) | Type: task | Phase: 2 Local services

Planning priority: P1 - Required product, integration or release work after its prerequisites.

Planning complexity: L - Local session lifecycle plus native OAuth, token/callback security and browser sessions.

Dependencies: [#40](https://github.com/Do-Zu/dozu/issues/40), [#11](https://github.com/Do-Zu/dozu/issues/11), [#12](https://github.com/Do-Zu/dozu/issues/12), [#31](https://github.com/Do-Zu/dozu/issues/31), [#27](https://github.com/Do-Zu/dozu/issues/27)

## Outcome
Reuse current local user/role/session business logic and preserve Google sign-in through the provider's installed-app flow.

## Acceptance criteria
- [ ] Persist accounts/roles/sessions locally; generate per-installation session/JWT secrets and secure localhost cookie/CSRF policy.
- [ ] Use a registered desktop/native Google client, system browser, PKCE/state/nonce and a short-lived loopback callback; validate issuer/audience and identity mapping.
- [ ] Do not ship confidential web-client secrets; document consent/client registration requirements and test supported redirect/port behavior.
- [ ] Verify login/refresh/restart/logout, replay and wrong-state rejection, local browser sessions and internet loss during provider login.
- [ ] External authentication failures must not require a central Dozu server or destroy existing local records.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## DESKTOP-SHELL: [Task] Integrate Electron with the complete managed local application

[GitHub #15](https://github.com/Do-Zu/dozu/issues/15) | Type: task | Phase: 3 Full application

Planning priority: P1 - Required product, integration or release work after its prerequisites.

Planning complexity: L - Native shell integration, runtime readiness, multiple windows and process recovery.

Dependencies: [#4](https://github.com/Do-Zu/dozu/issues/4), [#13](https://github.com/Do-Zu/dozu/issues/13), [#12](https://github.com/Do-Zu/dozu/issues/12), [#28](https://github.com/Do-Zu/dozu/issues/28)

## Outcome
Launch the existing local Next.js app inside Electron with the managed service stack and native lifecycle.

## Acceptance criteria
- [ ] Load the local origin only after required services/migrations are ready; show useful startup/recovery progress without a terminal.
- [ ] Retain every route, locale, role/navigation and dynamic topic URL; serve the same frontend to an optional browser.
- [ ] Validate installed-resource loading, Unicode/space paths, read-only install location, single instance and window lifecycle.
- [ ] Keep native capabilities narrow and external provider pages in the system browser where required.
- [ ] Verify quit/crash recovery does not leave orphan API/database/embedding processes or lose local writes.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## FEATURE-SLICE: [Task] Prove an end-to-end local study workflow without reducing release scope

[GitHub #16](https://github.com/Do-Zu/dozu/issues/16) | Type: task | Phase: 3 Full application

Planning priority: P1 - Required product, integration or release work after its prerequisites.

Planning complexity: M - One bounded workflow integrating existing UI with an established local stack.

Dependencies: [#15](https://github.com/Do-Zu/dozu/issues/15), [#14](https://github.com/Do-Zu/dozu/issues/14), [#18](https://github.com/Do-Zu/dozu/issues/18)

## Outcome
Use a representative workflow to validate the architecture early; all other existing features remain mandatory.

## Acceptance criteria
- [ ] Create/edit/study a topic through the retained UI, local Express, DB/files/jobs/embedding and required provider call where relevant.
- [ ] Read the same local changes in Electron and a localhost browser using one backend instance.
- [ ] Verify persistence after full application restart and external-integration failure handling.
- [ ] Preserve roles/subscription logic according to the real payment/integration decisions, not hardcoded fake access.
- [ ] Add integration evidence and record remaining matrix work explicitly; this proof is not a limited MVP release.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## MVP-FEATURES: [Task] Preserve every existing page, role and feature in the local desktop

[GitHub #17](https://github.com/Do-Zu/dozu/issues/17) | Type: task | Phase: 3 Full application

Planning priority: P1 - Required product, integration or release work after its prerequisites.

Planning complexity: XL - Full-product parity over 84 pages and multiple roles; split into feature-specific implementation tasks before starting.

Dependencies: [#16](https://github.com/Do-Zu/dozu/issues/16), [#27](https://github.com/Do-Zu/dozu/issues/27), [#41](https://github.com/Do-Zu/dozu/issues/41), [#42](https://github.com/Do-Zu/dozu/issues/42), [#43](https://github.com/Do-Zu/dozu/issues/43), [#44](https://github.com/Do-Zu/dozu/issues/44)

## Outcome
Complete the full parity matrix, including every existing admin/teacher/student, study, material, generation, account and commercial workflow.

## Acceptance criteria
- [ ] Exercise all 84 inventoried page entrypoints, 20 layouts, shared and route-scoped components; refresh the inventory if sources change.
- [ ] Preserve all navigation, CRUD, permissions, en/vi, settings, schedule, progress, games, quizzes, flashcards, editor/mindmap and classroom behavior.
- [ ] Retain real Google/YouTube/email/payment/AI integrations wherever feasible; record unresolved provider constraints with proposed solutions.
- [ ] Keep local records/files authoritative and no required central Dozu app service/cloud DB/sync.
- [ ] Do not pass completion by omitting/hiding/stubbing screens or simulating external success; every row needs evidence.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## FILES: [Task] Replace required cloud storage with local files and localhost URLs

[GitHub #18](https://github.com/Do-Zu/dozu/issues/18) | Type: task | Phase: 2 Local services

Planning priority: P1 - Required product, integration or release work after its prerequisites.

Planning complexity: L - Local storage adapter, secure streaming/range requests, metadata and attachment migration.

Dependencies: [#29](https://github.com/Do-Zu/dozu/issues/29), [#40](https://github.com/Do-Zu/dozu/issues/40), [#34](https://github.com/Do-Zu/dozu/issues/34)

## Outcome
Preserve upload/download/avatar/editor/material workflows while storing application-owned bytes and metadata locally.

## Acceptance criteria
- [ ] Provide local storage adapters for R2/S3/Cloudinary-backed application storage and authenticated localhost streaming/upload routes.
- [ ] Retain native/browser file selection, MIME/size validation, progress, export/save and media range requests.
- [ ] Prevent traversal/arbitrary file reads; use app-owned roots and local authorization.
- [ ] Persist thumbnails/generated content/attachment references and verify restart/backup consistency.
- [ ] Permit genuine remote ingestion/discovery where requested, but do not make uploaded/application-owned files depend on cloud storage.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## REALTIME: [Task] Preserve local realtime and streaming with network failure recovery

[GitHub #19](https://github.com/Do-Zu/dozu/issues/19) | Type: task | Phase: 3 Full application

Planning priority: P1 - Required product, integration or release work after its prerequisites.

Planning complexity: L - Authenticated sockets/streams, job progress and crash/reconnect/idempotency behavior.

Dependencies: [#14](https://github.com/Do-Zu/dozu/issues/14), [#16](https://github.com/Do-Zu/dozu/issues/16), [#30](https://github.com/Do-Zu/dozu/issues/30)

## Outcome
Keep Socket.IO/generation streams for local UI/browser sessions and explicitly designed external integration sessions.

## Acceptance criteria
- [ ] Preserve auth, expiry/refresh, rooms/events/progress and role checks against the same local backend.
- [ ] Recover sleep/resume/crash/reconnect without duplicate domain mutations or lost durable jobs.
- [ ] Distinguish local service failures from third-party internet loss with translated retry/cancel behavior.
- [ ] Verify payment/AI/provider retries are idempotent where required and never fake success.
- [ ] Remote classroom reachability follows CLASSROOM design; do not silently add cloud sync or a hosted relay.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## NOTIFICATIONS: [Task] Preserve schedules and native notifications from local state

[GitHub #20](https://github.com/Do-Zu/dozu/issues/20) | Type: task | Phase: 3 Full application

Planning priority: P2 - Required supporting work scheduled after the core foundations; not removed from release scope.

Planning complexity: M - OS notifications and persistent reminder scheduling once local job infrastructure exists.

Dependencies: [#15](https://github.com/Do-Zu/dozu/issues/15), [#30](https://github.com/Do-Zu/dozu/issues/30), [#2](https://github.com/Do-Zu/dozu/issues/2)

## Outcome
Run reminders/notification state locally with explicit app-running/background behavior and genuine configured email delivery where applicable.

## Acceptance criteria
- [ ] Persist schedules/history locally and restore jobs on restart with timezone/DST correctness.
- [ ] Handle OS permission denial, notification click routing and duplicate prevention.
- [ ] Document whether reminders need the app running and agree any background/startup component explicitly.
- [ ] Verify sleep/resume and process ownership on each OS; no central notification server dependency.
- [ ] Preserve existing web notification and email-trigger semantics through the local services and EMAIL task.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## MEDIA: [Task] Preserve PDF/editor/media and real YouTube/URL integrations locally

[GitHub #21](https://github.com/Do-Zu/dozu/issues/21) | Type: task | Phase: 3 Full application

Planning priority: P1 - Required product, integration or release work after its prerequisites.

Planning complexity: L - PDF/editor/audio/video, converters and genuine external ingestion/provider restrictions.

Dependencies: [#16](https://github.com/Do-Zu/dozu/issues/16), [#18](https://github.com/Do-Zu/dozu/issues/18), [#27](https://github.com/Do-Zu/dozu/issues/27)

## Outcome
Keep existing media features and internet-enabled content fetching while moving required processing/storage to the user's computer.

## Acceptance criteria
- [ ] Verify PDF.js workers, TipTap/editor, mindmap/canvas exports, audio capture/playback, video and local material URLs in packaged Chromium.
- [ ] Retain real YouTube metadata/transcript/video and URL ingestion where provider rules permit; handle connectivity/quotas/cookies honestly.
- [ ] Adapt the existing proxy rewrite and backend requests securely, including URL validation/SSRF controls without breaking intended content fetching.
- [ ] Bundle required local converters/rendering/transcription resources or explicitly retained external provider configuration; no unexpected browser/runtime download.
- [ ] Store app-owned content/metadata/generated files locally; do not replace requested online integrations with offline simulations.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## QA: [Task] Verify complete local-first desktop parity across all supported OSes

[GitHub #22](https://github.com/Do-Zu/dozu/issues/22) | Type: task | Phase: 4 Release

Planning priority: P1 - Required product, integration or release work after its prerequisites.

Planning complexity: XL - Complete feature/role/locale and multi-OS acceptance matrix; split into test suites and platform runs.

Dependencies: [#17](https://github.com/Do-Zu/dozu/issues/17), [#18](https://github.com/Do-Zu/dozu/issues/18), [#19](https://github.com/Do-Zu/dozu/issues/19), [#21](https://github.com/Do-Zu/dozu/issues/21), [#20](https://github.com/Do-Zu/dozu/issues/20), [#39](https://github.com/Do-Zu/dozu/issues/39), [#37](https://github.com/Do-Zu/dozu/issues/37)

## Outcome
Produce full release evidence for local runtime/data ownership and preserved real third-party integrations.

## Acceptance criteria
- [ ] Execute every route/role/locale/feature matrix row on packaged clients and retain website regression evidence.
- [ ] Use clean machines without developer runtimes/database/Docker/WSL and verify local backend/data startup.
- [ ] Test provider sandbox/authorized real flows and callback/secret constraints; no narrow happy-path smoke test can prove full parity.
- [ ] Disconnect internet and verify local data/core workflows remain usable while external actions show accurate errors/retry.
- [ ] Cover native permissions/DPI/keyboard, crash/sleep/ports, data consistency and explicit integration blockers.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## PACKAGING: [Task] Build self-contained installers with all required local services

[GitHub #23](https://github.com/Do-Zu/dozu/issues/23) | Type: task | Phase: 4 Release

Planning priority: P1 - Required product, integration or release work after its prerequisites.

Planning complexity: XL - Multi-runtime installers with native resources across OS/CPU combinations; split by packaging target.

Dependencies: [#15](https://github.com/Do-Zu/dozu/issues/15), [#7](https://github.com/Do-Zu/dozu/issues/7), [#38](https://github.com/Do-Zu/dozu/issues/38), [#33](https://github.com/Do-Zu/dozu/issues/33)

## Outcome
Generate per-platform installers that supply the entire local app stack and resource manifest.

## Acceptance criteria
- [ ] Package Next assets/server, Express/runtime, PostgreSQL/pgvector/tools, FastAPI/Python/model, local workers and native resources.
- [ ] Use native OS/CPU CI jobs and validate dynamic libraries/native ABIs, licenses/checksums and relocatable resource paths.
- [ ] Require no manual install/configuration of backend/database/Node/Python/Redis/Docker/WSL.
- [ ] Produce agreed Windows/macOS/Linux formats with clear install/upgrade/uninstall support and version metadata.
- [ ] Test clean install/launch, optional integration setup and full local workflow before release signing.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## SIGNING: [Task] Sign local-first desktop releases and notarize macOS artifacts

[GitHub #24](https://github.com/Do-Zu/dozu/issues/24) | Type: task | Phase: 4 Release

Planning priority: P1 - Required product, integration or release work after its prerequisites.

Planning complexity: L - Platform signing/notarization, helper processes, hardened runtime and release credentials.

Dependencies: [#23](https://github.com/Do-Zu/dozu/issues/23)

## Outcome
Configure trusted distribution for the shell and its bundled native sidecars.

## Acceptance criteria
- [ ] Confirm signing identities and protect release private keys in CI environments, never in source or client artifacts.
- [ ] Sign/notarize applicable app, helper executables/frameworks and installer resources; validate on clean downloaded installs.
- [ ] Test platform behavior for embedded PostgreSQL/Python helpers, hardened runtime and resource extraction.
- [ ] Fail release builds clearly if required signing/notarization is missing; distinguish unsigned test artifacts.
- [ ] Document renewal/revocation and verify downloaded installer signatures separately from update-package signatures.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## UPDATES: [Task] Upgrade the bundled local stack with data-safe migrations

[GitHub #25](https://github.com/Do-Zu/dozu/issues/25) | Type: task | Phase: 4 Release

Planning priority: P1 - Required product, integration or release work after its prerequisites.

Planning complexity: L - Signed upgrades across app/database/native versions with migration recovery.

Dependencies: [#23](https://github.com/Do-Zu/dozu/issues/23), [#24](https://github.com/Do-Zu/dozu/issues/24), [#35](https://github.com/Do-Zu/dozu/issues/35)

## Outcome
Support signed application/resource/database-compatible upgrades without making local use depend on an update server.

## Acceptance criteria
- [ ] Verify manual signed installer/package updates; any optional online check is deliberate and not required to start/read local data.
- [ ] Track app/API/DB/pgvector/Python/model compatibility and migrate local schema/config safely.
- [ ] Create a consistent pre-upgrade backup, preserve records/files/secrets and handle interrupted/incompatible upgrades.
- [ ] Reject tampered packages and test failed-update recovery, rollback limits and old cluster/tool compatibility.
- [ ] Do not introduce data synchronization or require a central Dozu app backend for upgrade/entitlement checks.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## BETA: [Task] Validate local-first beta, distribution and data-lifecycle support

[GitHub #26](https://github.com/Do-Zu/dozu/issues/26) | Type: task | Phase: 4 Release

Planning priority: P1 - Required product, integration or release work after its prerequisites.

Planning complexity: L - Cross-platform release evidence, full feature triage and installation/data-lifecycle validation.

Dependencies: [#22](https://github.com/Do-Zu/dozu/issues/22), [#24](https://github.com/Do-Zu/dozu/issues/24), [#25](https://github.com/Do-Zu/dozu/issues/25), [#10](https://github.com/Do-Zu/dozu/issues/10), [#36](https://github.com/Do-Zu/dozu/issues/36)

## Outcome
Run release acceptance for the full application, including realistic integration configuration and local ownership.

## Acceptance criteria
- [ ] Document supported OS/CPU/resources, local service lifecycle, per-feature internet requirements and provider credentials/callback limitations.
- [ ] Complete full feature-matrix beta evidence; triage unresolved provider/classroom/commercial constraints explicitly.
- [ ] Verify local backup/restore, migration recovery and both retain/delete uninstall paths for every installer type.
- [ ] Publish install/upgrade/support instructions that require no manual backend/database setup.
- [ ] Record release owner/exit criteria, known limitations and rollback; do not claim complete parity while material workflows are unverified.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## INTEGRATIONS: [Ticket] Resolve desktop integration callbacks, secrets and shared-state limits

[GitHub #27](https://github.com/Do-Zu/dozu/issues/27) | Type: ticket | Phase: 0 Requirements

Planning priority: P0 - Architecture/foundation work that unblocks the implementation path.

Planning complexity: L - Provider contracts, credential ownership, public callbacks and classroom architecture decisions.

Dependencies: [#3](https://github.com/Do-Zu/dozu/issues/3), [#2](https://github.com/Do-Zu/dozu/issues/2)

## Outcome
Preserve real third-party integrations and explicitly resolve the limits of a local backend with no operator-maintained central application infrastructure.

## Acceptance criteria
- [ ] Inventory Google, SMTP, PayOS/SePay, YouTube, LLM/Lambda, feedback and classroom public-endpoint/credential/state requirements with source evidence.
- [ ] Use native/public OAuth or scoped user-owned credentials; never distribute Dozu merchant/SMTP/vendor confidential secrets.
- [ ] For payments, decide merchant-self-hosting versus customer-paying-Dozu and validate a genuine provider-supported flow/entitlement authority.
- [ ] For required inbound callbacks, verify authenticated outbound reconciliation where supported or document an opt-in scoped tunnel/endpoint with availability/delivery constraints.
- [ ] For classrooms, decide local-only sessions versus reachable host/LAN/tunnel architecture without adding cloud DB/sync; keep pages/features in scope and unresolved gaps visible.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## SUPERVISOR: [Task] Supervise local backend, database and embedding process lifecycle

[GitHub #28](https://github.com/Do-Zu/dozu/issues/28) | Type: task | Phase: 1 Foundation

Planning priority: P0 - Architecture/foundation work that unblocks the implementation path.

Planning complexity: L - Dependent process orchestration, ports, locks, ownership and failure recovery.

Dependencies: [#29](https://github.com/Do-Zu/dozu/issues/29), [#40](https://github.com/Do-Zu/dozu/issues/40), [#8](https://github.com/Do-Zu/dozu/issues/8), [#12](https://github.com/Do-Zu/dozu/issues/12)

## Outcome
Make the Electron main process own startup, health, crash recovery and shutdown of every local service.

## Acceptance criteria
- [ ] Start DB/migration/seed, jobs/embedding, API, Next and window in dependency order with explicit ready/version contracts.
- [ ] Generate/allocate loopback ports and credentials, bind explicitly, and handle collisions/single-instance/multiple OS users.
- [ ] Track owned process IDs/locks and clean up on normal quit, crash, update and uninstall without touching unrelated processes.
- [ ] Handle low disk/RAM, non-admin/read-only install, Unicode/space paths and interrupted first boot with actionable UI.
- [ ] Validate utilityProcess or bundled Node approach; no terminal/manual backend commands.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## LOCAL-DB: [Task] Bundle and initialize per-user PostgreSQL with pgvector

[GitHub #29](https://github.com/Do-Zu/dozu/issues/29) | Type: task | Phase: 1 Foundation

Planning priority: P0 - Architecture/foundation work that unblocks the implementation path.

Planning complexity: L - Native PostgreSQL/pgvector initialization, ACLs, migrations and data integrity across OSes.

Dependencies: [#5](https://github.com/Do-Zu/dozu/issues/5), [#34](https://github.com/Do-Zu/dozu/issues/34), [#38](https://github.com/Do-Zu/dozu/issues/38)

## Outcome
Preserve PostgreSQL/Drizzle/vector behavior with a privately managed local database instance.

## Acceptance criteria
- [ ] Bundle PostgreSQL, matching pgvector and dynamic libraries/tools for each target OS/CPU.
- [ ] Initialize a user-owned non-global cluster with generated credentials/ACLs and loopback-only database access; handle Unix non-root and Windows permissions.
- [ ] Apply extension/schema migrations and seed required roles/settings atomically with versioned recovery.
- [ ] Verify JSONB, vector(384), cosine queries/HNSW and existing repository behavior on clean installations.
- [ ] Test restart/crash/port conflict/low disk, consistent backup and upgrades with no external DB or manual configuration.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## LOCAL-QUEUE: [Task] Replace desktop Redis/BullMQ consumers with durable local adapters

[GitHub #30](https://github.com/Do-Zu/dozu/issues/30) | Type: task | Phase: 2 Local services

Planning priority: P0 - Architecture/foundation work that unblocks the implementation path.

Planning complexity: XL - Replacement covers queues/cache/pubsub/counters/payment/socket consumers; split by adapter and consumer.

Dependencies: [#29](https://github.com/Do-Zu/dozu/issues/29), [#3](https://github.com/Do-Zu/dozu/issues/3)

## Outcome
Remove the desktop dependency on manually installed Redis/WSL while preserving queues, cache, pubsub, recommendation/counter and payment/socket semantics.

## Acceptance criteria
- [ ] Inventory all Redis imports and define local adapters for jobs/retries/delays/events/cache/counters/payment mappings.
- [ ] Persist durable state in local PostgreSQL and use bounded process-local caching only for disposable values.
- [ ] Preserve cancellation/progress/priorities/backoff/schedules and recover interrupted jobs with idempotent mutations.
- [ ] Retain existing website Redis profile if needed; selecting desktop mode must not initialize cloud/Redis clients.
- [ ] Verify recommendations, word-frequency, notifications, generation, subscriptions/payments and sockets against old behavior.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## PROVIDER-SECRETS: [Task] Store user-scoped provider credentials securely on the device

[GitHub #31](https://github.com/Do-Zu/dozu/issues/31) | Type: task | Phase: 2 Local services

Planning priority: P1 - Required product, integration or release work after its prerequisites.

Planning complexity: L - OS credential stores, key lifecycle, renderer isolation and safe backup/delete behavior.

Dependencies: [#34](https://github.com/Do-Zu/dozu/issues/34), [#27](https://github.com/Do-Zu/dozu/issues/27)

## Outcome
Support genuine external integrations without bundling shared publisher secrets or storing raw provider keys in renderer state.

## Acceptance criteria
- [ ] Classify OAuth client IDs/public native credentials versus user-scoped secrets and confidential publisher credentials.
- [ ] Use supported OS credential storage with explicit handling when secure storage is unavailable; no silent insecure fallback.
- [ ] Provide in-app setup/test/revoke for required user-owned SMTP/merchant/AI credentials and redact logs/errors.
- [ ] Replace raw provider-key persistence paths appropriately; renderer receives scoped operations/status rather than secret values.
- [ ] Verify per-user isolation, backup/export treatment, rotation/revocation and deletion of owned credential entries at uninstall.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## LOCAL-ASSETS: [Task] Bundle frontend assets and required local processing resources

[GitHub #32](https://github.com/Do-Zu/dozu/issues/32) | Type: task | Phase: 1 Foundation

Planning priority: P1 - Required product, integration or release work after its prerequisites.

Planning complexity: M - Resource inventory, tracing, copied assets and disconnected local rendering checks.

Dependencies: [#5](https://github.com/Do-Zu/dozu/issues/5), [#3](https://github.com/Do-Zu/dozu/issues/3)

## Outcome
Ensure the retained UI and local workflows load from installed resources while preserving deliberate external content features.

## Acceptance criteria
- [ ] Package Next public/static/traced assets, fonts, icons, i18n, PDF workers and local baseline images.
- [ ] Audit converter/media/browser/transcription dependencies and include resources needed for local processing.
- [ ] Verify local pages/navigation with empty caches and internet unavailable; external content features may show specific connectivity state.
- [ ] Do not infer all URL literals are runtime fetches or blanket-block YouTube/provider APIs.
- [ ] Remove accidental CDN/runtime fallback dependencies for bundled resources and record license/checksum provenance.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## FIRST-BOOT: [Task] Validate automatic first-run setup on clean user machines

[GitHub #33](https://github.com/Do-Zu/dozu/issues/33) | Type: task | Phase: 3 Full application

Planning priority: P1 - Required product, integration or release work after its prerequisites.

Planning complexity: L - Clean-machine multi-OS initialization, interrupted setup and runtime/resource failures.

Dependencies: [#15](https://github.com/Do-Zu/dozu/issues/15), [#29](https://github.com/Do-Zu/dozu/issues/29), [#40](https://github.com/Do-Zu/dozu/issues/40), [#8](https://github.com/Do-Zu/dozu/issues/8), [#32](https://github.com/Do-Zu/dozu/issues/32)

## Outcome
Prove the installer provides a working local app without developer setup or a required central Dozu server.

## Acceptance criteria
- [ ] Install as ordinary users with no Node/Python/PostgreSQL/Redis/Docker/WSL and empty app/browser caches.
- [ ] Automatically create data roots/local credentials/DB/extensions/migrations/seeds and start services/UI.
- [ ] Verify basic local use before optional integration credentials are configured; missing third-party keys must not crash bootstrap.
- [ ] Test internet available/unavailable, port conflicts, interrupted setup/retry and installed-resource integrity.
- [ ] Record OS/CPU-specific installation and initial-study evidence; first-run external OAuth/payment calls may require internet legitimately.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## DATA-PATHS: [Task] Define app-owned local data paths and ownership manifest

[GitHub #34](https://github.com/Do-Zu/dozu/issues/34) | Type: task | Phase: 1 Foundation

Planning priority: P0 - Architecture/foundation work that unblocks the implementation path.

Planning complexity: M - Well-bounded ownership manifest and canonical paths/permissions across platforms.

Dependencies: [#4](https://github.com/Do-Zu/dozu/issues/4)

## Outcome
Track every persistent and transient application-owned location for data ownership, backup and safe uninstall.

## Acceptance criteria
- [ ] Use appropriate non-roaming/local per-user data paths on Windows/macOS/Linux and separate immutable installed resources.
- [ ] Inventory DB/WAL/files/jobs/accounts/settings/generated content, browser storage, logs/cache/temp/models/backups/secrets/update staging.
- [ ] Enforce directory ownership/permissions and canonical path boundaries; support multiple users and Unicode/space paths.
- [ ] Distinguish app-managed data from user-selected external exports and unrelated resources.
- [ ] Expose documented storage/size/location information and a machine-readable cleanup/backup ownership manifest.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## BACKUP: [Task] Back up and restore local database, files and application settings

[GitHub #35](https://github.com/Do-Zu/dozu/issues/35) | Type: task | Phase: 4 Release

Planning priority: P1 - Required product, integration or release work after its prerequisites.

Planning complexity: L - Consistent database/files capture, versioned restore, secrets and interrupted recovery.

Dependencies: [#29](https://github.com/Do-Zu/dozu/issues/29), [#18](https://github.com/Do-Zu/dozu/issues/18), [#34](https://github.com/Do-Zu/dozu/issues/34), [#31](https://github.com/Do-Zu/dozu/issues/31)

## Outcome
Provide consistent user-controlled local backup/export and restore without a cloud synchronization service.

## Acceptance criteria
- [ ] Capture database/files/jobs/settings consistently with schema/version/checksum manifest.
- [ ] Handle credentials explicitly with safe exclusion or encrypted/user-authorized transfer; never expose provider secrets in plaintext exports.
- [ ] Validate restore integrity/compatibility and confirm overwrites with recoverable pre-restore state.
- [ ] Test interrupted/low-disk restore, separate installation import, file references and local record completeness.
- [ ] Document user-selected exported backups separately from app-owned data subject to uninstall cleanup.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## UNINSTALL: [Task] Offer keep-data or permanent app-data deletion on every OS

[GitHub #36](https://github.com/Do-Zu/dozu/issues/36) | Type: task | Phase: 4 Release

Planning priority: P1 - Required product, integration or release work after its prerequisites.

Planning complexity: L - Destructive lifecycle behavior and retention/deletion across three installer ecosystems.

Dependencies: [#23](https://github.com/Do-Zu/dozu/issues/23), [#34](https://github.com/Do-Zu/dozu/issues/34), [#31](https://github.com/Do-Zu/dozu/issues/31)

## Outcome
Make each supported uninstall workflow offer retention or permanent deletion of all app-owned local data.

## Acceptance criteria
- [ ] Implement an explicit keep/delete choice with destructive confirmation for Windows/macOS/Linux installer types; DMG/AppImage removal alone is insufficient.
- [ ] Stop owned services and verify exact canonical app roots before deleting DB/WAL/files/jobs/settings/browser storage/cache/logs/temp/backups/model overrides and credential entries.
- [ ] Preserve unrelated paths and user-chosen exports outside app ownership; report locked files/permissions and partial cleanup accurately.
- [ ] Test cancellation, retain/reinstall, delete/reinstall, multi-user ownership and failed cleanup with fixtures on each OS.
- [ ] Describe logical permanent deletion accurately without promising forensic erasure from SSD/snapshots.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## NETWORK-GATE: [Task] Verify local data authority and deliberate third-party network use

[GitHub #37](https://github.com/Do-Zu/dozu/issues/37) | Type: task | Phase: 4 Release

Planning priority: P1 - Required product, integration or release work after its prerequisites.

Planning complexity: L - Cross-process endpoint tracing plus data-ownership and integration-failure validation.

Dependencies: [#16](https://github.com/Do-Zu/dozu/issues/16), [#18](https://github.com/Do-Zu/dozu/issues/18), [#44](https://github.com/Do-Zu/dozu/issues/44), [#41](https://github.com/Do-Zu/dozu/issues/41), [#42](https://github.com/Do-Zu/dozu/issues/42), [#43](https://github.com/Do-Zu/dozu/issues/43)

## Outcome
Prove no central application backend/database/storage is required while allowing genuine integration traffic.

## Acceptance criteria
- [ ] Trace frontend/backend/child-process DB, HTTP, storage, socket and provider endpoints in packaged tests.
- [ ] Fail tests for accidental legacy hosted Dozu API, external database, required cloud object storage or application-data sync.
- [ ] Allow documented Google/YouTube/SMTP/payment/AI/selected content requests and verify payload scope/log redaction.
- [ ] Block or stop central Dozu services and confirm local records/workflows and localhost browser continue to work.
- [ ] Disconnect internet and test accurate per-feature errors/recovery without globally blocking legitimate integrations or simulating success.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## SUPPLY-CHAIN: [Task] Assemble verified per-platform runtimes, binaries and licenses

[GitHub #38](https://github.com/Do-Zu/dozu/issues/38) | Type: task | Phase: 1 Foundation

Planning priority: P0 - Architecture/foundation work that unblocks the implementation path.

Planning complexity: L - Native binary/model provenance, redistribution, dependency closure and architecture checks.

Dependencies: [#7](https://github.com/Do-Zu/dozu/issues/7)

## Outcome
Create reproducible release manifests for all bundled runtimes/extensions/resources and their redistribution obligations.

## Acceptance criteria
- [ ] Pin source/version/checksum/architecture for Electron/Node strategy, PostgreSQL/pgvector/tools, Python/native libraries and embedding resources.
- [ ] Verify all required runtime dynamic libraries and native ABIs on clean target machines.
- [ ] Record licenses/attribution and permitted binary/model redistribution; obtain artifacts during controlled build/release assembly.
- [ ] Keep source credentials, developer caches and user data out of installers; supply component inventory and provenance.
- [ ] Define installed-resource verification and upgrade compatibility without requiring user-side package managers or runtime downloads.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## LOCAL-WEB: [Task] Serve browser and Electron interfaces through the same localhost stack

[GitHub #39](https://github.com/Do-Zu/dozu/issues/39) | Type: task | Phase: 3 Full application

Planning priority: P1 - Required product, integration or release work after its prerequisites.

Planning complexity: M - Browser session bootstrap and same-local-backend behavior after auth/transports are established.

Dependencies: [#15](https://github.com/Do-Zu/dozu/issues/15), [#14](https://github.com/Do-Zu/dozu/issues/14), [#11](https://github.com/Do-Zu/dozu/issues/11)

## Outcome
Retain the browser website interface backed by the exact same local service/data instance used by Electron.

## Acceptance criteria
- [ ] Open the existing local Next origin in a system browser through a safe session bootstrap, not privileged credentials embedded in URLs.
- [ ] Verify shared local data and authenticated API/socket/stream/file access in both interfaces.
- [ ] Keep loopback Host/Origin/CSRF/session controls compatible with both without permissive wildcard exposure.
- [ ] Test route reload/deep links, local ports, simultaneous sessions and backend lifetime after window close.
- [ ] Retain website build capability independently; no central deployment is required to use either local interface.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## LOCAL-BOOTSTRAP: [Task] Add a local backend profile with automatic seeds and lazy integrations

[GitHub #40](https://github.com/Do-Zu/dozu/issues/40) | Type: task | Phase: 2 Local services

Planning priority: P0 - Architecture/foundation work that unblocks the implementation path.

Planning complexity: L - Profile-based service wiring, lazy providers, seeds and local execution of cloud job handlers.

Dependencies: [#29](https://github.com/Do-Zu/dozu/issues/29), [#30](https://github.com/Do-Zu/dozu/issues/30)

## Outcome
Reuse Express domain logic while initializing local services/configuration automatically and deferring optional external integrations until configured.

## Acceptance criteria
- [ ] Inject local DB/files/jobs/cache/secrets configuration; generate required per-installation auth/bootstrap values.
- [ ] Remove eager remote-client/module-global initialization that crashes startup when SMTP/merchant/LLM/cloud keys are absent.
- [ ] Execute existing Lambda job handlers locally while retaining deliberate third-party provider requests.
- [ ] Seed required roles/permissions/plans/provider metadata idempotently with product-correct access semantics; do not fake paid entitlements.
- [ ] Verify local profile startup with no external credentials, explicit loopback binding and clean shutdown/health.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## PAYMENTS: [Task] Preserve real payments with secure desktop reconciliation

[GitHub #41](https://github.com/Do-Zu/dozu/issues/41) | Type: task | Phase: 2 Local services

Planning priority: P1 - Required product, integration or release work after its prerequisites.

Planning complexity: XL - Merchant ownership and provider reconciliation/callback feasibility are unresolved; split after design validation.

Dependencies: [#27](https://github.com/Do-Zu/dozu/issues/27), [#31](https://github.com/Do-Zu/dozu/issues/31), [#40](https://github.com/Do-Zu/dozu/issues/40)

Blocking decision: Payment ownership is undecided: does each user supply their own merchant account, or are customers paying Dozu? The choice determines who can hold merchant secrets and how genuine payment/entitlement verification works. Resolve in #27 before implementation.

## Outcome
Adapt PayOS/SePay checkout/status/history for the agreed merchant/customer ownership model without distributing Dozu merchant secrets.

## Acceptance criteria
- [ ] Record owner of merchant keys and transaction authority; choose user-owned merchant credentials or provider-managed checkout/entitlement flow as appropriate.
- [ ] Keep real checkout in supported browser/provider flow; validate redirect binding, order/amount/currency/account and never trust success URL as payment proof.
- [ ] Implement documented authenticated provider status reconciliation (current PayOS getPaymentStatus is unimplemented), durable local mappings and idempotent subscription updates.
- [ ] When webhooks are mandatory, prove provider-supported scoped tunnel/public callback delivery/signature/replay behavior and host-offline recovery; no silent hosted Dozu relay.
- [ ] Test failure/cancel/refund/restart/duplicate events and preserve payment/admin/history UI; explicitly report unresolved provider constraints.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## EMAIL: [Task] Preserve genuine email delivery and desktop return-link flows

[GitHub #42](https://github.com/Do-Zu/dozu/issues/42) | Type: task | Phase: 2 Local services

Planning priority: P1 - Required product, integration or release work after its prerequisites.

Planning complexity: L - Real delivery with delegated credentials plus secure local verification/recovery return paths.

Dependencies: [#27](https://github.com/Do-Zu/dozu/issues/27), [#31](https://github.com/Do-Zu/dozu/issues/31), [#14](https://github.com/Do-Zu/dozu/issues/14), [#30](https://github.com/Do-Zu/dozu/issues/30)

## Outcome
Retain SMTP/provider mail behavior using user-scoped or delegated credentials and local durable submission state.

## Acceptance criteria
- [ ] Configure/test real SMTP or supported delegated provider auth in-app without bundling a publisher mailer password.
- [ ] Preserve delivery/retry/error reporting and local message/audit records; no fake delivery/outbox-only replacement.
- [ ] Design verification/password-reset links for local app recovery safely; handle another-device clicks, loopback reachability, tokens and expiry explicitly.
- [ ] Keep browser/Electron account flows and templates/translations compatible with provider requirements.
- [ ] Test configured delivery, missing/revoked credentials, offline retry, restart/idempotency and secret redaction.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## CLASSROOM: [Task] Preserve classroom workflows with an explicit reachable-host design

[GitHub #43](https://github.com/Do-Zu/dozu/issues/43) | Type: task | Phase: 2 Local services

Planning priority: P1 - Required product, integration or release work after its prerequisites.

Planning complexity: XL - Remote participant topology, reachability, TLS and host availability are unresolved; split after architecture decision.

Dependencies: [#27](https://github.com/Do-Zu/dozu/issues/27), [#14](https://github.com/Do-Zu/dozu/issues/14), [#30](https://github.com/Do-Zu/dozu/issues/30)

Blocking decision: The participant topology is undecided: same-device browser sessions, LAN clients, or remote internet participants reaching a user-owned host/tunnel. Resolve host ownership, authentication/TLS and availability in #27 before implementation.

## Outcome
Preserve classroom pages/roles/assignments/quizzes/live events and specify how participants access an authoritative local host.

## Acceptance criteria
- [ ] Retain all teacher/student/admin records/workflows on the local database; test multiple browser/window sessions first.
- [ ] For remote participants, decide and prove opt-in authenticated LAN/reachable user host/tunnel access, ownership, NAT/TLS and authorization; loopback alone cannot connect independent installations.
- [ ] Do not add central Dozu servers, cloud database or data synchronization as an implicit solution.
- [ ] Define host availability, reconnect, participant identity/access/revocation and data visibility with explicit user-facing limits.
- [ ] Validate real event delivery and persisted classroom state; no local-record simulation presented as remote collaboration.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

## AI-PROVIDERS: [Task] Preserve external AI integrations from the local backend

[GitHub #44](https://github.com/Do-Zu/dozu/issues/44) | Type: task | Phase: 2 Local services

Planning priority: P1 - Required product, integration or release work after its prerequisites.

Planning complexity: L - Preserve provider streaming/schema/quotas while moving orchestration and credential handling local.

Dependencies: [#27](https://github.com/Do-Zu/dozu/issues/27), [#31](https://github.com/Do-Zu/dozu/issues/31), [#40](https://github.com/Do-Zu/dozu/issues/40), [#8](https://github.com/Do-Zu/dozu/issues/8)

## Outcome
Reuse genuine LLM provider/model configuration and output contracts while executing orchestration locally and persisting application content locally.

## Acceptance criteria
- [ ] Preserve configured provider calls, streaming/cancellation, quotas and structured flashcard/quiz/mindmap outputs with scoped user-owned credentials.
- [ ] Run required job handlers locally instead of depending on an operator-maintained Lambda/proxy; persist prompts/results/progress locally.
- [ ] Explain submitted content/provider processing and limit payloads to the requested feature; cloud APIs do not become the application's data store.
- [ ] Do not distribute publisher-paid shared API keys or impose an unrequested local generative model requirement.
- [ ] Test valid/revoked/missing keys, rate limits/internet loss/retry and local embedding/vector behavior without breaking unrelated local use.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.
