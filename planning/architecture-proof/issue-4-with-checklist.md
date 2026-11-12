<!-- dozu-tracking:start -->
## Work tracking
Use the live **status:**, **priority:** and **complexity:** labels above; **Assignees** identifies the owner. These labels are separate from the task/ticket type.

**Planning complexity:** XL - Multi-OS packaging experiment with Node, PostgreSQL/pgvector and Python compatibility unknowns; split the proof into platform work.
Complexity is a provisional scope/uncertainty estimate, not a delivery-time commitment. XL work must be split into executable subtasks before starting.
**Planning priority:** P0 - Architecture/foundation work that unblocks the implementation path.
<!-- dozu-tracking:end -->

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

<!-- dozu-roadmap:DECISION-STACK -->

Phase: 0 Requirements | Priority: P0

Parent roadmap: https://github.com/Do-Zu/dozu/issues/1

## Dependencies
- #3 - [Task] Audit complete UI/backend and local-first integration baselines
- #2 - [Ticket] Record local-first requirements and full feature-preservation matrix


<!-- dozu-proof-checklist:start -->
## Executable architecture proof (started 2026-11-10)

Shared component experiments execute in order; native platforms have explicit subissues. Evidence lives in local `planning/architecture-proof/` with sanitized logs/manifests/scripts. These unchecked gates do not change the acceptance criteria above.

- [ ] P1 — Measure pinned runtime/model/browser/font/conversion/transcription assets, hashes, complete footprint and installer feasibility; count every asset, report missing assets, no first-run downloads.
- [ ] P2 — Sanitized production build and Electron utilityProcess or pinned bundled Node startup of retained Next standalone + Express; dynamic en/vi routes, streams/sockets and process cleanup; fix only measured necessary build/runtime blockers.
- [ ] P3 — Disposable native PostgreSQL/pgvector: 20 migration hashes, extension, seeds, vector/cosine/HNSW/SQL contracts, local writes and restart persistence.
- [ ] P4 — Pinned offline CPU Python/model with fresh user paths, API consumer contract including known batch 500, startup/steady/processing memory and model/cache manifest.
- [ ] P5 — Native DOC/DOCX/TXT→PDF, URL→PDF/browser assets, whisper.cpp tiny + FFmpeg, fonts/licenses/libraries and real fixtures; no capability removed.
- [ ] P6 — Native packaged matrix on every approved OS/CPU baseline, clean installation without developer dependencies (subissues below). Cross-builds are not evidence.
- [ ] P7 — Complete-process cold/warm UI/backend timing, normal/peak RAM+CPU/size; loopback/auth/secret review, restart/upgrade/backup/uninstall keep/delete evidence and conditional ADR/options. Approved budgets stay unchanged.

### Native execution subissues
- [ ] #45 — windows: https://github.com/Do-Zu/dozu/issues/45
- [ ] #46 — macos: https://github.com/Do-Zu/dozu/issues/46
- [ ] #47 — linux: https://github.com/Do-Zu/dozu/issues/47

Current workspace is Windows only; macOS/Linux native acceptance remains unpassed. Shared experiments can progress here. No assignee is invented. P1–P5 are component checks; P6/P7 must still validate full packaged behavior on supported hardware.
<!-- dozu-proof-checklist:end -->
