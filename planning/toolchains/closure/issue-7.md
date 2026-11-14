<!-- dozu-tracking:start -->
## Work tracking
Priority P0; complexity M — portable JavaScript build tooling and measured developer entry points. Preserve the existing assignee. Full desktop/native release acceptance is tracked separately below.
<!-- dozu-tracking:end -->

## Outcome
Provide the committed JavaScript tooling foundation needed to continue the desktop migration: measured version pins, portable command/path primitives, root developer/build/website-package entry points and explicit validation limits.

## Authorized scope split — 2026-11-13
The user explicitly directed completing this ticket and transferring work that belongs to later desktop steps into separate issues so migration can proceed. This replaces #7's previous overlapping build/runtime/release scope with the completed foundation below. **Transferred work remains mandatory for the desktop release; it is not passed, waived or removed from v1 by closing #7.**

The original acceptance text and pre-split issue are preserved in `planning/toolchains/closure/` and earlier GitHub comments. Their remaining proof is mapped below. #4's contradictory closed/completed metadata is not used as proof; it is historical context rather than a prerequisite for this independent tooling foundation. #6 is the completed prerequisite. #4/#45 remain untouched.

## Acceptance criteria — completed tooling foundation
- [x] Pin and check the measured JavaScript build baseline: Node 22.22.0, pnpm 10.28.2, Turbo 2.5.8 and TypeScript 5.8.3; align version files and document version/security policy without claiming current release security approval.
- [x] Inventory imported script assumptions and fix demonstrated environment/cwd/build-output defects using portable primitives; validate compiled API alias resolution and explicit writable-data/config-relative path components on the available Windows developer host, with native target verification transferred to #49.
- [x] Provide root development, individual-app, production-start, build and standalone-website packaging commands with explicit prerequisites and artifact boundaries; distinguish developer commands from the self-contained end-user installers owned by #23/#33.
- [x] Record frozen-install, API/Next production-build, website-package and restricted-filesystem component/HTTP evidence, including inherited lint/startup failures and exact native/full-stack limits; do not suppress failures or report mocked/partial checks as integrated desktop proof.
- [x] Separate framework/security upgrades, shipped runtime/ABI resources, real migrations/startup and native/installer gates into the open delivery issues below, preserve approved scope and remove the circular expectation that downstream runtime proof must complete before this tooling foundation closes.

## Source and validation evidence
Source is committed and the remote `dev` SHA was verified as `8e7b7d134ec450ecd0244ab8deaee3d67b9379bb`. Relevant commits: `33334e4` tooling, `17243ca` email/local URL, `f225d0c` follow-up tracking, `8e7b7d1` payment exclusion. This is not a new deployment or installer certification.

- Toolchain/workspace checks pass. Frozen offline installation, actual API/Next production builds and root website packaging pass; 22 standalone links are relative and contained. The native proof is Windows developer-host evidence only.
- 1,239 compiled alias references resolve; disposable data-root/config-path component checks and the Lambda ZIP metacharacter fixture pass. The current website probe passes 13 actual HTTP/payload/asset/font checks with writes/original-workspace reads denied and the owned server stopped. Authentication/browser/full-feature interaction is not implied.
- Email/payment compiled-module boundary tests pass with explicit repository/provider/query doubles. Real scrypt hashing is used for the account unit checks; real DB/session/financial/native integration remains unpassed.
- API lint retains 92 errors/139 warnings with zero added signatures at the final implementation checkpoint; changed payment UI/loader lint is clean. Full existing lint/Jest failures stay visible for #10/#40/#48.
- The real scrubbed API probe gets past email/PayOS initialization but reaches its ten-second bound against deliberately unavailable DB/Redis; `backendReady` is false. No real migrations or merchant/provider transactions ran.

Reviewable evidence: `planning/toolchains/README.md`, `planning/email-removal/README.md`, `planning/payment-removal/README.md`, their scripts/logs/JSON and the final closure verification. Toolchain/workspace and both compiled boundary suites were rerun successfully at the committed source before closure. Current build/runtime pins are measured inputs, not security approval.

## Original broad criteria — unpassed portions transferred
| Original criterion (historical wording) | Remaining evidence / delivery owner |
| --- | --- |
| Make scripts/environment/path handling portable across all three OSes. | **#49** native build/script matrix; full packaged native/runtime behavior under #22/#46/#47. Windows developer proof does not pass these targets. |
| Pin build toolchain/runtime versions and verify Electron/native-module ABI or standalone Node compatibility. | **#38** shipped Electron/Node strategy, binary hashes/native ABI/library/license manifests; **#8** Python/model locks and **#32** processing resources. Host Node/SWC smoke is not bundled-stack ABI proof. |
| Separate necessary framework/security upgrades from source movement with independent validation. | **#48** selects an exact supported/security-reviewed target and validates it independently. No framework upgrade was performed by #7. |
| Validate API aliases, production startup, migration paths, installed-resource paths and read-only installation behavior. | Alias/config/data-path components delivered here. **#40/#28** full API/readiness/supervision, **#29** real migration/bootstrap safety, **#34/#15** per-user ownership/installed-resource/OS ACL integration, **#32/#38** assembly remain open. |
| Provide root development and packaging commands; end users require no developer tools. | Developer/website commands delivered here. **#23/#33** self-contained installer/clean first-run/no-user-Node-Python-DB-Redis-Docker-WSL evidence remains open. |

Additional integration owners: #14 actual accounts/sessions, #16 end-to-end study flow, #10 inherited CI/lint/test validation, and #22 full feature/platform/resource/lifecycle proof. Existing #45 is closed with unchecked criteria and does not certify Windows; #22 retains that release gate. These are existing issues, not duplicated tasks.

#48/#49 remain open and move to roadmap #1 as independent follow-ups rather than unfinished subissues of this completed foundation. #38 can start after this foundation closes; its original #7 prerequisite no longer creates a #7→#38→#7 cycle. Final shipped runtime versions still need the #48 security review. No native host, full stack, migration, installer, budget or lifecycle gate becomes passing merely because #7 closes.

## Approved scope
Retain website/all other UI, local-first optional internet, PostgreSQL retained/pgvector deferred, required PDF/YouTube text embeddings and authoritative LAN classrooms. Redis remains; the older #30 replacement plan is not authorization to remove it. Outgoing email/local STT/payment execution are excluded per explicit user amendments; preserve associated history/data/pages and honest unavailable states. No paid entitlements or provider success are fabricated.

<!-- dozu-roadmap:TOOLCHAINS -->
Phase: 1 Foundation | Priority: P0
Parent roadmap: https://github.com/Do-Zu/dozu/issues/1

## Dependencies
- #6 — completed workspace/build graph: https://github.com/Do-Zu/dozu/issues/6

Historical #4 architecture proof is not treated as completed support and is not a dependency of this narrowed JavaScript foundation. Its unresolved delivery gates remain on the issues above and #1.
