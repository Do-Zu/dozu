"""Desktop file boundary. Ownership integration still belongs to #34/#18."""
from pathlib import Path
from urllib.parse import urlsplit
import requests
from .config import settings


def read_pdf(source: str, timeout: int) -> bytes:
    try:
        return _read_pdf(source, timeout)
    except (ValueError, requests.RequestException) as exc:
        raise RuntimeError("Invalid or unavailable authenticated local PDF") from exc


def _read_pdf(source: str, timeout: int) -> bytes:
    parsed = urlsplit(source)
    if parsed.scheme.lower() in {"http", "https"}:
        origin = urlsplit(settings.FILE_ORIGIN)
        if (not settings.FILE_TOKEN or len(settings.FILE_TOKEN) < 32
            or origin.scheme != "http" or origin.hostname not in {"127.0.0.1", "::1"}
            or not origin.port or origin.path not in {"", "/"} or origin.query or origin.fragment
            or origin.username or origin.password
            or parsed.scheme != origin.scheme or parsed.netloc != origin.netloc
            or parsed.username or parsed.password or parsed.fragment):
            raise RuntimeError("PDF URL is outside the configured authenticated loopback origin")
        with requests.Session() as session:
            session.trust_env = False
            with session.get(source, headers={"Authorization": "Bearer " + settings.FILE_TOKEN},
                             timeout=timeout, allow_redirects=False, stream=True) as response:
                if response.status_code != 200:
                    raise RuntimeError("Authenticated local PDF request failed or redirected")
                chunks, size = [], 0
                for chunk in response.iter_content(65536):
                    size += len(chunk)
                    if size > settings.MAX_FILE_BYTES:
                        raise RuntimeError("PDF exceeds the local file size limit")
                    chunks.append(chunk)
                return b"".join(chunks)
    if source.startswith(("\\\\", "//")) or not settings.FILE_ROOT:
        raise RuntimeError("PDF requires a configured local file root")
    root, path = Path(settings.FILE_ROOT), Path(source)
    if not root.is_absolute() or not path.is_absolute():
        raise RuntimeError("PDF paths must be absolute")
    try:
        root, path = root.resolve(strict=True), path.resolve(strict=True)
        if not path.is_relative_to(root) or not path.is_file() or path.suffix.lower() != ".pdf":
            raise RuntimeError("PDF is outside the authorized file root")
        with path.open("rb") as stream:
            data = stream.read(settings.MAX_FILE_BYTES + 1)
        if len(data) > settings.MAX_FILE_BYTES:
            raise RuntimeError("PDF exceeds the local file size limit")
        return data
    except OSError as exc:
        raise RuntimeError("Local PDF is unavailable") from exc
