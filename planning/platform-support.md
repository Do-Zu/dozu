# Agreed v1 desktop support contract — Task #2

Approved by the user on 2026-11-10. This is the initial v1 support contract and engineering target set, not evidence of compatibility or measured performance. If the selected framework or bundled backend cannot meet a target, provide benchmark evidence and an explicit recommendation before changing the agreement.

Scope amended by the user on **2026-11-11**: [speech-to-text removed from v1; PostgreSQL retained; pgvector deferred](v1-scope-2026-11-11.md). Text embeddings for PDF/YouTube reference retrieval remain relevant and require a smaller-runtime proof. Existing OS/hardware/resource budgets are unchanged.

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
| Minimum | 64-bit dual-core | 4 GB | 2 GB for installation and initial data | 1366 × 768; integrated graphics; HDD-compatible, SSD preferred |
| Recommended | 64-bit quad-core or better | 8 GB or more | 5 GB | 1920 × 1080; SSD |
| High performance | 6–8+ cores | 16 GB or more | Dataset/workload-dependent; no additional number specified | NVMe SSD; larger datasets and concurrent background workloads |

A dedicated GPU is not required for normal functionality. Provide a low-resource mode for 4 GB machines using efficient process management, lazy initialization, bounded caching and reduced background concurrency. Preserve functionality; do not achieve budgets by silently removing pages or required processing.

## Performance and disk targets

| Production-build metric | Minimum-spec device | Recommended device |
| --- | --- | --- |
| Cold launch to interactive UI | ≤ 10 s | ≤ 5 s |
| Warm launch to interactive UI | ≤ 5 s | ≤ 3 s |
| Local backend ready | ≤ 8 s | ≤ 4 s |
| Normal application memory, including backend and database | ≤ 700 MB | ≤ 1 GB |

Installer target: **≤ 250 MB**. Installed application target, including bundled backend: **≤ 750 MB**. Require **at least 2 GB free before installation**, covering installation and initial data. User-generated data and imported media may grow beyond the application footprint. Account for runtime/model/assets in the application footprint; do not hide them in a first-run download or call them user data to satisfy the budget.

Use production builds and documented repeatable workloads on minimum supported configurations. Document OS/CPU/RAM/storage, dataset/media sizes, model revision, cache state, concurrency, network state and measurement method. Report all resident app-owned processes, including Electron, Next, API, database and any running embedding/converter/transcription processes. Keep interactive-UI and backend-ready timings separate; an interactive shell is not proof the database/model is ready. Measure background and processing peaks as well as the agreed normal workload. No numerical CPU cap, conversion/embedding peak-memory cap or peak upgrade-space budget was supplied; measure and report them rather than inventing an agreement.

## Local runtime and data lifecycle

Backend and primary data storage run locally. Internet is permitted for genuine Google authentication, email, YouTube and other external services; classroom v1 is LAN, and payments are explicitly deferred/blocked under #41. No externally hosted application backend is required for core local functionality. Bundle/provision required dependencies through installation; no manual Node, Python, database, Docker, WSL or developer tooling. Retain the earlier self-contained baseline model/runtime requirement.

PostgreSQL is retained by the user's 2026-11-11 decision; **pgvector is deferred from v1**. #4/#29 must prove relational migrations, PostgreSQL-specific SQL/JSONB, seeds, repository contracts and persistence without requiring the extension. Existing vector-dependent schema/queries need a reviewed compatibility path for retained PDF/YouTube reference retrieval; ordinary PostgreSQL storage plus application-side ranking is an unproven candidate. Preserve migration/data history and a future extension path. No database replacement is authorized.

Upgrades preserve data. Uninstall retains the earlier explicit keep-data/delete-all-app-owned-data choice, with reliable removal of app-owned databases, caches, logs and local data while protecting unrelated files. All managed data stays on the device unless the feature explicitly requires external communication. LAN participants access the user-owned host's authoritative data; no cloud database/sync is introduced.

## Evidence gates

#4/#38 must prove each agreed native OS/CPU combination and resource budget; #21/#32 include resources required by retained media/conversion/text-embedding/font/browser workflows. Exclude deferred Whisper/speech-model/pgvector resources; FFmpeg requires a retained non-STT consumer. Electron + Next + Express + PostgreSQL + text-embedding/runtime and conversion resources have not yet been shown to fit these budgets. No target is relaxed based on that uncertainty.

#22/#23/#25/#33/#35/#36 validate clean installation, startup/readiness, memory/core functionality, dependency compatibility, low-resource mode, restart/recovery, upgrades/backup/restore and uninstall on the minimum configurations. Release compliance requires actual evidence. Signing/distribution remain #24/#26. A benchmark failure requires evidence and an explicit recommendation before changing this contract.
