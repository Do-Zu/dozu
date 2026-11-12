<!-- dozu-tracking:start -->
## Work tracking
Use the live **status:**, **priority:** and **complexity:** labels above; **Assignees** identifies the owner. These labels are separate from the task/ticket type.

**Planning complexity:** M - Development orchestration and diagnostic documentation after local service contracts exist.
Complexity is a provisional scope/uncertainty estimate, not a delivery-time commitment. XL work must be split into executable subtasks before starting.
**Planning priority:** P2 - Required supporting work scheduled after the core foundations; not removed from release scope.
<!-- dozu-tracking:end -->

## Outcome
Provide developer commands and diagnostics matching the managed desktop runtime while retaining website development.

## Acceptance criteria
- [ ] Run Next/Express/DB/embedding/jobs with explicit readiness and generated local configuration.
- [ ] Document development-only tooling separately from the installer: Docker may help development but is never a desktop runtime prerequisite.
- [ ] Provide placeholder-only environment templates and optional integration configuration instructions.
- [ ] Verify local browser and Electron point to the same API/DB/files with no compiled hosted Dozu endpoint.
- [ ] Document non-destructive stop/reset, logs, port conflicts and platform-specific native dependency troubleshooting.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All existing pages remain in scope; explicit v1 capability deferrals in the 2026-11-11 amendment below apply.

<!-- dozu-roadmap:DEV-INFRA -->

Phase: 1 Foundation | Priority: P2

Parent roadmap: https://github.com/Do-Zu/dozu/issues/1

## Dependencies
- #7 - [Task] Pin portable toolchains and runtime-compatible builds
- #29 - [Task] Bundle and initialize per-user PostgreSQL (pgvector deferred)
- #40 - [Task] Add a local backend profile with automatic seeds and lazy integrations
- #8 - [Task] Bundle local FastAPI, Python and baseline embedding model

<!-- dozu-v1-scope-2026-11-11:start -->
## User-approved v1 scope amendment — 2026-11-11

- Remove local speech-to-text from this version: no whisper.cpp server, tiny speech model, speech startup/readiness gate or speech-only assets. Retain independent media playback and genuine existing YouTube transcript text retrieval. Preserve source/page inventory; no fake transcript or new cloud STT fallback.
- Keep PostgreSQL; **defer pgvector**. A private relational cluster, reviewed migrations/seeds, persistence and data-safe upgrades remain required. Current vector(384), `<=>` and HNSW consumers need explicit reviewed adaptation; do not blindly run vector-dependent migrations, discard data or replace PostgreSQL.
- The measured 479.729 MB MiniLM snapshot is a separate **text-embedding model**, used by retained PDF/YouTube reference search and ingestion. The user's condition for dropping its experiment is not met: keep smaller-runtime/quantization proof scoped to these consumers. No working smaller runtime or pgvector-free ranking implementation is claimed.
- Ordinary PostgreSQL array/JSONB vector storage plus bounded application-side cosine ranking is an evaluation candidate only. Prove owner/topic filtering, 384-value shape, ranking/topK/ties, persistence/migration, quality and realistic scale/resource budgets before adopting it. Semantic reference retrieval has not been deferred by this decision.
- Exclude FFmpeg only when its sole consumer is deferred speech-to-text; separately prove any retained non-STT need. Keep required document/URL/PDF/editor/media/font/browser resources. OS/CPU/installers, 250 MB installer/750 MB installed and memory/startup targets remain unchanged. Payments remain deferred under #41; classrooms remain LAN.

Source trace: `PdfFileEmbeddingStrategy.ts`, `YoutubeEmbeddingStrategy.ts`, `BaseEmbeddingStrategy.queryTopSimilarity()`, `inputSet.service.ts`, UI topic `components/reference/Reference.tsx`, and separate `features/whisper/api/whisper.service.ts`. Full record: local `planning/v1-scope-2026-11-11.md`. Earlier audits/measurements are historical evidence. Planning updates are not implemented feature removal or passing acceptance.
<!-- dozu-v1-scope-2026-11-11:end -->
