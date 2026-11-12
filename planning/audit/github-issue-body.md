<!-- dozu-tracking:start -->
## Work tracking
Use the live **status:**, **priority:** and **complexity:** labels above; **Assignees** identifies the owner. These labels are separate from the task/ticket type.

**Planning complexity:** L - Cross-repository behavior audit, integration inventory and independent build/contract baselines.
Complexity is a provisional scope/uncertainty estimate, not a delivery-time commitment. XL work must be split into executable subtasks before starting.
**Planning priority:** P0 - Architecture/foundation work that unblocks the implementation path.
<!-- dozu-tracking:end -->

## Outcome
Capture existing behavior and source provenance before migration, including external-provider dependencies and every UI workflow.

## Acceptance criteria
- [x] Record source commits, licenses, dirty trees, DB/extensions/migrations, workers, provider initialization, external endpoints and deployment paths without exposing credentials.
- [x] Run website lint/build, API typecheck/lint/Jest and embedding health/contract baselines in appropriate isolated environments; document pre-existing failures.
- [x] Inventory every route/layout/component/provider/hook, role, locale and interaction; static route discovery alone is not full parity evidence.
- [x] Trace Google/SMTP/payment/webhook/YouTube/LLM/R2/Cloudinary/Lambda/Redis consumers and identify what must stay local versus deliberate third-party API calls.
- [x] Record runtime downloads, compiled API URLs, cloud credential assumptions and the safe source/history import strategy.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

<!-- dozu-roadmap:BASELINE -->

Phase: 0 Requirements | Priority: P0

Parent roadmap: https://github.com/Do-Zu/dozu/issues/1

## Dependencies
None; this work can start independently.


## Completed audit evidence (2026-11-09)
Local evidence: planning/audit/README.md, feature-parity.md/json, ui-ledger.md, backend-endpoints.md/json, database.md/json, configuration.md/json, systems.md, findings.md and baselines/. Source commits and tracked trees remain unchanged. All 84 pages have workflow/source/follow-up entries; runtime desktop parity remains unverified.

Website lint/build and API lint/Jest have documented existing failures; API typecheck passes. Genuine cached CPU embedding HTTP tests expose a batch list-versus-Dict response bug. Ignored local migrations, missing bootstrap, eager providers, conversion/transcription runtimes, callback/secret limits and safe source/history import are recorded.

Audit coverage/reference verification passes. Audit completion does not implement the desktop, certify real third-party flows or resolve payment ownership #41 / classroom topology #43. Implementation issues remain unfinished.
