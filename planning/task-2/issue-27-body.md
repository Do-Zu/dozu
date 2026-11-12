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
- [ ] For payments, decide merchant-self-hosting versus customer-paying-Dozu and validate a genuine provider-supported flow/entitlement authority.
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

## Requirements-stage decision record — 2026-11-10 (Task #2)

Local record: `planning/integration-decisions.md` (not pushed). Existing source/provider evidence is in completed audit #3. No live provider flow is certified by this update.

- Established constraints: every installation owns its local backend/database/files/jobs; Electron and browser share them; no required central Dozu backend/cloud database/sync. Real internet-enabled integrations and all existing pages remain in scope.
- Credential ownership: no shared publisher merchant/SMTP/vendor secret in installers/config/renderer responses. Use user-owned credentials or supported delegation. Optional providers initialize lazily and cannot crash unrelated local use.
- Proposed adaptations requiring proof: Google native/system-browser authorization with a loopback return; user-owned/delegated mail with a desktop return path; direct configured AI calls from local Express; authoritative local uploads/content and real YouTube/transcript/media ingestion.
- Callback design: prefer genuine authenticated outbound reconciliation when it preserves provider semantics; any required public endpoint/tunnel is explicit, user-owned, opt-in, scoped/authenticated and documented for TLS, delivery, availability, replay and idempotency. The actual payment/email solution still requires ownership/provider proof. No implicit central callback service.
- **Unresolved #41:** each user operates their own merchant account versus customers paying Dozu for an entitlement. Dozu merchant secrets cannot be distributed to customers. Preserve checkout/history/admin functionality while deciding the real reconciliation/entitlement authority.
- **Unresolved #43:** same-computer sessions, LAN participants, or remote participants reaching a user-owned host. Record identity/roles, TLS/auth/ACL, reachability, uptime and reconnect/conflict handling. Separate installations do not automatically share state.

The user has been asked for these ownership/topology choices in the Task #2 session. They remain unresolved until answered. #2's remaining criterion concerns agreed product requirements; this item's genuine provider/callback proofs remain separate implementation work. No new dependency edge or completion claim is introduced.

