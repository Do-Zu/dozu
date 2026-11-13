# Authoritative local-first requirements

Recorded from the latest user clarification on 2026-11-09. This file supersedes earlier online-first and fully air-gapped assumptions.

**2026-11-14 accepted resource amendment:** [Current hardware/resource contract](resource-contract-2026-11-14.md): minimum 8 GB RAM, 64-bit/four physical cores, SSD/10 GB free; recommended 16 GB, 6–8 cores, SSD/20 GB free. Initial-release installer ≤1.5 GB, installed app ≤3 GB, normal combined app RAM ≤2 GB and one-job peak ≤3 GB, cold UI ≤15 s and complete backend/model ready ≤30 s. Warm UI remains ≤5/3 s. Keep the pinned CPU model for initial integration; ONNX optimization can follow later. These supersede older numeric limits below and in historical notes, without passing runtime/native/lifecycle ACs. See [the acceptance review](resource-amendment-2026-11-14/acceptance-review.md).

**2026-11-11 amendment:** [v1 scope decision](v1-scope-2026-11-11.md) removes local speech-to-text, retains PostgreSQL and defers pgvector. PDF/YouTube text-reference retrieval still consumes a separate embedding model, so its smaller-runtime experiment remains relevant. This explicit amendment supersedes earlier full-feature wording only for the specified deferrals; all pages/source inventory and other retained capabilities remain.

1. Preserve the complete existing Next.js website UI: all pages, layouts, components, navigation, roles, translations and features.
2. Package and run the existing Express backend/business logic locally on every user's computer.
3. Keep the database, user information, study progress, settings, uploads/generated files and durable job state local. Each user's computer is the primary source of truth.
4. Allow internet connectivity for genuine Google OAuth, YouTube, email, payments, configured AI and other necessary third-party integrations.
5. Preserve real functionality wherever technically feasible; do not substitute simulations or silently drop integration-dependent pages/features.
6. Require no operator-maintained central Dozu backend, cloud database or cloud synchronization.
7. Browser and Electron interfaces use the same local backend/data through localhost.
8. Supply the frontend/runtime, backend, database and required local dependencies through the installer; users do not manually set up developer tools/services.
9. Offer a tested choice to retain or permanently delete all app-owned local data during uninstall on each supported platform.
10. Explicitly identify integration limits involving confidential publisher secrets, public callbacks, centralized state and reachability; propose secure desktop-compatible flows and verify them before claiming parity.

The architecture does not require all third-party features to work without internet. First-party local startup/data access must not require a central Dozu server or cloud store. Optional external provider credentials can be configured in-app; missing credentials affect the relevant integration rather than crashing the local backend.

Recommendation: Electron supervising the current Next.js standalone frontend, existing Express local runtime profile, bundled PostgreSQL without a v1 pgvector prerequisite, local files/jobs/cache and a proven text-embedding runtime for retained PDF/YouTube references. Whisper/speech-to-text is deferred. Preserve real third-party APIs with native/public OAuth and user-scoped credentials where appropriate.

Full plan: [monorepo-desktop-plan.md](monorepo-desktop-plan.md).
Roadmap: https://github.com/Do-Zu/dozu/issues/1.
Integration decision record: https://github.com/Do-Zu/dozu/issues/27.

Implementation is not complete. Issue #3's baseline audit has completed evidence in [audit/README.md](audit/README.md); implementation acceptance remains open. Planning or static route counts do not prove working installers or feature parity.

## Task #2 requirements evidence — 2026-11-10

The [full preservation matrix](feature-preservation.md) / [JSON](feature-preservation.json) records every existing route's workflow, role intent, gate evidence, en/vi locales, layouts and follow-up work. Coverage is verified against the unchanged tracked UI commit: 84 pages, 20 layouts and 164 shared TSX components, with all route-scoped code covered by the linked audit ledger. All existing admin, teacher/student, billing/history, auth, generation, media, games, study, schedule/settings and navigation flows remain required. All page inventory remains; the user explicitly deferred/blocked payment execution under #41 on 2026-11-10. Classroom v1 supports other devices on the same LAN; remote internet participants are not a v1 requirement.

Preservation acceptance includes the retained website build, Electron and a localhost browser, existing themes/layouts/translations, allowed and denied roles, local persistence after restart, loading/empty/error/retry states and genuine external-provider behavior where applicable. Every runtime result remains unverified; source-intended roles require actual authorization proof during implementation.

The user agreed the initial [v1 platform/hardware/installer/performance contract](platform-support.md) on 2026-11-10. It includes Windows 10 22H2 legacy/Windows 11 primary x86-64, macOS 13+ Intel/ARM64, Ubuntu 22.04 LTS/Debian 12 x86-64, and specified budgets and low-resource mode. These are requirements awaiting benchmark validation. SQLite may be evaluated only with backend/business compatibility proof; PostgreSQL/pgvector is not silently replaced.

[INTEGRATIONS decisions](integration-decisions.md): payment execution is explicitly deferred/blocked under existing #41; preserve page/history inventory without fake success, and do not delete payment pages. Classroom v1 connects other devices on the same LAN to a user-owned authoritative host. #43's topology blocker is resolved; networking/auth/TLS and provider flows still require implementation proof under #27. No central Dozu backend/cloud DB/sync is introduced.

| Issue #2 criterion | Evidence / state |
| --- | --- |
| Mandatory local architecture and self-contained install | Recorded above; complete as a requirement, implementation pending. |
| Per-route/role/locale/feature matrix | Complete as source-backed requirements; [matrix](feature-preservation.md), [audit ledger](audit/ui-ledger.md). |
| All feature families and navigation remain in scope | Complete as scope; matrix includes placeholders and known gaps, not working feature claims. |
| Agreed OS/CPU/distro/installers/resource budgets | Agreed by user on 2026-11-10; platform-support.md. Benchmarks pending. |
| Callback/shared-secret/classroom decisions under INTEGRATIONS | User decisions recorded under #27: defer/block payments #41; LAN classroom #43. Callback/provider/LAN implementation proofs remain downstream. |


Task #2 is complete as requirements work (5/5 criteria). This does not certify release compliance or complete any implementation issue.
