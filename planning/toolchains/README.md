# Portable toolchains — issue #7

**Current disposition — 2026-11-13:** #7 is completed for the explicitly revised, committed JavaScript tooling foundation. The user authorized transferring later desktop acceptance to independent issues so migration can proceed. See [closure/read-back and next #38 step](closure/README.md). Original broad native/runtime/installer criteria remain unpassed under their listed owners; the open-status wording below records the historical implementation checkpoint and is superseded by that scope split.

2026-11-13, Asia/Bangkok. Started from clean `dev` at `5712218`, after reading imported application guidance, #6 workspace evidence, scope/support contracts and architecture/roadmap handoffs. **#7 remains In Progress; none of its five full acceptance criteria is checked.** This implements the independently executable JavaScript portability portion. No framework upgrade, deployment, database migration or installer certification is claimed.

## Implemented behavior

- Root and API Node version files now agree on 22.22.0. The API's previous `.nvmrc` was UTF-16 Node 20.18.3; it is now UTF-8/LF for Unix version managers. Root engines pin the exact build baseline. `tooling/toolchain-policy.json` records Node/pnpm/Turbo/TypeScript pins and explicitly leaves unselected bundled runtimes null. Root dev/build/package preflight checks the executing Node, pnpm user agent and installed build tools.
- Existing `cross-env`/`rimraf` commands are retained. Migration scripts now invoke the installed locked Drizzle CLI directly, without `npx` download fallback. Drizzle schema/output/env paths anchor to its config directory, including relocation; it no longer falls back to an unrelated cwd dotenv. Development Drizzle still selects `.env`, while API runtime selects `.env.development`: existing names are preserved, not silently unified. Prefer explicit inherited settings.
- Compiled and development API aliases both anchor to the directory containing `register`, independently of cwd or a missing `NODE_ENV`. A real production probe found that cleaning `dist` while retaining TypeScript incremental state could produce an incomplete successful build. Production builds now use `tsc --incremental false`, emitting the entire API after cleaning. Generated build/coverage output is excluded from source lint.
- `DOZU_DATA_DIR` must be absolute when supplied. Logs, upload middleware/service/config, generation uploads and conversion input/output resolve under it. `LOG_DIR`, `UPLOAD_DIR`, `UPLOAD_CONVERT_FILE_DIR`, and `OUTPUT_CONVERT_FILE_DIR` may override defaults; relative overrides resolve from the data directory, absolute overrides are preserved. Existing website deployments retain cwd defaults when no data directory is supplied. Avatar deletion uses the configured uploads root with a lexical escape guard. No historical user data is moved or deleted.
- Environment initialization no longer imports Winston while Winston imports environment config. Startup environment diagnostics use process streams, so dotenv loads before file transport paths are selected. Desktop data-root settings must be inherited before API startup; no packaged dotenv is required or supplied here.
- The Lambda ZIP helper passes paths as arguments/environment rather than interpolating them into shell code. Windows uses hidden, noninteractive PowerShell with literal paths; macOS/Linux use `zip` with an explicit cwd. These are developer-only packaging utilities. AWS deployment scripts were not invoked or modernized.
- Root development, individual app, production-start and website packaging commands are documented in the root README. `start:web` launches the existing standalone website without shell-specific environment assignments and defaults to `localhost`. The root package command still has no API `package` task or desktop installer task; no fake task was added.

## Evidence

Reproduce with the pinned build tools. `run-check.py` supplies an OS environment allowlist, empty registry config and explicit non-secret public loopback build settings. It never loads real dotenv/provider credentials. Runtime checks use disposable paths containing spaces, deny writes outside their data directory, and do not apply migrations.

```text
python planning/toolchains/run-check.py frozen-offline install --frozen-lockfile --ignore-scripts --offline
python planning/toolchains/run-check.py api-build --filter api-services build
python planning/toolchains/run-check.py api-lint --filter api-services lint
node planning/toolchains/verify-runtime.cjs
python planning/toolchains/verify-lambda.py
python planning/toolchains/inventory.py
python planning/toolchains/run-check.py root-package package
```

