"""Explicit installed resources; no developer cache or startup downloads."""
import os
from pathlib import Path


class Settings:
    PROFILE = os.getenv("DOZU_EMBEDDING_PROFILE", "website")
    MODEL_PATH = Path(os.getenv("DOZU_EMBEDDING_MODEL_PATH", str(
        Path(__file__).resolve().parents[3] / "resources" / "model")))
    BACKEND = os.getenv("DOZU_EMBEDDING_BACKEND", "torch")
    SERVICE_TOKEN = os.getenv("DOZU_EMBEDDING_TOKEN", "")
    FILE_ROOT = os.getenv("DOZU_EMBEDDING_FILE_ROOT", "")
    FILE_ORIGIN = os.getenv("DOZU_EMBEDDING_FILE_ORIGIN", "")
    FILE_TOKEN = os.getenv("DOZU_EMBEDDING_FILE_TOKEN", "")
    THREADS = int(os.getenv("DOZU_EMBEDDING_THREADS", "2"))
    MAX_FILE_BYTES = 32 * 1024 * 1024
    API_TITLE = "Dozu Embedding Service"
    API_VERSION = "1.0.0"

    def validate(self):
        if self.PROFILE not in {"website", "desktop"}:
            raise RuntimeError("Unknown embedding profile")
        if self.BACKEND not in {"torch", "onnx-int8"}:
            raise RuntimeError("Unknown embedding backend")
        if not 1 <= self.THREADS <= 8:
            raise RuntimeError("Embedding threads must be between 1 and 8")
        if self.PROFILE == "desktop" and len(self.SERVICE_TOKEN) < 32:
            raise RuntimeError("Desktop embedding requires a per-launch service token of at least 32 characters")


settings = Settings()
