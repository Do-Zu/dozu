<!-- dozu-tracking:start -->
## Work tracking
Use the live **status:**, **priority:** and **complexity:** labels above; **Assignees** identifies the owner. These labels are separate from the task/ticket type.

**Planning complexity:** M - Mostly structural source/history movement with provenance and secret checks.
Complexity is a provisional scope/uncertainty estimate, not a delivery-time commitment. XL work must be split into executable subtasks before starting.
**Planning priority:** P0 - Architecture/foundation work that unblocks the implementation path.
<!-- dozu-tracking:end -->

## Outcome
Move reviewed sources into apps/web, apps/api and services/embedding while retaining all UI and backend behavior.

## Acceptance criteria
- [x] Preserve agreed history/attribution/licenses, source-ref mapping and applicable AGENTS guidance; keep original checkouts intact.
- [x] Exclude credentials, local DBs/uploads/caches, nested .git, virtualenvs and node_modules from the public source import.
- [x] Verify source inventory/secret scan and document required path-only changes separately from behavior changes.
- [x] Keep Next route/component boundaries and server features; do not replace the UI with a selected subset.
- [x] Retain website build/deployment capability and record source/deployment rollback.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

<!-- dozu-roadmap:IMPORT -->

Phase: 1 Foundation | Priority: P0

Parent roadmap: https://github.com/Do-Zu/dozu/issues/1

## Dependencies
- #3 - [Task] Audit complete UI/backend and local-first integration baselines


## Source import acceptance evidence — 2026-11-12

Local sanitized snapshot imported into `apps/web`, `apps/api` and `services/embedding`: 1,899 files, with all 84 pages and 20 layouts retained. Complete tracked-path coverage, assets/binary hashes, source guidance/workflows and source modes were checked. Original source commits and tracked trees remain unchanged; no nested Git ancestry or credentials/local data/dependencies were imported.

Preserved source commit/blob/SHA256 mapping, existing license notices and author/committer history metadata. API license metadata inconsistency and missing UI/embedding licenses remain explicitly unresolved for future public redistribution; no grants were invented. This is a user-authorized local structural import, not public distribution approval.

Two minimal sanitation changes were documented separately from relocation: the retained backend-test page now uses the legitimate current session instead of a bundled token, and PostgreSQL documentation uses local configuration references. Bounded imported-byte scanning has no remaining known-pattern findings; it is not a complete historical secret audit. Twenty ignored original SQL migrations match audit hashes and are preserved as historical evidence outside active bootstrap paths; none was applied or rewritten.

Local evidence: `planning/source-import/report.md`, `import-manifest.json`, `verification.json`, `sanitation-review.json`, and reproducible inventory/import/verification scripts. Website build/deployment inputs and original-checkout rollback are preserved. Existing audit build/lint failures are not claimed fixed. The Windows Git executable-bit staging instruction is recorded for the retained pre-commit file.

#5 structural acceptance is ready for parent review. #6 may proceed with its separately recorded workspace/build changes. No runtime parity, feature/platform/resource budget or installer acceptance is claimed.