| Check | Result / evidence |
| --- | --- |
| Frozen offline install | PASS, existing installed workspace; lifecycle suppressed; `frozen-offline.json`. This is not a new clean-install proof. Lockfile/dependency versions unchanged. |
| API production compile | PASS; complete emission, `api-build.json`. The startup probe initially exposed missing output with stale incremental metadata; that is why compile behavior changed. |
| Full API source lint | FAIL inherited, 100 errors/143 warnings; `api-lint.json`. `lint-comparison.json` compares messages/rules ignoring line shifts: zero added or removed diagnostics. |
| Compiled alias resolution | PASS: 1,239 literal alias references in built JS resolve from an unrelated cwd; `all-compiled-aliases.log`. Resolution does not execute every consumer. |
| Read-only component paths | PASS: real upload/conversion middleware creates directories, fixture writes/reads work and Winston flushes an error record under the data root; an attempted cwd write is denied. Defaults, overrides and relative-root rejection pass; `runtime-checks.json`. |
| Migration config relocation | PASS for an exact config copy evaluated at a relocated filename using locked dependencies; schema/output resolve beside it. No dotenv, migration history or database is read/applied; `migration-config-paths.log`. |
| Standalone Node native smoke | PASS only for installed Windows x64 Next SWC loading and target-triple call: Node 22.22.0, module ABI 127, Node-API 10, binary hash in `runtime-checks.json`. Canvas fails to load (`MODULE_NOT_FOUND`); ignored lifecycle is not native delivery. |
| Full API production startup | UNPASSED. Scrubbed real entrypoint reaches inherited database/logging/Redis/mail initialization blockers. `production-startup.log` and `runtime-checks.json` retain the actual exit/timeout. No backend-ready or real DB integration claim. |
| Lambda archive | PASS Windows developer fixture with spaces, brackets, apostrophe and `$`; exact ZIP entries/content verified, no deployment; `lambda-package.json`. POSIX branch needs native execution. |
| Root packaging / website launch | PASS: `root-package.json` records all 3 tasks executed successfully. `website-proof.json` records the new root wrapper serving nine real page/asset/font checks with all filesystem writes denied and original workspace reads denied; owned server stopped. First sandbox build failed with EPERM, and sandbox loopback access failed with WinError 10013; external retries passed with the same scrubbed settings and Node filesystem restrictions. No OS acceptance is inferred. |

`inventory.json` records current imported scripts and source assumption locations, excluding untouched original checkouts and machine-local configuration. It flags historical `db:migrate:docker` (`push:pg` and a missing compiled schema path), Docker/Compose and AWS deployment tools, speech-only executable paths, and unpinned Python/model inputs. The obsolete Docker migration command is **not validated or recommended** and is never run by generic build/package commands. Archived migrations, including vector-dependent steps, remain unchanged and need the reviewed PostgreSQL-only migration path under #29/#30; do not run them blindly.

## Version and release policy

The exact measured JS build baseline is Node **22.22.0**, pnpm **10.28.2**, Turbo **2.5.8**, TypeScript **5.8.3**, Next **14.2.35** and React/ReactDOM **18.3.1**. Registry lock integrity remains authoritative for ranged direct/transitive package declarations. These pins do not mean current security approval.

Official vendor checks on 2026-11-13:

