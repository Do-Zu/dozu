<!-- dozu-embedding-component-ac-review-2026-11-14:start -->
## AC review after accepted resource revision — 2026-11-14

The original five release ACs above remain open. The resource amendment removes the old size-budget objection to the default pinned CPU baseline and defers ONNX optimization; it does not complete native packaging or final installation acceptance. The following **Windows developer-host component checks** are verified by [commit 66db470 and its evidence](https://github.com/Do-Zu/dozu/blob/66db470989b7f66280f3d1d4e4ba6ce82db834e0/planning/embedding-runtime/README.md), not full supported-platform release claims:

- [x] Exact 45-package baseline and 37-package ONNX candidate Windows CPython 3.13 wheel/hash closures, official artifact provenance and license/native inventories recorded.
- [x] Model/tokenizer/config files pinned to revision 86741b4e3f5cb7765a600d3a3d55a0f6a6cb443d; baseline CPU vectors have 384 finite normalized values.
- [x] Real packaged startup from local resources with fresh process caches and non-loopback process-level network denial; no Hub fallback or runtime/model download attempt observed.
- [x] Actual text, mixed/empty batch, PDF page and supplied transcript-text/time-reference HTTP contracts exercised: 28 checks per package, including security failures.
- [x] Missing token/model and corrupt resources exit nonzero; authenticated graceful shutdown exits 0: three failure cases per package.
- [x] Authenticated loopback PDF URLs and canonical test-root boundaries exercised in Unicode/space paths; package integrity/file sets unchanged after tests.
- [x] Baseline component measured at 1,249,334,226 installed bytes and 658,610,092 ZIP bytes, below the revised 3 GB/1.5 GB allowances **for the component alone**. This is not full-app installer/installed acceptance.
- [ ] Complete native dependency closure and clean supported OS/CPU proof: host Microsoft C++ runtime DLLs remain observed; #38/#23.
- [ ] Final owned user paths, permissions/read-only installation and actual API/supervisor integration: #34/#18/#28.
- [ ] Whole-app 8 GB/four-core SSD acceptance, combined 2 GB normal/3 GB peak RAM, 15 s UI/30 s full readiness, genuine installer/installed footprint and retained full workflows: #22/#23/#21/#29 and native owners.

No original release AC, issue state/owner or dependency link is changed by this component checklist. ONNX optimization/representation equivalence is deferred, while required baseline semantic behavior and English/Vietnamese workflow evidence remain release obligations. [Current cross-issue AC review](https://github.com/Do-Zu/dozu/blob/dev/planning/resource-amendment-2026-11-14/acceptance-review.md).
<!-- dozu-embedding-component-ac-review-2026-11-14:end -->
