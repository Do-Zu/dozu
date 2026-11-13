"""Summarize file integrity, native closure gaps and component footprints without hiding resources."""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import zipfile

HERE = Path(__file__).resolve().parent


def digest(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def summarize(name):
    report = json.loads((HERE / (name + "-contract.json")).read_text(encoding="utf-8"))
    package = Path(report["package"])
    manifest = json.loads((package / "package-manifest.json").read_text(encoding="utf-8"))
    def verify(row):
        path = package / row["path"]
        assert path.is_file() and path.stat().st_size == row["bytes"] and digest(path) == row["sha256"], row["path"]
    with ThreadPoolExecutor(max_workers=8) as pool:
        list(pool.map(verify, manifest["files"]))
    paths = [p for p in package.rglob("*") if p.is_file()]
    actual = {p.relative_to(package).as_posix() for p in paths}
    assert actual == {r["path"] for r in manifest["files"]} | {"package-manifest.json"}, "Unexpected runtime writes"
    archive = package.parent / ("component-" + name + ".zip")
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zipped:
        for path in sorted(paths):
            info = zipfile.ZipInfo(path.relative_to(package).as_posix(), date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            with zipped.open(info, "w") as out, path.open("rb") as source:
                while chunk := source.read(1024 * 1024): out.write(chunk)
    native = report["afterInferenceMemory"]["modules"]
    external = [p for p in native if not Path(p).is_relative_to(package)]
    msvc = [p for p in external if Path(p).name.lower().startswith(("msvcp140", "vcruntime140", "concrt140"))]
    rows = {"backend": report["backend"], "verifiedPackageFiles": len(paths), "unexpectedRuntimeWrites": 0,
        "installedBytesIncludingInventory": sum(p.stat().st_size for p in paths),
        "componentZipBytes": archive.stat().st_size, "componentZipSha256": digest(archive),
        "zipScope": "Embedding component archive, not the application installer",
        "backendReadySeconds": report["backendReadySeconds"], "readyWorkingSetBytes": report["readyMemory"]["workingSetBytes"],
        "observedProcessPeakWorkingSetBytes": report["afterInferenceMemory"]["peakWorkingSetBytes"],
        "nativeBundledModuleCount": len(native) - len(external), "externalLoadedModules": external,
        "unbundledMicrosoftRuntimeModules": msvc,
        "nativeClosure": "NOT COMPLETE: host VC++ runtime dependency must be pinned/provisioned and verified on clean targets under #38/#23",
        "freshProfile": True, "offlineContractPass": report["pass"], "httpChecks": len(report["checks"]),
        "packageManifestSha256": digest(package / "package-manifest.json"), "sourceManifest": str(package / "package-manifest.json")}
    return rows


summaries = [summarize(n) for n in ["onnx", "torch"]]
host = {"os": platform.platform(), "note": "Windows 11 Pro 10.0.26300; i5-13400F 10 cores/16 threads; physical RAM 34137870336 bytes. Developer host, not minimum 4GB/dual-core or clean machine. OS file cache was not evicted. Two inference threads; serial contract workload. Measurements include embedding process only; no whole-app/UI-ready/installer assertion."}
(HERE / "measurements.json").write_text(json.dumps({"host": host, "components": summaries}, indent=2) + "\n", encoding="utf-8")
native_payloads = []
for name in ["onnx", "torch"]:
    contract = json.loads((HERE / (name + "-contract.json")).read_text(encoding="utf-8"))
    manifest_path = Path(contract["package"]) / "package-manifest.json"
    native_payloads.append({"backend": contract["backend"], "packageManifestSha256": digest(manifest_path),
        "files": json.loads(manifest_path.read_text(encoding="utf-8"))["nativeFiles"]})
(HERE / "native-inventory-windows-x64.json").write_text(json.dumps({
    "scope": "Bundled native file hashes; loaded host VC++ gaps are separately listed in measurements.json",
    "components": native_payloads}, indent=2) + "\n", encoding="utf-8")
print(json.dumps([{k: s[k] for k in ["backend", "installedBytesIncludingInventory", "componentZipBytes", "readyWorkingSetBytes", "unbundledMicrosoftRuntimeModules"]} for s in summaries]))
