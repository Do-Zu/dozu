# Agreed v1 desktop support contract — Task #2

**Windows desktop state decision — 2026-11-14:** The user authorized researching and choosing Redis removal/replacement. [The selected path](v1-scope-2026-11-14-desktop-state.md) uses the already-bundled PostgreSQL for durable jobs/state plus bounded process-local disposable caching. This supersedes older desktop Redis-retention wording below; the website Redis profile is preserved. Research/component proof is complete, while the application migration and native release acceptance remain unimplemented/unpassed. #38 is Windows-only per its later scope; other platform inventory is not a blocker for that task.

Initially approved on 2026-11-10; **hardware and resource targets revised by explicit user acceptance on 2026-11-14**. The [accepted resource amendment](resource-contract-2026-11-14.md) supersedes the original tight budgets and permits completing initial desktop integration with the existing pinned CPU model before later optimization. These are agreed engineering targets, not evidence of supported hardware or measured full-stack compliance. Further changes require benchmark evidence and explicit agreement.

The **2026-11-11** [scope amendment](v1-scope-2026-11-11.md) removes speech-to-text, retains PostgreSQL and defers pgvector. Text embeddings for PDF/YouTube reference retrieval remain required. The 2026-11-14 approval makes smaller-runtime optimization follow-up work rather than a prerequisite to completing the initial baseline-model integration. [Outgoing email is excluded; Redis stays](v1-scope-2026-11-13-email.md), and [payment execution is excluded](v1-scope-2026-11-13-payments.md). OS/architecture/distribution requirements below are unchanged.

## OS, architecture and distribution

| Platform | Required v1 baseline | CPU | Installer |
| --- | --- | --- | --- |
| Windows | Windows 10 22H2, legacy compatibility; Windows 11, primary | x86-64 | NSIS .exe primary; .msi optional for enterprise |
| macOS | macOS 13 Ventura or later | Intel x86-64 and Apple Silicon ARM64 | Signed and notarized .dmg for each architecture |
| Linux | Ubuntu 22.04 LTS and Debian 12 minimum tested baselines; Ubuntu 24.04 LTS or newer recommended | x86-64 | .deb for Ubuntu/Debian; additional .AppImage where compatible |

32-bit systems are unsupported. Windows ARM64 and Linux ARM64 may be added only after native dependency validation; they are not current required v1 targets. Later recommended releases still require compatibility evidence; the wording above does not assert tests have run.

## Hardware

| Configuration | CPU | System RAM | Free disk | Display / storage |
| --- | --- | --- | --- | --- |
| Minimum | 64-bit, 4 physical cores | 8 GB | 10 GB free before installation | 1366 × 768; integrated graphics; SSD required |
| Recommended | 6–8 cores | 16 GB | 20 GB free | 1920 × 1080; SSD |

A dedicated GPU is not required; retained embeddings run on CPU. The 8 GB/four-core minimum is an accepted validation target and is not yet a verified support claim. Use one active user and at most one ingestion/embedding job at a time for minimum-device acceptance, with bounded batches/caches and controlled background concurrency. Concurrent LAN hosts and large libraries require separate capacity measurements; their workflows remain in scope. The earlier 4 GB/HDD minimum and 4 GB low-resource acceptance target are superseded. Preserve functionality while optimizing later.

## Performance and disk targets

| Production-build metric | Minimum-spec device | Recommended device |
| --- | --- | --- |
| Cold launch to interactive UI | ≤ 15 s | ≤ 15 s |
| Warm launch to interactive UI | ≤ 5 s | ≤ 3 s |
| Complete local backend/model ready | ≤ 30 s | ≤ 30 s |
| Normal combined application memory | ≤ 2 GB | ≤ 2 GB |
| Combined peak during one ingestion/embedding job | ≤ 3 GB | ≤ 3 GB |

Installer download target: **≤ 1.5 GB**. Installed application target: **≤ 3 GB**, including all bundled frontend/backend/database/cache runtimes, model and processing resources, attribution and verification metadata. Require **at least 10 GB free before installation**; 20 GB is recommended. Imported documents/media, growing databases and user backups require additional storage. Account for every shipped runtime/model/asset; no first-run runtime/model download or relabeling installed resources as user data. Installer/upgrade/restore preflight must calculate actual staging/data needs; initial free-space allowances are not unlimited upgrade or backup guarantees. GB/MB values use decimal bytes in evidence comparisons.

Use production builds and documented repeatable workloads on actual 8 GB/four-core SSD minimum configurations. Document OS/CPU/RAM/storage, dataset/media sizes, model revision, cache state, concurrency, network state and measurement method. Report all app-owned processes, including Electron, Next, Express, PostgreSQL, Redis and running embedding/conversion workers, with shared-memory accounting documented. Separate interactive-UI and complete backend/model readiness; an interactive shell is not proof the services/model are ready. Measure normal, background and one-job processing peaks against the 2 GB/3 GB combined targets. Warm-UI targets remain ≤5 s minimum/≤3 s recommended because the user did not revise them. No numerical CPU utilization cap or fixed peak upgrade-space budget was agreed; measure them and validate disk preflight.

## Local runtime and data lifecycle

Backend and primary data storage run locally. Internet is permitted for genuine Google authentication, YouTube and other retained external services; classroom v1 is LAN. Outgoing email, payment execution and speech-to-text remain excluded by the approved amendments. No externally hosted application backend is required for core local functionality. Bundle/provision required dependencies through installation; no manual Node, Python, database, Redis, Docker, WSL or developer tooling. Retain the self-contained pinned baseline model/runtime requirement.

PostgreSQL is retained by the user's 2026-11-11 decision; **pgvector is deferred from v1**. #4/#29 must prove relational migrations, PostgreSQL-specific SQL/JSONB, seeds, repository contracts and persistence without requiring the extension. Existing vector-dependent schema/queries need a reviewed compatibility path for retained PDF/YouTube reference retrieval; ordinary PostgreSQL storage plus application-side ranking is an unproven candidate. Preserve migration/data history and a future extension path. No database replacement is authorized.

Upgrades preserve data. Uninstall retains the earlier explicit keep-data/delete-all-app-owned-data choice, with reliable removal of app-owned databases, caches, logs and local data while protecting unrelated files. All managed data stays on the device unless the feature explicitly requires external communication. LAN participants access the user-owned host's authoritative data; no cloud database/sync is introduced.

## Evidence gates

#38/#8/#23 and native #22/#46/#47 must prove the required native OS/CPU combinations and revised resource budgets. #4/#45's closed historical metadata is not passing release evidence. #21/#32 include retained media/conversion/text-embedding/font/browser resources; exclude STT/pgvector-only resources, and require a retained non-STT consumer for FFmpeg. Electron + Next + Express + PostgreSQL + Redis + embedding/model and processing resources have not yet been shown to meet the complete revised budgets. The explicit 2026-11-14 approval changes the requirements; it does not change old measured results or pass implementation ACs.

#22/#23/#25/#28/#33/#35/#36 validate clean installation, startup/readiness, normal/peak memory and core functionality, dependency compatibility, bounded concurrency, restart/recovery, upgrades/backup/restore and uninstall on the revised minimum configurations. #34's final paths/ownership/read-only installation and #38's native dependency closure remain required. Signing/distribution remain #24/#26. Release compliance requires actual evidence; see the [AC review](resource-amendment-2026-11-14/acceptance-review.md).
