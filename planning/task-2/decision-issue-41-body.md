<!-- dozu-tracking:start -->
## Work tracking
Use the live **status:**, **priority:** and **complexity:** labels above; **Assignees** identifies the owner. These labels are separate from the task/ticket type.

**Planning complexity:** XL - Merchant ownership and provider reconciliation/callback feasibility are unresolved; split after design validation.
Complexity is a provisional scope/uncertainty estimate, not a delivery-time commitment. XL work must be split into executable subtasks before starting.
**Planning priority:** P1 - Required product, integration or release work after its prerequisites.

**Blocking decision/impediment:** User explicitly deferred/skipped payment execution during the local migration on 2026-11-10. Keep payments blocked under #41 until the user explicitly reopens the feature and chooses merchant ownership/provider flow; no live charges or simulated success. Existing payment/history/admin page inventory is retained.
<!-- dozu-tracking:end -->

## Outcome
Adapt PayOS/SePay checkout/status/history for the agreed merchant/customer ownership model without distributing Dozu merchant secrets.

## Acceptance criteria
- [ ] Record owner of merchant keys and transaction authority; choose user-owned merchant credentials or provider-managed checkout/entitlement flow as appropriate.
- [ ] Keep real checkout in supported browser/provider flow; validate redirect binding, order/amount/currency/account and never trust success URL as payment proof.
- [ ] Implement documented authenticated provider status reconciliation (current PayOS getPaymentStatus is unimplemented), durable local mappings and idempotent subscription updates.
- [ ] When webhooks are mandatory, prove provider-supported scoped tunnel/public callback delivery/signature/replay behavior and host-offline recovery; no silent hosted Dozu relay.
- [ ] Test failure/cancel/refund/restart/duplicate events and preserve payment/admin/history UI; explicitly report unresolved provider constraints.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

<!-- dozu-roadmap:PAYMENTS -->

Phase: 2 Local services | Priority: P1

Parent roadmap: https://github.com/Do-Zu/dozu/issues/1

## Dependencies
- #27 - [Ticket] Resolve desktop integration callbacks, secrets and shared-state limits
- #31 - [Task] Store user-scoped provider credentials securely on the device
- #40 - [Task] Add a local backend profile with automatic seeds and lazy integrations

## Explicit payment deferral — 2026-11-10

Blocked because: User explicitly deferred/skipped payment execution during the local migration on 2026-11-10. Keep payments blocked under #41 until the user explicitly reopens the feature and chooses merchant ownership/provider flow; no live charges or simulated success. Existing payment/history/admin page inventory is retained.

This user decision defers payment execution rather than authorizing page deletion. Future implementation must expose an honest blocked state and preserve local history/admin inventory. No payment functionality has been disabled in application code by this requirements task. Existing technical criteria are retained for an explicitly reopened payment feature, not a mandatory v1 payment release gate.
