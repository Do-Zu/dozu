# Workspace and build graph — issue #6

Implemented and verified 2026-11-12 after #5's sanitized snapshot passed its prerequisite checks. This is JavaScript workspace/build evidence, not a complete desktop or full-stack release.

## Results

| Check | Result | Evidence |
| --- | --- | --- |
| Source npm lock migration | PASS; temporary combined npm workspace input imported into one root pnpm lock | `lock-import-combined.json`, `lock-refresh.json`, `npm-locks/` |
| Clean frozen installation | PASS; empty isolated store/dependency tree, scripts suppressed, strict peers enabled | `frozen-install.json` (117.125 s), `direct-import-install.json` |
| Final frozen offline install | PASS; final manifests/lock agree without registry resolution | `final-frozen-offline.json` |
| Original dependency versions | PASS; all original declared specs and installed direct versions match source locks | `change-ledger.json` |
| Workspace/React/tracing checks | PASS; two real JS apps, React/ReactDOM 18.3.1 shared by Next/Tiptap/PDF consumers, monorepo tracing root | `final-workspace-verify.json` |
| Actual task graph | PASS; no invented web→API package dependency; web package depends on its build | `final-graph.json`, `graph-summary.json` |
| API/web typecheck | PASS after explicit declarations of consumed dependencies and reviewed adapter fix | `api-typecheck-final.json`, `web-typecheck-final.json` |
| Real production builds | PASS for retained API and complete Next application; two additional guarded web builds pass | `build-network.json`, `package-links-fixed.json`, `repeated-build.json` |
| Repeated-build dependency integrity | PASS; all 6,387 original Next package files unchanged after both guarded builds | `dependency-integrity-first.json`, `dependency-integrity-repeat.json` |
| Real package and isolated relocation | PASS; 22 relative contained links; Node denies original-workspace reads; real en/vi titles, login/payment/icon/JS/CSS/font return 200; process stopped | `repeated-package.json`, `relocated-proof.json`, `relocated-server.log` |
| Full lint | FAIL, inherited: web enum-parser crash; API 100 errors/143 warnings with API source unchanged | `web-lint.json`, `api-lint.json` |
| Changed adapter lint | PASS | `web-adapter-lint.json` |
| API Jest | FAIL, existing eager DB/Redis paths against deliberately unavailable loopback; suite does not pass | `api-test.json` |
| Docker/native/Python/full stack | UNVERIFIED; Docker Linux engine unavailable; no native platform/installer/Python-model compliance claim | See limitations below |

`change-ledger.json` lists the exact ten imported paths intentionally modified/deleted, hashes/reasons, eleven new root/tooling files and every original direct dependency comparison. `record-ledger.py` asserts there are no unreported deviations from the #5 import manifest. `python planning/source-import/verify-import.py --baseline-only` still verifies the immutable 1,899-file import, 84 pages, 20 layouts and 20 archived migration hashes against intact originals.

The parent independently reviewed all imported paths and final root/tooling hashes in `parent-review.json`. Runtime dev/start tasks pass their configured environment only while uncached; test and migration tasks pass explicit fixture/database variable names. Build caching uses declared public build inputs and remote caching is disabled.

## Repeat-build defect and correction

The first successful Next build preserved Windows pnpm directory junctions with absolute source targets in `.next/standalone`. Next 14's installed `lib/recursive-delete.js` explicitly follows directory symlinks; the next build's cleanup consequently removed files from the installed Next dependency tree. The failed retry is retained in `package-final.json`. An offline frozen reinstall restored only workspace-owned dependencies (`frozen-repair.json`).

The web prebuild now rejects linked output ancestors, unlinks previous standalone links without traversing them, then removes only the fixed owned standalone output. Postbuild validates every traced target has an internal copied equivalent and rewrites it as a true relative directory/file symlink. Packaging preserves those relative links and rejects absolute, escaping or dangling links. Both `build` and `build:prod` run these guards; observed lifecycle logs show 22 detaches and 22 normalizations on the second uncached build. Independent read-only review and full dependency hash comparisons passed. No Next package source was patched and no hoist workaround was added.

Relocation uses Node's long-path-aware copy: an initial Python copy hit Windows path-length errors before launch. A separate initial IPv4-only server probe reproduced the previously documented Next14 localhost middleware normalization issue (`relocated-ipv4-failure.log`); the successful probe uses **localhost for both binding and origin**. Node filesystem permissions permit only the copied artifact and explicitly reject reads of the original workspace package. These are sampled server/asset checks, not browser interaction or complete feature parity.

## Commands and retained website

From the repository root, use pnpm 10.28.2 with Node 22.22.0 for this measured build:

```powershell
pnpm install --frozen-lockfile --ignore-scripts
pnpm verify:workspace
pnpm typecheck
pnpm build
pnpm package
```

