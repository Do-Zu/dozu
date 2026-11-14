<!-- dozu-toolchains-followup:framework-security -->
## Outcome
Upgrade the imported application to a supported, security-reviewed framework/runtime baseline with independent regression evidence. This is the unresolved security-upgrade portion of #7, separate from source import #5 and portable tooling changes.

## Evidence and trigger
The measured baseline is Next 14.2.35, React/ReactDOM 18.3.1 and build Node 22.22.0. The #7 vendor-policy check found Next 14 unsupported; pins establish reproducibility, not current security approval. No framework upgrade was performed. Local evidence: `planning/toolchains/README.md`, `planning/email-removal/README.md`.

## Acceptance criteria
- [ ] Recheck current official vendor support/security advisories; record applicable findings and select exact supported patched Next/React/ESLint/Node versions. Do not substitute an unreviewed latest release.
- [ ] Keep the upgrade diff/reasons/lock changes independent from source movement and portability fixes; preserve all website/UI routes, locales and provider contracts.
- [ ] Pass production API/Next builds, repeated builds, peer/singleton checks and frozen install; record full and changed-source lint/test results against the baseline without suppressing inherited failures.
- [ ] Revalidate standalone tracing/link closure, relocation, startup, en/vi routes, bundled fonts/assets, API transport aliases and browser/desktop integration contracts after upgrades.
- [ ] Record native-module rebuild/runtime compatibility consequences for #38 and the native-script portability follow-up; obtain separate native evidence rather than inferring it from a Windows build.
- [ ] Publish exact version/lock/artifact hashes and an upgrade/rollback report. No end-user runtime downloads or source credentials in artifacts.

## Dependencies and boundaries
- Prerequisite: #6 completed workspace/build baseline (and preserved #5 import).
- Use #7's implemented tooling as an input; do **not** require #7 closure to start. This independent roadmap follow-up supplies release evidence to #1; it is outside the completed #7 foundation scope.
- Coordinate #38 for shipped runtimes and #22/#23 for complete release integration. This task does not certify installers/native platforms or close those issues by inference.

Parent: #1. Follow-up from completed tooling foundation: #7. Phase: 1 Foundation. Priority: P0. Complexity: L. No owner is assigned by inference.

## Approved scope
Preserve the website/all UI, local-first optional internet, PostgreSQL retained/pgvector deferred, required PDF/YouTube text embeddings and LAN classrooms. Local speech-to-text/STT-only assets and outgoing email are excluded; payments remain deferred under #41. Redis stays unchanged per the user's 2026-11-13 clarification; replacement alternatives are proposals only.


<!-- dozu-foundation-split-2026-11-13 -->
The user explicitly authorized closing #7 for its delivered JavaScript tooling foundation and moving later desktop acceptance to independent issues. This issue stays open and is parented to roadmap #1. Its original acceptance boxes and metadata are preserved. This work remains a required desktop release gate; #7 closure is not evidence it passed. Redis remains retained, while outgoing email, local STT and payment execution are excluded by explicit user scope amendments.
