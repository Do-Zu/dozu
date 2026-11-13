# Email removal and local backend URL

2026-11-13, follow-up to #7. See the [user-authorized scope amendment](../v1-scope-2026-11-13-email.md). Earlier `planning/toolchains/` logs/manifests describe the preceding checkpoint; the source and lockfile hashes from that checkpoint are historical after this follow-up.

## Changes

- Removed Nodemailer transport code, its direct API dependency and its type package. The lockfile removes only those two packages/importer entries; unrelated UI dependency resolutions are preserved. No SMTP settings are required or read by API code.
- Username/password registration no longer creates or sends verification codes. Login still verifies the password and rejects inactive accounts, without requiring an email ownership check. No account/email is marked verified, and no user records/migrations are rewritten. Existing authenticated profile password changes still require the current password.
- Email password-recovery and class-invitation service entrypoints throw HTTP 503 before repository access. Notification email methods return false, never fake success. Feedback still saves locally with `notified: false` and `shouldSendEmail: 0`; in-app daily/weekly/achievement/re-engagement notifications no longer depend on email templates or frontend URL settings. No real email is sent during validation.
- Kept the forgot-password page with a translated explanation and login link; email notification settings are visibly off/disabled. The email invitation tab explains manual invite-link sharing and disables sending. Registration success text in en/vi directs users to sign in. Existing legacy verification/token pages and history are preserved.
- Added `config.backendBaseUrl`: canonical `BACKEND_BASE_URL`, then `BACK_END_URL`, then `http://localhost:${PORT || 3333}`, with trailing slashes removed. Attachment URLs consume that configuration. A wildcard bind host is never used as the default public URL. For LAN hosts/reverse proxies or ephemeral ports, explicitly supply the intended public URL. No real dotenv file was read or edited.
- Redis code, dependencies, data semantics, jobs and pub/sub are unchanged. No Redis-free startup or full-stack acceptance is claimed.

## Verification

Commands from the repository root:

```text
python planning/email-removal/run-check.py frozen-install install --frozen-lockfile --ignore-scripts --offline
python planning/email-removal/run-check.py api-build --filter api-services build
node planning/email-removal/contract-check.cjs
node planning/email-removal/compare-web-lint.cjs
python planning/email-removal/run-check.py root-package package
```

`contract-check.json` executes actual compiled modules with explicit repository/provider doubles and real scrypt hashing. It checks registration without verification-code creation, correct-password login, wrong-password/inactive rejection, 503 email actions before repository reads/writes, false email delivery status, retained in-app reminder delivery without SMTP/frontend settings, and backend URL defaults/alias/precedence. These are **unit boundary checks**, not real PostgreSQL login, signed JWT, network delivery or installer evidence.

Build/install/lint records are beside this report. Targeted UI lint compares the unchanged HEAD versions and current source through the same ESLint API, ignoring line shifts; inherited diagnostics remain visible. The initial automatic offline lock refresh changed two unrelated `react-remove-scroll` resolutions; those were reverted before final install/build. A sandbox symlink replacement failed with EPERM; the scoped offline install succeeded outside the sandbox with lifecycle scripts suppressed. No framework upgrade, database migration, provider transaction or deployment ran.

Final results: frozen offline install, API build, root production package and compiled-module contract checks pass. `website-proof.json` records **11 real HTTP checks**, including both translated recovery notices with the email form absent, with all filesystem writes and original-workspace reads denied; the owned server was stopped. API lint still fails with **92 errors/143 warnings**, eight fewer errors than the preceding checkpoint and zero added diagnostic signatures. `web-lint-comparison.json` shows zero added diagnostic signatures across all four changed UI files; existing UI lint failures are not claimed fixed. `scope-verification.json` checks unchanged Redis source/dependency declarations and removal of only the two direct SMTP packages.

Full API startup still requires the retained Redis/database and remaining provider/local-adapter work. Email removal and URL defaults do not establish backend readiness, native packaging or full #7 acceptance. #7 stays In Progress with all five full acceptance boxes unchecked.

The bounded real entrypoint run in `production-startup.json` confirms the previous email/backend-URL import blocker is absent. It now exits at the inherited eager `PaymentBase configuration is not set properly`/PayOS initialization. Payments remain deferred under #41; no merchant credentials or fake payment configuration were supplied to make startup pass. Database logging/Redis initialization also remain outside this email-removal result.

## Suggested Redis alternatives — not implemented

For a future change, I recommend building around the PostgreSQL instance already required by the product:

| Current role | Candidate replacement | Required proof |
| --- | --- | --- |
| Disposable read caches | Bounded process-local cache with TTL/eviction, or no cache initially | Memory budget, stale-data invalidation, safe restart misses; never store the only copy of edits/counters here |
| BullMQ background jobs/results | PostgreSQL-backed queue such as [pg-boss](https://github.com/timgit/pg-boss) | Pin a compatible Node/PostgreSQL version, migrate every job/result consumer, verify idempotency, retries, cancellation, crash recovery and job visibility |
| Durable usage counters, recommendation frequencies and schedule edits | PostgreSQL tables and atomic transactions | Preserve limits/concurrency, counts, existing data, indexing and performance; current schedule edits use Redis as their only storage, so dropping the cache would lose behavior |
| Live updates/socket routing | Existing Socket.IO on the authoritative LAN API host; PostgreSQL notification signals when multiple processes need coordination | Reconnect/replay, owner/class isolation, multiple clients, host restart and job progress |

[PostgreSQL LISTEN/NOTIFY](https://www.postgresql.org/docs/current/sql-notify.html) can wake listeners after a transaction commits; keep durable events/state in tables and send record IDs, with polling/replay for reconnects. It is not a durable job queue or replacement for stored notification history. Database-backed jobs/state reduce the number of bundled services but add database load and require schema/lifecycle work. This is a proposal for a separate task; Redis stays in place now.
