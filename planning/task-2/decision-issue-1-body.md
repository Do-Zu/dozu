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
- [ ] #29 - [Task] Bundle and initialize per-user PostgreSQL with pgvector
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
