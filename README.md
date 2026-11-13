# Dozu

Local-first desktop delivery and the retained website share the imported applications in `apps/web`, `apps/api`, and `services/embedding`. Approved scope and platform requirements are in [planning](planning/README.md).

Outgoing email is excluded from this version. Username/password signup/login remain; email recovery and invitations are unavailable, with manual classroom invite links retained. Redis remains required by the existing implementation. `BACKEND_BASE_URL` defaults to `http://localhost:3333` using the configured API port; `BACK_END_URL` is an accepted alias. See the [email/URL follow-up](planning/email-removal/README.md) for exact behavior and checks.

Use **Node 22.22.0**, **pnpm 10.28.2** and the committed lockfile for the measured JavaScript baseline. These pins are reproducibility inputs; release security and native-runtime acceptance remain open.

From the repository root, on Windows PowerShell, macOS or Linux:

```text
pnpm install --frozen-lockfile --ignore-scripts
pnpm verify:toolchain
pnpm verify:workspace
pnpm dev
pnpm build
pnpm package
```

`dev:web` and `dev:api` run individual applications. Supply the genuine deployment-specific environment before starting development or building the website; public Next variables are build-time inputs. `dev` does not provision PostgreSQL, Redis, Python/model resources or provider credentials.

`package` builds both JavaScript applications and creates the standalone website at `apps/web/.package`; it does not produce a desktop installer or a self-contained API runtime. `package:web` selects the website. `start:web` launches that artifact with a default `localhost` bind; `start:api` starts compiled API output using the workspace dependencies. Supply `PORT`/`HOSTNAME` for the website and the required API configuration through your shell or supervisor.

Desktop supervision must supply an absolute, writable **`DOZU_DATA_DIR`** before spawning the API. Existing website deployments retain their working-directory storage default. Logs, uploads and conversion output can be relocated with this setting; it is not full local-data/runtime integration.

End-user installations must bundle their runtimes and assets and require no developer tools. That distribution path, full API startup, migrations, Python/model/browser resources, native ABI matrix and clean-machine acceptance are **unpassed**. See [#7 implementation and evidence](planning/toolchains/README.md) for exact checks, commands and limits. Do not use the historical Lambda/cloud/Docker scripts as desktop setup commands.
