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
    "docs/research/2026-09-01_Kairos_User_Screenshot_UI_Calibration_v0.5.md",
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
    trigger = auto.get("trigger", {})
    policy_auto = auto.get("default_execution_policy", {})

    require(auto.get("schema_version") == 2, "Autopilot schema must be v2", errors)
    require(auto.get("contract_id") == "AERIS-FULL-BUILD-AUTOPILOT-V2", "wrong Autopilot contract id", errors)
    require(core.get("repository") == "Space653000/0_JN1_AERIS", "wrong canonical Core repository", errors)
    require(core.get("branch") == "main", "canonical Core branch must be main", errors)
    require(core.get("authority") == "read_only_design_ssot", "Core must remain read-only design SSOT", errors)
    require(impl.get("repository") == "Space653000/0_JN1_AERIS_Local-computer-implementation", "wrong implementation repository", errors)
    require(roles.get("codex") == "primary_local_executor_installer_implementer", "Codex role drift", errors)
    require(roles.get("human_chief_engineer") == "final_authority_and_irreversible_release_approval", "Human authority drift", errors)
    require(roles.get("claude_code") == "optional_independent_reviewer_only_when_human_explicitly_requests", "Claude must be optional by default", errors)

    urls = set(trigger.get("canonical_urls", []))
    require("https://github.com/Space653000/0_JN1_AERIS" in urls, "Core URL missing from trigger", errors)
    require("https://github.com/Space653000/0_JN1_AERIS_Local-computer-implementation" in urls, "Implementation URL missing from trigger", errors)
    require(trigger.get("interpretation") == "AERIS_FULL_BUILD_AUTOPILOT_REQUEST", "wrong Full-Build trigger", errors)
    require(trigger.get("active_workspace_counts_as_target_path") is True, "active workspace must resolve target path", errors)
    require(trigger.get("requires_additional_prompt") is False, "second prompt must not be required", errors)
    require(trigger.get("requires_plan_confirmation") is False, "plan confirmation must not be required", errors)

    require(policy_auto.get("launch_claude_code") is False, "Claude must not launch by default", errors)
    require(policy_auto.get("launch_second_model_reviewer") is False, "second reviewer must not launch by default", errors)
    require(policy_auto.get("use_codex_tasks_or_scheduler") is False, "Codex scheduler must not be used", errors)
    require(policy_auto.get("close_software_only_gaps_before_final_opening") is True, "software-gap closure must be mandatory", errors)
    require(policy_auto.get("continue_until_no_safe_software_gap_remains") is True, "Full Build must continue through safe software gaps", errors)

    states = set(auto.get("truth_states", []))
    require({"NOT_IMPLEMENTED", "IMPLEMENTED", "TESTED", "VERIFIED", "BLOCKED_EXTERNAL"}.issubset(states), "truth states incomplete", errors)
    op_states = set(auto.get("operational_states", []))
    require({"CLOSED", "BOOTSTRAPPING", "BLOCKED", "OPEN_WITH_LIMITS", "OPEN_VERIFIED_SCOPE"}.issubset(op_states), "operational states incomplete", errors)

    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8-sig") if (ROOT / "AGENTS.md").exists() else ""
    claude = (ROOT / "CLAUDE.md").read_text(encoding="utf-8-sig") if (ROOT / "CLAUDE.md").exists() else ""
    policy = (ROOT / "aeris.policy.yaml").read_text(encoding="utf-8-sig") if (ROOT / "aeris.policy.yaml").exists() else ""
    read_order = (ROOT / "docs/governance/AI_READ_ORDER.md").read_text(encoding="utf-8-sig") if (ROOT / "docs/governance/AI_READ_ORDER.md").exists() else ""
    research = (ROOT / "docs/research/README.md").read_text(encoding="utf-8-sig") if (ROOT / "docs/research/README.md").exists() else ""
    sop = (ROOT / "docs/governance/AI_AUTOPILOT_SOP.md").read_text(encoding="utf-8-sig") if (ROOT / "docs/governance/AI_AUTOPILOT_SOP.md").exists() else ""

    require("AERIS_FULL_BUILD_AUTOPILOT_REQUEST" in agents, "AGENTS.md missing Full-Build trigger", errors)
    require("MUST NOT push" in agents and "canonical Core" in agents, "AGENTS.md Core no-write rule weakened/missing", errors)
    require("The two canonical GitHub URLs are the command" in agents, "AGENTS.md must make two URLs the command", errors)
    require("Software Gap Closure Loop" in agents, "AGENTS.md missing software-gap closure loop", errors)
    require("two URLs are the command" in sop, "Autopilot SOP must make two URLs sufficient", errors)
    require("Do not ask `確認執行`" in sop, "Autopilot SOP must forbid redundant plan confirmation", errors)
    require("independent reviewer" in claude.lower(), "CLAUDE.md optional reviewer contract missing", errors)

    # Policy must be semantically aligned with AGENTS/autopilot v2. These checks prevent stale authority text.
    require("trigger_interpretation: AERIS_FULL_BUILD_AUTOPILOT_REQUEST" in policy, "policy trigger must be Full-Build v2", errors)
    require("active_workspace_counts_as_target_path: true" in policy, "policy must allow selected workspace as target", errors)
    require("requires_additional_prompt: false" in policy, "policy must not require a second prompt", errors)
    require("requires_plan_confirmation: false" in policy, "policy must not require plan confirmation", errors)
    require("launch_claude_code: false" in policy, "policy must keep Claude off by default", errors)
    require("use_codex_tasks_or_scheduler: false" in policy, "policy must forbid Codex scheduler continuity", errors)
    require("close_software_only_gaps_before_final_opening: true" in policy, "policy must require software-gap closure", errors)
    require("continue_until_no_safe_software_gap_remains: true" in policy, "policy must continue through software-only gaps", errors)
    require("self_repair_and_same_context_approval: forbidden" in policy, "policy must prohibit same-context repair+approval", errors)
    require("trigger_required_inputs:" not in policy, "stale v1 trigger_required_inputs contract must be removed", errors)
    require("AERIS_AUTOPILOT_REQUEST" not in policy, "stale v1 AERIS_AUTOPILOT_REQUEST token must be removed", errors)

    require("AI_AUTOPILOT_SOP.md" in read_order and "AERIS_MASTER_RESEARCH_ARCHITECTURE_BASELINE_20260831.md" in read_order, "read order missing canonical documents", errors)
    require("AERIS UI v0.5" in research and "Current visual authority" in research, "research index must point to v0.5 direct-screenshot authority", errors)
    require("228px always-expanded labeled sidebar" in research, "research index must record the v0.4 sidebar regression explicitly", errors)

    for rel in ["docs/governance/AI_READ_ORDER.md", "docs/governance/AI_AUTOPILOT_SOP.md", "docs/research/README.md"]:
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
