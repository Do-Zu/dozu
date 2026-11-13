<!-- dozu-v1-payments-excluded-2026-11-13:start -->
## Explicit desktop scope: payments excluded — 2026-11-13

The user directed removal of PayOS because the desktop does not process payments. This supersedes payment-execution implementation as a v1 shipping requirement; the original unchecked criteria above are historical/deferred and are not marked completed.

- The current imported API no longer depends on @payos/node, initializes PaymentBase/PayOS, or silently falls back to SePay.
- Payment creation, gateway callbacks, payment SSE, status confirmation, paid subscription creation/upgrade, and admin refund/status mutation are explicitly unavailable before mutable access. No merchant credentials or fabricated payment/entitlement were supplied.
- Retain payment/admin/revenue/history pages, schemas, stored transaction/subscription data and read/export functions. No migration or historical data rewrite/deletion occurred. The authenticated checkout route now explains unavailability in en/vi and does not process PAID query parameters.
- Automatic free-plan initialization, normal usage accounting, subscription reads/cancellation, retained Redis and other approved v1 scope remain unchanged. A new blanket entitlement/unlocking policy is not implied.
- SDK removal, API/Next production builds, root website package and compiled boundary tests pass. Thirteen real website HTTP/payload/asset checks pass with writes denied. Unit tests use explicit query/provider doubles; real DB/financial/browser/native acceptance is not claimed.
- The real scrubbed API entrypoint gets past PayOS and remains running until its bounded ten-second limit against deliberately unavailable DB/Redis. Full backend readiness remains unpassed under #40/#28.
- Reintroducing payment execution requires an explicit product instruction and independent design/security/runtime validation. This update does not reopen payment execution or mark this issue's original criteria Done.

Local reviewable evidence: planning/v1-scope-2026-11-13-payments.md and planning/payment-removal/README.md, contract-check.json, root-package.json, website-proof.json and production-startup.json. Changes remain local/uncommitted; no provider transaction, database migration, source push or deployment ran. Existing issue status, assignees and Project fields are preserved.
<!-- dozu-v1-payments-excluded-2026-11-13:end -->

