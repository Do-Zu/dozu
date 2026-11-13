# Accepted hardware/resource revision and AC review — 2026-11-14

Authority: the user's explicit “I accepted, Update document and check any ACs” response to the proposed initial-release targets in the #8 chat. [Accepted contract](../resource-contract-2026-11-14.md), [canonical support requirements](../platform-support.md), [source-backed component evidence](../embedding-runtime/README.md).

## Requirements accepted

- [x] Minimum: 64-bit/four physical cores, 8 GB system RAM, SSD/10 GB free, integrated graphics and 1366 × 768 display.
- [x] Recommended: 6–8 cores, 16 GB RAM, SSD/20 GB free and 1920 × 1080 display; dedicated GPU optional.
- [x] Initial-release installer ≤1.5 GB and complete installed application ≤3 GB; all bundled resources count.
- [x] Combined app memory ≤2 GB normal and ≤3 GB peak during one ingestion/embedding job, including all owned services.
- [x] Cold UI ≤15 seconds and complete backend/model readiness ≤30 seconds. Existing warm UI ≤5/3 seconds was not revised.
- [x] Keep the existing pinned multilingual CPU baseline for initial integration; defer ONNX optimization without removing semantic-reference functionality or changing model/API contracts.

These are approved requirements. #2's existing “agree OS/CPU/installer/resource budgets” AC remains satisfied and its completed state is preserved. No new hardware/OS support is certified. The original 4 GB/HDD/250 MB/750 MB/700 MB constraints are superseded; measurements and closed/cancelled histories remain intact.

## Original #8 release criteria

| Criterion | Evidence reviewed | Result after resource approval |
| --- | --- | --- |
| 1. Complete Python/native package on every target, no user setup | Windows hash locks, embedded Python, native payload hashes; baseline still loads host msvcp140.dll | **Partial/open:** Microsoft runtime provisioning, clean target/native matrix and complete release resource assembly are absent. |
| 2. Bundle pinned model/tokenizer/config; preserve 384 values | Exact model revision and verified baseline CPU inference in an isolated Windows package | **Windows component verified; release AC open:** actual supported native installed artifacts remain unverified. |
| 3. Verified local paths and no Hub fallback | Fresh process caches, checksum validation, process-level non-loopback denial, missing/corrupt-model tests | **Windows component verified; release AC open:** final installed paths/read-only permissions and supported-target bootstrap still pending #34/#38. |
| 4. Real text/PDF/existing-transcript-text CPU behavior | 28 HTTP checks per representation, genuine extracted PDF text, supplied transcript text, small en/vi fixture | **Partial/open:** retained Express ingestion/repository/ranking and full native workflow acceptance are not demonstrated. ONNX equivalence is now optimization follow-up, not a baseline release prerequisite. |
| 5. Loopback lifecycle and authenticated user files | Local service/file credentials, path/URL failures, model readiness, exit-code and shutdown checks | **Partial/open:** final owner-root/permissions and actual #18/#28/#34 integration are missing. |

The [explicit Windows component checklist](issue-8-component-review.md) records seven verified checks with evidence and three remaining groups. It does not tick or narrow any original release AC, close #8 or imply macOS/Linux/Windows 10/minimum-device support. #8 remains In Progress. #38 remains Ready; #34 remains Waiting; the disputed #4 dependency is not resolved by accepting larger resources.

## Related delivery acceptance

| Owner | Reviewed effect | Still needs evidence |
| --- | --- | --- |
| #1 roadmap | Current accepted targets replace the older numeric proof expectation; product ACs remain unchecked | Complete retained application and all child release obligations. |
| #2 requirements | Existing budget-agreement AC stays checked; current hardware/performance tables are updated | No implementation or benchmark claim follows from requirements completion. |
| #22/#23/#26 | Use 8 GB/four-core SSD acceptance and the revised budgets | Full feature matrix, actual complete installers, native ABI/dependencies and distribution/lifecycle tests. |
| #28/#33/#34 | One-job minimum acceptance, actual staging/free-disk preflight and distinct UI/model readiness | Supervisor startup/recovery, ordinary-user clean install, owned paths/permissions/read-only install. |
| #25/#35/#36 | 10/20 GB initial free-space numbers do not promise arbitrary upgrade/backup capacity | Actual data/staging preflight, interrupted operations, preserve/restore and safe keep/delete behavior. |
| #38 | Baseline CPU model is allowed on the initial path; resource optimization can follow | Pin and provision Microsoft C++/other native libraries, licenses/security review and clean native targets. |
| #46/#47 | Replace the explicit old numeric measurement AC with the accepted limits; keep it unchecked | Native macOS Intel/ARM64 and Ubuntu/Debian evidence on the required configurations. |
| #4/#45 | Closed/cancelled metadata and historic measurements are preserved | They are not treated as new passing support evidence and are not reopened. |

No implementation AC is passed solely because its limit increased. Component installed size/ZIP/RAM/startup are not whole-application measurements. The existing 32+ GB developer host does not prove the 8 GB minimum. OS versions/architectures, feature/page inventory, local data authority, genuine providers, safety/security and lifecycle obligations remain unchanged. Redis and PostgreSQL stay; STT, SMTP/payment execution and pgvector remain excluded.

## Publication and preservation

`review_and_publish.py` prepares and applies only targeted issue-body revisions, verifies read-back, and checks that labels, state/reason, assignees, project status and explicit dependency sections stay unchanged. Only #8's related Project Blocker text is adjusted to remove the superseded size/optimization gate; a focused after snapshot records the result. Original issue-body/board snapshots are retained in the ignored `.runs` directory. No full backlog publisher/status synchronizer is run.

The existing manifest and other uncommitted #7 planning work are preserved. The backlog publisher prepends the accepted resource-contract fragment (and #8's bounded component review) at generation time, so later generation cannot reassert older limits as current without touching those unrelated local manifest changes. Historical local reports remain historical; current support/requirements and the #8 report link this amendment explicitly.
