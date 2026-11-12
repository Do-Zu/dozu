<!-- dozu-proof-native:linux -->
Parent: https://github.com/Do-Zu/dozu/issues/4

## Outcome
Run the complete candidate locally on **Ubuntu 22.04 and Debian 12 x64**, using **.deb plus .AppImage where compatible**. Native execution is required; cross-compilation and a passing requirements/audit ticket are insufficient.

## Sequence
Execute after the shared #4 P1–P5 component experiments establish a runnable candidate. This depends on those experiments, not on closing parent #4. It is a proof subtask, not a duplicate implementation ticket. Coordinate #22/#23/#24/#38 for the release implementation.

## Acceptance criteria
- [ ] Record native host OS/build, CPU/architecture, RAM/storage, production artifacts/checksums, toolchain/native ABI and dynamic library versions.
- [ ] Install on each stated baseline without system Node/Python/PostgreSQL/Docker/WSL or first-run runtime/model downloads.
- [ ] Run retained full Next standalone, Express, per-user PostgreSQL and real CPU FastAPI/model; account for all retained conversion/browser/text-embedding/font assets; exclude Whisper/tiny speech model and speech-only assets.
- [ ] Exercise dynamic routes/en+vi, shared Electron/browser local writes, files, sockets/streams, PDF/editor/media and a genuine configured system-browser provider flow. Preserve all 84 workflows; payments remain deferred under #41.
- [ ] Measure complete installer ≤250 MB/application ≤750 MB; all app-owned process normal memory ≤700 MB minimum/1 GB recommended; cold/warm interactive UI ≤10/5s minimum and ≤5/3s recommended; backend ready ≤8/4s. Record processing peaks and model/cache/network/concurrency state separately.
- [ ] Verify loopback/session boundaries, restart persistence, crash cleanup, upgrade/backup/restore, uninstall keep/delete and minimum-device/low-resource behavior, with logs.
- [ ] Publish native evidence into #4 P6/P7 and its ADR. Unrun hosts/checks remain unpassed; never relax the approved contract implicitly.

## Tracking
Priority P0; complexity L (native packaging/integration across runtime dependencies). Status waiting on #4 P1–P5 shared component experiments. No assignee is inferred. See local planning/architecture-proof/README.md for exact experiment order. Mac/Linux native hosts are not available in the current Windows workspace.

<!-- dozu-v1-scope-2026-11-11:start -->
## User-approved v1 scope amendment — 2026-11-11

- Remove local speech-to-text from this version: no whisper.cpp server, tiny speech model, speech startup/readiness gate or speech-only assets. Retain independent media playback and genuine existing YouTube transcript text retrieval. Preserve source/page inventory; no fake transcript or new cloud STT fallback.
- Keep PostgreSQL; **defer pgvector**. A private relational cluster, reviewed migrations/seeds, persistence and data-safe upgrades remain required. Current vector(384), `<=>` and HNSW consumers need explicit reviewed adaptation; do not blindly run vector-dependent migrations, discard data or replace PostgreSQL.
- The measured 479.729 MB MiniLM snapshot is a separate **text-embedding model**, used by retained PDF/YouTube reference search and ingestion. The user's condition for dropping its experiment is not met: keep smaller-runtime/quantization proof scoped to these consumers. No working smaller runtime or pgvector-free ranking implementation is claimed.
- Ordinary PostgreSQL array/JSONB vector storage plus bounded application-side cosine ranking is an evaluation candidate only. Prove owner/topic filtering, 384-value shape, ranking/topK/ties, persistence/migration, quality and realistic scale/resource budgets before adopting it. Semantic reference retrieval has not been deferred by this decision.
- Exclude FFmpeg only when its sole consumer is deferred speech-to-text; separately prove any retained non-STT need. Keep required document/URL/PDF/editor/media/font/browser resources. OS/CPU/installers, 250 MB installer/750 MB installed and memory/startup targets remain unchanged. Payments remain deferred under #41; classrooms remain LAN.

Source trace: `PdfFileEmbeddingStrategy.ts`, `YoutubeEmbeddingStrategy.ts`, `BaseEmbeddingStrategy.queryTopSimilarity()`, `inputSet.service.ts`, UI topic `components/reference/Reference.tsx`, and separate `features/whisper/api/whisper.service.ts`. Full record: local `planning/v1-scope-2026-11-11.md`. Earlier audits/measurements are historical evidence. Planning updates are not implemented feature removal or passing acceptance.
<!-- dozu-v1-scope-2026-11-11:end -->
