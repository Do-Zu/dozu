<!-- dozu-tracking:start -->
## Work tracking
Use the live **status:**, **priority:** and **complexity:** labels above; **Assignees** identifies the owner. These labels are separate from the task/ticket type.

**Planning complexity:** M - Workspace/lockfile/task-graph setup with Next tracing and peer-dependency validation.
Complexity is a provisional scope/uncertainty estimate, not a delivery-time commitment. XL work must be split into executable subtasks before starting.
**Planning priority:** P0 - Architecture/foundation work that unblocks the implementation path.
<!-- dozu-tracking:end -->

## Outcome
Use pnpm/Turborepo for TypeScript builds and explicit Python tooling without rewriting the application architecture.

## Acceptance criteria
- [x] Create private workspace definitions, one pnpm lockfile and real internal dependencies only where consumed.
- [x] Verify React singleton/peers, Next output tracing across monorepo boundaries and portable build outputs.
- [x] Declare lint/typecheck/test/build/package dependencies and environment inputs; persistent dev tasks and migrations are uncached.
- [x] Keep desktop binaries/models/runtime manifests and Python lockfiles in appropriate independent build pipelines.
- [x] Verify clean install/build and document current npm lockfile migration.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

<!-- dozu-roadmap:WORKSPACE -->

Phase: 1 Foundation | Priority: P0

Parent roadmap: https://github.com/Do-Zu/dozu/issues/1

## Dependencies
- #5 - [Task] Import current frontend/backend/embedding sources with provenance


## Workspace/build acceptance evidence — 2026-11-12

Implemented after #5's verified sanitized import. The existing web/API applications now use a private pnpm 10.28.2 / Turborepo 2.5.8 workspace with one root lockfile. Python/model/native assets remain independent delivery pipelines under #7/#8/#23/#32/#38; their runtime reproducibility is not certified by this JavaScript result.

- Clean frozen install passed with strict peers and lifecycle scripts suppressed; final frozen offline install also passed. Every original direct dependency declaration/version is preserved. Previously undeclared direct imports now declare exact versions from the original npm locks; cross-env is pinned for portable scripts. Original npm locks are archived with the migration record.
- React/ReactDOM 18.3.1 singleton checks passed across Next, Tiptap and PDF consumers. The real task graph contains no invented internal application dependencies. Build/package inputs and dependencies are declared; dev/start/watch, test and migration operations are uncached, with explicit environment handling.
- Production API and complete retained Next builds passed. A reviewed synchronous YouTube adapter guard resolves the pre-existing type blocker without changing the controller interface or casting a Promise to a number. Its targeted lint and independent source/type/runtime review passed.
- A measured Next14/Windows-pnpm repeat-build defect is fixed with bounded standalone-link detachment and relative-link normalization. Two actual guarded web builds/package checks passed; all 6,387 installed Next dependency files remained byte-identical. The second build detached and normalized 22 links.
- The copied standalone website passed nine genuine HTTP page/asset checks, including English/Vietnamese welcome titles, login/payment pages, icon, JS/CSS and a bundled font. All 22 links are relative and contained. Node filesystem permissions denied access to the original workspace while the copy served requests; the owned server process was stopped. This checks sampled website artifact portability, not full feature/runtime parity.

Full lint and API Jest still fail on recorded existing source/parser/eager DB/Redis paths; they are not reported as passing. Docker recipes use the root workspace context, but Docker image execution remains unverified because the host engine is unavailable. Original website checkouts/deployment inputs remain available for rollback, while new root CI/deployment wiring is #10. No migration, provider transaction, deployment, public push or installer certification was performed. The approved v1 scope and resource/platform contract are unchanged.

Reviewable local evidence: `planning/workspace/README.md`, `change-ledger.json`, `parent-review.json`, frozen-install/build/graph logs, dependency-integrity reports and `relocated-proof.json`. The immutable #5 baseline still verifies against unchanged original histories. No sensitive values or credential findings are included in this update.
