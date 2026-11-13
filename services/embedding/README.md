# Dozu text-embedding service

FastAPI service for retained text/PDF/YouTube transcript reference workflows. Speech-to-text is excluded. The default remains the exact multilingual MiniLM baseline on CPU; the smaller ONNX backend is an explicit evaluation candidate, not a selected production replacement.

The user accepted [larger initial desktop hardware/resource targets on 2026-11-14](../../planning/resource-contract-2026-11-14.md), keeping this baseline for initial integration and deferring optimization. Minimum validation is now 8 GB RAM/four physical cores/SSD, with 10 GB free before installation. Whole-app targets are installer ≤1.5 GB, installed ≤3 GB, normal/one-job peak RAM ≤2/3 GB, cold UI ≤15 s and full backend/model ready ≤30 s. Complete native packaging and actual minimum-device acceptance remain pending.

## Installed model contract

- Model: `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` at `86741b4e3f5cb7765a600d3a3d55a0f6a6cb443d`.
- 384 finite, unit-normalized floats; original 128-token truncation and mean pooling. No alternate model, GPU requirement, token, Hub fallback or startup download.
- `packaging/model-manifest.json` pins every model/tokenizer/config/card file by SHA256. Startup checks the selected backend's resources before loading and performs real inference before readiness.
- `requirements.txt` pins baseline direct dependencies. Complete **Windows x64 CPython 3.13 candidate** wheel/hash locks and native/license inventories are under `packaging/`. They are not Linux/macOS locks or a security-approved production version selection.

## Build-host acquisition and offline assembly

From the repository root, using a Windows x64 CPython 3.13 build interpreter with pip:

```powershell
python planning/embedding-runtime/acquire.py --model-source <existing-pinned-snapshot-directory>
python planning/embedding-runtime/acquire_licenses.py
python -m pip download --only-binary=:all: --require-hashes --dest planning/embedding-runtime/.downloads/wheels-torch -r services/embedding/packaging/requirements-torch-windows-x64.lock
python -m pip download --only-binary=:all: --require-hashes --dest planning/embedding-runtime/.downloads/wheels-onnx-pinned -r services/embedding/packaging/requirements-onnx-windows-x64.lock
python services/embedding/packaging/assemble_windows.py --backend torch --inputs planning/embedding-runtime/.downloads --destination <fresh-component-directory>
```

`acquire.py` copies cached baseline resources as regular files, verifies them against the pinned upstream Git/LFS objects, and obtains the official Python embeddable ZIP. Downloads run only on the controlled build host. Review generated provenance changes. Assembly verifies inputs and installs the hash-locked dependency closure offline into the embedded interpreter's isolated search path. It includes license texts/notices. End users do not run pip or install Python. `--backend onnx-int8` explicitly assembles the experimental upstream quantized representation and its separate closure.

**Native closure remains incomplete:** observed Microsoft C++ runtime DLLs load from this developer host. #38/#23 must pin/provision those redistributable prerequisites, review security/attribution and prove clean target machines. See [evidence and remaining gates](../../planning/embedding-runtime/README.md). These component directories are not self-contained release installers.

## Managed desktop process

Run `<component>/python/python.exe -I -B <component>/service/run.py` from any working directory. The supervisor supplies:

| Variable | Meaning |
| --- | --- |
| `DOZU_EMBEDDING_TOKEN` | Fresh per-launch bearer secret, at least 32 characters; never persist in release resources or log it |
| `DOZU_EMBEDDING_PORT` | Discovered loopback port; default 8686 |
| `DOZU_EMBEDDING_MODEL_PATH` | Absolute installed model directory; default is the component's `service/resources/model` |
| `DOZU_EMBEDDING_BACKEND` | `torch` default; `onnx-int8` evaluation only |
| `DOZU_EMBEDDING_THREADS` | 1–8; default 2; inference serialized in batches of at most 16 |
| `DOZU_EMBEDDING_FILE_ROOT` | Explicit authorized absolute local PDF root; final ownership/path integration waits for #34/#18 |
| `DOZU_EMBEDDING_FILE_ORIGIN` | Optional exact numeric HTTP loopback origin with port for a local authenticated file server |
| `DOZU_EMBEDDING_FILE_TOKEN` | Separate file-server bearer secret of at least 32 characters; redirects and external origins rejected |

The launcher defaults to the `desktop` profile, binds only `127.0.0.1`, and disables proxy-header trust. All desktop endpoints require `Authorization: Bearer <per-launch-token>` from loopback, reject browser Origin headers, and validate Host. `/health` succeeds only after checksum verification and CPU inference. Authenticated `POST /shutdown` drains through Uvicorn and unloads the model; startup failure exits nonzero.

`fileUrl` accepts an absolute PDF path within the canonical configured root or a URL on the exact authenticated loopback origin. Relative/UNC paths, root escapes, redirects and external URLs are rejected in desktop mode. PDF input is capped at 32 MiB. This is a component boundary: user/account ownership, caller token forwarding, durable local file storage, path-race/permission guarantees and read-only installation acceptance remain with #18/#28/#34.

## Retained website deployment

`DOZU_EMBEDDING_PROFILE=website` keeps the existing server-to-server website endpoint topology and signed remote PDF URLs. Deploy behind the existing website access controls. Supply the same verified local model directory; model startup never downloads in either profile. For developer execution, install the appropriate dependencies, then run `uvicorn src.app.main:app --host 127.0.0.1 --port 8686` from this directory with the website profile and model path configured. The legacy Docker recipe is website-only and unvalidated on Linux; mount verified model resources at `/opt/dozu-model` and set `DOZU_EMBEDDING_MODEL_PATH=/opt/dozu-model`. Native Linux dependency/image pinning remains pending, not covered by the Windows hash lock.

## HTTP contracts

| Endpoint | Input / result |
| --- | --- |
| `GET /health` | Model ID/revision, CPU/backend, dimension and readiness |
| `POST /single/text/embedding` | `{query: string}` → `{embedding: number[384]}` |
| `POST /segments/embedding` | `{segments: [{text, ...metadata}]}` → list of original segments plus embeddings; fixes the previous response-model 500 |
| `POST /embedding/compare` | `{query, pattern}` → similarity plus both vectors |
| `POST /pdf/page/embedding` | `{fileUrl}` → `{pageCount, embeddings: [{pageNumber, charCount, embedding}]}` |
| `POST /youtube/segments/embedding` | Supplied genuine transcript text/timestamps → `{count, embeddings}` |
| `POST /youtube/segments/similarity` | Supplied transcript text and query → ranked time references |
| `POST /youtube/segments` | Existing genuine provider transcript retrieval; requires internet, no speech recognition or synthetic transcript |

Text fields are bounded to 20,000 characters; supplied segment batches to 512. Empty text and empty batches retain valid behavior. Optional spaCy refinement is not included in either candidate closure; existing behavior without its optional model remains unchanged. No automatic spaCy download is performed.

## Verification

`planning/embedding-runtime/verify_package.py` exercises actual packaged CPU inference over HTTP with fresh Unicode/space user paths, no developer Python packages on the child search path and a process-level non-loopback network-denial guard. It covers text/batch/PDF/transcript text, security failures, missing/corrupt resources and graceful shutdown. `compare_quality.py` records limited en/vi numerical/retrieval smoke evidence. `summarize.py` verifies every package hash, detects runtime writes, inventories loaded native modules and measures complete component archives. Read the evidence limits before treating any result as release acceptance.
