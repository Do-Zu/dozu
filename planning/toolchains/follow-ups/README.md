# #7 completion review — 2026-11-13

**Superseded by the user's later scope decision:** [#7 foundation closure](../closure/README.md) completes only the delivered JavaScript tooling foundation, moves still-open #48/#49 to roadmap #1, and makes #38 Ready. The original broader proof stays unpassed on its delivery issues. The following open-parent/setup report and snapshots are historical; do not rerun its publisher against the completed foundation.

The user asked whether #7 could be Done and requested separate issues for work that must be resolved later. Its original acceptance criteria still lack native-host/full-runtime/installed-stack evidence, so **#7 remains open and In Progress**. No criterion was checked, waived or silently narrowed to close it. Current source work remains local/uncommitted.

Two missing executable tasks were created as actual #7 subissues and added to Project #6:

- [#48 — Framework/security baseline upgrade](https://github.com/Do-Zu/dozu/issues/48): Ready/P0/L; Project Todo. Independent exact-version selection and regression/security validation after source movement. No upgrade executed here.
- [#49 — Native portable-script validation](https://github.com/Do-Zu/dozu/issues/49): Waiting/P0/M; Project Todo. Explicit native Windows 10/11 x64, macOS 13+ x64/ARM64, Ubuntu 22.04/Debian 12 x64 build/script matrix; final run depends on #48, not parent #7 closure.

The existing issue responsibilities are reused, not duplicated: #38 shipped runtime/ABI manifests; #8 Python/model locks; #40 API profile/PayOS startup with #28 supervision; #29 migrations/bootstrap; #34/#15 data/resource/read-only installed behavior; #32 bundled resources; #23 self-contained installers; #33 clean first run; #22/#46/#47 complete native release evidence; #14 actual local-account/session integration. The exact acceptance-gap table is appended to #7 in `issue-7-addendum.md` and preserved in #7's source body in `planning/issues.json` to survive later generated-body publication. #40 received the concrete startup handoff in `backend-startup-handoff.md`.

#45 is closed with unchecked acceptance; it is not fresh Windows certification. #22 retains the full Windows release gate. #4's closed-state/closure-comment contradiction is not resolved by inference. Neither closed issue was reopened/closed, and none of their checkbox states was changed. Existing #7 labels, assignment, dependencies and Project custom fields were preserved.

The table maps responsibilities without adding reverse prerequisite edges. #1 still owns the reviewed transition between #7's delivered tooling milestone and downstream release proofs; #38 currently depends on #7, so requiring full #38 release proof as a reverse prerequisite would create a cycle. New #48/#49 never depend on #7 closure. This review does not silently modify existing dependency fields or treat closed/canceled proofs as completion.

Approved scope includes the user's email-removal amendment and clarification to **retain Redis**. Redis alternatives remain proposals; the old #30 replacement plan is not authorization to remove Redis in these tasks. No new email-delivery/Redis-replacement task was created.

`publish-followups.py` verifies the parent/child links, new Project fields, preserved existing #7 metadata and its five unchecked full criteria. `verification.json`, final issue snapshots and Project snapshots record the read-back. The first child-link request used an API parameter rejected with HTTP 422; the retry used the API's required `sub_issue_id`, and read-back verifies the actual result. No application code or test artifacts were changed by this tracking-only review.

The original 44-issue publication manifest is a historical inventory; #48/#49 are supplemental tasks recorded here with stable markers and live snapshots. No bulk publisher/tracking sync was run, so no unrelated issue bodies/statuses/owners were rewritten. No commit, source push or deployment was performed.
