"""Targeted accepted-contract publication. Does not change issue state/labels/owners/dependencies."""
import argparse
import json
from pathlib import Path
import re
import subprocess

HERE = Path(__file__).resolve().parent
PLANNING = HERE.parent
RUN = HERE / ".runs"
CONTRACT = (PLANNING / "resource-contract-2026-11-14.md").read_text(encoding="utf-8").strip()
COMPONENT = (HERE / "issue-8-component-review.md").read_text(encoding="utf-8").strip()
START = "<!-- dozu-resource-contract-2026-11-14:start -->"
END = "<!-- dozu-resource-contract-2026-11-14:end -->"
META = ["number", "title", "state", "stateReason", "labels", "assignees", "projectItems"]
RELEASE_OWNERS = {1, 2, 8, 22, 23, 25, 26, 28, 33, 34, 35, 36, 38, 46, 47, 49}
NATIVE_AC = ("- [ ] Measure the complete installer ≤1.5 GB and installed application ≤3 GB; all app-owned process "
    "normal memory ≤2 GB and peak during one ingestion/embedding job ≤3 GB; cold UI ≤15 s, complete backend/model ready ≤30 s; "
    "warm UI ≤5 s minimum/≤3 s recommended. Validate actual 8 GB/four-physical-core SSD hardware with 10 GB free before "
    "installation (16 GB/6–8 cores/20 GB free recommended). Record complete resources, cache/network/concurrency, processing peaks "
    "and actual upgrade/backup staging requirements; component proof does not pass the full-app/native AC.")


def gh(*args):
    result = subprocess.run(["gh", *map(str, args)], capture_output=True, encoding="utf-8", check=True)
    return json.loads(result.stdout) if result.stdout.strip() else None


def dependency_sections(body):
    return re.findall(r"(?m)^## Dependencies[^\n]*\n[\s\S]*?(?=\n## |\n<!--|\Z)", body)


def original_acs(body):
    match = re.search(r"(?m)^## Acceptance criteria[^\n]*\n([\s\S]*?)(?=\n## |\n<!--|\Z)", body)
    return re.findall(r"(?m)^- \[([ x])\]", match.group(1)) if match else []


def update_body(number, body):
    original_dependencies = dependency_sections(body)
    original_states = original_acs(body)
    # Remove only our idempotent block; preserve all other live content/history.
    body = re.sub(re.escape(START) + r"[\s\S]*?" + re.escape(END) + r"\s*", "", body)
    if number == 2:
        canonical = (PLANNING / "platform-support.md").read_text(encoding="utf-8")
        current = canonical[canonical.index("## Hardware"):canonical.index("## Local runtime and data lifecycle")]
        body, count = re.subn(r"(?m)^## Hardware\s*\n[\s\S]*?(?=^## Local runtime and data lifecycle)", lambda _: current,
                             body, flags=re.MULTILINE)
        assert count == 1, "Expected exactly one original #2 resource section"
    if number in {46, 47}:
        body, count = re.subn(r"(?m)^- \[ \] Measure complete installer [^\n]*", NATIVE_AC, body)
        assert count == 1 or NATIVE_AC in body, "Unexpected native resource AC"
    if number == 1:
        body = body.replace("250 MB/750 MB targets and all startup/memory targets remain unchanged.",
            "accepted 2026-11-14 hardware/resource targets above apply; complete installer and full-app acceptance remain unpassed.")
    tracking = re.match(r"[\s\S]*?<!-- dozu-tracking:end -->\s*", body)
    offset = tracking.end() if tracking else 0
    body = body[:offset] + CONTRACT + "\n\n" + body[offset:]
    if number == 8:
        body = re.sub(r"<!-- dozu-embedding-component-ac-review-2026-11-14:start -->[\s\S]*?<!-- dozu-embedding-component-ac-review-2026-11-14:end -->\s*", "", body)
        body = body.rstrip() + "\n\n" + COMPONENT + "\n"
    assert dependency_sections(body) == original_dependencies, f"Dependency text changed on #{number}"
    assert original_acs(body) == original_states, f"Original release AC states changed on #{number}"
    return body


def main():
    parser = argparse.ArgumentParser(); parser.add_argument("--publish", action="store_true")
    args = parser.parse_args()
    issues = json.loads((RUN / "all-issues-before.json").read_text(encoding="utf-8-sig"))
    targets = sorted([i for i in issues if (i["state"] == "OPEN" or i["number"] == 2) and
        (i["number"] in RELEASE_OWNERS or any(s in i["body"] for s in ["750 MB", "250 MB", "700 MB", "4 GB", "≤750", "≤250"]))],
        key=lambda i: i["number"])
    prepared = []
    for issue in targets:
        number = issue["number"]
        live = gh("issue", "view", number, "--repo", "Do-Zu/dozu", "--json", ",".join(META + ["body"])) if args.publish else issue
        body = update_body(number, live["body"])
        path = RUN / f"issue-{number}-body.md"; path.write_text(body, encoding="utf-8")
        assert update_body(number, body) == body, f"Amendment not idempotent on #{number}"
        if args.publish:
            if body != live["body"]:
                subprocess.run(["gh", "issue", "edit", str(number), "--repo", "Do-Zu/dozu", "--body-file", str(path)],
                               capture_output=True, encoding="utf-8", check=True)
            after = gh("issue", "view", number, "--repo", "Do-Zu/dozu", "--json", ",".join(META + ["body"]))
            assert after["body"] == body
            assert {k: live[k] for k in META} == {k: after[k] for k in META}, f"Unrelated metadata changed on #{number}"
            prepared.append(after)
            print(f"Verified #{number}: accepted contract/body only; original release AC states and metadata preserved", flush=True)
        else:
            prepared.append({"number": number, "bodyFile": str(path), "originalReleaseACs": original_acs(body),
                             "newVerifiedComponentChecks": 7 if number == 8 else 0})
    output = HERE / ("issue-verification.json" if args.publish else ".runs/prepared.json")
    output.write_text(json.dumps(prepared, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"mode": "published" if args.publish else "prepared", "issues": [i["number"] for i in prepared]}), flush=True)


if __name__ == "__main__":
    main()
