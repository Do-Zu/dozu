<!-- dozu-tracking:start -->
## Work tracking
Use the live **status:**, **priority:** and **complexity:** labels above; **Assignees** identifies the owner. These labels are separate from the task/ticket type.

**Planning complexity:** XL - Remote participant topology, reachability, TLS and host availability are unresolved; split after architecture decision.
Complexity is a provisional scope/uncertainty estimate, not a delivery-time commitment. XL work must be split into executable subtasks before starting.
**Planning priority:** P1 - Required product, integration or release work after its prerequisites.

<!-- dozu-tracking:end -->

## Outcome
Preserve classroom pages/roles/assignments/quizzes/live events and specify how participants access an authoritative local host.

## Acceptance criteria
- [ ] Retain all teacher/student/admin records/workflows on the local database; test multiple browser/window sessions first.
- [ ] Prove opt-in authenticated access from other devices on the same LAN to a user-owned authoritative host, with explicit TLS/auth/ACL, firewall and connection/discovery design; loopback alone cannot serve LAN clients. Remote internet/tunnel access is not a v1 requirement.
- [ ] Do not add central Dozu servers, cloud database or data synchronization as an implicit solution.
- [ ] Define host availability, reconnect, participant identity/access/revocation and data visibility with explicit user-facing limits.
- [ ] Validate real event delivery and persisted classroom state; no local-record simulation presented as remote collaboration.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

<!-- dozu-roadmap:CLASSROOM -->

Phase: 2 Local services | Priority: P1

Parent roadmap: https://github.com/Do-Zu/dozu/issues/1

## Dependencies
- #27 - [Ticket] Resolve desktop integration callbacks, secrets and shared-state limits
- #14 - [Task] Preserve local accounts and adapt genuine Google OAuth for desktop
- #30 - [Task] Replace desktop Redis/BullMQ consumers with durable local adapters

## Topology selected by user — 2026-11-10

Other devices on the same LAN connect to a user-owned authoritative local host. The prior topology-choice blocker is resolved. Ordinary prerequisites #27/#14/#30 remain; status is waiting, not complete. Remote internet/tunnel classroom access is not a v1 requirement. No central Dozu service/cloud DB/sync. Preserve local teacher/student/admin workflows; prove opt-in LAN exposure, roles/auth/TLS/ACL, firewall/discovery, host availability, identity/revocation, reconnect and real persisted events. No implementation checkbox is completed by this decision.
