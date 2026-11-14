# Windows Redis research and decision

2026-11-14. **Decision made: replace the desktop Redis service with PostgreSQL-backed durable state and a bounded in-process cache for disposable values. Application migration is not implemented by this research.** Authority and superseded restriction: [scope amendment](../v1-scope-2026-11-14-desktop-state.md). Windows 10 22H2 x64 and Windows 11 x64 remain required; macOS/Linux are ignored for this task.

## Why this choice

Dozu already needs bundled PostgreSQL. Adding another server, its native runtime/dependencies, license provisioning, backup/upgrade format and supervisor process is avoidable for the approved one-authoritative-host desktop topology. BullMQ's current [PostgreSQL backend](https://docs.bullmq.io/guide/postgresql) retains Queue/Worker/QueueEvents APIs. The exact published 6.7.6 package actually exports `withBackend`, `createPostgresBackend` and `runMigrations`; this was verified from downloaded package code and executed against the bundled Windows PostgreSQL. The app currently pins 5.49.1, so this is a tested upgrade candidate, not an already-available feature in the app.

Redis currently stores more than disposable cache. [Source audit](consumer-audit.json) identifies queues/retries/status/events, result mappings, feature/provider counters, socket sets and legacy frequency helpers. **Schedule edits currently write only Redis and have a database TODO.** Blind memory-only replacement would lose those edits. Feature-usage writes are currently asynchronous; the replacement must make PostgreSQL authoritative and atomic rather than preserving that race.

