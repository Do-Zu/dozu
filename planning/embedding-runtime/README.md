# Issue #8 — offline CPU component evidence

2026-11-13. **In Progress; no issue acceptance box or native release gate is marked complete.** This work was explicitly started independently of unfinished #38/#34. #5 is completed; #38 is Ready, not completed; #34 remains Waiting on the disputed #4 gate. Dependency links and the unassigned owner are preserved. The latest #4 closure comments do not establish complete native packaging. [Focused live tracking snapshot](tracking-snapshot.json).

## Delivered component work

- The existing `services/embedding` FastAPI code now loads only the verified, pinned multilingual MiniLM payload. All model/tokenizer/config files have SHA256 and pinned upstream Git/LFS provenance; cached symlinks are dereferenced into regular package files. There is no Hub fallback, arbitrary model substitution or first-run download. The default remains the original CPU Torch baseline.
- Exact Windows x64 CPython 3.13 wheel/hash locks cover the full baseline closure (45 packages) and explicit ONNX evaluation closure (37 packages). Official PyPI hashes were checked. Native wheel filenames, dependency metadata and license inventories are retained. Python 3.13.7's official embeddable ZIP is pinned by checksum; its executable has a valid Python Software Foundation signature. These are candidate versions, pending #38/#48 production/security review.
- An offline assembler includes embedded Python, dependencies, selected model files, source, full wheel notices, Python license and supplemental versioned license texts. No developer cache, dotenv, registry credential, user data or speech-only resource is used as a runtime dependency. The child uses `-I -B` and an explicit embedded search path; its PATH has no developer Python/pip.
- Desktop startup binds to loopback, authenticates service requests, rejects browser Origins and unexpected Hosts, verifies resources and performs inference before readiness. Authenticated shutdown drains and exits 0; missing token/model or corrupt resources exit 1 without network attempts. Local PDF paths are canonicalized within a configured root; optional local HTTP URLs use a separate bearer credential and exact numeric loopback origin, with no redirects. User ownership/storage integration remains pending.
- `/segments/embedding` now returns the actual segment list instead of failing its incompatible dictionary response model. Text, metadata, PDF page references and existing transcript start-time references remain real consumers. No fake embedding, transcript, provider success or STT fallback is introduced. Segment/text limits and serialized batches bound individual inference work.

The retained website profile keeps its server-to-server topology and genuine signed remote PDF URLs; it also requires staged verified local model files. The legacy website Docker recipe was adjusted to include model verification metadata and resolve transitive wheels; **Docker/Linux execution was not tested**. No UI/API/database/Redis/payment/email source or original repository history was changed by #8.

## Measured results

Full data: [measurements](measurements.json), [native payload hashes](native-inventory-windows-x64.json), [host and Python signature](host.json), [baseline contracts](torch-contract.json), [ONNX contracts](onnx-contract.json), [quality comparison](quality-comparison.json).

Decimal MB (1 MB = 1,000,000 bytes). Installed size includes all component files and the package inventory itself; archives include those same files. Component ZIPs are not NSIS/application installers.

| Component | Original Torch FP32 | Upstream ONNX quint8 AVX2 candidate |
| --- | ---: | ---: |
| Complete component files | 21,688 | 4,188 |
| Installed component | 1,249.334 MB | 291.441 MB |
| Component ZIP | 658.610 MB | 133.070 MB |
| Backend/model ready | 11.007 s | 2.268 s |
| Ready process working set | 745.570 MB | 498.086 MB |
| Observed process peak through workload | 781.668 MB | 582.967 MB |
| Actual HTTP checks passed | 28 | 28 |
| Fail-closed startup cases passed | 3 | 3 |
| Graceful shutdown exit | 0 | 0 |

Windows 11 Pro 10.0.26300 x64, i5-13400F (10 cores/16 logical processors), 34,137,870,336 bytes physical RAM. Two inference threads, serial HTTP workload, fresh process profile/cache in Unicode/space paths. **OS file cache was not evicted.** Times include checksum verification/model load and real inference. Memory uses GetProcessMemoryInfo on the actual embedded Python PID; peak is the OS-reported process peak through requests, not a continuously sampled whole-app workload. Electron/Next/Express/PostgreSQL/Redis/converters are absent. This is neither the minimum hardware nor a clean machine; no Windows 10/macOS/Linux support or whole-app performance claim follows.

The tests use the packaged interpreter and actual service/model over HTTP, with a Python audit hook rejecting non-loopback DNS/connect/bind. This is **process-level denial, not an OS firewall test**. No denied non-loopback attempt occurred. Tests cover 384 finite normalized values, same-text cosine, mixed/empty batches, malformed input, PDF text and blank PDF, supplied English/Vietnamese transcript text and time references, Unicode paths, absolute-root traversal rejection, authenticated loopback PDF HTTP, redirect/external URL denial, service/Host/Origin authentication, shutdown and missing/corrupt resources. Real online YouTube retrieval is preserved but was not exercised; no provider availability claim is made. Package hashes and exact file sets match after all tests, with zero observed package writes on these writable copies. **Read-only installation remains untested/pending #34.**

