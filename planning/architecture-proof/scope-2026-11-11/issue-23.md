<!-- dozu-tracking:start -->
## Work tracking
Use the live **status:**, **priority:** and **complexity:** labels above; **Assignees** identifies the owner. These labels are separate from the task/ticket type.

**Planning complexity:** XL - Multi-runtime installers with native resources across OS/CPU combinations; split by packaging target.
Complexity is a provisional scope/uncertainty estimate, not a delivery-time commitment. XL work must be split into executable subtasks before starting.
**Planning priority:** P1 - Required product, integration or release work after its prerequisites.
<!-- dozu-tracking:end -->

## Outcome
Generate per-platform installers that supply the entire local app stack and resource manifest.

## Acceptance criteria
- [ ] Package Next assets/server, Express/runtime, PostgreSQL/tools, FastAPI/Python/model, local workers and native resources.
- [ ] Use native OS/CPU CI jobs and validate dynamic libraries/native ABIs, licenses/checksums and relocatable resource paths.
- [ ] Require no manual install/configuration of backend/database/Node/Python/Redis/Docker/WSL.
- [ ] Produce agreed Windows/macOS/Linux formats with clear install/upgrade/uninstall support and version metadata.
- [ ] Test clean install/launch, optional integration setup and full local workflow before release signing.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All existing pages remain in scope; explicit v1 capability deferrals in the 2026-11-11 amendment below apply.

<!-- dozu-roadmap:PACKAGING -->

Phase: 4 Release | Priority: P1

Parent roadmap: https://github.com/Do-Zu/dozu/issues/1

## Dependencies
- #15 - [Task] Integrate Electron with the complete managed local application
- #7 - [Task] Pin portable toolchains and runtime-compatible builds
- #38 - [Task] Assemble verified per-platform runtimes, binaries and licenses
- #33 - [Task] Validate automatic first-run setup on clean user machines

<!-- dozu-v1-scope-2026-11-11:start -->
## User-approved v1 scope amendment — 2026-11-11

- Remove local speech-to-text from this version: no whisper.cpp server, tiny speech model, speech startup/readiness gate or speech-only assets. Retain independent media playback and genuine existing YouTube transcript text retrieval. Preserve source/page inventory; no fake transcript or new cloud STT fallback.
- Keep PostgreSQL; **defer pgvector**. A private relational cluster, reviewed migrations/seeds, persistence and data-safe upgrades remain required. Current vector(384), `<=>` and HNSW consumers need explicit reviewed adaptation; do not blindly run vector-dependent migrations, discard data or replace PostgreSQL.
- The measured 479.729 MB MiniLM snapshot is a separate **text-embedding model**, used by retained PDF/YouTube reference search and ingestion. The user's condition for dropping its experiment is not met: keep smaller-runtime/quantization proof scoped to these consumers. No working smaller runtime or pgvector-free ranking implementation is claimed.
- Ordinary PostgreSQL array/JSONB vector storage plus bounded application-side cosine ranking is an evaluation candidate only. Prove owner/topic filtering, 384-value shape, ranking/topK/ties, persistence/migration, quality and realistic scale/resource budgets before adopting it. Semantic reference retrieval has not been deferred by this decision.
- Exclude FFmpeg only when its sole consumer is deferred speech-to-text; separately prove any retained non-STT need. Keep required document/URL/PDF/editor/media/font/browser resources. OS/CPU/installers, 250 MB installer/750 MB installed and memory/startup targets remain unchanged. Payments remain deferred under #41; classrooms remain LAN.

Source trace: `PdfFileEmbeddingStrategy.ts`, `YoutubeEmbeddingStrategy.ts`, `BaseEmbeddingStrategy.queryTopSimilarity()`, `inputSet.service.ts`, UI topic `components/reference/Reference.tsx`, and separate `features/whisper/api/whisper.service.ts`. Full record: local `planning/v1-scope-2026-11-11.md`. Earlier audits/measurements are historical evidence. Planning updates are not implemented feature removal or passing acceptance.
<!-- dozu-v1-scope-2026-11-11:end -->
