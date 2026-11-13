## #7 local implementation checkpoint — 2026-11-13

Started the independently executable portability work from clean `dev` at `5712218`, following completed #6. Issue and existing Project #6 item are **In Progress**; existing assignment, other fields and dependency links are preserved. Work is local/uncommitted, not pushed, merged or released.

Implemented in the imported monorepo (original nested checkouts preserved):

- Aligned UTF-8/LF Node version files with the exact measured Node 22.22.0 build baseline; verified pnpm 10.28.2, Turbo 2.5.8 and TypeScript 5.8.3. Added root preflight/development/start/website packaging commands and documented their limits.
- Anchored API aliases and Drizzle config paths independently of cwd; migration commands use the locked local CLI without npx download fallback. No migration/history/vector step was applied or changed.
- Added explicit absolute `DOZU_DATA_DIR` routing for logs/uploads/conversion paths, retaining website cwd defaults and existing overrides. Removed environment/logger initialization cycle. Desktop supervision and full local-data integration remain open.
- Fixed a directly reproduced production-build defect: cleaning dist while keeping incremental TS state could produce a successful but incomplete output. Production compile now emits the complete API. Generated output is excluded from source lint.
- Removed shell interpolation from the legacy Lambda ZIP helper; verified a Windows fixture containing spaces, brackets, apostrophe and `$`, including exact archive contents. No cloud/deployment command ran.

Direct evidence:

- Frozen offline install passed (existing workspace, lifecycle suppressed, unchanged dependency lock).
- Full API and retained Next production builds plus root `pnpm package` passed; 3 actual tasks executed. The standalone website has 22 contained relative links.
- All **1,239** compiled alias references resolve from an unrelated cwd. Component upload/conversion writes and real Winston flushing pass with writes restricted to a disposable data directory; forbidden cwd writes fail. Relocated migration config resolves paths without DB access.
- The new website start wrapper served **9 real HTTP page/asset/font checks**, including en/vi pages, with all filesystem writes denied and original workspace reads denied; owned process stopped. Sandbox EPERM/socket restrictions required scoped external retries; Node filesystem restrictions remained in force.
- Windows x64 Next SWC loads under standalone Node 22.22.0 (module ABI 127, Node-API 10; binary hash recorded). This is not Electron/native-stack acceptance. Canvas remains unavailable after suppressed lifecycle scripts.
- API source lint retains exactly the inherited **100 errors/143 warnings**, with zero added/removed diagnostic signatures. Full API startup is **unpassed**: scrubbed real entrypoint encounters inherited DB/log serialization, Redis and eager mail configuration blockers; final run exits on missing `BACKEND_BASE_URL`. Real dotenv reads were deliberately denied in this probe. No backend-ready claim.

Reviewable local files: `planning/toolchains/README.md`, `inventory.json`, `runtime-checks.json`, `website-proof.json`, `root-package.json`, `lint-comparison.json`, scripts/logs and root `README.md`. New root commands create a website artifact and compiled API, **not a desktop installer**. End users must still receive bundled runtimes/assets without developer tools; that acceptance is unpassed.

Vendor policy checks identify Next 14 as unsupported. The measured Next 14.2.35/React baseline is preserved here; a supported security-reviewed framework upgrade requires its own exact target and independent regression evidence. Node pins likewise establish reproducibility, not latest-patch approval. Sources: [Next support policy](https://nextjs.org/support-policy), [Node release schedule](https://github.com/nodejs/Release), [Electron native ABI guidance](https://www.electronjs.org/docs/latest/tutorial/using-native-node-modules).

**Dependency reconciliation:** live #4 says closed/completed and has checked headline criteria, while its [user-directed closure record](https://github.com/Do-Zu/dozu/issues/4#issuecomment-6825382086) says NOT PLANNED and explicitly leaves full acceptance open; P4–P7/native subissues remain unchecked. This work does not alter #4 or infer completion from that state. Proposal: retain it as historical canceled work and explicitly map remaining gates to #1's existing delivery ledger before changing dependency completion logic. The user authorized independent #7 work; #7's #4 dependency remains visibly unresolved for full-stack/ABI acceptance.

**No full #7 acceptance box is checked.** All required Windows 10/11 x64, macOS 13+ x64/ARM64, Ubuntu 22.04/Debian 12 x64 native installer/minimum-host tests remain unpassed. So do selected bundled Electron/Node/Python/PostgreSQL runtimes, model/browser/converter resources, reviewed migrations, security/upgrade validation and complete lifecycle/resource budgets. Scope remains exactly the approved v1 scope, including retained website/UI/PDF/YouTube text embeddings, PostgreSQL without pgvector, no local STT, deferred payments and LAN classrooms.
