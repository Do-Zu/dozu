"""Measured en/vi numerical and retrieval smoke comparison; never selects the candidate."""
import json
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
fixture = json.loads((HERE / "retrieval-fixture.json").read_text(encoding="utf-8"))
baseline = json.loads((HERE / "torch-contract.json").read_text(encoding="utf-8"))
candidate = json.loads((HERE / "onnx-contract.json").read_text(encoding="utf-8"))
a = np.array(json.loads(Path(baseline["vectors"]).read_text()), dtype=float)
b = np.array(json.loads(Path(candidate["vectors"]).read_text()), dtype=float)
assert a.shape == b.shape == (36, 384)
count = len(fixture["documents"])
rows = []
cross_language = []
for i, query in enumerate(fixture["queries"]):
    aa = np.argsort(-(a[:count] @ a[count + i]), kind="stable")[:3].tolist()
    bb = np.argsort(-(b[:count] @ b[count + i]), kind="stable")[:3].tolist()
    rows.append({"query": query["text"], "expectedTopic": query["topic"], "baselineTop3": aa, "candidateTop3": bb,
        "baselineTop1Relevant": fixture["documents"][aa[0]]["topic"] == query["topic"],
        "candidateTop1Relevant": fixture["documents"][bb[0]]["topic"] == query["topic"],
        "sameTop1": aa[0] == bb[0], "top3Overlap": len(set(aa) & set(bb)) / 3})
    opposite = np.array([j for j in range(count) if j % 2 != i % 2])
    cross_a = int(opposite[np.argmax(a[opposite] @ a[count + i])])
    cross_b = int(opposite[np.argmax(b[opposite] @ b[count + i])])
    cross_language.append({"queryIndex": i, "baselineTop1": cross_a, "candidateTop1": cross_b,
        "baselineRelevant": fixture["documents"][cross_a]["topic"] == query["topic"],
        "candidateRelevant": fixture["documents"][cross_b]["topic"] == query["topic"]})
cosines = (a * b).sum(axis=1)
report = {"modelRevision": baseline["health"]["revision"], "baseline": "torch-fp32", "candidate": "upstream ONNX dynamic quint8 AVX2",
    "fixture": "16 bilingual documents, 16 en/vi queries, 4 empty/Unicode/long inputs; hand-authored component smoke only",
    "vectorCount": len(a), "dimension": 384, "maximumAbsoluteDelta": float(abs(a - b).max()),
    "meanVectorCosine": float(cosines.mean()), "minimumVectorCosine": float(cosines.min()),
    "baselineTop1Relevant": sum(r["baselineTop1Relevant"] for r in rows),
    "candidateTop1Relevant": sum(r["candidateTop1Relevant"] for r in rows),
    "sameTop1Count": sum(r["sameTop1"] for r in rows), "queries": rows,
    "oppositeLanguageOnly": {"baselineRelevant": sum(r["baselineRelevant"] for r in cross_language),
        "candidateRelevant": sum(r["candidateRelevant"] for r in cross_language), "queries": cross_language},
    "candidateSingleVersusMixedBatch": candidate["singleVersusBatch"],
    "decision": "Evaluation only. No default model/backend change, no broad en/vi quality equivalence claim, no agreed budget relaxed. Requires representative user corpus/ranking/storage compatibility review under #8/#21/#29 before selection."}
(HERE / "quality-comparison.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps({k: v for k, v in report.items() if k not in {"queries", "decision"}}))
