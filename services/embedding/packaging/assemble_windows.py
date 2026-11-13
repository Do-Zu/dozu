"""Offline build-host assembly. End users run the resulting bundled interpreter, never pip."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import zipfile

HERE = Path(__file__).resolve().parent
SERVICE = HERE.parent
ROOT = SERVICE.parents[1]


def sha(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--backend", choices=["torch", "onnx-int8"], required=True)
    parser.add_argument("--inputs", type=Path, required=True)
    parser.add_argument("--destination", type=Path, required=True)
    args = parser.parse_args()
    if sys.platform != "win32" or sys.version_info[:2] != (3, 13):
        raise RuntimeError("This assembly requires a Windows x64 CPython 3.13 build host")
    destination = args.destination.resolve()
    if destination.exists():
        raise RuntimeError("Choose a fresh destination; assembly never overwrites artifacts")
    inputs = args.inputs.resolve()
    suffix = "torch" if args.backend == "torch" else "onnx"
    wheelhouse = inputs / ("wheels-torch" if suffix == "torch" else "wheels-onnx-pinned")
    runtime_manifest = json.loads((HERE / "python-windows-x64.json").read_text())
    runtime_zip = inputs / "python-3.13.7-embed-amd64.zip"
    assert sha(runtime_zip) == runtime_manifest["sha256"]
    model_manifest = json.loads((HERE / "model-manifest.json").read_text())
    # Verify all inputs before executing any extracted runtime or native package.
    for row in model_manifest["files"]:
        if args.backend in row["backends"]:
            assert sha(inputs / "model" / row["path"]) == row["sha256"]
    with zipfile.ZipFile(runtime_zip) as archive:
        archive.extractall(destination / "python")
    packaged_service = destination / "service"
    shutil.copytree(SERVICE / "src", packaged_service / "src", ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    shutil.copyfile(SERVICE / "run.py", packaged_service / "run.py")
    (packaged_service / "packaging").mkdir()
    for name in ["model-manifest.json", "python-windows-x64.json", f"requirements-{suffix}-windows-x64.lock", f"requirements-{suffix}-windows-x64.json"]:
        shutil.copyfile(HERE / name, packaged_service / "packaging" / name)
    shutil.copytree(HERE / "licenses", destination / "licenses")
    for row in model_manifest["files"]:
        if args.backend in row["backends"]:
            target = packaged_service / "resources/model" / row["path"]
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(inputs / "model" / row["path"], target)
    target_site = destination / "python/Lib/site-packages"
    environment = {k: v for k, v in os.environ.items() if k.upper() in {"SYSTEMROOT", "WINDIR", "TEMP", "TMP", "PATH"}}
    build_temp = destination.parent / (destination.name + " build-temp")
    build_temp.mkdir()
    environment.update(TEMP=str(build_temp), TMP=str(build_temp), PIP_CONFIG_FILE=os.devnull)
    result = subprocess.run([sys.executable, "-m", "pip", "install", "--no-index", "--require-hashes",
        "--only-binary=:all:", "--find-links", str(wheelhouse), "--target", str(target_site),
        "--no-compile", "--disable-pip-version-check", "-r", str(HERE / f"requirements-{suffix}-windows-x64.lock")],
        env=environment, capture_output=True, text=True)
    (destination / "build-install.log").write_text(result.stdout + result.stderr, encoding="utf-8")
    result.check_returncode()
    (destination / "python/python313._pth").write_text("python313.zip\n.\nLib/site-packages\n../service\nimport site\n", encoding="utf-8")
    rows = [{"path": p.relative_to(destination).as_posix(), "bytes": p.stat().st_size, "sha256": sha(p)}
            for p in sorted(destination.rglob("*")) if p.is_file()]
    manifest = {"target": "windows-x64-cp313", "backend": args.backend, "files": rows,
                "installedBytes": sum(r["bytes"] for r in rows),
                "nativeFiles": [r for r in rows if r["path"].endswith((".exe", ".dll", ".pyd"))],
                "scope": "Component package, not whole-app installer or clean-target compatibility proof"}
    # Count the inventory itself in installed footprint; omit its self-referential hash.
    payload_bytes = manifest["installedBytes"]
    for _ in range(4):
        encoded = (json.dumps(manifest, indent=2) + "\n").encode("utf-8")
        manifest["installedBytes"] = payload_bytes + len(encoded)
    (destination / "package-manifest.json").write_bytes((json.dumps(manifest, indent=2) + "\n").encode("utf-8"))
    print(json.dumps({k: v for k, v in manifest.items() if k not in {"files", "nativeFiles"}}))


if __name__ == "__main__":
    main()
