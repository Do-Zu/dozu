# Issue #38 — runtime supply-chain candidate evidence

**User scope update — 2026-11-14: focus on Windows only; ignore macOS/Linux.** [Machine-readable scope](../../resources/manifests/scope.json) now requires only Windows x64, with Windows 10 22H2 legacy and Windows 11 primary validation. Acquisition and generation target Windows; validation excludes non-Windows artifacts, metadata and gates. Historical foreign-platform inventory below is retained for traceability and does not block #38. No other platform's support is claimed. Windows runtime/licensing/installer/integrity/resource requirements remain unpassed where stated.

2026-11-14. **Open / In Progress / P0 / L; no acceptance criterion is complete.** #7 is closed for its explicitly narrowed JavaScript foundation only. The current branch remains `dev`; pre-existing uncommitted planning/toolchain-closure work was preserved. This work adds manifests, build-host inspection/verification tools and evidence; it does not claim a shipping desktop binary or native support.

Canonical outputs are under [resources/manifests](../../resources/manifests/README.md). Read the [license/native review](licenses-and-native.md), [integrity/upgrade contract](integrity-and-upgrades.md) and [machine-readable open gates](../../resources/manifests/gates.json).

## Initial inventory matrix — foreign rows now historical

| Required target | Electron / separate Node | PostgreSQL and tools | Python CPU embedding | Redis | Native result |
| --- | --- | --- | --- | --- | --- |
| Windows 10 22H2 / Windows 11 x64 | 45.2.3 / 22.22.0 official ZIP hashes; actual archive bytes checked | EDB 17.12-1 ZIP bytes pinned from current official endpoint; nine tool version probes pass on developer Windows 11; source 17.12 also pinned | Existing CPython 3.13.7 embedded ZIP + 45-wheel Torch 2.9.1 closure + exact multilingual model; input bytes checked; CRT/launcher gates remain | Native artifact unresolved; no entitlement/port assumed | Windows 11 **developer-host components only**; neither clean Windows 11 nor Windows 10 certified |
| macOS 13+ Intel x64 | Official per-target ZIP/tar SHA256 metadata; bytes/execution unverified | 17.12 source pinned; shipping binary/lib/ABI unverified | 3.13.7 source pinned; foreign wheel metadata only; Torch 2.9.1 has **no Intel wheel** | 7.2.17 source pinned; native build unverified | Not run |
| macOS 13+ ARM64 | Official per-target ZIP/tar SHA256 metadata; bytes/execution unverified | 17.12 source pinned; shipping binary/lib/ABI unverified | 3.13.7 source pinned; candidate CPython-3.13/ARM64 wheels listed; no resolved lock/native proof | 7.2.17 source pinned; native build unverified | Not run |
| Ubuntu 22.04 / Debian 12 x64 | Official per-target ZIP/tar SHA256 metadata; bytes/execution unverified | 17.12 source pinned; shipping binary/lib/ABI unverified | 3.13.7 source pinned; explicit official Torch 2.9.1+cpu wheel hash metadata; no resolved closure/native proof | 7.2.17 source pinned; native build unverified | Not run; recommended Ubuntu 24.04+ also needs testing |

The [active Windows target](../../resources/manifests/targets/win32-x64.json) retains null shipping artifacts/resource manifests where unresolved, empty clean-machine results and `releaseEligible: false`. NSIS exe is primary and MSI optional. The three non-Windows target files are historical, outside this task's acceptance. Windows ARM64 and 32-bit are not required. Do not relabel source archives or metadata as native shipping binaries.

The current candidate strategy uses standalone Node children for complete Next and Express, supervised by Electron. Windows Node ABI 127/Node-API 10 is measured from the downloaded binary; earlier Electron utility-process evidence is ABI 150/Node-API 10. Application native modules must target standalone Node. This resolves the ABI boundary as a candidate design, not as implemented supervisor/security/release proof. #48 must approve final supported versions and affected checks must be repeated after repinning.

## Executed evidence

