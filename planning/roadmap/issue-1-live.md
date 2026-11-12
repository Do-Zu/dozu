<!-- dozu-tracking:start -->
## Work tracking
Use the live **status:**, **priority:** and **complexity:** labels above; **Assignees** identifies the owner. These labels are separate from the task/ticket type.

**Planning complexity:** XL - Umbrella delivery spanning the full product; execute through child tasks, not as one work item.
Complexity is a provisional scope/uncertainty estimate, not a delivery-time commitment. XL work must be split into executable subtasks before starting.
**Planning priority:** P0 - Architecture/foundation work that unblocks the implementation path.

### Live views
- [Your Project #6 board](https://github.com/orgs/Do-Zu/projects/6)
- [Doing](https://github.com/Do-Zu/dozu/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22status%3Ain-progress%22) | [Review](https://github.com/Do-Zu/dozu/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22status%3Ain-review%22) | [Ready](https://github.com/Do-Zu/dozu/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22status%3Aready%22)
- [Blocked](https://github.com/Do-Zu/dozu/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22status%3Ablocked%22) | [Waiting on prerequisites](https://github.com/Do-Zu/dozu/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22status%3Awaiting%22)

### Workflow rules
Keep exactly one status, priority and complexity label per issue. Assign an owner when work starts. Waiting means ordinary dependencies remain; blocked requires a specific reason. Close as completed only after acceptance evidence/review; a closed-not-planned item is not done. Start no more than one issue per owner unless deliberately agreed. Your main board is [Dozu Project #6](https://github.com/orgs/Do-Zu/projects/6). Issue labels and project fields are initialized consistently, but no automatic two-way synchronization is configured. Built-in Labels and Assignees reflect their issues; custom project Status/Priority/Complexity must be maintained deliberately. Local dashboard counts are snapshots refreshed by sync-issue-tracking.ps1.

Priority: P0 architecture/foundation unblockers; P1 required feature/integration/release work; P2 required supporting work later in the sequence; P3 optional/future only if explicitly added. Complexity: S contained; M moderate; L cross-system/native/security; XL umbrella/high uncertainty requiring breakdown.
<!-- dozu-tracking:end -->

## Outcome
Package the complete existing website, backend and local data stack for Windows, macOS and Linux. Internet-enabled third-party features remain genuine integrations. Each user's computer is the primary source of truth.

## Acceptance criteria
- [ ] Next.js frontend, Express/business logic, PostgreSQL, local files/jobs and FastAPI run on the user's machine without manual runtime/database setup.
- [ ] Preserve ALL pages, layouts, components, navigation, roles, locales and features; retain the website build and a localhost browser interface using the same local backend.
- [ ] Google/YouTube/email/payments/AI/classroom integration limitations have verified desktop-compatible designs; no online feature is silently removed or replaced with a simulation.
- [ ] Application data, accounts, progress, settings, jobs and uploads remain local; no required central Dozu service, cloud database or synchronization.
- [ ] Clean-machine installation, restart/crash recovery, upgrade/backup/restore, complete feature parity and uninstall keep/delete options pass on every supported platform.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All existing pages remain in scope; explicit v1 capability deferrals in the 2026-11-11 amendment below apply.

## Authoritative requirement update
The user's latest clarification requires a self-hosted, local-first desktop with optional internet connectivity. It supersedes both earlier remote-backend and fully air-gapped assumptions. Third-party APIs are allowed; the application backend and authoritative storage remain local.

## Recommended stack
Electron + TypeScript supervising the existing Next.js standalone app, existing Express API, bundled PostgreSQL, durable local jobs/cache adapters, and bundled FastAPI/embedding model. Preserve external AI provider interfaces with scoped user-owned credentials. pnpm workspaces/Turborepo + uv for development/build tooling.

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
Electron/local browser → local Next.js → localhost Express → local PostgreSQL/files/jobs/FastAPI. Express may call third-party Google, YouTube, SMTP, payments and configured AI providers when requested. Backend code is shared; every desktop installation owns its own backend instance and database.

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

<!-- dozu-roadmap:ROADMAP -->

Phase: All | Priority: P0

## Dependencies
None; this work can start independently.

## Delivery checklist
- [x] #2 - [Ticket] Record local-first requirements and full feature-preservation matrix
- [x] #3 - [Task] Audit complete UI/backend and local-first integration baselines
- [ ] #4 - [Ticket] Prove Electron can package the complete local Next.js and service stack
- [ ] #5 - [Task] Import current frontend/backend/embedding sources with provenance
- [ ] #6 - [Task] Establish reproducible monorepo workspaces and build graph
- [ ] #7 - [Task] Pin portable toolchains and runtime-compatible builds
- [ ] #8 - [Task] Bundle local FastAPI, Python and baseline embedding model
- [ ] #9 - [Task] Provide local-stack development and packaging diagnostics
- [ ] #10 - [Task] Build local desktop artifacts while retaining website CI/deployment
- [ ] #11 - [Task] Route every frontend transport to the runtime-discovered local API
- [ ] #12 - [Task] Add narrow desktop host adapters around the retained Next.js UI
- [ ] #13 - [Task] Preserve the full Next.js UI, navigation, themes and en/vi assets
- [ ] #14 - [Task] Preserve local accounts and adapt genuine Google OAuth for desktop
- [ ] #15 - [Task] Integrate Electron with the complete managed local application
- [ ] #16 - [Task] Prove an end-to-end local study workflow without reducing release scope
- [ ] #17 - [Task] Preserve every existing page, role and feature in the local desktop
- [ ] #18 - [Task] Replace required cloud storage with local files and localhost URLs
- [ ] #19 - [Task] Preserve local realtime and streaming with network failure recovery
- [ ] #20 - [Task] Preserve schedules and native notifications from local state
- [ ] #21 - [Task] Preserve PDF/editor/media and real YouTube/URL integrations locally
- [ ] #22 - [Task] Verify complete local-first desktop parity across all supported OSes
- [ ] #23 - [Task] Build self-contained installers with all required local services
- [ ] #24 - [Task] Sign local-first desktop releases and notarize macOS artifacts
- [ ] #25 - [Task] Upgrade the bundled local stack with data-safe migrations
- [ ] #26 - [Task] Validate local-first beta, distribution and data-lifecycle support
- [ ] #27 - [Ticket] Resolve desktop integration callbacks, secrets and shared-state limits
- [ ] #28 - [Task] Supervise local backend, database and embedding process lifecycle
- [ ] #29 - [Task] Bundle and initialize per-user PostgreSQL (pgvector deferred)
- [ ] #30 - [Task] Replace desktop Redis/BullMQ consumers with durable local adapters
- [ ] #31 - [Task] Store user-scoped provider credentials securely on the device
- [ ] #32 - [Task] Bundle frontend assets and required local processing resources
- [ ] #33 - [Task] Validate automatic first-run setup on clean user machines
- [ ] #34 - [Task] Define app-owned local data paths and ownership manifest
- [ ] #35 - [Task] Back up and restore local database, files and application settings
- [ ] #36 - [Task] Offer keep-data or permanent app-data deletion on every OS
- [ ] #37 - [Task] Verify local data authority and deliberate third-party network use
- [ ] #38 - [Task] Assemble verified per-platform runtimes, binaries and licenses
- [ ] #39 - [Task] Serve browser and Electron interfaces through the same localhost stack
- [ ] #40 - [Task] Add a local backend profile with automatic seeds and lazy integrations
- [ ] #41 - [Task] Preserve real payments with secure desktop reconciliation
- [ ] #42 - [Task] Preserve genuine email delivery and desktop return-link flows
- [ ] #43 - [Task] Preserve classroom workflows with an explicit reachable-host design
- [ ] #44 - [Task] Preserve external AI integrations from the local backend

## v1 requirements agreed — 2026-11-10

#2 records the user-approved OS/CPU/installer/hardware/resource contract and low-resource mode. Classrooms support other devices on the same LAN (#43), with the user-owned host authoritative. Payment execution is explicitly deferred/skipped and tracked by the existing blocked #41; it is an explicit exception to prior all-feature payment release wording, not authorization to delete payment/history/admin pages. Remaining payment implementation criteria apply only upon explicit reopening. No central backend/cloud DB/sync is introduced. Budgets are targets awaiting proof; provide benchmark evidence and an explicit recommendation before changing them. Requirements completion does not complete implementation or release compliance.

<!-- dozu-v1-scope-2026-11-11:start -->
## User-approved v1 scope amendment — 2026-11-11

- Remove local speech-to-text from this version: no whisper.cpp server, tiny speech model, speech startup/readiness gate or speech-only assets. Retain independent media playback and genuine existing YouTube transcript text retrieval. Preserve source/page inventory; no fake transcript or new cloud STT fallback.
- Keep PostgreSQL; **defer pgvector**. A private relational cluster, reviewed migrations/seeds, persistence and data-safe upgrades remain required. Current vector(384), `<=>` and HNSW consumers need explicit reviewed adaptation; do not blindly run vector-dependent migrations, discard data or replace PostgreSQL.
- The measured 479.729 MB MiniLM snapshot is a separate **text-embedding model**, used by retained PDF/YouTube reference search and ingestion. The user's condition for dropping its experiment is not met: keep smaller-runtime/quantization proof scoped to these consumers. No working smaller runtime or pgvector-free ranking implementation is claimed.
- Ordinary PostgreSQL array/JSONB vector storage plus bounded application-side cosine ranking is an evaluation candidate only. Prove owner/topic filtering, 384-value shape, ranking/topK/ties, persistence/migration, quality and realistic scale/resource budgets before adopting it. Semantic reference retrieval has not been deferred by this decision.
- Exclude FFmpeg only when its sole consumer is deferred speech-to-text; separately prove any retained non-STT need. Keep required document/URL/PDF/editor/media/font/browser resources. OS/CPU/installers, 250 MB installer/750 MB installed and memory/startup targets remain unchanged. Payments remain deferred under #41; classrooms remain LAN.

Source trace: `PdfFileEmbeddingStrategy.ts`, `YoutubeEmbeddingStrategy.ts`, `BaseEmbeddingStrategy.queryTopSimilarity()`, `inputSet.service.ts`, UI topic `components/reference/Reference.tsx`, and separate `features/whisper/api/whisper.service.ts`. Full record: local `planning/v1-scope-2026-11-11.md`. Earlier audits/measurements are historical evidence. Planning updates are not implemented feature removal or passing acceptance.
<!-- dozu-v1-scope-2026-11-11:end -->


<!-- dozu-roadmap-checkpoint-2026-11-12:start -->
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

