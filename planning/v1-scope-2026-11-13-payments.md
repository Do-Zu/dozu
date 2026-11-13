# Scope amendment — desktop payments excluded, 2026-11-13

Authority: the user stated, “I think I'll remove PayOS for payment because this desktop not payment any more.” This makes the existing payment-execution deferral explicit in the current desktop implementation.

- Remove the PayOS SDK/provider and its eager startup/configuration requirement. Do not substitute SePay or another payment provider.
- The current desktop version does not execute payments, create bank/checkout links, accept gateway confirmations, issue refunds or activate paid subscriptions from callbacks. Return an explicit unavailable result before payment/subscription mutation. Never fabricate a successful payment, grant paid entitlements, or consume merchant credentials to make startup pass.
- Preserve the payment route, history/admin/revenue views, historical gateway labels, schemas and existing records. The payment route explains unavailability and does not process bookmarked `status=PAID` query strings. Existing read queries/exports, subscription records, normal feature-usage checks and automatic free-plan initialization remain; this instruction does not define a new blanket entitlement/unlocking policy.
- No payment/history records, migration files, user data or existing deployment are deleted/changed by a live transaction. The current shared imported API/website build exposes the unavailable payment capability; no website deployment was performed. Original source checkouts/history remain intact.
- #41 remains the historical/deferred payment tracker. Reintroducing payment execution requires a new explicit product instruction and validated provider design. Do not mark its original payment-implementation criteria Done merely because PayOS was removed.

Other decisions remain unchanged: outgoing email and local STT are excluded; Redis is retained; PostgreSQL retained/pgvector deferred; website/all other UI, required PDF/YouTube text embeddings, optional internet and authoritative LAN classrooms stay in scope. No resource/platform/lifecycle gate is waived.

Implementation and exact evidence: [payment removal report](payment-removal/README.md).