- [Validation](validation.json): **7 active Windows/source artifact pins**, all **7 archives** locally verified, **45 Windows baseline wheel archives** and **10 retained baseline model files** checked by exact SHA256/size. The active Windows target's model/lock references are hash-bound. Six earlier non-Windows Electron/Node pins and foreign-wheel metadata are historical inventory, excluded from current acceptance. Node OpenPGP and independently signed Python/source/EDB archive identity remain explicit Windows provenance gates.
- [Windows native inventory](../../resources/manifests/native-windows-x64.json): **456** actual PE files hashed and inspected for machine type, normal imports and delay imports. PostgreSQL's external C++ runtime imports and actual host-loaded embedding `msvcp140.dll` remain unresolved. Six foreign-architecture setuptools launcher templates are findings, not suppressed errors. [Ten signed CRT candidates](../../resources/manifests/microsoft-crt-candidate.json) are inventoried from Visual Studio Redist, not provisioned into a release.
- [Windows probes](windows-probes.json): downloaded Node reports x64/22.22.0/ABI 127/Node-API 10; the current Windows SWC native module loads. Nine PostgreSQL 17.12 executables return successful `--version`: postgres, initdb, pg_ctl, psql, pg_dump, pg_restore, pg_isready, pg_upgrade and pg_basebackup. Scrubbed environment/PATH points to the candidate runtime plus System32. This does not hide installed system DLLs, create a cluster, run migrations or establish real backend readiness.
- [Component inventories](component-inventory-checks.json): real offline exact-file verification for candidate standalone Node (2 files) and official Electron Windows payload (73 files). The latter includes upstream demo resources; it is an inspection set, not Dozu packaging. Existing #8 embedded package inventory is hash-referenced, not duplicated or promoted to a clean runtime. Its prior inference/HTTP results retain their original [limits](../embedding-runtime/README.md).
- [Application resource inventory](../../resources/manifests/application-resources.json): **288 local public/current built-static assets** with hashes, frozen pnpm/build-input hashes and current converter/browser consumers. Local PDF worker matches installed pdfjs-dist 4.8.69; three retained viewers still select an unpkg worker and remain #32 work. Puppeteer 24.32.0 selects headless-shell 143.0.7499.40; native browser archives and a local office converter are unselected, not silently omitted.
- [Integrity checks](integrity-checks.json): **11** positive/negative checks cover trusted manifest digest, changed/missing/extra files, target/release mismatch, credential paths, traversal, directory changes and escaping directory links. Sandbox denied junction creation; the same disposable fixture passed outside the sandbox. No OS security policy was relaxed and no user files were deleted. Native macOS links/modes and protected read-only installation are not certified.
- Five primary license texts extracted from verified archives, archive-bound by [license evidence](../../resources/manifests/license-evidence.json). Complete dependency redistribution obligations remain open, particularly EDB's native libraries, Microsoft runtime entitlement/provisioning, Windows Redis, foreign Python closures and conversion/fonts/browser resources.

Host: Windows 11 Pro 10.0.26300 x64, i5-13400F, 34,137,870,336 bytes physical RAM. This is a developer host, not a clean or minimum device. No installer, whole-app benchmark, complete production import closure, DB cluster/migration, Redis server, real online provider or Linux/macOS run is claimed. The accepted 8 GB/four-core/SSD, installer ≤1.5 GB/installed ≤3 GB, app normal/peak RAM ≤2/3 GB, UI ≤15 s and backend/model ≤30 s limits remain unpassed. ONNX is optional evaluation; the exact multilingual CPU model and 384-dimensional semantic PDF/YouTube text references remain required.

## Acceptance and exact next work

