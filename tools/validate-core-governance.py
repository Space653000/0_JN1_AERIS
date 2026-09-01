#!/usr/bin/env python3
"""Deterministic, read-only validation of AERIS Core governance contracts."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "AGENTS.md",
    "CLAUDE.md",
    "aeris.policy.yaml",
    "aeris.autopilot.json",
    "docs/governance/AI_READ_ORDER.md",
    "docs/governance/AI_AUTOPILOT_SOP.md",
    "docs/research/README.md",
    "docs/research/AERIS_MASTER_RESEARCH_ARCHITECTURE_BASELINE_20260831.md",
    "docs/research/AERIS_WEB_UI_CONTROL_PLANE_BASELINE_20260831.md",
]


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    errors: list[str] = []
    for rel in REQUIRED_FILES:
        require((ROOT / rel).is_file(), f"missing required governance/read-order file: {rel}", errors)

    try:
        auto = json.loads((ROOT / "aeris.autopilot.json").read_text(encoding="utf-8-sig"))
    except Exception as exc:
        errors.append(f"aeris.autopilot.json unreadable: {exc}")
        auto = {}

    core = auto.get("canonical_core", {})
    impl = auto.get("implementation", {})
    roles = auto.get("human_ai_roles", {})
    require(core.get("repository") == "Space653000/0_JN1_AERIS", "wrong canonical Core repository", errors)
    require(core.get("branch") == "main", "canonical Core branch must be main", errors)
    require(core.get("authority") == "read_only_design_ssot", "Core must remain read-only design SSOT", errors)
    require(impl.get("repository") == "Space653000/0_JN1_AERIS_Local-computer-implementation", "wrong implementation repository", errors)
    require(roles.get("codex") == "primary_local_executor_installer_implementer", "Codex role drift", errors)
    require(roles.get("claude_code") == "independent_reviewer_acceptance_auditor", "Claude reviewer role drift", errors)
    require(roles.get("human_chief_engineer") == "final_authority_and_irreversible_release_approval", "Human authority drift", errors)

    states = set(auto.get("truth_states", []))
    require({"NOT_IMPLEMENTED", "IMPLEMENTED", "TESTED", "VERIFIED", "BLOCKED_EXTERNAL"}.issubset(states), "truth states incomplete", errors)
    op_states = set(auto.get("operational_states", []))
    require({"CLOSED", "BOOTSTRAPPING", "BLOCKED", "OPEN_WITH_LIMITS", "OPEN_VERIFIED_SCOPE"}.issubset(op_states), "operational states incomplete", errors)

    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8-sig") if (ROOT / "AGENTS.md").exists() else ""
    claude = (ROOT / "CLAUDE.md").read_text(encoding="utf-8-sig") if (ROOT / "CLAUDE.md").exists() else ""
    policy = (ROOT / "aeris.policy.yaml").read_text(encoding="utf-8-sig") if (ROOT / "aeris.policy.yaml").exists() else ""
    read_order = (ROOT / "docs/governance/AI_READ_ORDER.md").read_text(encoding="utf-8-sig") if (ROOT / "docs/governance/AI_READ_ORDER.md").exists() else ""

    require("AERIS_AUTOPILOT_REQUEST" in agents, "AGENTS.md missing Autopilot trigger", errors)
    require("MUST NOT modify this canonical GitHub repository" in agents, "AGENTS.md Core no-write rule weakened/missing", errors)
    require("independent reviewer" in claude.lower(), "CLAUDE.md independent-review contract missing", errors)
    require("self_repair_and_same_context_approval: forbidden" in policy, "policy must prohibit same-context repair+approval", errors)
    require("AI_AUTOPILOT_SOP.md" in read_order and "AERIS_MASTER_RESEARCH_ARCHITECTURE_BASELINE_20260831.md" in read_order, "read order missing canonical documents", errors)

    # Validate relative Markdown links in the two governance SOPs.
    for rel in ["docs/governance/AI_READ_ORDER.md", "docs/governance/AI_AUTOPILOT_SOP.md"]:
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8-sig")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            if "://" in target or target.startswith("#"):
                continue
            resolved = (path.parent / target).resolve()
            require(resolved.exists(), f"broken relative link in {rel}: {target}", errors)

    if errors:
        print("AERIS_CORE_GOVERNANCE=FAIL")
        for item in errors:
            print(f"- {item}")
        return 1
    print("AERIS_CORE_GOVERNANCE=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
