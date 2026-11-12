# Complete application baseline audit — issue #3

Date: 2026-11-09 (Asia/Bangkok). Scope: existing Next.js UI, Express/TypeScript business backend and Python/FastAPI embedding service in `D:\product\dozu`. **The audit is complete; application migration and desktop feature parity are not implemented or verified.**

The source supports retaining Next standalone, Express and PostgreSQL/pgvector with CPU FastAPI under an Electron supervisor. The recommendation remains conditional on #4. Actual source also requires document/URL converters (Gotenberg/LibreOffice and Puppeteer/browser resources) and speech transcription (whisper.cpp/tiny model/FFmpeg). These dependencies must be included in proof/installer scope.

## Read the evidence

| Document | Contents |
| --- | --- |
| [Feature-parity matrix](feature-parity.md) / [JSON](feature-parity.json) | One row per existing page with reviewed workflow, role intent/gates, local implications, source and follow-up issue links. Every row's runtime parity remains UNVERIFIED. |
| [UI ledger](ui-ledger.md) / [graph JSON](ui-workflows.json) | All pages/layouts/non-entry TSX, hooks/providers/contexts and navigation/config sites; inherited layouts, imports, handlers and reachability. Join interactionSources to source-inventory calls to inspect full interactions without duplicated data. |
| [Backend endpoint ledger](backend-endpoints.md) / [JSON](backend-endpoints.json) | Complete mounted methods/paths, controller and middleware source; aliases and unreachable route declarations. |
| [Systems and integrations](systems.md) | Business capabilities, state/jobs/cache/realtime/files, real providers, callback/secret/merchant/reachability limits, runtime/deployment assumptions and secure options. |
| [Database ledger](database.md) / [JSON](database-inventory.json) | All model/barrel/table/enum/column/import dependencies, ignored local migrations, hashes and bootstrap gaps. |
| [Configuration](configuration.md) / [JSON](configuration-inventory.json) | Runtime plus build/deployment variable names and consumer lines; public hostname candidates, no credential values. |
| [Findings](findings.md) | F01–F19, uncertainties and follow-up mapped to the existing backlog. |
| [Source provenance](source-provenance.json) / [source inventory](source-inventory.json) | Sanitized origins, exact commits, clean/dirty status, tracked dotenv/license path metadata, hashes and declarations/imports/calls for source/config files. |
| [Runtime dependencies](runtime-dependencies.json) | Direct installed-versus-lock versions, lock hashes, metadata-only env-path history counts. |
| [Baseline runs](baselines/results.json) / [individual Jest](baselines/jest-suites.json) / [real embedding HTTP](baselines/embedding-contract.json) | Commands, durations, exit codes and logs; actual expected and observed HTTP results. |

## Provenance and coverage

| Source | Commit | Branch | Initial/final tracked tree |
| --- | --- | --- | --- |
| UI | `5e1ceb263a29e2fde2359c36f43d0118a8d622f0` | feature/markable-content | clean / unchanged |
| API | `173f3f1cbcc81b89ad3eea81723698f7bb7eb876` | feature/markable-content | clean / unchanged |
| Embedding | `188d0d229a38ee51f48f1e5d5f06cf69f16870c6` | migrate/structure | clean / unchanged |

Verified against the old inventory: **84 pages, 20 layouts and 164 shared src/components TSX files**. The expanded ledger includes **584 non-entry TSX files**, **132 hook/provider/context source files**, and **550 navigation/config sites** (dynamic/duplicate sites included). The shared 164 are part of the 584, not additional to it. Every page has reviewed workflow notes; placeholder routes and missing navigation destinations are explicit.

Backend: **330 unique `/api` method/path pairs** across 52 reachable registration declarations, plus the separate `/health`; 53 declarations exist and the top-level classFeed module is unreachable from API imports. FastAPI has eight explicit endpoints plus default docs/OpenAPI routes. Database: **72 table and 27 enum declarations in 74 model/barrel files**, with **20 locally present but Git-ignored migrations**. These totals measure coverage only.

The scan includes all tracked source/config files relevant to the services and ignored local migration artifacts. A filesystem-versus-Git comparison found no extra untracked `.ts/.tsx/.js/.py/.json` source files under the three src directories. Build output, installed dependencies, caches, uploads/data and dotenv/token contents are excluded. Source hashes and origin/commit identities anchor the evidence. The parent checkout currently sees source/planning folders as untracked nested trees; no source-history import or commit was performed.

## Independent baseline results

