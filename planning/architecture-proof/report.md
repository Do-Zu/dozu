# First Windows architecture experiments — issue #4

2026-11-10, Asia/Bangkok. **Partial proof; #4 remains open/in progress. All parent acceptance criteria and P1–P7 completion gates remain unchecked.**

The retained Next server can execute inside Electron's Node utility process on this host. The unmodified default embedding/runtime combination does **not** fit the agreed installed-size budget. This does not establish a full packaged app, installer, all-platform support or feature parity.

## Scope, hardware and immutable inputs

- Windows 11 Pro 10.0.26300 x64, Intel i5-13400F (10 cores/16 threads), approximately 32 GB RAM; [hardware](hardware.json). No minimum 4 GB/dual-core device, HDD or recommended 8 GB device benchmark was run. Physical storage type/display and clean-machine prerequisites were not validated.
- Original UI `5e1ceb263a29e2fde2359c36f43d0118a8d622f0`, API `173f3f1cbcc81b89ad3eea81723698f7bb7eb876`, embedding `188d0d229a38ee51f48f1e5d5f06cf69f16870c6`. All three source trees remain clean. No source/history import, merge or source commit occurred. Input files/hashes are in the three `*-inputs.json` manifests.
- Pinned experimental Electron **45.2.3 win32-x64**, bundled Node **24.22.2**, Chromium **156.0.8078.80**, modules ABI **150**. Official ZIP 158,182,975 bytes; SHA256 `489cd061908e697394b004298bf5ffd345c935d10e8ca197ba819f019ab2dec0`, verified before extraction. [Supplier metadata](electron-acquisition.json). This pin is a Windows experiment, not a production selection or proof of other baseline OS support.
- Build tool Node 22.22.0 from the existing developer machine; Next 14.2.35/React 18.3.1. The runtime Next experiment uses Electron's Node, not that system Node executable.
- Embedding uses existing Python **3.13.7**, torch **2.9.1**, sentence-transformers **5.1.1**, transformers **4.57.1**, FastAPI **0.117.1**, Uvicorn **0.37.0**. [All installed package versions](python-installed-versions.json). This existing venv/base Python is **not a portable bundled Python proof**.
- CPU model `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`, snapshot **86741b4e3f5cb7765a600d3a3d55a0f6a6cb443d**, explicitly selected from existing cache, all 10 snapshot files hashed in [inventory](inventory.json). Model weight SHA256 `eaa086f0ffee582aeb45b36e34cdd1fe2d6de2bef61f8a559a1bbc9bd955917b`.

Nested Git metadata, real dotenv, registry auth, user data and production databases were excluded from proof copies. Build copies reuse existing dependencies, with no clean `npm ci`/pip resolution claim. Runtime child environments contain only an OS allowlist and explicit local proof settings. No provider credentials or transactions were used. The hidden renderer blocks non-loopback requests; embedding uses offline Hub flags/fresh HF_HOME and an explicit existing snapshot. This is not an OS-wide firewall-denial test. No first-run asset provisioning is implemented.

## P1: size feasibility

All MB below are decimal (10^6 bytes); JSON also records MiB. Measurements are logical file lengths, not filesystem compressed sizes or development-directory totals represented as a release closure.

| Measured resource | Bytes | MB | Meaning |
| --- | ---: | ---: | --- |
| One model weight (`model.safetensors`) | 470,641,600 | 470.642 | One format only; no duplicate weights counted |
| Entire model snapshot | 479,728,964 | 479.729 | Includes tokenizer/config/pooling, not hidden as user data |
| Actually loaded `torch_cpu.dll` | 262,656,512 | 262.657 | Loaded module path independently observed through Windows PSAPI |
| Executed `electron.exe` | 249,831,936 | 249.832 | Only the main executable, not all Electron resources |
| **Weight + CPU DLL + Electron executable** | **983,130,048** | **983.130** | **Already exceeds 750 MB installed target** |
| Full extracted Electron archive | 374,135,000 approximately | 374.135 | Exact summed bytes in inventory; includes resources/DLLs/locales |
| Staged conservative Next/React closure + emitted UI/public/static | 128,202,924 | 128.203 | 20 runtime package directories; not a minimal trace or every workflow verified |
| Existing FFmpeg executable | 99,455,488 | 99.455 | Developer asset only; final redistribution/build selection unapproved |
| Existing Puppeteer cache | 667,667,000 approximately | 667.667 | Both Chrome and headless shell present; **not both declared mandatory** |
| Existing Python environment (excluding pycache) | 872,821,000 approximately | 872.821 | Includes development/optional files; **not a minimal required release size** |

