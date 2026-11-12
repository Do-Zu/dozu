# Sanitized source import — #5 acceptance report

Local import completed and verified on 2026-11-12. Sources now live in `apps/web`, `apps/api` and `services/embedding`. Original checkouts and histories remain unchanged. Runtime feature parity, public redistribution clearance and #6 workspace changes are separate.

| Original | Pinned commit | Destination | Files | Excluded paths |
| --- | --- | --- | --- | --- |
| dozu-ui-service | 5e1ceb263a29e2fde2359c36f43d0118a8d622f0 | apps/web | 1,226 | .env.local, .npmrc |
| dozu-api-service | 173f3f1cbcc81b89ad3eea81723698f7bb7eb876 | apps/api | 637 | .env.local, .env.production, .npmrc |
| dozu-embedding-service | 188d0d229a38ee51f48f1e5d5f06cf69f16870c6 | services/embedding | 36 | None |

## Evidence and reproduction

- `preflight.py` / `preflight.json`: HEAD blob inventory, exclusion ledger and bounded findings by path/rule only.
- `import-snapshot.py` / `import-manifest.json`: source commit/blob/mode/SHA256/byte mapping, imported hashes, sanitation ledger, author/committer/parent/timestamp metadata. Commit messages, historical blobs and unsanitized ancestry were not imported.
- `verify-import.py` / `verification.json`: baseline verification of 1,899 files, complete tracked-path coverage, source modes, exact byte/binary parity except two explicit sanitation changes, 84 pages and 20 layouts, all tracked AGENTS/skills/workflows, original clean trees/HEADs and 20 ignored SQL hashes.
- `sanitation-review.json`: classified bounded scanning results and limitations, without credential values or source diffs containing them.
- `legacy-migrations/`: byte-identical SQL history outside active migration paths. Original journals/snapshots remain untouched in the original checkout. #29 owns reviewed migration/seed/adaptation work; these files are not automatically applied.

Commands from the root, before downstream #6 edits:

```powershell
python -X utf8 planning/source-import/preflight.py
python -X utf8 planning/source-import/import-snapshot.py
python -X utf8 planning/source-import/verify-import.py
```

The importer refuses to overwrite changed targets. The verifier compares the exact baseline import; after #6 changes package/build files, use that task's explicit change ledger. Captured #5 verification records the initial snapshot, not a claim that downstream files never change.

For later verification without confusing intentional #6 changes with import corruption, run `python -X utf8 planning/source-import/verify-import.py --baseline-only`. It reconstructs each sanitized baseline from the pinned original Git blobs, verifies all immutable manifest hashes/coverage and writes `verification-baseline.json`, without overwriting current application files. Compare the live tree to that manifest using #6's explicit workspace change ledger; this reconstruction does not certify downstream changes.

The initial preflight's overbroad `uploads` segment exclusion was corrected before import: all nine tracked API upload source files are present. Only five dotenv/registry-auth files are excluded. Their blobs and root credential files were never read. Ignored user data/databases/caches/dependencies/virtual environments and nested Git metadata were never copied.

## Explicit sanitation changes

1. `apps/web/src/app/[locale]/auth/testBackEnd/page.tsx`: remove the embedded bearer token and automatic session overwrite. Retain the page, profile button and handler; use the existing API wrapper/current legitimate session. No fake authentication or success response. Existing user-facing text is unchanged.
2. `apps/api/containers/database/postgres/README.md`: replace the documented development password/credential URL with untracked local configuration instructions. Runtime code is unchanged.

These changes are separated from structural relocation. All other imported files are byte-identical to pinned source blobs. No disposable #4 behavior patch, schema adaptation or v1 capability removal was adopted.

## History, attribution and licenses

Strategy: sanitized snapshot with source commit/blob mapping. Full history stays in the unchanged originals for attribution and rollback. Existing copyright/license notices are retained. Author/committer metadata and parent hashes for each imported HEAD's ancestry are in `import-manifest.json`; source identities are also in `../audit/source-provenance.json`.

API's Apache-2.0 LICENSE and ISC package metadata are preserved as found. UI/embedding have no tracked license files. No new license grant or ownership assertion is invented. Local import is user-authorized; public redistribution still requires resolving existing metadata/permission gaps and dependency/native/model notices. This task grants no public release clearance.

Git mode `100755` is recorded for `apps/web/.husky/pre-commit`; all other source entries are `100644`. Windows permissions do not encode Git's executable bit. After staging the file, preserve it explicitly:

```powershell
git update-index --chmod=+x -- apps/web/.husky/pre-commit
```

No index mutation/history rewrite was performed by #5.

## Website and deployment rollback

All website source, assets, lockfiles, Docker/config inputs and nested workflow definitions are retained. Source-relative application boundaries are unchanged. Nested `.github/workflows` files preserve the original deployment definitions; monorepo activation/root contexts and portable scripts belong to #6/#10. Retention is not a passing website build/deployment claim: known original build/lint failures remain recorded by #3.

No deployment or remote configuration changed. Rollback uses the original UI/API/embedding repositories and pinned commits above, with separately managed untracked local/provider configuration. Existing deployed artifacts remain unchanged. Do not restore excluded env files through history import, copy production data into seeds or deploy an unverified monorepo artifact. Future deployment must retain its previous artifact/configuration under #10/#26.

## Acceptance boundary

All five #5 structural criteria are satisfied locally: provenance/attribution/guidance; exclusions; complete inventory and bounded scan; all route/component/server-feature source retained; website/deployment inputs and rollback documented. Existing license ambiguity explicitly gates public distribution. Runtime parity, installer/platform acceptance, retrieval quality and resource budgets do not pass by source import.
