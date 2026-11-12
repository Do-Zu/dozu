# Architecture proof — issue #4

**Current tracker state — 2026-11-12:** #4 is closed **not planned**, with acceptance unpassed; descriptions of it as in progress below are historical. #1 coordinates the remaining proof through existing delivery children; #5 source-import review has started. See [delivery reconciliation](../roadmap/README.md). The 2026-11-11 amendment supersedes older speech/pgvector wording.

Started 2026-11-10 (Asia/Bangkok). **In progress; no parent acceptance criterion passed.**

**Current scope (2026-11-11):** [speech-to-text removed; PostgreSQL kept; pgvector deferred](../v1-scope-2026-11-11.md). The large measured model is for retained PDF/YouTube text references, so P4's smaller-runtime experiment remains relevant. Historical measurements are not rewritten or automatically discounted.

First evidence: [Windows experiment report](report.md), [proposed ADR](adr-0001.md), [structured results](results.json). Native validation subissues: [#45 Windows](https://github.com/Do-Zu/dozu/issues/45), [#46 macOS](https://github.com/Do-Zu/dozu/issues/46), [#47 Linux](https://github.com/Do-Zu/dozu/issues/47). They await the shared component experiments, not parent closure.

**2026-11-11 continuation:** User reports the welcome preview works smoothly. [PostgreSQL-only component proof](postgres-only/report.md) now verifies native isolated startup, candidate migrations, relational writes, restart and backup/restore without pgvector. Original migration defects, missing feedback migration, candidate-only patches and unproven integration/scale/platform work are recorded; P3 and parent acceptance remain unchecked.

**Backend continuation:** [Retained Express connected to PostgreSQL-only](backend-local/report.md) passes 36 real HTTP/persistence checks after scoped candidate startup fixes. TypeScript passes; existing full lint failures remain with zero new source diagnostics. Cold-start uncertainty, local account/bootstrap/cache/jobs/embeddings, UI integration and product packaging remain open; P2/P3 and full acceptance stay unchecked.

Requirements: [approved support/resource contract](../platform-support.md). Baseline: [audit](../audit/README.md), [all 84 workflows](../audit/feature-parity.md), [findings](../audit/findings.md), [systems](../audit/systems.md). #2/#3 are completed requirements/audit work, not runtime compatibility evidence. Payments remain deferred in #41; classrooms use a user-owned LAN host.

## Sequenced proof checklist

These are bounded experiments under #4, not new feature implementations. Each result must name its command, immutable inputs, artifacts, method and limitations. Native clean-machine execution is separated into linked subissues because it needs different hosts. Do not import/merge source history as part of these experiments.

| Step | Experiment and completion evidence | Prerequisites | Implementation follow-up |
| --- | --- | --- | --- |
| P1 | Inventory runtime/model/native/browser/font/converter assets; measure byte sizes and compression with hashes. Produce installed/installer lower bounds and list every absent asset. Do not count development dependencies or duplicate model formats as mandatory. | #2/#3 | #7 #23 #32 #38 |
| P2 | Build unchanged retained Next standalone and Express in sanitized copies; reproduce failures, apply only measured necessary fixes with explicit patches; test Electron utilityProcess or pinned bundled Node, loopback readiness, dynamic routes/locales, sockets/streams, full UI assets and cleanup. Distinguish module/HTTP startup from backend-ready/interactive UI. | P1 first measurements | #11 #15 #28 #39 #40 |
| P3 | Disposable per-user native PostgreSQL without pgvector: review all 20 migration hashes and vector-dependent steps, prove relational/bootstrap/seeds/SQL CRUD/restart persistence/isolated stop; evaluate extension-free retained text-vector storage/ranking with parity and scale evidence. Preserve data/history; no unreviewed vector migration edits. | P2 API build; native binaries available | #29 #30 #33 #40 |
| P4 | Pinned CPU Python/runtime/model offline with fresh user paths: single/batch/PDF vectors and actual API consumer shape, model revision/cache state, startup/steady/processing memory. Record existing batch 500 honestly. No first-run asset download. | P1 inventory; P2 supervision | #8 #21 #32 #38 #44 |
| P5 | Native DOC/DOCX/TXT conversion, URL→PDF/browser reuse and retained PDF/editor/media/font/library resources; genuine fixtures/fidelity. Exclude deferred Whisper/tiny speech model and speech-only FFmpeg; prove any retained non-STT FFmpeg need separately. | P1; component manifests | #21 #23 #32 #38 |
| P6 | Native packaged OS/CPU matrix: Windows 10 22H2 and Windows 11 x64 NSIS; macOS 13+ x64 and ARM64 DMGs; Ubuntu 22.04 and Debian 12 x64 deb plus compatible AppImage. Clean host with no developer tools; checksums/native ABI/dynamic libraries. Cross-builds never count as native execution. | P2–P5 component integration | #22 #23 #24 #26 #38 |
| P7 | Aggregate app-owned process memory/CPU, launch/readiness and processing peaks; cold/warm method on minimum/recommended hardware; loopback/Host/Origin/session/secret checks; data-safe restart/upgrade/backup/uninstall keep/delete. Record conditional ADR, options and any budget failures without changing contract. | P1–P6 evidence | #25 #28 #31 #34 #35 #36 #37 |

- [ ] P1 complete resource manifest and measured complete installer/application footprint.
- [ ] P2 retained Next/Express/Electron production process proof.
- [ ] P3 clean native local DB/bootstrap/persistence proof.
- [ ] P4 bundled offline CPU Python/model proof.
- [ ] P5 complete conversion/media native resources proof.
- [ ] P6 every approved native platform/CPU packaged proof.
- [ ] P7 representative resource/security/data lifecycle measurements and accepted ADR.

## Evidence rules

Use disposable `.runs/` and `.downloads/` below this directory, excluded from Git. Keep scripts, sanitized logs, manifests and reports outside them. Source repositories, real dotenv files, registry auth configuration, credentials, user data and production databases must not enter proof copies. Child processes use a small environment allowlist and explicit loopback test configuration. Inventory may read approved cache assets by path; existing cache availability is not proof that an installer supplies them.

Record logical file bytes and MiB (2^20) as well as decimal MB (10^6). The contract says MB: do not silently reinterpret it as MiB; report both. A compressed subset is not an NSIS installer measurement. Unknown resources remain unknown, not zero. A development environment size is evidence about that environment only; a component lower bound must identify exactly which files are genuinely required by that candidate.

No macOS or Linux native host is currently attached to this Windows workspace. Native execution on those platforms remains pending. The current Windows host also does not establish Windows 10 or minimum-device compliance.