| Check | Observed result | Evidence / limit |
| --- | --- | --- |
| Website lint | **FAIL**, exit 1 | 1,548 Error and 3,683 Warning diagnostics in [ui-lint.log](baselines/ui-lint.log); repeated diagnostics across files are not unique defects. |
| Website production build | **FAIL**, exit 1 | JS compiles, CSS nesting warning, then YouTube adapter Promise<number>/number type error. [ui-build.log](baselines/ui-build.log). Lint is skipped by Next config. |
| API typecheck | **PASS**, exit 0 | `tsc --noEmit --incremental false`, [empty success log](baselines/api-typecheck.log). |
| API lint | **FAIL**, exit 1 | 243 diagnostics: 100 errors, 143 warnings. [api-lint.log](baselines/api-lint.log). |
| API full Jest | **FAIL**, exit 1 | Eager Redis client emits unhandled ECONNREFUSED against deliberately unavailable loopback endpoint. [api-jest.log](baselines/api-jest.log). |
| Individual Jest suites | **3 pass / 4 fail** | Class comments 16 pass, package controller 9 pass, R2 mocked upload 10 pass. Subscription middleware 1 pass/28 fail, schedule service 1 fail/4 skipped, schedule integration and Anki have no tests. Totals: 36 pass/29 fail/4 skip; two empty suites. [Per-suite logs](baselines/jest-suites.json). These are existing unit/mocked tests, not live integration success. |
| Embedding empty-cache offline startup | **FAIL**, exit 1 | Neither primary nor fallback model is in isolated HF cache; startup tries Hub identity resolution and fails offline. [embedding-startup.log](baselines/embedding-startup.log). |
| Genuine cached CPU HTTP contracts | **9 expected outcomes / 1 failure**, probe exit 1 | Actual loopback Uvicorn, real cached model revision 86741b4e…, Python 3.13.7. Health/single/compare/segment-processing/PDF work, invalid payloads 422, blank PDF 400. Batch `/segments/embedding` returns 500 from existing list-vs-Dict response bug. [Results](baselines/embedding-contract.json), [log](baselines/embedding-contract.log). |

No application defect was fixed as part of this audit. Failures above are recorded baselines, not failed audit acceptance. The audit criterion requires running and documenting them; it does not require migrating or repairing the application.

## Isolation and reproducibility

Commands ran in disposable `planning/audit/.runs/` copies of tracked source, excluding dotenv/token files and data/build output. Junctions reused installed node_modules and checks used the existing embedding venv; generated outputs targeted the disposable copies. Registry configuration is excluded from reruns and removed from those copies; no npm/pip install/auth, deploy, DB migration or live provider action was run. All direct UI/API installed dependencies match package-lock versions (155 UI, 76 API); transitive clean-install reproducibility remains unproven. Node 22.22.0/npm 10.9.4 and host Python 3.12.7 orchestrated runs; embedding venv Python is 3.13.7.

Children receive a small environment allowlist with no inherited provider credentials. API test DB/Redis targets deliberately use an unavailable loopback port and UI public API points to localhost. The real embedding test sets offline Hub mode, an explicit existing model snapshot path and CPU thread limits; its fixture file server binds 127.0.0.1. No authentication/provider success is mocked by that probe. Individual existing Jest tests retain their own mocks. `--forceExit` is declared and does not certify cleanup.

From the workspace root:

```powershell
node planning/audit/collect-inventory.cjs
python -X utf8 planning/audit/collect-dependencies.py
python -X utf8 planning/audit/generate-reports.py
python -X utf8 planning/audit/run-baselines.py
python -X utf8 planning/audit/run-jest-suites.py
# Optional genuine HTTP contracts using an approved existing local model path:
$env:AUDIT_MODEL_PATH = '<absolute path to model snapshot>'
python -X utf8 planning/audit/run-baselines.py embedding-contract
Remove-Item Env:AUDIT_MODEL_PATH
python -X utf8 planning/audit/verify-audit.py
```

The model probe intentionally exits nonzero for the known batch response bug. Direct Next/tsc/ESLint/Jest executables implement the package checks while avoiding install/deploy scripts and source dotenv loading. Script reruns must stay isolated; do not change them to load a checkout's real `.env` merely to produce a passing result. Dependency junction creation or loopback server execution can need sandbox permission in this host.

Initial audit harness issues (an overbroad upload-directory exclusion, unavailable optional TestClient dependency and PDF fixture construction) were corrected; only final corrected logs/results are authoritative. The corrected API typecheck is green. Negative-test PDF rejection is an expected outcome, not an application failure.

## Issue #3 acceptance evidence

- Source identities/clean trees/licenses, database/extensions/migrations, workers, eager provider initialization, external destinations and deployment paths: source-provenance, database, systems, configuration and findings.
- Website lint/build, API typecheck/lint/Jest and real embedding health/contract baselines executed with failures documented: baselines and table above.
- Every page/layout/component/hook/provider, role/locale intent and navigation/interaction source traced: full UI ledger and page matrix, with explicit runtime uncertainty and known empty/missing routes.
- Google/SMTP/payment/webhook/YouTube/LLM/R2/Cloudinary/Lambda/Redis consumers classified into authoritative local state versus deliberate third-party calls: systems integration/state tables and source consumer inventory.
- Runtime downloads, compiled API URLs, cloud assumptions and safe source/history import strategy recorded: systems/runtime/deployment/import sections, findings and direct dependency metadata.

Payment ownership #41 and classroom topology #43 remain unresolved and do not block completion of this audit. No implementation issue is completed by this evidence. No desktop installer, complete parity, live provider certification or clean-machine build is claimed.
