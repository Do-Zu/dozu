# #7 foundation completion and desktop handoff

2026-11-13. The user explicitly authorized finishing this ticket, separating work needed at later desktop steps into other issues, and moving forward. This supersedes the earlier decision to leave #7 open with overlapping build/runtime/release acceptance.

#7 is now scoped to the **measured JavaScript build-tooling foundation**. Its five revised criteria cover the implemented pins/preflight, portable primitives and measured path/build fixes, root developer/website packaging commands, bounded validation with honest failures, and a complete transfer of later release proof. The previous five broad criteria are preserved verbatim in `original-acceptance.json`/`issues-before.json`, and their unpassed portions remain mandatory desktop delivery work. No old native/full-stack/installer criterion is asserted to have passed.

Implementation is committed at `8e7b7d134ec450ecd0244ab8deaee3d67b9379bb`, verified against live GitHub `dev`. The checkout was clean before this tracking/documentation change. Relevant commits are `33334e4` tooling, `17243ca` email/local URL, `f225d0c` follow-up tracking and `8e7b7d1` payment exclusion. This is source evidence, not a deployment or native installer result.

The toolchain/workspace checks, both compiled-module boundary suites and payment scope verification were rerun successfully. Existing committed receipts record frozen offline install, API/Next production builds, root website packaging, 22 contained links, 1,239 alias resolutions, data/config/ZIP component checks and 13 website HTTP/payload/asset samples. The runtime unit tests use explicit repository/provider/query doubles; the auth unit test uses real scrypt. API lint retains 92 errors/139 warnings, and full backend readiness remains unpassed against the deliberately unavailable DB/Redis fixture. No broad test was relabeled passing.

## Tracking transition

- #7: close completed for the revised foundation scope; Project Done. Only its measured JavaScript foundation is completed. Its prerequisite becomes completed #6; historical #4 is removed from this narrow task's prerequisite field, with the reason documented in the issue. #4/#45 states and evidence remain untouched.
- #48/#49: remain open with their existing labels, priorities, complexities and assignments; actual parent moves from #7 to open roadmap #1. They are independent mandatory follow-ups, not unfinished subissues counted as part of #7's completed foundation.
- #38: becomes Ready/Todo because its actual foundation prerequisite #7 is complete. Its native/runtime acceptance boxes remain unchecked. No #7→#38→#7 dependency is created. Final shipped artifact versions still need #48's independent security review.
- #1: stays In Progress, preserves its owner/fields, checks only the revised #7 foundation in the delivery list and retains unchecked #48/#49 gates plus every other desktop acceptance obligation.

No extra duplicate issues are needed. #48 owns supported framework/security validation; #49 native build/script proof; #38/#8/#32 shipped runtime/ABI/model/resources; #40/#28/#29/#34/#15 startup/migrations/ownership/installed paths; #23/#33/#22/#46/#47 installers/clean first run/native release proof; #14/#16 real accounts/study integration; #10 full CI/lint/test validation. These remain desktop release gates. Existing #45's closed/unchecked state is not Windows certification; #22 retains that gate.

## Next executable step

**#38 — assemble verified per-platform runtimes, binaries and licenses.** Begin with candidate artifact/strategy inventory, exact versions/hashes/architectures, redistribution licenses and native library closure; include the retained Redis runtime. No owner/start is invented by setting Ready. Do not reintroduce SMTP, PayOS, STT-only resources or pgvector; retain required PDF/YouTube text embeddings, PostgreSQL, other UI/website features and LAN scope. Native compatibility, size/startup/RAM/lifecycle and clean end-user installation still require direct evidence.

`prepare.py` snapshots current bodies, original criteria, metadata, live source SHA and prepared changes. `publish.py` applies only the declared transition and verifies issue states/criteria/dependencies, real parent links, Project values and preservation of unrelated ownership/fields. `verification.json` and final snapshots are the read-back record. Earlier reports/status snapshots remain historical, not current instructions. The source publication manifest is updated to preserve the same scoped acceptance/dependency split on later publication; no bulk issue sync is run.

No application source, package version, existing user data, credentials, original checkout, database migration or deployment changes in this closure step. No automatic full-stack/native completion is claimed. These local documentation/manifest edits are reviewable separately from the already committed implementation.
