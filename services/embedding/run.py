"""Loopback launcher; supervisor supplies paths, port and per-launch token."""
import os


def main():
    os.environ.setdefault("DOZU_EMBEDDING_PROFILE", "desktop")
    from src.app.core.config import settings
    settings.validate()
    import uvicorn
    from src.app.main import app
    port = int(os.getenv("DOZU_EMBEDDING_PORT", "8686"))
    server = uvicorn.Server(uvicorn.Config(app, host="127.0.0.1", port=port,
        proxy_headers=False, access_log=False, timeout_graceful_shutdown=10))
    app.state.shutdown_callback = lambda: setattr(server, "should_exit", True)
    server.run()
    if not server.started:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