- [Node release schedule](https://github.com/nodejs/Release) lists 22 as Maintenance LTS through 2027-04-30. [22.22.0 release notes](https://nodejs.org/en/blog/release/v22.22.0) establish this exact security-release baseline, not that it is the latest patch. [Version-specific build requirements](https://github.com/nodejs/node/blob/v22.22.0/BUILDING.md) list Windows 10+, macOS 11+ x64/ARM64, and Linux x64 kernel 4.18+/glibc 2.28+; vendor EOL caveats still apply. This is an upstream compatibility input, not native app evidence. Recheck current security patches before shipping.
- [Next support policy](https://nextjs.org/support-policy) lists 14 as unsupported, 16 Active LTS and 15 Maintenance LTS (extended through 2027-01-31). A supported, security-reviewed Next/React/ESLint migration is a separate release prerequisite. Select an exact current patched target after advisory review; validate all routes/locales, server semantics, build/rebuild, standalone links, browser/desktop/provider behavior and native modules independently. No framework source/version is changed by this portability work, and no upgrade is claimed passed.
- [Electron native module guidance](https://www.electronjs.org/docs/latest/tutorial/using-native-node-modules) requires the actual Electron ABI/rebuild or compatible Node-API proof, not host Node ABI inference. [utilityProcess](https://www.electronjs.org/docs/latest/api/utility-process) uses Electron's Node child runtime; [support policy](https://www.electronjs.org/docs/latest/tutorial/electron-timelines) covers only the latest three stable majors. Historical #4 Electron 45.2.3 Windows acquisition is not a selected/pinned production runtime manifest. No Electron binary is added or loaded here.
- [pnpm 10 installation requirements](https://pnpm.io/10.x/installation) support this Node baseline. Lifecycle scripts remain suppressed; selectively building approved native/browser dependencies needs its own reviewed delivery evidence.
- [Puppeteer current requirements](https://pptr.dev/guides/system-requirements) are for current 25.x, not proof about installed 24.32.0. The imported exact package/lock is preserved. Pin and hash the selected browser and native libraries per platform, then exercise genuine URL-to-PDF before release; no browser download occurred here.
- [PostgreSQL version policy](https://www.postgresql.org/support/versioning/) requires supported/current minor maintenance and reviewed upgrade steps. No production DB binary was selected by this task. Python's mutable `3.13-slim` image, unpinned requirements and model revisions/cache writes remain open under #8/#23/#32/#38. Do not freeze an arbitrary workstation `pip freeze` as a portable lock.

Change Node/Next/Electron/Python/database versions in separate reviewed changes with exact artifacts/hashes, license/security review and independent regression evidence. A development tool pin must never silently select the installer runtime, auto-download missing production resources, or waive the approved support/resource budgets.

## Dependency and platform limits

Live #4 is contradictory: API state is closed/completed and main acceptance/P1-P3 boxes are checked, while its user-directed closure comment says NOT PLANNED and P4-P7/native child gates remain unchecked. #1's reconciliation says cancellation is not completion. No fresh evidence reconciles those states. This task preserves #4, its checklist, assignment and dependencies. Proposal: retain #4 as historical canceled work and explicitly map its unresolved gates to the existing #1 delivery ledger before changing dependency completion logic. Do not automatically mark dependents ready/done from closed state.

The user explicitly authorized #7's independent work despite that gate. #7's existing #4/#6 dependency fields remain intact; issue and Project Status move only to In Progress. Full runtime/native acceptance remains pending under the existing linked delivery tasks. No owner is invented.

All required native targets remain **UNPASSED**: Windows 10 22H2 x64, Windows 11 x64, macOS 13+ x64, macOS 13+ ARM64, Ubuntu 22.04 x64 and Debian 12 x64. This Windows developer host supplies component evidence only, not clean-machine/minimum-spec/installer validation. No macOS/Linux native host is attached. Node permission checks are not native OS ACL or packaged-install acceptance; the path settings still need real desktop supervision and integration. Full Python/model/browser/converter resources, DB migrations/bootstrap, Electron ABI, signing, budgets, lifecycle and end-user-without-tools proof remain open.

Approved scope is unchanged: retain website/all UI, local-first optional internet, PostgreSQL retained/pgvector deferred, required PDF/YouTube text embeddings retained, local speech-to-text/STT-only assets excluded, payments deferred under #41, classroom LAN. No original nested checkout, real user data or migration history was changed. Work is local and reviewable; no source push or deployment is implied by a GitHub status/comment update.
