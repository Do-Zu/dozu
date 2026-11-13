"""Turn resolver-selected wheels into an exact, platform-specific hash lock/inventory."""
import argparse
from email.parser import BytesParser
import hashlib
import json
from pathlib import Path
import zipfile
import urllib.request
from concurrent.futures import ThreadPoolExecutor

parser = argparse.ArgumentParser()
parser.add_argument("wheelhouse", type=Path)
parser.add_argument("output", type=Path)
parser.add_argument("--verify-pypi", action="store_true")
args = parser.parse_args()
rows = []
for wheel in sorted(args.wheelhouse.glob("*.whl")):
    with wheel.open("rb") as stream:
        sha = hashlib.file_digest(stream, "sha256").hexdigest()
    with zipfile.ZipFile(wheel) as archive:
        metadata = BytesParser().parsebytes(archive.read(next(n for n in archive.namelist() if n.endswith(".dist-info/METADATA"))))
        native = [n for n in archive.namelist() if n.endswith((".dll", ".pyd", ".so", ".dylib"))]
        licenses = [n for n in archive.namelist() if any(s in n.lower() for s in ["license", "notice", "copying"])]
    rows.append({"name": metadata["Name"], "version": metadata["Version"], "wheel": wheel.name,
                 "sha256": sha, "bytes": wheel.stat().st_size, "requiresDist": metadata.get_all("Requires-Dist", []),
                 "license": metadata.get("License-Expression") or metadata.get("License"),
                 "licenseFiles": licenses, "nativeFiles": native,
                 "provenance": f"https://pypi.org/pypi/{metadata['Name']}/{metadata['Version']}/json"})
assert rows and len({r["name"].lower() for r in rows}) == len(rows)
if args.verify_pypi:
    def verify(row):
        with urllib.request.urlopen(row["provenance"], timeout=30) as response:
            upstream = json.load(response)
        resource = next(f for f in upstream["urls"] if f["filename"] == row["wheel"])
        assert row["sha256"] == resource["digests"]["sha256"] and row["bytes"] == resource["size"]
        row["source"] = resource["url"]
        row["verifiedAgainstPyPI"] = True
    with ThreadPoolExecutor(max_workers=8) as pool:
        list(pool.map(verify, rows))
args.output.write_text("# Windows x64 CPython 3.13 candidate; builder installs offline with --require-hashes.\n" + "".join(
    f"{r['name']}=={r['version']} --hash=sha256:{r['sha256']}\n" for r in rows), encoding="utf-8")
args.output.with_suffix(".json").write_text(json.dumps({"target": "cp313-win_amd64", "packages": rows}, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"packages": len(rows), "wheelBytes": sum(r["bytes"] for r in rows), "nativeFiles": sum(len(r["nativeFiles"]) for r in rows)}))
