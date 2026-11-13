<!-- dozu-payments-removal-checkpoint:40:2026-11-13 -->
## PayOS import blocker removed — 2026-11-13

The latest user instruction excludes payment execution from desktop. The @payos/node SDK, eager PaymentBase/PayOS startup and unused SePay fallback processing are removed. Payment/paid-upgrade/refund/status/callback operations now return unavailable before mutable access; history/read/export data and free-plan initialization remain. See #41's new scope amendment and the update on #7; no merchant keys or fake paid entitlements were introduced.

The previous `PaymentBase configuration is not set properly` failure is absent in the real compiled-entrypoint probe (`planning/payment-removal/production-startup.json` and `.log`). With real dotenv/host config reads denied, a disposable Puppeteer no-download config and deliberately unavailable loopback DB/Redis, the process remains running until the ten-second bound and is stopped. It logs inherited DB serialization/connection and retained Redis/embedding setup problems. This is not backend-ready evidence or a verified browser/model runtime.

Keep full local-profile/bootstrap/health/shutdown/restart work open here and under #28/#29/#8/#23. Redis remains retained per user instruction; do not remove it as a workaround. No new duplicate startup issue is needed, and no acceptance criterion or existing status/assignee/Project field is marked completed by the absence of PayOS.
