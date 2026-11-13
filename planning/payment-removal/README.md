# PayOS and desktop payment execution removal

2026-11-13, following the [user's explicit scope amendment](../v1-scope-2026-11-13-payments.md). This resolves the PayOS import/configuration blocker observed under #7/#40; it does not certify full backend readiness or complete either ticket.

## Behavior

- Removed the `@payos/node` dependency, gateway implementation and eager PaymentBase initialization. Removed unused SePay fallback/link/webhook processing so the application does not silently switch providers. Historical type/gateway labels remain for stored data and read views; API DTOs no longer import an SDK.
- Payment creation, PayOS/SePay callbacks, payment SSE and transaction-status confirmation return 503 before database/cache/provider access. Direct payment service methods enforce the same boundary. Public subscription creation/paid-upgrade endpoints and admin refund/status mutations are also unavailable; no paid transaction or entitlement is fabricated.
- User/admin payment history and revenue/export reads remain. Existing schemas, migration history, records and gateway/status values are not rewritten or deleted. Automatic free-plan creation, authenticated subscription reads/cancellation and normal usage accounting are unchanged. Removing payments does not grant paid features or define a new entitlement policy.
- The authenticated `/payment` route now shows translated en/vi availability text. It no longer imports checkout hooks, reads payment query parameters, displays bank QR/link instructions or reacts to `status=PAID` callbacks. Existing admin/history routes, website build and original source checkouts are retained.
- Redis remains in the application. Only the removed payment consumers stop using it; no Redis/BullMQ/cache/job replacement or data deletion ran. Email stays excluded. No merchant/SMTP credentials or real dotenv files were read or supplied.

## Evidence and limits

```text
python planning/payment-removal/run-check.py frozen-install install --frozen-lockfile --ignore-scripts --offline
python planning/payment-removal/run-check.py api-build --filter api-services build
python planning/payment-removal/run-check.py api-lint --filter api-services lint
node planning/payment-removal/contract-check.cjs
node planning/payment-removal/compare-web-lint.cjs
python planning/payment-removal/probe-api-start.py
python planning/payment-removal/run-check.py root-package package
python planning/payment-removal/probe-web.py
```

- Frozen offline install passes with lifecycle scripts suppressed. The dependency delta removes only PayOS and its otherwise unused `crypto@1.0.1` npm package; all other existing lock resolutions are retained. The built-in Node crypto used for passwords remains. `lock-before.yaml` records the pre-removal lockfile; no dependency/framework upgrade was performed.
- API production compile and root production package pass. The root command executes actual API/Next builds and website packaging, preserving 22 contained standalone links. This is not a complete desktop installer or native-host matrix result.
- `contract-check.json` executes actual compiled controllers/services with explicit query/provider doubles. It verifies 503 responses for payment/callback/paid-upgrade/admin refund/status operations before reads/writes; history queries still preserve old gateway/status fields and apply the user filter/limit. It also checks the absent direct SDK link and checkout source's lack of payment/callback effects. These are unit/source boundary checks, not real financial transactions, database history reads, HTTP authentication or browser interaction.
- Full API lint retains 92 errors/139 warnings, with zero added diagnostic signatures versus the preceding email-removal checkpoint; four old warnings were removed with payment code. `web-lint-comparison.json` shows no added diagnostics and zero current errors/warnings in the changed payment page and translation loader. Inherited repository lint failures are not claimed fixed.
- The bounded real API entrypoint probe gets past PayOS/PaymentBase without merchant keys and remains running until its ten-second limit amid deliberately unavailable loopback DB/Redis initialization. `backendReady` remains false. The probe supplies an isolated `.puppeteerrc.json` only to prevent config discovery outside the disposable directory; it does not provide/download/certify a browser. Real dotenv/host config reads and writes outside the test data directory are denied. The owned process is bounded/stopped. No full-stack readiness claim follows from the absence of the PayOS error.
- `website-proof.json` records real website/asset/font sampling with filesystem writes and original-workspace reads denied; its payment callback-URL checks verify HTTP status and translated payload only. The retained authentication wrapper means these checks do not prove a signed-in browser interaction. No provider payment/refund/webhook or database migration ran.

The current shared imported API/website build disables this capability; original deployments were not modified. Remaining local profile/bootstrap/readiness work stays under #40/#28/#29/#8 and the native/installer/resource gates stay under the existing #7 follow-up ledger. #7 stays In Progress and #41's deferred criteria are not marked complete. All changes remain local/uncommitted; no source push or deployment is performed.
