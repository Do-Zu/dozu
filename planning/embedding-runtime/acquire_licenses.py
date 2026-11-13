"""Fill wheel attribution gaps from versioned upstream license sources."""
import hashlib
import json
from pathlib import Path
import urllib.request

OUT = Path(__file__).resolve().parents[2] / "services/embedding/packaging/licenses"
OUT.mkdir(exist_ok=True)
SOURCES = {
    "model-Apache-2.0.txt": "https://www.apache.org/licenses/LICENSE-2.0.txt",
    "tokenizers-0.22.1-LICENSE.txt": "https://raw.githubusercontent.com/huggingface/tokenizers/v0.22.1/LICENSE",
    "tqdm-4.67.1-LICENCE.txt": "https://raw.githubusercontent.com/tqdm/tqdm/v4.67.1/LICENCE",
    "flatbuffers-25.12.19-LICENSE.txt": "https://raw.githubusercontent.com/google/flatbuffers/v25.12.19/LICENSE",
}
rows = []
for name, source in SOURCES.items():
    with urllib.request.urlopen(source, timeout=30) as response:
        data = response.read()
    (OUT / name).write_bytes(data)
    rows.append({"path": name, "source": source, "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)})
(OUT / "provenance.json").write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"licenseFiles": len(rows)}))