The three-file bound is sufficient to reject this **exact unquantized model + observed torch CPU DLL + Electron executable** combination under 750 MB. It also exceeds 750 MiB, so the finding does not depend on interpreting MB/MiB. Removing headers/dev dependencies/extra cached browser copies cannot solve that bound. It says nothing conclusive about a different quantized model/runtime or framework version.

The snapshot was streamed through XZ/LZMA2 preset 6 in lexical file order: **410,574,192 bytes (410.574 MB)**, versus the 250 MB installer target. Output was hashed/counted and discarded; method/checksum/time are in [model-compression.json](model-compression.json). This is evidence that ordinary lossless compression is insufficient for this model, **not an NSIS installer measurement or a mathematical bound on every compressor**. No complete installer exists or passed.

Missing/unproven footprint remains PostgreSQL/pgvector, portable Python closure/base DLLs, API/jobs/cache, native document converter/LibreOffice-compatible behavior and fonts, whisper.cpp/tiny model, and final FFmpeg/browser resources/licenses. Unknown sizes are not zero. Reusing Electron Chromium for URL→PDF is an experiment to perform, not an established capability. Source's optional spaCy/thinc imports were observed in the venv; `en_core_web_sm` is absent and source falls back without sentence refinement. Its optional package/model policy must be explicit in the processing manifest, not silently removed to improve numbers.

## P2: actual production build and Electron startup

1. Sanitized unchanged Next production build reproduced F01 (Promise<number>/number), [baseline](ui-build-baseline.log). Original website source remains unchanged and still has that baseline defect.
2. A **disposable-copy-only** [type guard patch](ui-f01-typeguard.patch) checks that the raw ready-event IFrame player returns a number and explicitly rejects an asynchronous facade. No type-check suppression, static-export conversion or UI deletion. Adapter number/zero/seek/async-rejection contract checks pass, [log](ui-f01-adapter-contract.log). Genuine YouTube playback/provider flow remains untested.
3. Full production Next build/type validation then passes, [log](ui-build-typeguard.log), retaining every generated page including dynamic locale routes. Build still skips lint by existing configuration; the audit's lint failures remain. A build success is not runtime parity.
4. Express production TypeScript compile passes, [log](api-build-baseline.log). Under Electron, the actual compiled entrypoint exits without HTTP readiness on missing `BACKEND_BASE_URL`; with only local frontend/backend URLs it gets further and exits on missing PayOS configuration. [First run](electron-api-empty-child.log), [local URLs](electron-api-local-urls-child.log). Eager Redis attempts remain. A DB-object logger also reports circular-JSON serialization during import. No dummy merchant keys, fake provider success, swallowed route errors or simulated API were added.
5. Binding Next to `127.0.0.1` exposed Next 14 URL normalization to `localhost` and middleware self-proxy failure; [failed attempt](electron-web-ipv4-child.log). Using **both binding and origin `localhost`** resolved the sampled requests. Production port discovery, multiple instances, hostile Host/Origin and IPv4/IPv6 policy remain follow-up work.
6. Initial standalone output preserved the developer dependency link. The proof rejected that as self-contained evidence. [Trace repair](repair-tracing.py) removed only the exact directory link and copied approved traced files; trace alone still omitted necessary package files. [Conservative package staging](stage-next-packages.py) then supplied Next/React's declared production package closure; [manifest](next-packaged-closure.json). Original dependency files were not edited. Runtime module resolution was guarded to **reject any absolute module path outside the staged standalone root**.
7. With that guard enabled, Electron utilityProcess executes retained standalone and a hidden BrowserWindow loads the existing welcome UI with nodeIntegration=false/contextIsolation=true/sandbox=true. `/en/welcome`, `/vi/welcome`, `/en/topics/proof-topic`, `/vi/auth/login` and an emitted JavaScript chunk return HTTP 200. [Structured process/HTTP evidence](electron-web-contained.json), [log](electron-web-contained-child.log), [capture](next-welcome.png).

