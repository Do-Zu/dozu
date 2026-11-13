"""Verified CPU text vectors from a pinned multilingual model, with no fallback."""
import hashlib
import json
import os
from pathlib import Path
from threading import Lock
import numpy as np
from .config import settings

REVISION = "86741b4e3f5cb7765a600d3a3d55a0f6a6cb443d"
MODEL_ID = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
MANIFEST = Path(__file__).resolve().parents[3] / "packaging" / "model-manifest.json"


def verify_model(path: Path, backend: str):
    if not path.is_absolute() or not path.is_dir():
        raise RuntimeError("An absolute installed model directory is required")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if manifest["revision"] != REVISION or manifest["modelId"] != MODEL_ID:
        raise RuntimeError("Unexpected model provenance")
    entries = [f for f in manifest["files"] if backend in f["backends"]]
    if not entries:
        raise RuntimeError("Missing model resource manifest")
    for entry in entries:
        resource = (path / entry["path"]).resolve(strict=True)
        if not resource.is_relative_to(path.resolve()) or not resource.is_file():
            raise RuntimeError("Model resource escapes installed directory")
        with resource.open("rb") as stream:
            digest = hashlib.file_digest(stream, "sha256").hexdigest()
        if resource.stat().st_size != entry["bytes"] or digest != entry["sha256"]:
            raise RuntimeError(f"Model checksum mismatch: {entry['path']}")


class ModelManager:
    def __init__(self):
        self.model = None
        self.tokenizer = None
        self.lock = Lock()

    def load_model(self):
        settings.validate()
        verify_model(settings.MODEL_PATH, settings.BACKEND)
        os.environ["HF_HUB_OFFLINE"] = "1"
        os.environ["TRANSFORMERS_OFFLINE"] = "1"
        os.environ["HF_HUB_DISABLE_TELEMETRY"] = "1"
        os.environ["TOKENIZERS_PARALLELISM"] = "false"
        if settings.BACKEND == "torch":
            import torch
            from sentence_transformers import SentenceTransformer
            torch.set_num_threads(settings.THREADS)
            self.model = SentenceTransformer(str(settings.MODEL_PATH), device="cpu",
                local_files_only=True, trust_remote_code=False)
            if self.model.get_sentence_embedding_dimension() != 384 or self.model.max_seq_length != 128:
                raise RuntimeError("Unexpected baseline model contract")
        else:
            import onnxruntime as ort
            from tokenizers import Tokenizer
            self.tokenizer = Tokenizer.from_file(str(settings.MODEL_PATH / "tokenizer.json"))
            self.tokenizer.enable_truncation(max_length=128)
            self.tokenizer.enable_padding(pad_id=0, pad_token="[PAD]")
            options = ort.SessionOptions()
            options.intra_op_num_threads = settings.THREADS
            options.inter_op_num_threads = 1
            self.model = ort.InferenceSession(str(settings.MODEL_PATH / "onnx/model_quint8_avx2.onnx"),
                sess_options=options, providers=["CPUExecutionProvider"])
        self.embed_single("Readiness verifies real CPU inference.")

    def ensure_model(self):
        if self.model is None:
            raise RuntimeError("Model not loaded yet")

    def embed_batch(self, texts: list[str]):
        self.ensure_model()
        if not texts:
            return np.empty((0, 384), dtype=np.float32)
        result = []
        with self.lock:
            for offset in range(0, len(texts), 16):
                batch = texts[offset:offset + 16]
                if settings.BACKEND == "torch":
                    vectors = self.model.encode(batch, batch_size=16, normalize_embeddings=True,
                        convert_to_numpy=True, show_progress_bar=False)
                else:
                    encodings = self.tokenizer.encode_batch(batch)
                    inputs = {
                        "input_ids": np.array([e.ids for e in encodings], dtype=np.int64),
                        "attention_mask": np.array([e.attention_mask for e in encodings], dtype=np.int64),
                        "token_type_ids": np.array([e.type_ids for e in encodings], dtype=np.int64),
                    }
                    inputs = {i.name: inputs[i.name] for i in self.model.get_inputs()}
                    hidden = self.model.run(None, inputs)[0]
                    mask = inputs["attention_mask"][..., None].astype(np.float32)
                    vectors = (hidden * mask).sum(axis=1) / np.maximum(mask.sum(axis=1), 1e-9)
                    vectors /= np.maximum(np.linalg.norm(vectors, axis=1, keepdims=True), 1e-12)
                if vectors.shape != (len(batch), 384) or not np.isfinite(vectors).all():
                    raise RuntimeError("Embedding contract requires 384 finite values per text")
                if not np.allclose(np.linalg.norm(vectors, axis=1), 1, atol=1e-4):
                    raise RuntimeError("Embedding vectors must be normalized")
                result.append(vectors)
        return np.concatenate(result)

    def embed_single(self, text: str):
        return self.embed_batch([text])[0].tolist()

    def unload(self):
        self.model = None
        self.tokenizer = None

    def get_health_info(self):
        self.ensure_model()
        return {"status": "ok", "model": MODEL_ID, "revision": REVISION,
                "device": "cpu", "dimension": 384, "normalized": True, "backend": settings.BACKEND}


model_manager = ModelManager()
