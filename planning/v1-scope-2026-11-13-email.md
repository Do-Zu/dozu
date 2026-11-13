# Scope amendment — email delivery, 2026-11-13

Authority: the user instructed, “We'll remove email sending, redis cache, BACK_END_URL you can setting,” then clarified Redis: “SKIP remove Redis, but you can suggest way to alternative solution.”

- Remove outgoing email from this version. Do not require SMTP credentials, create SMTP transports, or report an email as sent. Keep pages and independent in-app notifications, feedback storage, account/profile functionality and manual classroom invite links.
- Preserve username/password registration and login. Registration no longer generates email verification codes, and login no longer requires the email-verification flag. Password verification and active-account checks remain. Email contact details are not verified by this flow; do not set `isVerified` to true or treat contact email as proof of identity. Existing accounts and verification/password-token history are not rewritten.
- Email-based password recovery and classroom email invitations are explicitly unavailable. Reject requests before creating recovery/invitation records. Keep signed-in password changes protected by the current password. No replacement signed-out recovery mechanism, secret disclosure or authentication bypass is introduced. Designing local recovery remains follow-up work.
- **Redis remains unchanged**, including caches, jobs, pub/sub, usage limits and recommendation data. Alternative designs are suggestions only, not approved replacement work or passing Redis-free startup evidence.
- The backend public URL defaults to `http://localhost:3333` (using configured `PORT` when present). `BACKEND_BASE_URL` overrides it; `BACK_END_URL` is accepted as a lower-priority alias. Set an explicit reachable URL for LAN/deployments and an actual bound port when using ephemeral ports. No credential/environment file is written.

This amendment supersedes older email-delivery requirements only. The retained website/all UI, local-first optional internet, PostgreSQL retained/pgvector deferred, retained PDF/YouTube text embeddings, excluded local STT, deferred payments and LAN classrooms remain unchanged. Full packaged/native/security/lifecycle acceptance is still unpassed.

Implementation, exact tests and Redis alternatives: [follow-up report](email-removal/README.md).
