"""Explicit build-host provenance refresh. Never imported by app/installer startup.

Fetches official metadata and selected archives, records hashes, and does not install
or execute downloads. Review generated JSON before committing; this is not approval.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import html
import json
from pathlib import Path
import re
import shutil
import urllib.request
import urllib.parse

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = ROOT / "resources/manifests"
CACHE = HERE / ".downloads"


def sha(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def get(url):
    request = urllib.request.Request(url, headers={"User-Agent": "Dozu-build-provenance/38"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read()


def download(url, name, expected=None):
    path = CACHE / name
    if not path.exists():
        partial = path.with_suffix(path.suffix + ".partial")
        request = urllib.request.Request(url, headers={"User-Agent": "Dozu-build-provenance/38"})
        with urllib.request.urlopen(request, timeout=30) as response, partial.open("wb") as stream:
            shutil.copyfileobj(response, stream)
        partial.replace(path)
    actual = sha(path)
    if expected and actual != expected:
        raise ValueError(f"Checksum mismatch: {name}")
    return {"source": url, "filename": name, "sha256": actual, "bytes": path.stat().st_size,
            "archiveBytesVerified": True}


def save(name, data):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true", required=True)
    parser.add_argument("--electron-metadata", type=Path, help="Optional authenticated gh api release snapshot")
    args = parser.parse_args()
    CACHE.mkdir(parents=True, exist_ok=True)
    rows = []
    release_url = "https://api.github.com/repos/electron/electron/releases/tags/v45.2.3"
    release = json.loads(args.electron_metadata.read_text(encoding="utf-8-sig")) if args.electron_metadata else json.loads(get(release_url))
    assert release["tag_name"] == "v45.2.3"
    assets = {a["name"]: a for a in release["assets"]}
    sums_asset = assets["SHASUMS256.txt"]
    sums = get(sums_asset["browser_download_url"])
    assert hashlib.sha256(sums).hexdigest() == sums_asset["digest"].removeprefix("sha256:")
    expected = {line.split()[-1].lstrip("*"): line.split()[0] for line in sums.decode().splitlines()}
    for target, arch in [("win32-x64", "x64"), ("darwin-x64", "x64"), ("darwin-arm64", "arm64"), ("linux-x64", "x64")]:
        name = f"electron-v45.2.3-{target}.zip"
        a = assets[name]
        digest = a["digest"].removeprefix("sha256:")
        assert digest == expected[name]
        row = {"id": f"electron-{target}", "component": "electron", "version": "45.2.3", "target": target,
               "architecture": arch, "source": a["browser_download_url"], "filename": name,
               "sha256": digest, "bytes": a["size"], "provenance": release_url,
               "checksumEvidence": sums_asset["browser_download_url"], "checksumEvidenceSha256": hashlib.sha256(sums).hexdigest(),
               "archiveBytesVerified": False, "nativeExecutionVerified": False, "license": "MIT + Chromium/third-party notices"}
        if target == "win32-x64":
            row.update(download(row["source"], name, digest))
        rows.append(row)
    node_base = "https://nodejs.org/dist/v22.22.0/"
    node_sums = get(node_base + "SHASUMS256.txt")
    node_hashes = {line.split()[-1].lstrip("*"): line.split()[0] for line in node_sums.decode().splitlines()}
    for target, arch in [("win-x64", "x64"), ("darwin-x64", "x64"), ("darwin-arm64", "arm64"), ("linux-x64", "x64")]:
        name = f"node-v22.22.0-{target}." + ("zip" if target == "win-x64" else "tar.gz")
        row = {"id": f"node-{target}", "component": "node", "version": "22.22.0", "target": target, "architecture": arch,
               "source": node_base + name, "filename": name, "sha256": node_hashes[name],
               "checksumEvidence": node_base + "SHASUMS256.txt", "checksumEvidenceSha256": hashlib.sha256(node_sums).hexdigest(),
               "archiveBytesVerified": False, "nativeExecutionVerified": False, "license": "MIT + bundled dependency notices",
               "signatureVerification": "OpenPGP release-key verification pending; HTTPS checksum comparison only"}
        if target == "win-x64":
            row.update(download(row["source"], name, row["sha256"]))
        rows.append(row)
    pg_base = "https://ftp.postgresql.org/pub/source/v17.12/"
    name = "postgresql-17.12.tar.bz2"
    pg_digest = get(pg_base + name + ".sha256").decode().split()[0]
    rows.append({"id": "postgresql-source", "component": "postgresql", "version": "17.12", "target": "source-only",
                 "architecture": "source", "checksumEvidence": pg_base + name + ".sha256",
                 "license": "PostgreSQL", "nativeExecutionVerified": False, **download(pg_base + name, name, pg_digest)})
    # Current official EDB index resolves fileid=1260667 to this versioned archive.
    pg_windows = download('https://sbp.enterprisedb.com/getfile.jsp?fileid=1260667', 'postgresql-17.12-1-windows-x64-binaries.zip')
    rows.append({"id": "postgresql-win32-x64", "component": "postgresql", "version": "17.12-1", "target": "win32-x64", "architecture": "x64",
                 "provenance": "https://www.enterprisedb.com/download-postgresql-binaries",
                 "checksumEvidence": "Computed from official HTTPS archive; independently published checksum/signature binding pending",
                 "license": "PostgreSQL + EDB archive dependency notices", "nativeExecutionVerified": False, **pg_windows})
    redis_hash_revision = "8feaeea1ac6ee82ca026a9f3c8b39eb280593929"
    redis_hash_url = f"https://raw.githubusercontent.com/redis/redis-hashes/{redis_hash_revision}/README"
    redis_hashes = get(redis_hash_url).decode()
    entries = re.findall(r"hash redis-(7\.2\.\d+)\.tar\.gz sha256 ([a-f0-9]{64})", redis_hashes)
    assert entries, "No pinned BSD-branch Redis source found"
    version, digest = max(entries, key=lambda x: tuple(map(int, x[0].split('.'))))
    name = f"redis-{version}.tar.gz"
    rows.append({"id": "redis-source", "component": "redis", "version": version, "target": "source-only",
                 "architecture": "source", "checksumEvidence": redis_hash_url, "license": "BSD-3-Clause (7.2 branch; bundled deps separately)",
                 "nativeExecutionVerified": False, **download("https://download.redis.io/releases/" + name, name, digest)})
    name = "Python-3.13.7.tar.xz"
    rows.append({"id": "python-source", "component": "python", "version": "3.13.7", "target": "source-only", "architecture": "source",
                 "license": "PSF-2.0 + bundled notices", "checksumEvidence": "Computed from HTTPS download; independent signed-source verification pending",
                 "nativeExecutionVerified": False, **download("https://www.python.org/ftp/python/3.13.7/" + name, name)})
    py = json.loads((ROOT / "services/embedding/packaging/python-windows-x64.json").read_text())
    old_path = ROOT / "planning/embedding-runtime/.downloads" / "python-3.13.7-embed-amd64.zip"
    assert sha(old_path) == py["sha256"]
    rows.append({**py, "id": "python-win32-x64", "component": "python", "target": "win32-x64", "architecture": "x64",
                 "filename": old_path.name, "archiveBytesVerified": True, "nativeExecutionVerified": False,
                 "license": "PSF-2.0 + bundled notices", "executionEvidence": "planning/embedding-runtime/torch-contract.json (developer host only)"})
    save("artifact-candidates.json", {"schemaVersion": 1, "status": "candidate-not-release", "reviewDate": "2026-11-14",
         "notice": "Hashes are not security approval, architecture execution, clean-machine support or reproducible-build proof. Source archives are not shipping binaries.",
         "artifacts": rows})
    # Inventory exact baseline wheel availability without treating foreign wheels as tested locks.
    packages = json.loads((ROOT / "services/embedding/packaging/requirements-torch-windows-x64.json").read_text())["packages"]
    def availability(p):
        data = json.loads(get(p["provenance"]))
        wheels = [{"filename": f["filename"], "source": f["url"], "sha256": f["digests"]["sha256"], "bytes": f["size"],
                   "requiresPython": f.get("requires_python"), "yanked": f.get("yanked", False)}
                  for f in data["urls"] if f["filename"].endswith(".whl") and "cp313t" not in f["filename"] and
                  ("-cp313-" in f["filename"] or "-abi3-" in f["filename"] or "-none-any.whl" in f["filename"]) and
                  ("macosx" in f["filename"] or "manylinux" in f["filename"] or "none-any" in f["filename"])]
        return {"name": p["name"], "version": p["version"], "provenance": p["provenance"], "wheels": wheels}
    with ThreadPoolExecutor(max_workers=6) as pool:
        availability_rows = list(pool.map(availability, packages))
    cpu_index = 'https://download.pytorch.org/whl/cpu/torch/'
    cpu_links = []
    for url in re.findall(r'href="([^"]+)"', get(cpu_index).decode()):
        url = html.unescape(urllib.parse.urljoin(cpu_index, url))
        name = urllib.parse.unquote(urllib.parse.urlsplit(url).path.rsplit('/', 1)[-1])
        if name == 'torch-2.9.1+cpu-cp313-cp313-manylinux_2_28_x86_64.whl':
            digest = urllib.parse.urlsplit(url).fragment.removeprefix('sha256=')
            assert re.fullmatch('[a-f0-9]{64}', digest)
            cpu_links.append({'filename': name, 'source': url.split('#')[0], 'sha256': digest,
                              'provenance': cpu_index, 'archiveBytesVerified': False})
    assert len(cpu_links) == 1
    save("embedding-wheel-availability.json", {"status": "metadata-only-not-resolved-locks", "pythonABI": "cp313",
         "limitations": "No foreign wheels downloaded/loaded. Platform tag/minimum OS, marker resolution, CPU-only Torch source, transitive closure and ABI checks remain required.",
         "torchCpuIndexCandidates": cpu_links, "packages": availability_rows})
    print(json.dumps({"artifacts": len(rows), "foreignWheelPackages": len(packages), "redisVersion": version}))


if __name__ == "__main__":
    main()
