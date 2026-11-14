# Candidate runtime and installed-resource manifests — #38

**2026-11-14: incomplete candidates, no supported clean target certified.** [Evidence, commands and acceptance ledger](../../planning/runtime-manifests/README.md). The approved [platform/resource contract](../../planning/platform-support.md) is unchanged. #7 supplies the JavaScript foundation only.

- [Artifact pins](artifact-candidates.json): official sources, exact versions/architectures/hashes, archive-byte verification distinguished from upstream metadata and native execution. PostgreSQL/Redis/Python **source** pins are not shipped binaries.
- [Target records](targets): Windows x64, macOS Intel/ARM64, Linux x64; explicit nulls and [gates](gates.json) prevent unresolved cells being interpreted as success.
- [Foreign Python wheel availability](embedding-wheel-availability.json): CPython 3.13/compatible stable-ABI metadata, not resolved foreign locks. CPU Linux Torch has a separate official-index candidate; default Linux PyPI Torch is not a CPU-only selection.
- [Windows PE inventory](native-windows-x64.json): actual file hashes, machine types, normal and delay imports; basename availability is not loader resolution.
- [Microsoft CRT candidates](microsoft-crt-candidate.json): signed, versioned files in a Visual Studio **Redist** directory; redistribution entitlement and app-local placement remain gates. Never harvest DLLs from System32.
- [Primary license evidence](license-evidence.json) and [texts](licenses): archive-bound primary notices. Complete third-party/binary/model redistribution approval remains open.
- [Installed component candidates](installed-candidates): verified Windows Node/Electron leaf inventories, explicitly inspection-only. Electron still contains its upstream demo app. These are not complete Dozu installed-resource manifests.

Initial runtime strategy: separate pinned standalone Node children for Next and Express; Electron owns supervision/windowing. Electron's embedded Node does not load application native dependencies. Standalone Node's Windows probe reports ABI 127/Node-API 10. Electron 45.2.3's earlier utility-process probe reports ABI 150/Node-API 10; equal Node-API levels do not make arbitrary native binaries ABI-compatible. Final supervisor/fuse/security integration is unpassed.

The required installed resource set must contain the complete existing UI, Express production closure, PostgreSQL tools/lib/share, native Redis, isolated Python CPU embedding closure, pinned model/tokenizer/config/card/notices, local PDF workers, fonts, media and native conversion/browser resources. STT/whisper, SMTP, payment execution and pgvector are excluded. Electron's `ffmpeg.dll` remains an intrinsic browser media dependency, distinct from an external STT FFmpeg executable. No user runtime download/package manager, central Dozu service or cloud database is introduced.

`tooling/resource-integrity.cjs` generates and verifies an explicit allowlisted file/directory/link inventory offline. A trusted digest and expected target/resource-set must come from the signed package/supervisor. A checksum stored beside mutable resources is not authentication. See the [integrity/upgrade contract](../../planning/runtime-manifests/integrity-and-upgrades.md) before integrating it.