**Runtime gaps remain even with HTTP 200:** topic rendering logs `ReferenceError: location is not defined`; standalone image optimization reports missing `sharp`; Electron reports a CSP warning. No authenticated topic data was loaded. An HTTP 200/dynamic server route/hydrated welcome shell is not a passing topic workflow, editor/PDF/media capability, role gate or complete interactive app.

The sample's HTTP readiness is **4.839 s** and hidden DOM-load probe **10.248 s**, timed from inside Electron's main script, excluding earlier executable startup. Deliberate waits/extra HTTP probes are included. These are **not cold/warm launch-to-interactive acceptance timings**. Five Electron-owned processes (main, GPU, networking utility, renderer, Next utility) are enumerated with CPU and memory samples every 200 ms. Their last working-set snapshot sums to **550.871 MB** (Electron memory units multiplied by 1024); API/DB/Python/converters were not running in this group. Shared pages may be double counted. This is not the approved full-app normal workload.

## P3: local DB/bootstrap not executed

No PostgreSQL binary was found on PATH or the standard Windows install path. Official EDB PostgreSQL 17.11 Windows binary archive and its official alternate endpoint both returned **HTTP 403**, [repeatable availability evidence](database-availability.json). Visual Studio C++ x64 tools are available for building pinned pgvector once a verified PostgreSQL distribution is obtained. No alternate unverified binary was substituted.

No native cluster, extension, migrations, first-boot seeds, SQL/vector/HNSW test, user write or persistence test was run. The audit's 20 Git-ignored migration hashes remain the migration provenance reference, not bootstrap success. This is an environment acquisition impediment, not evidence that PostgreSQL itself is infeasible. Native DB work remains P3/#29/#40.

## P4: genuine offline CPU component

Actual retained FastAPI/Uvicorn runs on loopback with CPU thread limits OMP=2/MKL=2, explicit model snapshot and fresh HF_HOME/offline flags. OS file cache was not evicted. Dataset: one short English sentence plus one identical-string comparison and a one-segment batch; no production records/imported media. [Serial result](embedding-runtime-serial.json), [log](embedding-runtime-serial.log).

| Probe | Observed result |
| --- | --- |
| Model/backend health ready | 6.332 s serial run on warm OS file cache; readiness includes actual startup model load |
| Single text | HTTP 200; 384 finite values; norm 0.9999999764; request 0.0422 s |
| Identical comparison | HTTP 200; similarity 0.9999999279 |
| Batch segments | **HTTP 500**, existing list/Dict response validation defect reproduced |
| Idle after requests | **762,408,960 bytes WS (762.409 MB)**; private bytes **1,209,597,952** |
| Native library inventory | 270 loaded modules; includes exact torch CPU DLL and optional spaCy/thinc dependencies |

An earlier run during build/compression activity took 45.369 s and retained approximately 761 MB. It is explicitly a **contended component sample**, not a cold-launch acceptance benchmark. Serial repeat resolved that timing ambiguity. The existing venv has optional spaCy and other packages beyond requirements, so these memory numbers do not prove a minimal clean Python closure's memory. They are a measured warning for this actual environment, not a claim that every optimized candidate must fail. No app memory result is obtained by pretending to add independently timed snapshots.

Base Python, venv and snapshot are still developer assets outside an installer. Stop used forced termination, not validated graceful shutdown. No full media peak, long-running job/cache growth, low-resource mode, quality/retrieval comparison or fresh-machine offline provisioning test was run.

## Native matrix, security and data lifecycle

| Required host/package | Evidence in this chat | Gate |
| --- | --- | --- |
| Windows 10 22H2 x64 / NSIS | No native host run, no installer | Unpassed, #45 |
| Windows 11 x64 / NSIS | Current developer host component experiments only | Packaged/clean/minimum-device unpassed, #45 |
| macOS 13+ Intel x64 / signed notarized DMG | No attached native host | Unpassed, #46 |
| macOS 13+ ARM64 / signed notarized DMG | No attached native host | Unpassed, #46 |
| Ubuntu 22.04 x64 / deb, compatible AppImage | No attached native host | Unpassed, #47 |
| Debian 12 x64 / deb, compatible AppImage | No attached native host | Unpassed, #47 |

