"""Controlled build-host acquisition, never called by service startup or an installer."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import urllib.request

ROOT = Path(__file__).resolve().parents[2]
SERVICE = ROOT / "services/embedding"
OUT = Path(__file__).resolve().parent
REVISION = "86741b4e3f5cb7765a600d3a3d55a0f6a6cb443d"
MODEL_ID = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
FILES = ["config.json", "config_sentence_transformers.json", "model.safetensors", "modules.json",
         "README.md", "sentence_bert_config.json", "special_tokens_map.json", "tokenizer.json",
         "tokenizer_config.json", "1_Pooling/config.json", "onnx/model_quint8_avx2.onnx"]


def digest(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def download(url, destination):
    destination.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url, timeout=60) as response, destination.open("wb") as stream:
        shutil.copyfileobj(response, stream)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-source", type=Path, required=True)
    args = parser.parse_args()
    url = f"https://huggingface.co/api/models/{MODEL_ID}/revision/{REVISION}?blobs=true"
    with urllib.request.urlopen(url, timeout=30) as response:
        metadata = json.load(response)
    assert metadata["sha"] == REVISION
    siblings = {f["rfilename"]: f for f in metadata["siblings"]}
    rows = []
    for name in FILES:
        destination = OUT / ".downloads/model" / name
        source = args.model_source / name
        remote = siblings[name]
        source_url = f"https://huggingface.co/{MODEL_ID}/resolve/{REVISION}/{name}"
        if not destination.exists():
            destination.parent.mkdir(parents=True, exist_ok=True)
            if source.is_file():
                shutil.copyfile(source, destination)  # dereference cached symlinks into actual payload
            else:
                download(source_url, destination)
        sha = digest(destination)
        if remote.get("lfs"):
            assert sha == remote["lfs"]["sha256"] and destination.stat().st_size == remote["lfs"]["size"]
        else:
            data = destination.read_bytes()
            assert hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest() == remote["blobId"]
        rows.append({"path": name, "bytes": destination.stat().st_size, "sha256": sha,
                     "source": source_url, "upstreamGitBlob": remote["blobId"],
                     "backends": ["onnx-int8"] if name.startswith("onnx/") else
                                 ["torch"] if name == "model.safetensors" else ["torch", "onnx-int8"]})
        print(name, destination.stat().st_size, flush=True)
    manifest = {"modelId": MODEL_ID, "revision": REVISION, "license": "Apache-2.0",
                "licenseEvidence": f"https://huggingface.co/{MODEL_ID}/blob/{REVISION}/README.md",
                "dimension": 384, "maxSequenceLength": 128, "normalized": True,
                "verification": "SHA256 equals upstream LFS SHA256 or bytes equal upstream Git blob SHA1; regular copied files", "files": rows}
    (SERVICE / "packaging/model-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    python_url = "https://www.python.org/ftp/python/3.13.7/python-3.13.7-embed-amd64.zip"
    python_zip = OUT / ".downloads/python-3.13.7-embed-amd64.zip"
    if not python_zip.exists():
        download(python_url, python_zip)
    runtime = {"version": "3.13.7", "architecture": "win-amd64", "source": python_url,
               "sha256": digest(python_zip), "bytes": python_zip.stat().st_size,
               "status": "Candidate for native Windows 11 host proof only; #38/#48 must review production version and clean-target compatibility"}
    (SERVICE / "packaging/python-windows-x64.json").write_text(json.dumps(runtime, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
