"""Build the Task #2 requirements matrix from the immutable Task #3 audit."""
import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent


def read(name):
    return json.loads((BASE / name).read_text(encoding="utf-8-sig"))


def main():
    audit = read("audit/feature-parity.json")
    inventory = read("route-inventory.json")
    pages = audit["pages"]
    tracked = subprocess.check_output(
        ["git", "-C", str(ROOT / "dozu-ui-service"), "ls-files", "src"], text=True
    ).splitlines()
    actual_pages = {"dozu-ui-service/" + p for p in tracked if p.startswith("src/app/") and p.endswith("/page.tsx")}
    actual_layouts = {"dozu-ui-service/" + p for p in tracked if p.startswith("src/app/") and p.endswith("/layout.tsx")}
    shared = [p for p in tracked if p.startswith("src/components/") and p.endswith(".tsx")]
    assert len({p["id"] for p in pages}) == len(pages) == 84
    assert {p["source"] for p in pages} == actual_pages == {p["source"] for p in inventory["pages"]}
    assert set(inventory["layouts"]) == actual_layouts and len(actual_layouts) == 20
    assert len(shared) == inventory["sharedComponentTsxCount"] == 164
    commit = subprocess.check_output(["git", "-C", str(ROOT / "dozu-ui-service"), "rev-parse", "HEAD"], text=True).strip()
    assert commit == inventory["sourceCommit"]
    for page in pages:
        assert page["workflow"] and page["rolesAndWorkflows"] and page["followUpIssues"]
        assert set(page["locales"]) == {"en", "vi"}
        assert set(page["layouts"]) <= actual_layouts
        assert page["runtimeParity"] == "UNVERIFIED"
    payload = {
        "requirementsDate": "2026-11-10",
        "scopeAmendedDate": "2026-11-11",
        "integrationExecutionPolicy": {"payments": "DEFERRED_BLOCKED_41", "classroom": "LAN_USER_OWNED_HOST", "speechToText": "DEFERRED_V1", "database": "POSTGRESQL_RETAINED", "pgvector": "DEFERRED_V1", "textEmbedding": "RETAINED_PDF_YOUTUBE_REFERENCES", "decisionRecord": "v1-scope-2026-11-11.md"},
        "sourceCommit": commit,
        "auditSha256": hashlib.sha256((BASE / "audit/feature-parity.json").read_bytes()).hexdigest(),
        "scope": "All page inventory retained; payments deferred under #41; classroom v1 is LAN. User removed local speech-to-text from v1 and deferred pgvector on 2026-11-11; PostgreSQL and PDF/YouTube text reference retrieval remain required. Runtime parity is unverified.",
        "surfaces": ["retained website build", "packaged Electron", "localhost browser using same backend/data"],
        "coverage": {"pages": len(pages), "layouts": len(actual_layouts), "sharedComponentTsx": len(shared)},
        "families": dict(Counter(p["family"] for p in pages)),
        "requiredScenarios": ["render and navigate", "en/vi and inherited layouts/themes", "authorized role and denied access", "existing mutations persist locally", "loading/empty/validation/error/retry", "restart and shared localhost data", "provider missing/offline/failed/success when applicable", "files/streams/sockets/media when applicable"],
        "pages": [dict(p, releaseScope="REQUIRED", capabilityScopeAmendment="v1-scope-2026-11-11.md", requirementsEvidence="Source inventory retained; explicit v1 capability exceptions apply; execution unverified") for p in pages],
    }
    (BASE / "feature-preservation.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = ["# Full feature-preservation requirements — Task #2", "", "Recorded 2026-11-10 from the completed [Task #3 audit](audit/README.md). All 84 source pages remain required. This matrix records scope; runtime parity is unverified. Role text describes source intent, and explicit gate evidence is preserved in the [JSON matrix](feature-preservation.json). A route name is not proof of authorization.", "", "The retained website build, packaged Electron and localhost browser are required surfaces. Electron and the local browser share one local Express/database/files stack; their browser-local tokens and drafts require explicit compatibility work. Preserve all existing layouts, themes, translations, interactions and external integrations.", "", "## Coverage and acceptance", "", "Verified against tracked UI source at `" + commit + "`: 84 pages, 20 layouts and 164 shared src/components TSX files. The [UI ledger](audit/ui-ledger.md) additionally covers all 584 non-entry TSX files (including those 164), 132 hook/provider/context sources and 550 navigation/config sites. Route-scoped code remains required. [Navigation gaps/placeholders and failures](audit/findings.md) remain visible and do not authorize dropping a page.", "", "Each applicable route must eventually pass:", ""]
    lines.extend("- " + s + "." for s in payload["requiredScenarios"])
    lines += ["", "**User scope amendment 2026-11-11:** [local speech-to-text removed from v1; PostgreSQL retained; pgvector deferred](v1-scope-2026-11-11.md). Source workflow descriptions below remain historical inventory, including convert/transcribe wording. They do not re-require deferred speech recognition. Retained PDF/YouTube reference search uses a separate text-embedding model, so its smaller-runtime proof remains relevant. All 84 pages remain required; independent playback and genuine existing transcript text retrieval remain. No deferred capability is marked implemented."]
    lines += ["", "These are future implementation/release checks under #13/#17/#22/#37/#39, not passing results for this requirements task. Existing placeholders, mocks or static charts must not be reported as functional parity. Source-level backend contract candidates remain candidates. All mutable first-party data/files/jobs must be local; genuine provider calls remain internet-enabled when needed.", "", "## Complete page matrix", "", "| ID / route / family | Required workflow | Role intent | Locales | Source | Follow-up |", "| --- | --- | --- | --- | --- | --- |"]
    for p in pages:
        lines.append(f'| {p["id"]} `{p["route"]}` / {p["family"]} | {p["workflow"]} | {p["rolesAndWorkflows"]} | en, vi | [page](<../{p["source"]}>) | ' + ", ".join(f'[#{u.rsplit("/",1)[1]}]({u})' for u in p["followUpIssues"]) + " |")
    lines += ["", "## Family coverage", "", "| Family | Required pages |", "| --- | --- |"]
    lines.extend(f"| {family} | {count} |" for family, count in payload["families"].items())
    lines += ["", "Admin provider/keys/models/plans/subscriptions/payments/revenue/feedback/stats, teacher/student classrooms/activities/approval, account/auth/reset, payment/history, generation/Feynman, PDF/YouTube/media/editors, games, topics/flashcards/quizzes, schedules/settings/profile/streaks, public/diagnostic and navigation flows are represented above and in the linked interaction ledger. Missing destination routes and incomplete features are tracked gaps, not silent omissions.", "", "[Platform agreement](platform-support.md) and [integration decisions](integration-decisions.md) were approved by the user on 2026-11-10. Payment execution is explicitly deferred/blocked under #41: retain page/history/admin inventory and implement an honest unavailable state; no fake success or page deletion. Payment provider-success execution is deferred until explicitly reopened. Classroom v1 supports other devices on the same LAN via a user-owned authoritative local host; remote internet/tunnel participants are not required for v1. All runtime proof remains pending.", ""]
    (BASE / "feature-preservation.md").write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({"status": "PASS", "coverage": payload["coverage"], "familyCounts": payload["families"], "sourceCommit": commit}))


if __name__ == "__main__":
    main()
