"""FastAPI entrypoint shared by website and supervised local service."""
from contextlib import asynccontextmanager
import hmac
from fastapi import BackgroundTasks, FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from starlette.middleware.trustedhost import TrustedHostMiddleware
from .core.config import settings
from .core.model_manager import model_manager
from .api.api import api_router


@asynccontextmanager
async def lifespan(app):
    model_manager.load_model()
    try:
        yield
    finally:
        model_manager.unload()


def create_app():
    app = FastAPI(title=settings.API_TITLE, version=settings.API_VERSION, lifespan=lifespan)
    app.include_router(api_router)
    if settings.PROFILE == "desktop":
        app.add_middleware(TrustedHostMiddleware, allowed_hosts=["127.0.0.1", "localhost", "[::1]"])

        @app.middleware("http")
        async def local_auth(request: Request, call_next):
            if (not request.client or request.client.host not in {"127.0.0.1", "::1"}
                or request.headers.get("origin") is not None
                or not settings.SERVICE_TOKEN
                or not hmac.compare_digest(request.headers.get("authorization", "").encode("utf-8"),
                                           ("Bearer " + settings.SERVICE_TOKEN).encode("utf-8"))):
                return JSONResponse({"detail": "Local service authentication required"}, status_code=401)
            return await call_next(request)

        @app.post("/shutdown")
        def shutdown(background_tasks: BackgroundTasks):
            callback = getattr(app.state, "shutdown_callback", None)
            if callback is None:
                raise HTTPException(503, "Shutdown requires the managed launcher")
            background_tasks.add_task(callback)
            return {"status": "stopping"}
    return app


app = create_app()