### Smaller-runtime comparison

The ONNX file comes from the **same pinned model revision**, with explicit artifact path `onnx/model_quint8_avx2.onnx`, SHA256 and license. It uses the original tokenizer, 128-token truncation, attention-mask mean pooling and normalization; output remains 384-dimensional on CPU. No substitute English-only model is selected.

The hand-authored smoke set has 16 bilingual documents, 16 en/vi queries and four empty/Unicode/long inputs. Both representations produced a relevant top result for 15/16 queries and the same top document for all 16. Restricting candidates to the opposite language also produced 15/16 relevant results for each. This small fixture does not establish representative product quality.

Across 36 vectors, baseline-to-candidate cosine mean was 0.994861, minimum 0.984649; maximum absolute component difference was 0.031043. INT8 dynamic quantization also changes with batch composition: the single-versus-mixed-batch example had cosine 0.996469 and max component delta 0.014837. These are observed differences, not a relaxed equivalence threshold. Existing stored vectors/ranking, ties/topK, scale and representative English/Vietnamese retrieval must be reviewed under #8/#21/#29 before adopting this candidate.

**Recommendation:** do not ship the measured FP32/Torch representation under the unchanged 750 MB installed target: this component alone is about 1.249 GB. Continue the explicit ONNX candidate investigation, including full-stack normal/peak RAM, complete installer/installed footprint and minimum CPU/native compatibility, before selecting it. A 291 MB component and 133 MB ZIP do not prove the complete application's 750/250 MB targets. The 700 MB normal whole-app memory and startup targets are unchanged; this experiment does not pass them.

## Acceptance ledger — still open

| #8 criterion | Verified component evidence | Remaining acceptance |
| --- | --- | --- |
| Complete Python/native packaging; no user setup | Windows embedded interpreter, exact hashed closures, native payload inventory, actual CPU execution | Both packages load host Microsoft C++ libraries: baseline `msvcp140.dll`; ONNX `MSVCP140.dll` and `MSVCP140_1.dll`. Pin/provision permitted redistributables and verify clean targets under #38/#23. Other required OS/CPU locks and native proof are absent. |
| Pinned model and 384-vector contract | Baseline and explicit quantized artifact provenance/checksums; real finite normalized vectors | Production representation, representative en/vi quality/storage compatibility and complete release-resource selection are not approved. |
| Local resources without download/fallback | Fresh cache, verified installed paths, non-loopback denial, missing/corrupt resource failure | Installer verification, upgrade/resource tamper handling and complete platform integration remain pending. |
| Real text/PDF/transcript-text CPU consumers | 28 HTTP checks per representation; limited bilingual/cross-language smoke comparison | Express ingestion/storage/ranking and owner/topic isolation depend on #18/#21/#29; real online transcript-provider behavior and minimum-machine/full-stack tests remain unpassed. |
| Loopback readiness/shutdown and authenticated files | Per-launch service bearer, separate local file credential, canonical test root, positive/negative path/URL tests, graceful stop/nonzero failed startup | Final user root/permissions/ownership manifest and read-only installation require #34; supervisor and API token forwarding plus local storage require #28/#18. Canonical resolution is not proof against a concurrent hostile filesystem actor. |

No target or dependency link is rewritten. Redis stays; PostgreSQL stays without pgvector. Speech-to-text, speech-only assets, outgoing email and payment execution stay excluded per approved v1 scope. Page/media inventory is untouched. License files are retained, but final redistribution/security review is not certified by this component experiment.

## Reproduce

See [service build/launch contract](../../services/embedding/README.md). On a controlled Windows CPython 3.13 build host, acquire official resources/licenses and the **committed hash locks**, then assemble into fresh directories. Never run acquisition or pip on an end user's first launch. Model payloads/wheels/ZIPs are excluded from Git; checksums, license texts, source and sanitized evidence are tracked.

```powershell
python services/embedding/packaging/assemble_windows.py --backend torch --inputs planning/embedding-runtime/.downloads --destination "planning/embedding-runtime/.runs/Verified torch tiếng Việt"
python services/embedding/packaging/assemble_windows.py --backend onnx-int8 --inputs planning/embedding-runtime/.downloads --destination "planning/embedding-runtime/.runs/Verified onnx-int8 tiếng Việt"
python planning/embedding-runtime/verify_package.py "planning/embedding-runtime/.runs/Verified torch tiếng Việt" --output planning/embedding-runtime/torch-contract.json
python planning/embedding-runtime/verify_package.py "planning/embedding-runtime/.runs/Verified onnx-int8 tiếng Việt" --output planning/embedding-runtime/onnx-contract.json
python planning/embedding-runtime/compare_quality.py
python planning/embedding-runtime/summarize.py
```

Use new destination names when those copies already exist; assembly refuses overwrite. The first sandboxed pip attempt failed on its redirected temporary-directory permissions; the assembler now uses its own isolated build-temp directory. A sandboxed native startup timed out; the successful final runs occurred outside that sandbox with sanitized environments and the network-denial hook. These environment limitations are not passing native-target evidence. No credentials file was accessed.
