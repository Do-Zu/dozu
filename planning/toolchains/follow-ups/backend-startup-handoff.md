## Concrete startup blocker from #7 — 2026-11-13

The user requested explicit tracking of unfinished work from #7. This existing issue already owns the API local-profile/startup task; no duplicate issue was created.

The latest real bounded entrypoint probe is in local `planning/email-removal/production-startup.json` and `.log`. It runs compiled `apps/api/dist/index.js` with scrubbed environment, denied real dotenv reads, disposable DOZU_DATA_DIR and deliberately unavailable loopback DB/Redis endpoints. The old email/BACKEND_BASE_URL import blocker is gone. It now exits at `PaymentBase configuration is not set properly`, through `PayOSManager.initializeBase`/its module-global initialization. DB/log serialization and retained Redis initialization also still require real integration evidence.

Please include these concrete acceptance checks in this task's existing local-profile criteria:
- [ ] Remove eager PayOS/merchant/provider initialization from ordinary API import/startup. Payment execution is deferred under #41; preserve pages/history and return an explicit unavailable state for deferred actions rather than inventing merchant configuration or success.
- [ ] With real disposable local PostgreSQL and the retained Redis runtime configured, prove readiness, loopback binding, genuine auth/topic/write/readback, shutdown and restart without SMTP/payment/optional cloud keys. Do not count the current deliberately unavailable-fixture probe or mocked auth tests as that proof.
- [ ] Preserve the user's email-removal behavior (no SMTP transport; unavailable emailed recovery/invitations; local signup/login and in-app notifications retained). Settings: BACKEND_BASE_URL canonical, BACK_END_URL alias, local default using PORT.
- [ ] Keep Redis in this work. The user explicitly said skip its removal; an older #30 replacement plan must not silently override that instruction. Packaging must account for the retained runtime; alternatives are proposals only.

Track full supervision under #28 and first-run/installer proof under #23/#33. #7 remains In Progress with full acceptance unpassed. No assignee/status/other existing fields are changed by this handoff.
