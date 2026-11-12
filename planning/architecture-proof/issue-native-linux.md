<!-- dozu-proof-native:linux -->
Parent: https://github.com/Do-Zu/dozu/issues/4

## Outcome
Run the complete candidate locally on **Ubuntu 22.04 and Debian 12 x64**, using **.deb plus .AppImage where compatible**. Native execution is required; cross-compilation and a passing requirements/audit ticket are insufficient.

## Sequence
Execute after the shared #4 P1–P5 component experiments establish a runnable candidate. This depends on those experiments, not on closing parent #4. It is a proof subtask, not a duplicate implementation ticket. Coordinate #22/#23/#24/#38 for the release implementation.

## Acceptance criteria
- [ ] Record native host OS/build, CPU/architecture, RAM/storage, production artifacts/checksums, toolchain/native ABI and dynamic library versions.
- [ ] Install on each stated baseline without system Node/Python/PostgreSQL/pgvector/Docker/WSL or first-run runtime/model downloads.
- [ ] Run retained full Next standalone, Express, per-user PostgreSQL/pgvector and real CPU FastAPI/model; account for all conversion/browser/whisper.cpp/tiny-model/FFmpeg/font assets.
- [ ] Exercise dynamic routes/en+vi, shared Electron/browser local writes, files, sockets/streams, PDF/editor/media and a genuine configured system-browser provider flow. Preserve all 84 workflows; payments remain deferred under #41.
- [ ] Measure complete installer ≤250 MB/application ≤750 MB; all app-owned process normal memory ≤700 MB minimum/1 GB recommended; cold/warm interactive UI ≤10/5s minimum and ≤5/3s recommended; backend ready ≤8/4s. Record processing peaks and model/cache/network/concurrency state separately.
- [ ] Verify loopback/session boundaries, restart persistence, crash cleanup, upgrade/backup/restore, uninstall keep/delete and minimum-device/low-resource behavior, with logs.
- [ ] Publish native evidence into #4 P6/P7 and its ADR. Unrun hosts/checks remain unpassed; never relax the approved contract implicitly.

## Tracking
Priority P0; complexity L (native packaging/integration across runtime dependencies). Status waiting on #4 P1–P5 shared component experiments. No assignee is inferred. See local planning/architecture-proof/README.md for exact experiment order. Mac/Linux native hosts are not available in the current Windows workspace.
