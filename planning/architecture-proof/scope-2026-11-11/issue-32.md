<!-- dozu-tracking:start -->
## Work tracking
Use the live **status:**, **priority:** and **complexity:** labels above; **Assignees** identifies the owner. These labels are separate from the task/ticket type.

**Planning complexity:** M - Resource inventory, tracing, copied assets and disconnected local rendering checks.
Complexity is a provisional scope/uncertainty estimate, not a delivery-time commitment. XL work must be split into executable subtasks before starting.
**Planning priority:** P1 - Required product, integration or release work after its prerequisites.
<!-- dozu-tracking:end -->

## Outcome
Ensure the retained UI and local workflows load from installed resources while preserving deliberate external content features.

## Acceptance criteria
- [ ] Package Next public/static/traced assets, fonts, icons, i18n, PDF workers and local baseline images.
- [ ] Audit retained converter/media/browser/text-embedding dependencies and include resources needed for local processing.
- [ ] Verify local pages/navigation with empty caches and internet unavailable; external content features may show specific connectivity state.
- [ ] Do not infer all URL literals are runtime fetches or blanket-block YouTube/provider APIs.
- [ ] Remove accidental CDN/runtime fallback dependencies for bundled resources and record license/checksum provenance.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All existing pages remain in scope; explicit v1 capability deferrals in the 2026-11-11 amendment below apply.

<!-- dozu-roadmap:LOCAL-ASSETS -->

Phase: 1 Foundation | Priority: P1

Parent roadmap: https://github.com/Do-Zu/dozu/issues/1

## Dependencies
- #5 - [Task] Import current frontend/backend/embedding sources with provenance
- #3 - [Task] Audit complete UI/backend and local-first integration baselines

<!-- dozu-v1-scope-2026-11-11:start -->
## User-approved v1 scope amendment — 2026-11-11

- Remove local speech-to-text from this version: no whisper.cpp server, tiny speech model, speech startup/readiness gate or speech-only assets. Retain independent media playback and genuine existing YouTube transcript text retrieval. Preserve source/page inventory; no fake transcript or new cloud STT fallback.
- Keep PostgreSQL; **defer pgvector**. A private relational cluster, reviewed migrations/seeds, persistence and data-safe upgrades remain required. Current vector(384), `<=>` and HNSW consumers need explicit reviewed adaptation; do not blindly run vector-dependent migrations, discard data or replace PostgreSQL.
- The measured 479.729 MB MiniLM snapshot is a separate **text-embedding model**, used by retained PDF/YouTube reference search and ingestion. The user's condition for dropping its experiment is not met: keep smaller-runtime/quantization proof scoped to these consumers. No working smaller runtime or pgvector-free ranking implementation is claimed.
- Ordinary PostgreSQL array/JSONB vector storage plus bounded application-side cosine ranking is an evaluation candidate only. Prove owner/topic filtering, 384-value shape, ranking/topK/ties, persistence/migration, quality and realistic scale/resource budgets before adopting it. Semantic reference retrieval has not been deferred by this decision.
- Exclude FFmpeg only when its sole consumer is deferred speech-to-text; separately prove any retained non-STT need. Keep required document/URL/PDF/editor/media/font/browser resources. OS/CPU/installers, 250 MB installer/750 MB installed and memory/startup targets remain unchanged. Payments remain deferred under #41; classrooms remain LAN.

Source trace: `PdfFileEmbeddingStrategy.ts`, `YoutubeEmbeddingStrategy.ts`, `BaseEmbeddingStrategy.queryTopSimilarity()`, `inputSet.service.ts`, UI topic `components/reference/Reference.tsx`, and separate `features/whisper/api/whisper.service.ts`. Full record: local `planning/v1-scope-2026-11-11.md`. Earlier audits/measurements are historical evidence. Planning updates are not implemented feature removal or passing acceptance.
<!-- dozu-v1-scope-2026-11-11:end -->
