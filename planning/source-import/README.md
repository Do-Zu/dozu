# Source import preflight — #5

**Completed and reviewed — 2026-11-12:** #5 is closed completed. See [acceptance report](report.md) and immutable import verification. #6 workspace/build work is also completed separately in ../workspace/README.md. The preflight narrative below is historical.

**Current state — 2026-11-12:** local sanitized import is complete and verified. Read [the acceptance report](report.md) and `verification.json` for the current 1,899-file baseline. The initial preflight narrative below is historical: its overbroad uploads exclusion was corrected, all nine API upload source files are preserved, and the two findings were sanitized without removing their pages. #6 may now proceed; public redistribution clearance remains separate.

Started 2026-11-12 under roadmap #1. #3 is closed as completed, satisfying the only declared prerequisite. #6 remains waiting. This step changes no application behavior and imports no source/history yet.

Run `python planning/source-import/preflight.py`. [preflight.json](preflight.json) maps each original HEAD to its intended monorepo path, recording Git blob IDs, modes, SHA256 and byte size for eligible files, license paths and exclusions. All three tracked trees were clean before and after the run, matching the completed audit's commits.

| Original | Destination | Eligible files | Exclusions | Findings requiring review |
| --- | --- | --- | --- | --- |
| dozu-ui-service | apps/web | 1,226 | 2 | JWT-shaped literal in `src/app/[locale]/auth/testBackEnd/page.tsx` |
| dozu-api-service | apps/api | 628 | 12 | Credential-shaped URL in `containers/database/postgres/README.md` |
| dozu-embedding-service | services/embedding | 36 | 0 | None from bounded rules |

Findings contain no matched values. They may include examples or expired credentials; validity was not probed. Do not copy the flagged files unchanged or remove their pages to bypass the review. Review/sanitize with explicit per-file patches and preserve the full page inventory before source adoption. The current scan is a HEAD-only heuristic, not a complete secret audit or evidence that historical refs/objects are safe.

Dotenv and registry-auth files were excluded by path before blob access; neither their contents nor root credential files were read. Ignored files, live databases, uploads, caches, virtual environments, dependencies and nested Git metadata were never traversed. Ignored SQL history remains in the original API checkout; the 20 migration hashes and review evidence remain in `planning/audit/database-inventory.json` and historical architecture proof. No migration was run or rewritten here.

Use a sanitized **snapshot** as the initial local import strategy. Keep original repositories intact as the history/rollback source, map every imported file to its original commit/blob, preserve existing author/license notices and applicable AGENTS guidance, and retain commit/author provenance separately before completing #5. Do not merge unsanitized ancestry. A rewritten-history strategy would need a separate all-ref/object review.

API has Apache-2.0 LICENSE versus ISC package metadata; UI/embedding have no tracked license files. Preserve notices as found; do not invent license grants. Redistribution clearance remains unresolved before public import/distribution. Local preflight can proceed within the user's authorized repositories.

Next #5 work: classify findings without exposing values, prepare minimal sanitation patches, review attribution/license discrepancy and preserved author metadata, then stage and verify the complete sanitized tree. Retain website Docker/workflow/config inputs and original deployment rollback; record necessary root-path changes separately. Do not adopt disposable #4 behavior patches as part of a source-only import. No clean website build, runtime parity or release permission is claimed by this inventory. #5 acceptance remains unchecked.
