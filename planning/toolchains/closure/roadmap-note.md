<!-- dozu-foundation-closure-2026-11-13:start -->
## Tooling foundation completed; desktop acceptance retained — 2026-11-13
The user explicitly authorized a scope split so migration can proceed. #7 is completed for the committed/measured JavaScript tooling foundation at verified dev SHA 8e7b7d134ec450ecd0244ab8deaee3d67b9379bb. Its original wider criteria are archived and transferred; they were not marked passing. This does not certify a shipped runtime, full API readiness, migrations, read-only native installation, clean-machine setup, budgets or platform parity.

Independent required follow-ups now parented to this roadmap:
- [ ] #48 — Supported framework/security upgrade and independent regression proof.
- [ ] #49 — Native portable-script/build matrix on all approved OS/CPU hosts.

Existing #38/#8/#32 own shipped runtime/ABI/resources; #40/#28/#29/#34/#15 own startup/migrations/installed paths; #23/#33/#22/#46/#47 own installers/native release evidence; #14/#16 own real account/study integration; #10 owns full CI/lint/test validation. These remain open. #38 becomes Ready after #7's foundation completion and is the next executable desktop migration step, not a completed runtime proof. Final runtime versions still need the #48 security review.

The closed #4/#45 metadata is not used as passing support evidence and those issues are unchanged. #7's narrowed foundation depends on completed #6, eliminating the prior circular expectation of downstream runtime acceptance before build-tooling completion. Redis stays retained; email/STT/payment execution are excluded; PostgreSQL without pgvector, retained PDF/YouTube text embeddings, website/UI and LAN scope remain authoritative. No owner is invented and no unrelated status/field is changed.
<!-- dozu-foundation-closure-2026-11-13:end -->