| #38 acceptance criterion | Delivered here | Why it remains unchecked |
| --- | --- | --- |
| Source/version/checksum/architecture for all Windows runtimes/resources | Windows Electron/Node/PG archive pins; PG/Redis/Python source pins; existing model/wheel locks; actual resource/native inventories | Windows Redis and complete Windows converter/runtime closure remain unresolved; candidate versions are not final #48 security approval |
| Required dynamic libraries and native ABIs on clean targets | Static PE/import/machine scan; actual Node/SWC and nine PG version probes on developer host | CRT loader closure, actual consumer/CPU/plugin loads and every clean baseline remain unproven |
| Licenses/attribution/permitted redistribution; controlled acquisition | Explicit build-host acquisition, source/byte evidence, primary license texts and component inventories | Full library/source/license obligations, Windows Redis entitlement, VC distribution entitlement and final native notice closure remain unapproved |
| No source credentials/cache/user data in installer; component/provenance inventory | Minimal Node candidate stage, explicit allowlist/path-denial helper, current frozen input/resource hashes | No complete Dozu stage/installer exists here; final production closure and actual content/secret scan remain required |
| Installed-resource verification and upgrade compatibility without user setup/download | Executable offline inventory verifier with adversarial fixtures; concrete compatibility/activation/repair contract | Trusted signed-root/supervisor integration, full target manifest, schema ranges, protected paths and native upgrade/recovery tests remain required |

**Next dependency to resolve inside #38: `WINDOWS-REDIS`** — select a redistributable native Windows Redis-compatible artifact, pin version/source/hash/license, and prove existing BullMQ/Lua/pubsub/AOF/RDB semantics. Official Windows documentation points to Memurai; no commercial entitlement or unofficial binary was assumed. This is mandatory Redis retention, not a Redis-removal proposal. In the same supply-chain path, close Windows CRT loader/redistribution and EDB dependency provenance/notice coverage before claiming a self-contained Windows stack.

The remaining active gates are Windows-only: #38/#8 close Windows CPU Python/native dependency and launcher-template packaging; #32 resolves Windows local conversion/browser/PDF/font resources; #48 approves supported/security versions; #24/#28/#34 integrate the signed immutable resource root and Windows paths; #29 proves real migrations/storage compatibility; #22 runs clean Windows 10/11 release/lifecycle tests. Mac Intel Torch, foreign Python/PG/Redis builds and #46/#47 do not block #38 under the latest instruction. #49 remains a separate developer-script issue. Dependencies/assignees are not invented, and this evidence does not close #38 or satisfy #8's #38 dependency.

## Reproduce focused work

Acquisition is a deliberate controlled-build action, never a runtime/installer action. Requires a Windows x64 CPython 3.13 **build** interpreter, Node and the existing #8 verified cache/component; use the committed hash locks to reproduce that component first. Existing caches and `.runs` are ignored; do not commit archives or user data. The anonymous GitHub API was rate-limited; authenticated `gh api` supplied release metadata, with no token printed or stored in manifests.

```powershell
gh api repos/electron/electron/releases/tags/v45.2.3 > <temporary-release-metadata.json>
python planning/runtime-manifests/acquire_candidates.py --refresh --electron-metadata <temporary-release-metadata.json>
python planning/runtime-manifests/inspect_windows.py
./planning/runtime-manifests/collect_windows_metadata.ps1
python planning/runtime-manifests/application_resources.py
python planning/runtime-manifests/generate.py
node planning/runtime-manifests/check-integrity.cjs
python planning/runtime-manifests/validate.py
python planning/runtime-manifests/validate.py --release
```

Use the native CPython path when `python` resolves to MSYS or another interpreter. `--refresh` regenerates candidates for human review, not automatic release approval; the recorded official Redis hash-list revision fixes the selected 7.2.17 source. Current EDB index fileid 1260667 returned HTTP 200 and resolved to `postgresql-17.12-1-windows-x64-binaries.zip`; the old #4 HTTP 403 is historical. [Endpoint check](postgres-windows-acquisition.json).

`validate.py` passes candidate consistency. `--release` exits **1 intentionally** with every unresolved required gate; an expected refusal is not a failed candidate-consistency check. Full app builds/tests were not repeated because application source/dependencies were unchanged. After a baseline/security/assembler change, rerun the affected imports/ABI/integrity checks; do not present unchanged historical component results as a new full release run.

Primary sources are linked in the [native/license review](licenses-and-native.md), the exact artifact source/checksum/provenance fields and the existing pinned model/wheel evidence. No issue acceptance box was checked by this work.