| Option | Evidence | Decision |
| --- | --- | --- |
| Existing Redis / Memurai | [Memurai license configuration](https://docs.memurai.com/en/config-license) requires an appropriate license file; [developer edition](https://www.memurai.com/faq) is for development/testing. Production/OEM redistribution entitlement was not obtained. | Do not add a commercial runtime dependency to solve a service we can eliminate. This is a product/packaging choice, not a claim that licensed Memurai cannot work. |
| Microsoft Garnet 2.2.12 | Official Microsoft release and digest verified. Windows archive downloaded (26,426,802 bytes); `GarnetServer.exe --help` exits 2147516566 because it requires .NET 10 and this host has only .NET 8. [Probe](garnet-runtime-probe.json). Garnet's [compatibility documentation](https://microsoft.github.io/garnet/docs/welcome/compatibility) requires application-specific validation. | Not selected: adds app-local .NET provisioning or a new source-published package plus queue-compatibility/persistence proof. No .NET runtime was installed. Startup failure does **not** prove Redis-protocol incompatibility; its BullMQ compatibility remains untested. |
| Community Redis Windows ports | The examined [redis-windows project](https://github.com/redis-windows/redis-windows) uses MSYS2/Cygwin and recommends local development, not production. Its wrapper license does not cover upstream Redis or bundled runtime obligations. | Not selected: extra port/toolchain/native provenance and support obligations. No abandoned Redis 5 binary, Docker or WSL fallback is introduced. |
| Valkey | [Official Windows documentation](https://valkey.io/topics/installation/) does not offer supported native Windows deployment; it points to WSL for development. | Does not meet the no-WSL/self-contained Windows requirement as an official supported binary path. |
| pg-boss 12.38.2 | Official [project](https://github.com/timgit/pg-boss), MIT package metadata; current Node requirement fits this build baseline. | Viable alternative but not selected: introduces another queue API when BullMQ's current PostgreSQL backend already passes the needed initial proof. Not runtime-tested here. |
| PostgreSQL + BullMQ 6.7.6 + bounded memory cache | Exact isolated package lock, real Windows cluster startup, actual queue operations and restart durability; 12 checks passed. | **Selected desktop integration path.** No additional native server/runtime is needed. Production app migration, performance and clean-target gates remain open. |

## Actual proof and limits

[Native run](postgres-native-probe.json), [before-restart checks](postgres-before.json), [after-restart checks](postgres-after.json), [actual jobs/events/tables](postgres-observed.json). Exact evaluation registry metadata and integrity values are in [candidate-metadata.json](candidate-metadata.json); the complete isolated dependency lock is [evaluation-package-lock.json](evaluation-package-lock.json). Lifecycle install scripts were disabled and application lockfiles were not modified.

The downloaded standalone Node 22.22.0 runs BullMQ 6.7.6 and pg 8.14.1 against the previously hashed EDB PostgreSQL 17.12-1 binaries. A new test cluster uses SCRAM password authentication and only numeric loopback; generated credentials never appear in the evidence/command output. It uses fresh schemas and synthetic probe jobs/counters, not application migrations, user records or external provider doubles. It applies actual BullMQ SQL migrations explicitly and repeats them. Twelve passing checks cover:

1. Explicit migrations in both before/after phases are repeatable (two checks).
2. Pending job creation without a worker.
3. Forty concurrent durable counter increments with no lost update.
4. Timestamp-based exclusion of an expired result-cache entry.
5. Actual stop/start of PostgreSQL preserves pending job, counter and JSON result data.
6. Worker consumes that pending job and returns its actual computed result.
7. First-attempt failure retries with exponential backoff and then succeeds.
8. A delayed job waits before execution.
9. Reusing an existing job ID does not execute it again.
10. Exhausted attempts retain failure state, reason and attempt count.
11. QueueEvents delivers actual progress and completion events.

Both clients/workers and the owned database cluster were stopped; `postmaster.pid` was absent. The final seven orchestration phases all exited 0. This is Windows 11 developer-host component evidence using ASCII data paths, not Windows 10, a clean/minimum machine, crash/power-loss/idempotent-mutation proof, all BullMQ features, measured whole-app footprint/memory, or integrated application parity. Restart is a genuine database stop/start, but it is **not** a forced-crash/active-job recovery test. Result/counter SQL is a storage proof, not a deployed application schema. No representative throughput comparison was performed.

Two failures stay visible. [Unicode-path attempt](postgres-unicode-path-probe.json): `initdb` could not open a password file containing Vietnamese characters; #34/#38 must solve tool/data path handling. Subsequent ASCII success does not pass that gate. [Sandbox bootstrap](postgres-sandbox-bootstrap.json) timed out; the successful run was outside that sandbox. An earlier outside-sandbox launcher [timed out waiting for inherited output-pipe EOF](postgres-launcher-pipe-failure.json) despite a ready server; using regular file-backed logs fixed it. The affected owned cluster was explicitly stopped before retrying. #28 should retain this Windows daemon-launcher lesson.

## Selected boundaries and migration work packages

These are executable work packages for existing #29/#30/#28/#34/#48, not claims those issues are done. #30 remains its existing XL/waiting umbrella until its implementation prerequisites/work breakdown are addressed; no owner or completed criterion is invented.

| Package | Concrete changes and acceptance |
| --- | --- |
| **1. Desktop queue/profile boundary — next** | Adapt `apps/api/src/libs/bullmq/bullmq.ts` behind an explicit desktop/website factory. Desktop selects `withBackend(createPostgresBackend)` and a bounded connection config; website retains Redis. Lazy-load profile dependencies so desktop startup never constructs ioredis or Lambda clients. Pin/review the BullMQ upgrade and test actual compiled types/API call sites before changing app locks. Preserve `getJob/getState`, progress/results, delayed/priority/retry/removal semantics. |
| **2. Reviewed database state/migrations** | #29 supplies a real per-user cluster and application migration chain. Add reviewed schema/versioned BullMQ migrations once per bootstrap; use a dedicated bounded queue pool/search path and account for LISTEN connections. PostgreSQL schema downgrades are not supported by this backend: backups and compatible binary/schema version guards are required. Persist schedule edits, job/result mappings, corpus statistics where actually used and atomic quota counters with owner/topic/period isolation. Existing data must be imported/drained deliberately, never dropped because it was formerly in Redis. |
| **3. Cache and presence adapters** | Bounded TTL/size process cache for regenerated schedule reads and disposable markers; Map/Set for live sockets and same-host event fan-out. Treat presence as reconstructible on reconnect. Retain durable provider quota windows and data mutations in PostgreSQL. A separate worker process requires explicit IPC or PostgreSQL LISTEN/NOTIFY; do not assume EventEmitter crosses process boundaries. No fake-success fallback. |
| **4. Consumer parity and failure tests** | Exercise actual generation/status/SSE paths, schedule edits across restart, concurrent quotas, cooldowns, socket reconnect/fan-out and retained recommendations. Prove bounded cache eviction/expiry, no token/key/cross-user leakage, cancellation/priorities/schedulers, stalled/active-job recovery and idempotent application writes. Review [BullMQ v5→v6 migration](https://docs.bullmq.io/guide/migrations/migrate-from-v5-to-v6), including persisted repeatable jobs and website/Lambda compatibility; an import search alone cannot certify existing data. |
| **5. Windows release gate** | Remove desktop Redis artifacts only after migrated production import closure passes. Replace the binary-acquisition gate with proof of no Redis socket/process/runtime download, final component hashes/licenses, migrated state compatibility, Unicode/read-only installation, crash/backup/restore and clean Windows 10/11 launch. #38 and all other ACs remain unchecked until their actual evidence is complete. |

Other architecture remains fixed: PostgreSQL retained without pgvector, required MiniLM multilingual CPU/384 vectors and genuine PDF/YouTube transcript references, all UI/pages, optional real internet providers, LAN classrooms, no central Dozu backend/cloud database/sync, and no STT/SMTP/payment execution.

## Reproduce

Build-host actions only, from repository root; use native Windows CPython 3.13 if `python` resolves to MSYS. The previous #38 download/extraction and standalone Node stage must exist. Never run these acquisition/install commands on an end user's first launch.

```powershell
python planning/windows-cache/acquire.py
python planning/windows-cache/prepare_evaluation.py
python planning/windows-cache/run_postgres.py
```

`acquire.py` inspects current registry metadata for comparison; the evaluated exact versions are pinned by the evaluation package/lock and recorded results. Reproduction should install the recorded lock via `npm ci --ignore-scripts` rather than repin transitive dependencies. The test cluster is always a fresh directory; no existing PostgreSQL service or application data root is used. The source audit and proof are sufficient to select the strategy, not to claim the application has been converted.
