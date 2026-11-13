<!-- dozu-toolchains-followup-ledger:start -->
## Completion review and executable follow-ups — 2026-11-13

The user requested a completion check and a separate issue for each unfinished task that can be resolved later. **The original acceptance criteria above are not yet passed; #7 remains open/In Progress.** Creating or linking follow-ups is not completion evidence, and the original criteria are not rewritten or checked merely to close this ticket.

Implemented evidence is in the [tooling checkpoint](https://github.com/Do-Zu/dozu/issues/7#issuecomment-6845196827) and [email/URL follow-up](https://github.com/Do-Zu/dozu/issues/7#issuecomment-6845746927). Work remains local/uncommitted in the current checkout; a source-review/merge result is not claimed. API and Next builds, website packaging, compiled aliases, restricted component writes and eleven website HTTP checks pass. API lint retains 92 errors/143 warnings with zero added diagnostic signatures; changed UI files also have zero added signatures. These are partial results with stated boundaries.

### Every remaining gap has an issue

| Original #7 criterion / unfinished task | Executable owner issue(s) | Current evidence limit |
| --- | --- | --- |
| Native portability of development/build/package scripts, env handling and paths | **New #49** | Windows developer-host checks only; no complete approved native-host matrix |
| Supported framework/security upgrade independently validated after source movement | **New #48** | Measured pins preserved; Next 14 baseline is not a security approval or completed upgrade |
| Shipped Electron/standalone Node strategy, version/hash pins, complete native ABI/library closure | #38 | Host Node ABI 127/Node-API 10 and Windows SWC load only; not bundled Electron/native-stack acceptance |
| Locked portable Python/native wheels/model/tokenizer and offline retained text-embedding contracts | #8, with resources in #32/#38 | Mutable image/unpinned Python inputs and unverified bundled assets remain |
| API production startup/readiness without optional merchant/cloud keys | #40, supervised lifecycle #28 | Real scrubbed entrypoint now fails at eager PayOS/PaymentBase configuration; email/URL blocker is removed |
| Real extension-free PostgreSQL migrations/bootstrap/seed/data preservation | #29 | Only config-path relocation checked; no migration was applied by #7 |
| Installed-resource ownership, writable per-user roots and genuinely read-only installed stack | #34 and #15, assembled assets #32/#38 | Explicit DOZU_DATA_DIR/component writes and read-only website sampling only; no full OS ACL/packaged proof |
| End users need no Node/Python/database/Redis/Docker/WSL/developer setup; full desktop package commands | #23, clean first boot #33 | Root commands currently build JavaScript and the standalone website, not a self-contained desktop installer |
| Full native install/runtime/workflow/resource/lifecycle validation | #22 with #46/#47 and #23/#33 | All approved native target gates remain unpassed. #45 is closed with unchecked criteria, so its closed state is not Windows certification; #22 retains that gate |
| Real local account/session/restart validation after explicit email removal | #14, exercised through #16/#22 | Compiled-module auth tests use repository/provider doubles; no real PostgreSQL/session/security certification |

Existing issues are reused rather than duplicated. #48 and #49 are new children of #7, with written acceptance criteria and Project #6 items. They do not depend on #7 being closed: #48 can use completed #6, while #49's final run waits for #48's selected baseline and native hosts. Ownership/assignees are not invented.

The table is a responsibility map, not new reverse prerequisite edges. #1 already coordinates the dependency transition: in particular, #38 currently depends on #7's tooling foundation, so do not create a #7→#38→#7 completion cycle. A reviewed distinction between the delivered tooling milestone and downstream release proofs is required before administrative closure can be considered; no dependency field is silently rewritten here. #4's contradictory closed/completed/checked state versus NOT PLANNED closure remains historical and does not prove full support. #4/#45 are not reopened or closed by this update.

### Current scope remains authoritative
Outgoing email and local STT are excluded; PostgreSQL is retained and pgvector deferred; required PDF/YouTube text embeddings, all website/UI pages and LAN classrooms remain. Payment execution is deferred under #41. The user explicitly said **skip Redis removal**; #30's older replacement plan is not authorization to implement replacement during these follow-ups. Redis remains in the current runtime and must be accounted for in packaging. Its alternatives are proposals only.

No full #7 criterion, native target, full-stack startup or installer gate is marked complete by this issue split.
<!-- dozu-toolchains-followup-ledger:end -->
