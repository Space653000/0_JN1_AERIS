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
    "docs/AERIS_BLUEPRINT_ZH_TW.md",
    "docs/governance/AERIS_DECISION_LOG.md",
    "docs/governance/AERIS_TRACEABILITY_MATRIX.md",
    "docs/governance/SOL_INDEPENDENT_REVIEW_GATE_V2.md",
    "aeris.traceability.json",
]

CURRENT_GOVERNANCE_DOCS = [
    "README.md",
    "AGENTS.md",
    "aeris.review.json",
    "aeris.traceability.json",
    "docs/AERIS_BLUEPRINT_ZH_TW.md",
    "docs/governance/AI_READ_ORDER.md",
    "docs/governance/README.md",
    "docs/governance/AERIS_DECISION_LOG.md",
    "docs/governance/AERIS_TRACEABILITY_MATRIX.md",
    "docs/governance/SOL_INDEPENDENT_REVIEW_GATE_V2.md",
]

REQUIRED_AD_REQUIREMENTS = {
    "AERIS-AD-A-001",
    "AERIS-AD-A-002",
    "AERIS-AD-A-003",
    "AERIS-AD-B-001",
    "AERIS-AD-B-002",
    "AERIS-AD-C-001",
    "AERIS-AD-C-002",
    "AERIS-AD-D-001",
    "AERIS-AD-D-002",
}


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

    try:
        trace = json.loads((ROOT / "aeris.traceability.json").read_text(encoding="utf-8-sig"))
    except Exception as exc:
        errors.append(f"aeris.traceability.json unreadable: {exc}")
        trace = {}

    try:
        review = json.loads((ROOT / "aeris.review.json").read_text(encoding="utf-8-sig"))
    except Exception as exc:
        errors.append(f"aeris.review.json unreadable: {exc}")
        review = {}

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

    # A-D Core/WHAT delivery contract.
    require(trace.get("schema_version") == 1, "traceability schema must be v1", errors)
    require(trace.get("traceability_id") == "AERIS-A-D-TRACEABILITY-20260907", "wrong A-D traceability id", errors)
    require(trace.get("source_baseline", {}).get("core_base_sha") == "fa65e86a8612b227ef4c9e6976ef0060ca2221ac", "A-D Core base SHA drift", errors)
    workstreams = trace.get("workstreams", {})
    for key in ("A", "B", "C", "D"):
        require(workstreams.get(key, {}).get("status") in {"IMPLEMENTED", "INDEPENDENT_REVIEW_PASSED"}, f"workstream {key} must be implemented or independently reviewed", errors)
    require(workstreams.get("E", {}).get("status") == "NOT_STARTED", "workstream E must remain NOT_STARTED", errors)

    requirements = trace.get("requirements", [])
    requirement_ids = {item.get("id") for item in requirements if isinstance(item, dict)}
    require(len(requirement_ids) == len(requirements), "traceability requirement IDs must be unique and non-empty", errors)
    require(REQUIRED_AD_REQUIREMENTS.issubset(requirement_ids), "A-D requirement IDs incomplete", errors)
    for item in requirements:
        if not isinstance(item, dict):
            errors.append("every traceability requirement must be an object")
            continue
        rid = item.get("id", "<missing>")
        require(item.get("owner") in {"CORE", "IMPLEMENTATION"}, f"{rid} has invalid owner", errors)
        require(bool(item.get("requirement")), f"{rid} missing requirement text", errors)
        require(bool(item.get("acceptance")), f"{rid} missing acceptance rule", errors)
        if item.get("workstream") in {"A", "B", "C", "D"}:
            require(bool(item.get("evidence")), f"{rid} missing evidence paths", errors)

    ownership = trace.get("ownership_contract", {})
    require(set(ownership.get("core_owns", [])) == {"product_requirements", "governance", "acceptance_criteria", "research_provenance"}, "Core WHAT ownership drift", errors)
    require(set(ownership.get("implementation_owns", [])) == {"runtime", "scripts", "prompts", "deployment"}, "Implementation HOW ownership drift", errors)
    version_tuple = trace.get("four_way_version_tuple", {})
    require(set(version_tuple.get("required_records", [])) == {"core_blueprint", "implementation", "local_checkout", "evidence_bundle"}, "four-way version tuple incomplete", errors)
    require(version_tuple.get("current_end_to_end_alignment_claim") == "NOT_CLAIMED", "A-D must not claim runtime end-to-end alignment", errors)

    require(review.get("schema_version") == 2, "review contract must be schema v2", errors)
    require(review.get("review_id") == "AERIS-SOL-INDEPENDENT-REVIEW-20260907", "wrong current review id", errors)
    routing = review.get("review_routing", {})
    require(routing.get("implementer", {}).get("model") == "gpt-5.6-sol", "A-D implementer must be Sol", errors)
    require(routing.get("independent_reviewer", {}).get("model") == "gpt-5.6-sol", "A-D independent reviewer must be Sol", errors)
    require(routing.get("independent_reviewer", {}).get("isolated_context") is True, "reviewer context must be isolated", errors)
    require(routing.get("return_to_astra_required") is False, "Astra return must not be required", errors)
    require(review.get("human_authority", {}).get("final_authority") is True, "Human final authority must remain explicit", errors)
    require(review.get("review_result", {}).get("status") in {"PENDING", "PASS", "FAIL", "BLOCKED"}, "review result has invalid status", errors)
    automatic_git = review.get("automatic_git_actions", {})
    for action in ("checkout", "merge", "push"):
        require(automatic_git.get(action) is False, f"automatic {action} must be forbidden", errors)
    history = review.get("history", [])
    require(any(item.get("review_id") == "AERIS-ASTRA-SOL-REVIEW-20260907" and item.get("status") == "SUPERSEDED_HISTORICAL" for item in history if isinstance(item, dict)), "legacy Astra/Sol review must be retained as history", errors)
    admission = auto.get("admission_precondition", {})
    require(admission.get("contract") == "aeris.review.json", "Autopilot must use the current review contract", errors)
    require(admission.get("traceability_contract") == "aeris.traceability.json", "Autopilot must use the A-D traceability contract", errors)
    require(admission.get("implementation_how_batch_E") == "NOT_STARTED", "Autopilot must preserve E as NOT_STARTED", errors)
    require(admission.get("return_to_astra_required") is False, "Autopilot must not require an Astra return", errors)
    for action in ("checkout", "merge", "push"):
        require(admission.get("automatic_git_actions", {}).get(action) is False, f"Autopilot automatic {action} must be forbidden", errors)

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
    require("traceability_contract: aeris.traceability.json" in policy, "policy must reference the A-D traceability contract", errors)
    require("gate: docs/governance/SOL_INDEPENDENT_REVIEW_GATE_V2.md" in policy, "policy must reference the current Sol review gate", errors)
    require("implementation_how_batch_E: NOT_STARTED" in policy, "policy must preserve E as NOT_STARTED", errors)
    require("return_to_astra_required: false" in policy, "policy must not require an Astra return", errors)
    for action in ("checkout", "merge", "push"):
        require(f"automatic_{action}: false" in policy, f"policy automatic {action} must be forbidden", errors)
    require("trigger_required_inputs:" not in policy, "stale v1 trigger_required_inputs contract must be removed", errors)
    require("AERIS_AUTOPILOT_REQUEST" not in policy, "stale v1 AERIS_AUTOPILOT_REQUEST token must be removed", errors)

    require("AI_AUTOPILOT_SOP.md" in read_order and "AERIS_MASTER_RESEARCH_ARCHITECTURE_BASELINE_20260831.md" in read_order, "read order missing canonical documents", errors)
    require("AERIS_BLUEPRINT_ZH_TW.md" in read_order and "aeris.traceability.json" in read_order, "read order missing current blueprint or traceability contract", errors)
    require("AERIS UI v0.5" in research and "Current visual authority" in research, "research index must point to v0.5 direct-screenshot authority", errors)
    require("228px always-expanded labeled sidebar" in research, "research index must record the v0.4 sidebar regression explicitly", errors)

    blueprint = (ROOT / "docs/AERIS_BLUEPRINT_ZH_TW.md").read_text(encoding="utf-8-sig") if (ROOT / "docs/AERIS_BLUEPRINT_ZH_TW.md").exists() else ""
    matrix = (ROOT / "docs/governance/AERIS_TRACEABILITY_MATRIX.md").read_text(encoding="utf-8-sig") if (ROOT / "docs/governance/AERIS_TRACEABILITY_MATRIX.md").exists() else ""
    require("https://www.agent-zero.ai/" in blueprint, "blueprint missing Agent Zero provenance URL", errors)
    require("不是 100 個常駐代理" in blueprint, "blueprint must reject the 100 resident-agent interpretation", errors)
    require("## 五步工作流" in blueprint, "blueprint missing five-step workflow", errors)
    require("Core 只擁有 WHAT" in blueprint and "Implementation 擁有 HOW" in blueprint, "blueprint missing WHAT/HOW ownership", errors)
    require("NOT_STARTED" in matrix and "AERIS-AD-E-001" in matrix, "traceability matrix must show E as NOT_STARTED", errors)
    for rid in REQUIRED_AD_REQUIREMENTS | {"AERIS-AD-E-001"}:
        require(rid in matrix, f"traceability matrix missing {rid}", errors)

    for item in requirements:
        if not isinstance(item, dict):
            continue
        for evidence in item.get("evidence", []):
            evidence_path = evidence.split("#", 1)[0]
            require((ROOT / evidence_path).is_file(), f"{item.get('id', '<missing>')} references missing evidence: {evidence}", errors)

    for rel in ["docs/governance/AI_READ_ORDER.md", "docs/governance/AI_AUTOPILOT_SOP.md", "docs/research/README.md"]:
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8-sig")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            if "://" in target or target.startswith("#"):
                continue
            link_path = target.split("#", 1)[0]
            resolved = (path.parent / link_path).resolve()
            require(resolved.exists(), f"broken relative link in {rel}: {target}", errors)

    for rel in CURRENT_GOVERNANCE_DOCS:
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8-sig")
        require("審查優先：HOLD_FOR_SOL_RED_TEAM" not in text, f"obsolete active review hold in current document: {rel}", errors)
        require("C:\\0_JN1_AERIS" not in text and "C:\\Users\\" not in text, f"private absolute local path leaked into Core: {rel}", errors)
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            if "://" in target or target.startswith("#"):
                continue
            link_path = target.split("#", 1)[0]
            resolved = (path.parent / link_path).resolve()
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
