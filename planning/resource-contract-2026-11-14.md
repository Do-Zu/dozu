<!-- dozu-resource-contract-2026-11-14:start -->
## Accepted desktop resource contract — 2026-11-14

Authority: the user explicitly accepted the proposed larger initial-release hardware/resource targets in the #8 chat. This supersedes earlier 4 GB/dual-core/HDD, 250 MB installer, 750 MB installed, 700 MB/1 GB normal-memory, cold UI 10/5 s and backend-ready 8/4 s requirements wherever they appear below or in historical scope notes. OS versions, CPU architecture matrix, installer formats, feature/data/security/lifecycle obligations and deferred capabilities are unchanged. Requirements approval is not benchmark or release acceptance.

| Hardware | Minimum | Recommended |
| --- | --- | --- |
| CPU | 64-bit, 4 physical cores | 6–8 cores |
| System RAM | 8 GB | 16 GB |
| Storage | SSD; 10 GB free before installation | SSD; 20 GB free |
| Graphics | Integrated graphics; CPU inference | Dedicated GPU optional |
| Display | 1366 × 768 | 1920 × 1080 |

| Initial-release whole-application target | Limit |
| --- | --- |
| Installer download | ≤ 1.5 GB |
| Installed application, all bundled runtimes/model/resources included | ≤ 3 GB |
| Normal combined app memory | ≤ 2 GB RAM |
| Peak during one ingestion/embedding job | ≤ 3 GB RAM |
| Interactive UI after cold launch | ≤ 15 s |
| Complete local backend/model readiness | ≤ 30 s |

Memory includes Electron, Next, Express, PostgreSQL, Redis and running embedding/conversion workers. The existing warm-UI targets were not changed: ≤5 s on minimum and ≤3 s on recommended hardware. Imported documents/media, growing databases and user backups require additional disk. Installation/update/restore preflight must calculate actual staging and data requirements rather than assuming the initial free-space allowance covers unlimited data.

Keep the existing pinned multilingual CPU model for the initial integration path; smaller/quantized runtime optimization may follow later. ONNX is an evaluation candidate, not a release prerequisite or an approved model substitution. Preserve real semantic PDF/YouTube transcript references, the 384-dimensional API contract, English/Vietnamese behavior, local authority and genuine provider integrations. No STT, SMTP, payment execution or pgvector is restored by this amendment; Redis and PostgreSQL remain retained.

Minimum-hardware acceptance uses one active user with one ingestion job at a time; concurrent LAN hosting and large-library capacity require separate measured tests. Validate the complete application on actual 8 GB/four-core SSD hardware and every required native OS/architecture before advertising support. Component proof, larger allowances and approval do not pass installer, full-stack memory/startup, native dependency, file-path/ownership or lifecycle ACs.

Canonical requirements and evidence rules: [platform-support.md](https://github.com/Do-Zu/dozu/blob/dev/planning/platform-support.md). Prior measurements and closed issue histories remain historical evidence; no completed/cancelled issue is reopened or counted as release proof by this change.
<!-- dozu-resource-contract-2026-11-14:end -->
