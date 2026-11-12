# Retained website API image; desktop bundling is a separate delivery pipeline.
# Build from the repository root: docker build -f apps/api/Dockerfile .
FROM node:22.22.0-bookworm-slim AS builder
WORKDIR /workspace
RUN corepack enable && corepack prepare pnpm@10.28.2 --activate
COPY package.json pnpm-lock.yaml pnpm-workspace.yaml ./
COPY apps/web/package.json ./apps/web/package.json
COPY apps/api/package.json ./apps/api/package.json
RUN pnpm --filter api-services install --frozen-lockfile --ignore-scripts
COPY apps/api ./apps/api
RUN pnpm --filter api-services build

FROM node:22.22.0-bookworm-slim AS runner
WORKDIR /workspace
RUN corepack enable && corepack prepare pnpm@10.28.2 --activate
COPY package.json pnpm-lock.yaml pnpm-workspace.yaml ./
COPY apps/web/package.json ./apps/web/package.json
COPY apps/api/package.json ./apps/api/package.json
RUN pnpm --filter api-services install --prod --frozen-lockfile --ignore-scripts
COPY --from=builder /workspace/apps/api/dist ./apps/api/dist
ENV NODE_ENV=production
USER node
EXPOSE 3444
# Supply deployment credentials at runtime; never COPY dotenv into an image.
CMD ["pnpm", "--filter", "api-services", "start"]
