<!-- dozu-tracking:start -->
## Work tracking
Use the live **status:**, **priority:** and **complexity:** labels above; **Assignees** identifies the owner. These labels are separate from the task/ticket type.

**Planning complexity:** L - Provider contracts, credential ownership, public callbacks and classroom architecture decisions.
Complexity is a provisional scope/uncertainty estimate, not a delivery-time commitment. XL work must be split into executable subtasks before starting.
**Planning priority:** P0 - Architecture/foundation work that unblocks the implementation path.
<!-- dozu-tracking:end -->

## Outcome

Preserve real third-party integrations and explicitly resolve the limits of a local backend with no operator-maintained central application infrastructure.



## Acceptance criteria

- [ ] Inventory Google, SMTP, PayOS/SePay, YouTube, LLM/Lambda, feedback and classroom public-endpoint/credential/state requirements with source evidence.

- [ ] Use native/public OAuth or scoped user-owned credentials; never distribute Dozu merchant/SMTP/vendor confidential secrets.

- [ ] Payments are explicitly deferred/blocked under #41 by user decision. If reopened, decide merchant-self-hosting versus customer-paying-Dozu and validate a genuine provider-supported flow/entitlement authority.

- [ ] For required inbound callbacks, verify authenticated outbound reconciliation where supported or document an opt-in scoped tunnel/endpoint with availability/delivery constraints.

- [ ] For classrooms, decide local-only sessions versus reachable host/LAN/tunnel architecture without adding cloud DB/sync; keep pages/features in scope and unresolved gaps visible.



## Architecture constraints

The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.



<!-- dozu-roadmap:INTEGRATIONS -->



Phase: 0 Requirements | Priority: P0



Parent roadmap: https://github.com/Do-Zu/dozu/issues/1



## Dependencies

- #3 - [Task] Audit complete UI/backend and local-first integration baselines

- #2 - [Ticket] Record local-first requirements and full feature-preservation matrix



## Agreed requirements decisions — 2026-11-10

Supersedes the previous unresolved topology/requirements note. User-approved platform, installer, low-resource mode and performance contract is in #2 and local `planning/platform-support.md`.

- Payments: user explicitly defers/skips execution for the local migration. Reuse #41 as the single blocker. Merchant ownership and payment callback/reconciliation are deferred. Keep page/history inventory; do not delete pages, charge, ship merchant secrets or simulate success. Reopening requires an explicit user decision and genuine provider proof.
- Classrooms: user selects other devices on the same LAN. One user-owned host remains authoritative; opt-in LAN access serves participants. Identity/roles, TLS/auth/ACL, host discovery/connection, firewall, availability/reconnect/revocation and persisted events need proof under #43. Core loopback binding must not be widened indiscriminately. Internet/tunnel classrooms are not a v1 requirement; no cloud DB/sync.
- Existing no-central-backend and no-shared-publisher-secret constraints remain. Google/mail return paths and genuine provider/LAN proof remain work here and in #14/#42/#43/#44. The payment-specific proof criteria below apply only if #41 is explicitly reopened; they do not block requirements completion or other migration work.

This records product choices only; no implementation checkbox here is marked complete.

