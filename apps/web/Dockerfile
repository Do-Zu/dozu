# Build from the repository root: docker build -f apps/web/Dockerfile .
FROM node:22.22.0-bookworm-slim AS builder
WORKDIR /workspace
RUN corepack enable && corepack prepare pnpm@10.28.2 --activate
COPY package.json pnpm-lock.yaml pnpm-workspace.yaml ./
COPY apps/web/package.json ./apps/web/package.json
COPY apps/api/package.json ./apps/api/package.json
RUN pnpm --filter dozu-ui-service install --frozen-lockfile --ignore-scripts
COPY apps/web ./apps/web
COPY tooling ./tooling
ARG NEXT_PUBLIC_API_URL
ARG NEXT_PUBLIC_API_STREAM_SSE_URL
ARG NEXT_PUBLIC_GOOGLE_REDIRECT_URI
ARG NEXT_PUBLIC_OAUTH_CLIENT_ID
ENV NEXT_PUBLIC_API_URL=$NEXT_PUBLIC_API_URL \
    NEXT_PUBLIC_API_STREAM_SSE_URL=$NEXT_PUBLIC_API_STREAM_SSE_URL \
    NEXT_PUBLIC_GOOGLE_REDIRECT_URI=$NEXT_PUBLIC_GOOGLE_REDIRECT_URI \
    NEXT_PUBLIC_OAUTH_CLIENT_ID=$NEXT_PUBLIC_OAUTH_CLIENT_ID \
    NEXT_TELEMETRY_DISABLED=1
RUN pnpm --filter dozu-ui-service build && pnpm --filter dozu-ui-service package

FROM node:22.22.0-bookworm-slim AS runner
WORKDIR /app
ENV NODE_ENV=production HOSTNAME=0.0.0.0 PORT=3000
COPY --from=builder --chown=node:node /workspace/apps/web/.package ./
USER node
EXPOSE 3000
CMD ["node", "apps/web/server.js"]