The package is `apps/web/.package`; start it from that directory with `HOSTNAME=localhost`, an available `PORT`, and `node apps/web/server.js`. This is a website artifact built with explicit public build-time API/provider settings. The probe's API settings are deliberately unconfigured loopback; it cannot perform a real backend workflow. Use genuine deployment-specific public settings when building the retained website.

Root-context Docker recipes are retained for `docker build -f apps/web/Dockerfile .` and `docker build -f apps/api/Dockerfile .`. Docker was not executed because this host's Linux engine pipe is unavailable. The imported nested `.github/workflows/` are preserved historical deployment inputs, not automatically active monorepo CI; #10 owns new root CI/deployment wiring. Do not run their old per-repo npm commands against this pnpm snapshot. The original untouched source checkouts and recorded source commits retain the existing independent website/deployment rollback path; no deployment was performed here. API image configuration is supplied at runtime rather than copying dotenv into an image.

## Limits and independent pipelines

Installation intentionally disables lifecycle scripts, and pnpm's workspace policy separately allows esbuild while recording ignored native/browser scripts. No downloaded Puppeteer browser, native canvas/converter, portable Python, model, database or desktop runtime is certified by the JS build. Source `services/embedding/requirements.txt` remains unpinned and its mutable Python image is unchanged: #7/#8 must provide pinned toolchain, service lock/wheel/model and native portability evidence. No synthetic package.json was added to pretend Python participates in the JS graph. Runtime assets/model manifests remain independent delivery work under #8/#23/#32/#38.

Full lint/Jest failures remain visible and need their own source/optional-provider/local-adapter fixes; no suppression or fake passing test script was introduced. Turbo dry-run includes `<NONEXISTENT>` nodes for API `package` and web `test` because these scripts do not exist; it never reports them as executed checks. API production output is `apps/api/dist`, with dependencies handled by the retained website API recipe; no standalone API/runtime artifact is asserted.

No database migration, external-provider transaction, cloud deploy, source-history merge or public push was performed. No installer size, minimum-hardware budget, full UI interaction, data lifecycle, security review or additional OS/CPU compatibility criterion is passed by these results.

## Implementation decisions

The pnpm workspace will contain the actual JavaScript applications (`apps/web`, `apps/api`) and future real packages under `packages/*`; the Python embedding service remains an independent pipeline. There is no source-level dependency between the web/API packages, so the graph must not invent one merely to force build ordering.

Pin pnpm 10.28.2 (available on this host) and Turborepo 2.5.8 (public registry metadata checked). Import both source npm lockfiles with the workspace declared, then record resolution changes and validate a frozen install. Preserve original npm locks/hashes as migration/rollback evidence rather than silently mixing package managers. Source dependency versions remain unchanged unless a measured incompatibility requires a reviewed adjustment.

Use explicit build/typecheck/lint/test/package tasks. Development/start/watch tasks and database migrations remain uncached. Builds hash source/config plus public Next build variables, and never cache runtime migrations, data, credentials or deployment transactions. Keep package/model/native runtime resources outside this JavaScript graph until their own verified pipelines exist.

Next 14.2.35 uses `experimental.outputFileTracingRoot`; set it to the monorepo root and keep standalone output. Public/static assets require explicit packaging alongside standalone server output. Verify relocation and trace closure rather than assuming this config makes an artifact portable. Keep the website app, pages, locales, SSR and rewrites intact.

Source API scripts use Windows `set` syntax; portable wrappers are a build-tooling change, recorded separately from #5 byte parity. Website builds/deployment contexts must use the root workspace context. Original repositories remain unchanged for rollback; deployment actions are never run by generic build/package commands.

Lifecycle inventory from the original npm locks is in `source-lifecycle-inventory.json`. Begin installation with lifecycle scripts suppressed; inspect package install scripts before selectively enabling necessary native tooling. Puppeteer's browser/native conversion assets remain required proof under their delivery tasks; an ignored installer script is not evidence those assets are bundled. No existing dotenv or credential configuration is loaded during checks.

Validation must report actual lock import/frozen install, peer/React singleton, graph/dry-run, API typecheck/build, UI typecheck/lint/build and any relocatable standalone checks. Known UI YoutubePlayerAdapter build/type failure and other audited baseline errors remain visible; config-only success cannot close #6.

References: [pnpm import](https://pnpm.io/10.x/cli/import), [pnpm workspace settings](https://pnpm.io/10.x/settings), [Turbo configuration](https://turborepo.com/docs/reference/configuration), [Next 14 standalone output](https://nextjs.org/docs/14/app/api-reference/next-config-js/output). The installed Next 14.2.35 schema was inspected for the exact experimental option location.