Loopback bind and renderer isolation were configured in experiments; Host/Origin/session/CSRF authorization and provider secret storage are not validated. Existing API listen-without-host, SSE/socket authorization and eager-provider issues remain. No real system-browser provider flow, LAN participant, Docker/WSL prerequisite elimination, upgrade, backup/restore, crash recovery or uninstall keep/delete test passed. No actual user data was used. No performance/support target changed. Payments remain deferred/blocked in #41.

## Recommendation and next bounded experiments

See [proposed ADR](adr-0001.md). Retain the complete Next/Express product while treating **this unoptimized default payload as rejected under 750 MB**. Before building a full installer, evaluate a smaller CPU embedding runtime and quantized representation of the same multilingual model behind the FastAPI/API contracts. Compare en/vi vectors/retrieval and report quality/latency/memory/size; no quality threshold or model replacement is pre-approved. Resolve `sharp`/topic SSR, optional-provider lazy startup and durable jobs without hiding current failures.

In parallel with that component sequence (not parallel agent work), obtain provenance/checksum-verified native PostgreSQL/pgvector, establish migrations/seeds, and quantify actual document/media dependencies. Test Electron Chromium reuse only with URL→PDF fidelity/sandbox evidence. These are options to prove; **do not remove functionality, replace PostgreSQL without compatibility evidence, introduce cloud dependencies or relax budgets**. Actual clean native Windows/macOS/Linux installers and full process measurements remain required before an accepted architecture decision or closing #4.

## Tracking verification and primary references

[GitHub progress comment](https://github.com/Do-Zu/dozu/issues/4#issuecomment-6770301111), [tracking readback](tracking-verification.json) and [process cleanup](cleanup.json): #4 is open/in progress in labels and Project, unassigned, all original acceptance text preserved and unchecked. Three waiting/Todo native subissues are linked. All original Project field definitions/custom values outside #4 are preserved. Readback observed Assignee additions on #2/#3 during this work; they were left intact. No owned proof processes remained after cleanup.

Methods follow the [Electron utilityProcess API](https://www.electronjs.org/docs/latest/api/utility-process) and [Next 14 standalone output contract](https://nextjs.org/docs/14/app/api-reference/next-config-js/output), including separate public/static copying. The adapter guard is grounded in the [YouTube IFrame API](https://developers.google.com/youtube/iframe_api_reference), while the installed react-youtube/youtube-player ready-event forwarding was inspected locally. These documents describe APIs; the experiment logs establish only the narrow observations above.

## Reproduce and inspect

From workspace root, use scripts here with the existing approved build dependencies. All generated binaries/models/working copies stay under ignored `.runs/` and `.downloads/`; logs/manifests/scripts are retained outside. Network/process/junction actions can require sandbox escalation on this host.

```powershell
python -X utf8 planning/architecture-proof/inventory.py
python -X utf8 planning/architecture-proof/compress-model.py
python -X utf8 planning/architecture-proof/build.py ui
python -X utf8 planning/architecture-proof/build.py api
python -X utf8 planning/architecture-proof/ui-typeguard-build.py
# Remove the traced developer link; stage packages and public/static assets:
python -X utf8 planning/architecture-proof/repair-tracing.py
python -X utf8 planning/architecture-proof/stage-next-packages.py
python -X utf8 planning/architecture-proof/run-electron.py web-contained
python -X utf8 planning/architecture-proof/run-electron.py api-empty
python -X utf8 planning/architecture-proof/run-electron.py api-local-urls
./dozu-embedding-service/.venv/Scripts/python.exe -X utf8 planning/architecture-proof/embedding-probe.py serial
./planning/architecture-proof/probe-db-download.ps1
python -X utf8 planning/architecture-proof/summarize.py
```

Download/extract only the official Electron archive in acquisition metadata and verify its digest before these runtime commands; no tool automatically supplies it on a new machine. The typeguard build script always prepares a clean source copy first. Rebuilding Next can recreate its dependency link, so rerun repair/staging before treating later runtime results as contained. `results.json`, input manifests and `evidence-manifest.json` provide machine-readable details and hashes. Earlier failed probes/harness corrections are retained in logs; final `web-contained` and serial embedding results are authoritative for their narrow checks.
