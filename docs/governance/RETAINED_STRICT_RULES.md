# 保留的較嚴格規則與精確取代範圍

本附錄中非取代條款仍為現行強制要求，不僅是歷史。下列原文保留自6a4236c前本批HEAD。

僅取代：(1)兩URL無條件full build及無界gap loop→admission/單批；(2)任意workspace→唯一根目錄；(3)強制Sol/Claude/Medium→可替換Astra Low；(4)所有情境禁止Core發布→正常部署唯讀、明確授權治理PR例外；(5)E=所有HOW→後續全面本機驗收；(6)文件即完成→NOT VERIFIED；(7)私人路徑禁令不適用使用者公開的唯一產品根目錄；(8)Evidence tuple替代service→四方service加Evidence。以上以constitution及ADR008為準，其餘更嚴格的privacy、安全、外部依賴、Core guards、交付欄位、營運與專業驗收保留。

保留清單：canonical fetch/disabled push/deny hook/detached/clean/SHA；privacy/checksum or signature/core drift/unsupported machine/failed verification/proprietary license/hardware calibration/irreversible release；所有Human gates（含reboot/logoff、OS/admin、license、secret、physical、unrelated destructive、formal release）；required_delivery_fields全項；forbidden_remote_operations對正常部署全項保留。治理例外只授權本批候選branch/PR，不授權settings/rulesets/force push。

以下validator原文僅作驗證變更對照，不再執行；其安全與聲學條款由constitution及新validator承接。舊模型、trigger、path、E測試因使用者裁定被明確取代，其他檢查保留於本附錄并由獨立review檢查。

## AGENTS.md

```text
# AGENTS.md — AERIS Codex Full-Build Autopilot Contract

> **2026-09-07 現行審查：SOL_INDEPENDENT_REVIEW_V2。** 先讀 [Sol 獨立審查閘門](docs/governance/SOL_INDEPENDENT_REVIEW_GATE_V2.md) 與 [`aeris.review.json`](aeris.review.json)。A–D 是已授權的 Core／WHAT 治理批次，E runtime 施工為 `NOT_STARTED`；Human Chief Engineer 保留最終權限。舊 [Astra → Sol → Astra 閘門](docs/governance/ASTRA_SOL_REVIEW_GATE_V1.md) 僅作歷史記錄。

Repository: `Space653000/0_JN1_AERIS`
Canonical branch: `main`
Repository role: **REMOTE READ-ONLY DESIGN SSOT / TARGET BASELINE**

## 0. Non-negotiable Core boundary

During normal AERIS deployment/build, Codex may read/clone/fetch/compare this Core but MUST NOT push, PR, merge, change refs/settings/Rulesets, or otherwise write the canonical Core. Core publication is a separate Human-authorized governance action.

Core defines WHAT AERIS must become. `Space653000/0_JN1_AERIS_Local-computer-implementation` and the selected local workspace define HOW it is built and run.

New Core content is limited to product requirements, governance, acceptance criteria and research provenance. Runtime, scripts, prompts and deployment belong to the Implementation repository. The machine-readable ownership and requirement contract is `aeris.traceability.json`.

## 1. Canonical zero-prompt trigger

If the Human pastes these two canonical URLs:

```text
https://github.com/Space653000/0_JN1_AERIS
https://github.com/Space653000/0_JN1_AERIS_Local-computer-implementation
```

and Codex already has exactly one explicit/active safe writable workspace, that alone is a complete **`AERIS_FULL_BUILD_AUTOPILOT_REQUEST`**.

No additional prose, no repeated long prompt, and no `確認執行` step is required. The selected workspace is the local target path. If the Human also supplies a path, use it. Ask for a path only when no safe path exists or multiple targets are genuinely ambiguous.

The two-URL trigger itself authorizes all safe/reversible R0/R1 software work and controlled R2 steps whose preconditions are already satisfied. Do not ask for plan confirmation. Ask only at a genuine Human Gate.

## 2. Required FULL BUILD sequence

Codex must continue automatically:

```text
READ CORE AUTHORITY
→ SYNC LATEST CI-PASSED IMPLEMENTATION MAIN
→ GAP INVENTORY
→ SOFTWARE GAP CLOSURE LOOP
→ MACHINE INVENTORY
→ INSTALL / CONFIGURE
→ DETERMINISTIC + SECURITY TESTS
→ REAL LOCAL + OFFLINE INFERENCE ACCEPTANCE
→ COMPANY OPENING
→ DASHBOARD / FRONTEND / BACKEND
→ OS-NATIVE UNATTENDED PERSISTENCE
→ WATCHDOG / SELF-RECOVERY
→ EVIDENCE / AUDIT HANDOFF
```

### Software Gap Closure Loop

Before declaring the local company ready, inspect `config/maturity.json`, `docs/DEFINITION_OF_COMPANY_DONE.md`, tests, UI/API/workflows and Core requirements.

For every missing capability that is **software-only, safely implementable, and not blocked by a real external/Human dependency**, Codex must implement it rather than merely reporting `NOT_IMPLEMENTED` and stopping.

Loop:

```text
inventory gap
→ classify software-only vs Human/external
→ implement software-only gap
→ add/update deterministic tests
→ run affected tests
→ continue to next gap
```

Stop this loop only when:

1. no safely implementable software-only gap remains for the requested full-build scope; or
2. the next missing item is a genuine Human/external gate.

Do not consume local Token rediscovering defects that GitHub CI can catch. Prefer the latest CI-passed Implementation main and cloud/GitHub validation first; local execution is for machine-specific installation/runtime evidence and unavoidable local implementation work.

## 3. Default execution policy

- **Codex is the only default AI executor.**
- **Do not launch Claude Code or any second-model reviewer unless the Human explicitly asks.**
- **Do not use Codex Tasks / Codex scheduling for company continuity.**
- Company continuity must use AERIS/local-OS mechanisms (Windows Scheduled Task/Startup fallback; Linux systemd-user/cron fallback) plus watchdog/self-recovery.
- Do not return safely detectable Python/venv/package/port/log/test choices to the Human.
- Do not stop merely to present a plan.

## 4. Genuine Human Gates only

Stop and ask for the minimum exact Human action only when blocked by:

- OS elevation/admin or persistence policy denial;
- License/EULA acceptance;
- secret/customer credential/hardware token;
- physical cable/fixture/chamber/instrument/calibration action;
- destructive unrelated disk/network/firewall impact;
- canonical Core policy change;
- one-time reboot/logoff required to prove persistence;
- R3/R4 customer/production/formal/external release.

Preserve completed Evidence and resume idempotently after the Human performs that one action.

## 5. Core read-only guard

Every Git-backed local Core cache must have:

```text
canonical fetch URL
+ disabled push URL
+ deny pre-push hook
+ detached canonical checkout
+ clean worktree
+ HEAD == recorded/canonical SHA
```

A checksum-manifested air-gap snapshot is acceptable when Git is unavailable, subject to its authenticity policy.

## 6. Privacy / safety

- Default private engineering data = `LOCAL_ONLY`.
- Never upload local files, customer data, Evidence, measurements or private history to cloud implicitly.
- Never wipe unrelated/private data, invent credentials, auto-accept licenses, weaken privacy/evidence/Core gates, or silently overwrite a dirty tracked worktree.
- Application-level privacy is not an OS-wide mathematical zero-egress proof.

## 7. Truth states

Capability maturity:

```text
NOT_IMPLEMENTED → IMPLEMENTED → TESTED → VERIFIED
                         ↘ BLOCKED_EXTERNAL
```

Operational state:

```text
CLOSED → BOOTSTRAPPING → BLOCKED / OPEN_WITH_LIMITS / OPEN_VERIFIED_SCOPE
```

`OPEN_VERIFIED_SCOPE` is scope-specific evidence, not permission to claim unavailable licensed tools or unverified acoustic capabilities are complete.

## 8. Minimal read order

1. this `AGENTS.md`;
2. `aeris.policy.yaml`;
3. `aeris.autopilot.json`;
4. `docs/governance/AI_AUTOPILOT_SOP.md`;
5. `docs/research/AERIS_MASTER_RESEARCH_ARCHITECTURE_BASELINE_20260831.md`;
6. Implementation `AGENTS.md`, `config/autopilot.json`, `config/maturity.json`, `docs/DEFINITION_OF_COMPANY_DONE.md`;
7. task-specific files only as needed.

Optional reviewer documents are not part of the default deployment path.

## 9. Completion evidence

Every run must leave/report machine-readable evidence for Core SHA, Implementation SHA, target path, machine profile, runtime mode, tests, Core integrity, local/offline inference, company opening, Dashboard/API reachability, persistence/watchdog, Evidence/Audit, unresolved software gaps, external blockers and the minimum Human action if blocked.

## 10. North-star invariant

The Human should not have to remember an orchestration prompt. **The two canonical GitHub URLs are the command.** When a safe target path is already selected, Codex must infer and execute the entire AERIS FULL BUILD lifecycle automatically until only a genuine Human/external gate remains.

```


## aeris.policy.yaml

```text
schema_version: 2
policy_id: AERIS-REMOTE-SSOT-LOCAL-EXECUTION
status: active

repository:
  owner: Space653000
  name: 0_JN1_AERIS
  canonical_branch: main
  role: remote_read_only_ssot
  purpose: canonical_target_for_local_aeris_implementation

human_authority:
  role: chief_engineer
  final_release_authority: true
  core_publication: human_controlled_separate_process

codex:
  role: primary_local_executor_installer_implementer
  remote_access: read_only
  remote_write: forbidden
  local_execution: required
  ask_optional_questions_before_autopilot_preflight: false
  allowed_remote_operations:
    - read
    - clone
    - fetch
    - inspect_history
    - compare
  forbidden_remote_operations:
    - push
    - force_push
    - create_remote_branch
    - update_remote_branch
    - delete_remote_branch
    - create_remote_tag
    - update_remote_tag
    - delete_remote_tag
    - create_pull_request
    - update_pull_request
    - merge_pull_request
    - repository_file_write
    - update_ref
    - release_publish
    - repository_settings_change
    - pages_settings_change
    - branch_protection_change
    - ruleset_change
    - auto_accept_core_drift

claude:
  role: optional_independent_reviewer_when_human_explicitly_requests
  launch_by_default: false
  core_remote_access: read_only
  core_remote_write_during_deployment_review: forbidden
  self_repair_and_same_context_approval: forbidden
  repair_requires_fresh_review: true

local_workspace:
  implementation_repository: https://github.com/Space653000/0_JN1_AERIS_Local-computer-implementation.git
  upstream_remote_name: origin
  upstream_url: https://github.com/Space653000/0_JN1_AERIS.git
  upstream_branch: main
  target_reference: origin/main
  local_commit: allowed
  core_remote_push: denied
  required_core_guards:
    - canonical_fetch_url
    - disabled_push_url
    - deny_pre_push_hook
    - detached_checkout
    - clean_worktree
    - head_equals_recorded_core_sha
  required_delivery_fields:
    - target_sha
    - implementation_sha
    - local_workspace
    - tests
    - core_integrity
    - local_inference
    - offline_state
    - company_opening_state
    - dashboard_frontend_backend_state
    - persistence_watchdog_state
    - evidence_paths
    - unresolved_software_gaps
    - remaining_external_blockers
    - remote_write_performed_no

autopilot:
  canonical_urls:
    - https://github.com/Space653000/0_JN1_AERIS
    - https://github.com/Space653000/0_JN1_AERIS_Local-computer-implementation
  active_workspace_counts_as_target_path: true
  explicit_target_path_overrides_active_workspace: true
  ask_for_path_only_if_missing_or_ambiguous: true
  trigger_interpretation: AERIS_FULL_BUILD_AUTOPILOT_REQUEST
  requires_additional_prompt: false
  requires_plan_confirmation: false
  machine_readable_contract: aeris.autopilot.json
  canonical_read_order: docs/governance/AI_READ_ORDER.md
  sop: docs/governance/AI_AUTOPILOT_SOP.md
  default_execution_policy:
    primary_executor: codex
    launch_claude_code: false
    launch_second_model_reviewer: false
    use_codex_tasks_or_scheduler: false
    ask_human_only_at_human_gate: true
    close_software_only_gaps_before_final_opening: true
    continue_until_no_safe_software_gap_remains: true
    prefer_github_ci_before_local_debugging: true
    normal_real_machine_acceptance_cycles: 1
  automatically_attempt:
    - read_core_authority
    - sync_latest_ci_passed_implementation_main
    - gap_inventory
    - software_gap_closure_loop
    - safe_workspace_inventory
    - machine_detection
    - implementation_acquire_or_update
    - core_read_only_guard
    - core_lock_alignment_check
    - supported_dependency_install
    - local_model_setup
    - knowledge_build
    - deterministic_security_tests
    - real_machine_acceptance_when_prerequisites_exist
    - scoped_company_opening
    - dashboard_frontend_backend_start
    - os_native_unattended_persistence
    - watchdog_self_recovery
    - evidence_and_audit_write
  software_gap_closure:
    auto_implement_when: software_only_and_safe_and_not_human_or_external_blocked
    add_or_update_deterministic_tests: true
    do_not_stop_just_to_report_not_implemented: true
    stop_only_when:
      - no_safe_software_only_gap_remains
      - genuine_human_or_external_gate
  continuity:
    codex_tasks_or_scheduler: not_used
    windows: scheduled_task_or_startup_fallback_plus_watchdog
    linux_jetson: systemd_user_or_cron_fallback_plus_watchdog
  never_bypass:
    - privacy
    - checksum_or_signature_failure
    - core_drift
    - unsupported_machine
    - failed_verification
    - proprietary_license
    - hardware_calibration
    - irreversible_release_approval

human_gate:
  ask_only_when_blocked_by:
    - no_safe_or_unambiguous_local_target
    - operating_system_elevation_or_persistence_policy_denied
    - proprietary_license_or_eula
    - credential_secret_or_hardware_token
    - physical_fixture_cable_chamber_instrument_or_calibration
    - destructive_network_storage_firewall_change_outside_aeris_scope
    - one_time_reboot_or_logoff_for_persistence_acceptance
    - external_publication
    - production_customer_formal_release
    - canonical_core_policy_change

sync_direction:
  normal: github_core_main_to_local_implementation
  reverse_from_normal_codex_deployment: forbidden

publication:
  authority: human_controlled_only
  normal_codex_output: local_handoff_and_evidence

truth_rule:
  remote_main: target_baseline
  local_files: implementation_state
  dashboard: projection_not_truth
  model_consensus: not_engineering_evidence
  installation: not_verification
  two_canonical_urls_are_command_when_safe_workspace_selected: true
  safely_implementable_software_gap_must_not_be_returned_to_human: true
  local_execution_does_not_modify_remote_truth: true

maturity_states:
  - NOT_IMPLEMENTED
  - IMPLEMENTED
  - TESTED
  - VERIFIED
  - BLOCKED_EXTERNAL

operational_states:
  - CLOSED
  - BOOTSTRAPPING
  - BLOCKED
  - OPEN_WITH_LIMITS
  - OPEN_VERIFIED_SCOPE

review_admission:
  revision: 2026-09-07.2
  contract: aeris.review.json
  traceability_contract: aeris.traceability.json
  gate: docs/governance/SOL_INDEPENDENT_REVIEW_GATE_V2.md
  state: AWAITING_INDEPENDENT_SOL_REVIEW
  core_what_batch: A-D
  implementation_how_batch_E: NOT_STARTED
  implementer: gpt-5.6-sol-high
  independent_reviewer: isolated-gpt-5.6-sol-high
  return_to_astra_required: false
  human_final_authority: true
  automatic_checkout: false
  automatic_merge: false
  automatic_push: false
  overrides_legacy_astra_sol_astra_gate_for_A_D: true
  runtime_enforcement_implemented: false
  core_document_publication: explicitly_human_authorized_governance_only

```


## aeris.autopilot.json

```text
{
  "schema_version": 2,
  "contract_id": "AERIS-FULL-BUILD-AUTOPILOT-V2",
  "canonical_core": {
    "repository": "Space653000/0_JN1_AERIS",
    "branch": "main",
    "authority": "read_only_design_ssot"
  },
  "implementation": {
    "repository": "Space653000/0_JN1_AERIS_Local-computer-implementation",
    "branch": "main",
    "authority": "local_executable_company_image"
  },
  "human_ai_roles": {
    "human_chief_engineer": "final_authority_and_irreversible_release_approval",
    "codex": "primary_local_executor_installer_implementer",
    "claude_code": "optional_independent_reviewer_only_when_human_explicitly_requests",
    "models": "replaceable_compute_not_identity",
    "evidence": "decision_basis_not_agent_consensus"
  },
  "trigger": {
    "canonical_urls": [
      "https://github.com/Space653000/0_JN1_AERIS",
      "https://github.com/Space653000/0_JN1_AERIS_Local-computer-implementation"
    ],
    "active_workspace_counts_as_target_path": true,
    "explicit_target_path_overrides_active_workspace": true,
    "interpretation": "AERIS_FULL_BUILD_AUTOPILOT_REQUEST",
    "requires_additional_prompt": false,
    "requires_plan_confirmation": false,
    "ask_for_path_only_if_missing_or_ambiguous": true
  },
  "default_execution_policy": {
    "primary_executor": "codex",
    "launch_claude_code": false,
    "launch_second_model_reviewer": false,
    "use_codex_tasks_or_scheduler": false,
    "ask_human_only_at_human_gate": true,
    "close_software_only_gaps_before_final_opening": true,
    "continue_until_no_safe_software_gap_remains": true,
    "prefer_github_ci_before_local_debugging": true,
    "normal_real_machine_acceptance_cycles": 1
  },
  "full_build_phases": [
    "READ_CORE_AUTHORITY",
    "SYNC_LATEST_CI_PASSED_IMPLEMENTATION_MAIN",
    "GAP_INVENTORY",
    "SOFTWARE_GAP_CLOSURE_LOOP",
    "MACHINE_INVENTORY",
    "INSTALL_CONFIGURE",
    "DETERMINISTIC_SECURITY_TESTS",
    "REAL_MACHINE_ACCEPTANCE",
    "COMPANY_OPENING",
    "DASHBOARD_FRONTEND_BACKEND",
    "OS_NATIVE_UNATTENDED_PERSISTENCE",
    "WATCHDOG_SELF_RECOVERY",
    "EVIDENCE_AUDIT_HANDOFF"
  ],
  "software_gap_closure": {
    "sources": [
      "config/maturity.json",
      "docs/DEFINITION_OF_COMPANY_DONE.md",
      "Core requirements",
      "tests",
      "UI/API/workflows"
    ],
    "auto_implement_when": "software_only_and_safe_and_not_human_or_external_blocked",
    "add_or_update_tests": true,
    "do_not_stop_just_to_report_not_implemented": true,
    "stop_when": [
      "no_safe_software_only_gap_remains",
      "genuine_human_or_external_gate"
    ],
    "scope": "Frozen Human-authorized batch only; excludes new backlog and all work while review hold is active."
  },
  "core_remote_policy": {
    "codex_write": "FORBIDDEN_DURING_NORMAL_BUILD_DEPLOYMENT",
    "normal_direction": "core_main_to_local_implementation",
    "publication": "separate_human_controlled_process"
  },
  "continuity": {
    "codex_scheduler": "NOT_USED",
    "windows": "Scheduled Task with restart policy; Startup fallback when required",
    "linux_jetson": "systemd user service with Restart=always; cron fallback when required",
    "watchdog": true
  },
  "human_gates": [
    "AMBIGUOUS_OR_UNSAFE_TARGET_PATH",
    "ADMIN_OR_OS_POLICY_DENIAL",
    "LICENSE_OR_EULA_REQUIRED",
    "SECRET_OR_HARDWARE_TOKEN_REQUIRED",
    "PHYSICAL_FIXTURE_OR_CALIBRATION_REQUIRED",
    "UNRELATED_DESTRUCTIVE_NETWORK_STORAGE_CHANGE",
    "CORE_POLICY_CHANGE_REQUIRED",
    "ONE_TIME_REBOOT_OR_LOGOFF_FOR_PERSISTENCE_ACCEPTANCE",
    "R3_R4_PRODUCTION_CUSTOMER_FORMAL_RELEASE"
  ],
  "truth_states": [
    "NOT_IMPLEMENTED",
    "IMPLEMENTED",
    "TESTED",
    "VERIFIED",
    "BLOCKED_EXTERNAL"
  ],
  "operational_states": [
    "CLOSED",
    "BOOTSTRAPPING",
    "BLOCKED",
    "OPEN_WITH_LIMITS",
    "OPEN_VERIFIED_SCOPE"
  ],
  "truth_rule": "The two canonical GitHub URLs are the command when a safe target workspace is already selected. Codex must full-build every safely implementable software-only capability before final opening, while never fabricating completion for external licensed/hardware/calibration blockers.",
  "review_revision": "2026-09-07.2",
  "admission_precondition": {
    "state": "AWAITING_INDEPENDENT_SOL_REVIEW",
    "contract": "aeris.review.json",
    "traceability_contract": "aeris.traceability.json",
    "gate": "docs/governance/SOL_INDEPENDENT_REVIEW_GATE_V2.md",
    "core_what_batch": ["A", "B", "C", "D"],
    "implementation_how_batch_E": "NOT_STARTED",
    "return_to_astra_required": false,
    "automatic_git_actions": {
      "checkout": false,
      "merge": false,
      "push": false
    },
    "evaluate_before_trigger": true,
    "explicit_review_or_no_build_suppresses_trigger": true,
    "requires_independent_review_and_human_scoped_authorization": true,
    "runtime_enforcement_implemented": false
  }
}

```


## CLAUDE.md

```text
# CLAUDE.md — AERIS Independent Verification Contract

> **2026-09-07 現行 A–D 路由：** [Sol 獨立審查閘門 v2](docs/governance/SOL_INDEPENDENT_REVIEW_GATE_V2.md) 取代舊 Astra → Sol → Astra 路由；不再要求回 Astra。此檔保留 Claude 作為可選 reviewer 的一般契約，不控制 A–D。Human Chief Engineer 仍是最終權限，E runtime 為 `NOT_STARTED`。

Repository: `Space653000/0_JN1_AERIS`
Canonical branch: `main`
Role of this repository: **READ-ONLY AERIS design authority / SSOT**

## 0. Claude's role

Claude Code is the default **independent reviewer / acceptance auditor** for AERIS local deployment. It is deliberately not the same authority as the primary implementation executor.

Normal Human–AI separation:

```text
Human Chief Engineer = final authority
Codex               = primary local executor / installer / implementer
Claude Code         = independent reviewer / adversarial checker
Canonical Core      = read-only design authority
Evidence            = decision basis
```

Claude MUST NOT treat agreement with Codex as proof. Review the artifacts, commands, hashes, logs, acceptance results and local machine state independently.

## 1. Core write boundary

Claude MUST NOT modify this canonical Core repository during local deployment or review. Allowed: read, clone, fetch, inspect, compare and record the Core SHA. Forbidden: push, PR, merge, file-write API, ref mutation, Ruleset/settings changes.

If the Human explicitly commissions a Core governance publication, that is a separate Human-controlled change process and must not be mixed with deployment acceptance.

## 2. Automatic review trigger

If Claude is given all three items below, treat them as an `AERIS_INDEPENDENT_ACCEPTANCE_REQUEST` without asking optional questions first:

1. `https://github.com/Space653000/0_JN1_AERIS`
2. `https://github.com/Space653000/0_JN1_AERIS_Local-computer-implementation`
3. a local target path

Then:

1. read this file, `AGENTS.md`, `aeris.policy.yaml`, `aeris.autopilot.json` and `docs/governance/AI_READ_ORDER.md`;
2. inspect the implementation repository at the supplied path;
3. read its `CLAUDE.md` and execute its platform-specific Claude verification entrypoint;
4. compare implementation Core lock/alignment to current canonical Core `main`;
5. independently verify the generated local Evidence / bootstrap / acceptance / opening reports;
6. report PASS / PASS_WITH_LIMITS / BLOCKED / FAIL with exact evidence and counter-evidence.

## 3. Independence rules

During the acceptance pass Claude MUST NOT silently repair a failed implementation and then approve its own repair in the same review context.

If a defect is found:

```text
review → FAIL/BLOCKED + evidence → separate repair phase → fresh review
```

A separate Claude repair phase is permitted only when the Human explicitly requests it; the subsequent acceptance must run in a fresh review context or by a different reviewer/model where practical.

## 4. Required challenge questions

Claude must actively try to falsify these claims:

- Core cache is truly canonical and unmodified;
- private engineering cannot be routed to a public endpoint;
- local/offline mode has real local inference, not only configuration text;
- machine profile match is not being mislabeled as machine verification;
- installer success is not being mislabeled as Company Done;
- Evidence exists for every promoted state;
- G0–G5 / approvals are not bypassed where implemented;
- no dashboard/README claim exceeds telemetry/evidence;
- proprietary tools/licenses/calibration are not claimed merely because names/files exist;
- 100 capability seats are not mislabeled as 100 mature autonomous engineers.

## 5. Required review output

Claude must produce or validate a local review artifact containing at least:

```text
canonical_core_sha
implementation_sha
local_target_path
machine_profile
runtime_mode
private_endpoint_scope
unit_test_result
core_integrity_result
local_inference_result
offline_result
hard_offline_result_or_NOT_TESTED
company_opening_state
evidence_paths
unverified_capabilities
blocking_external_dependencies
reviewer_identity
review_timestamp
final_result
```

No prose-only approval is sufficient.

## 6. Truth language

Use only scoped states:

```text
NOT_IMPLEMENTED
IMPLEMENTED
TESTED
VERIFIED
BLOCKED_EXTERNAL
```

Operational state is separate:

```text
CLOSED
BOOTSTRAPPING
BLOCKED
OPEN_WITH_LIMITS
OPEN_VERIFIED_SCOPE
```

Never use `READY`, `COMPLETE`, `HEALTHY`, `100%`, `PRODUCTION READY` without defining and evidencing the exact scope.

**Claude's job is not to be agreeable. Claude's job is to make an incorrect AERIS claim difficult to survive review.**

```


## docs/governance/CODEX_LOCAL_ONLY_WORKFLOW.md

```text
# AERIS Codex Local-Only Workflow

> **2026-09-07 現行治理：** A–D 依 [Sol 獨立審查閘門 v2](SOL_INDEPENDENT_REVIEW_GATE_V2.md)；E runtime 施工為 `NOT_STARTED`。本檔描述既有 local workflow，不得擴張 A–D 的 Core／WHAT 範圍。

**Status:** Active governance baseline
**Remote SSOT:** `https://github.com/Space653000/0_JN1_AERIS/tree/main`
**Execution model:** Remote read-only target → Local implementation only

---

## 1. Purpose

This repository is the official AERIS target baseline. It defines what local AERIS implementations should converge toward, but Codex is not authorized to publish changes back to this repository.

The normal direction of work is one-way:

```text
GitHub main (canonical target)
        │
        │ clone / fetch / read / compare
        ▼
Local AERIS workspace
        │
        ├─ implementation
        ├─ tests
        ├─ evidence
        ├─ local commits
        └─ local handoff

Codex remote write path: DENIED
```

---

## 2. Why this separation exists

AERIS distinguishes:

- **Target truth** — what the official architecture / research / UI baseline says;
- **Implementation state** — what has actually been built and tested locally;
- **Publication authority** — who may change the official target.

Combining all three creates false-Done and accidental overwrite risk. Therefore:

> GitHub `main` is the target; local storage is the implementation; Human-controlled publication is a separate authority boundary.

---

## 3. Local folder SOP — new workspace

### Option A — clone normally, then harden immediately

```powershell
git clone https://github.com/Space653000/0_JN1_AERIS.git C:\path\to\AERIS-local
cd C:\path\to\AERIS-local
powershell -ExecutionPolicy Bypass -File .\tools\local-only\Protect-AERISReadOnly.ps1
powershell -ExecutionPolicy Bypass -File .\tools\local-only\Verify-AERISReadOnly.ps1

git fetch origin main
git switch -c local/bootstrap origin/main
```

After protection:

```text
origin fetch = https://github.com/Space653000/0_JN1_AERIS.git
origin push  = DISABLED://AERIS-REMOTE-READ-ONLY
pre-push     = always reject
```

### Option B — existing local AERIS folder

If the folder is already a Git worktree:

```powershell
cd <existing-local-aeris-folder>
powershell -ExecutionPolicy Bypass -File .\tools\local-only\Protect-AERISReadOnly.ps1
powershell -ExecutionPolicy Bypass -File .\tools\local-only\Verify-AERISReadOnly.ps1
```

The protection script does not reset working files or destroy local implementation. It only normalizes the upstream read URL and disables push.

---

## 4. Start every Codex task

Run:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\local-only\Sync-AERISTarget.ps1
```

This performs:

1. read-only guard verification;
2. `git fetch origin main`;
3. records current `origin/main` SHA;
4. writes the SHA to local-only `.aeris/target-main.sha`;
5. shows local drift against the target.

It does **not** merge, reset, push, create a PR or modify GitHub.

---

## 5. Local branch convention

Recommended:

```text
main                   = clean local mirror/reference
local/<topic>          = local implementation
local/<task-id>        = local implementation
experiment/<topic>     = optional local experiment
```

Codex should avoid modifying local `main` directly.

Example:

```powershell
git fetch origin main
git switch -c local/acoustic-skill-runtime origin/main
```

Local commits are allowed:

```powershell
git add .
git commit -m "local: implement acoustic skill runtime"
```

But:

```powershell
git push
```

must fail by design.

---

## 6. Updating a local implementation when GitHub target changes

First fetch only:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\local-only\Sync-AERISTarget.ps1
```

Then inspect target changes:

```powershell
git log --oneline HEAD..origin/main
git diff HEAD..origin/main
```

Choose the integration strategy locally:

- rebase local branch onto `origin/main`;
- merge `origin/main` into the local branch;
- manually port only relevant target changes.

No reverse synchronization from Codex is allowed.

---

## 7. Codex completion contract

A local delivery is complete only when Codex reports:

```text
Target remote: Space653000/0_JN1_AERIS
Target branch: main
Target SHA: <SHA>
Remote write performed: NO
Local workspace: <absolute path>
Local branch: <branch>
Changed local files: <list>
Tests/evals: PASS/FAIL + evidence
Drift vs origin/main: <summary>
Remaining blockers/risks: <summary>
```

If `Remote write performed` is anything except `NO`, the workflow is non-compliant.

---

## 8. Human-controlled publication

If the official GitHub baseline itself needs to change, that is a separate governance operation.

Codex may prepare locally:

- patch / diff;
- changed-file list;
- test evidence;
- architecture rationale;
- rollback plan;
- publication handoff note.

Codex may not publish that package to this repository.

The Human Chief Engineer or another explicitly authorized publication path decides whether the official SSOT changes.

---

## 9. GitHub-side defense in depth

Repository files now include:

- `AGENTS.md` — Codex authority boundary;
- `aeris.policy.yaml` — machine-readable policy;
- `.github/CODEOWNERS` — Human ownership signal;
- local `pushurl` disable script;
- local deny `pre-push` hook;
- verification and one-way sync scripts.

For stronger GitHub-side enforcement, configure a GitHub Ruleset / branch protection on `main` that requires controlled review and blocks direct pushes for non-authorized actors. This connector cannot currently configure repository Rulesets/branch protection, so that final server-side lock must be enabled through GitHub repository settings by an administrator.

---

## 10. Canonical rule

> **Codex reads AERIS GitHub as the target. Codex builds AERIS locally. Codex does not change the AERIS GitHub target.**

```


## docs/governance/GITHUB_ACCESS_BOUNDARY.md

```text
# AERIS GitHub Access Boundary

> **2026-09-07 現行治理：** A–D 依 [Sol 獨立審查閘門 v2](SOL_INDEPENDENT_REVIEW_GATE_V2.md)。預設自動化不得自行 checkout、merge 或 push；Human 可對特定治理發布給出明確、有界的例外授權。

**Policy:** Codex runtime must have no GitHub write credential for `Space653000/0_JN1_AERIS`.

## Preferred access model

Because `Space653000/0_JN1_AERIS` is a public repository, Codex can clone, fetch and read the canonical target without any GitHub token.

Preferred Codex runtime:

```text
GitHub repository visibility: public
Codex GitHub credential: none
Fetch/clone: anonymous HTTPS
Push URL: disabled locally
pre-push hook: deny
Remote write API credential: none
```

This is stronger than relying only on prompt instructions.

## If authenticated read access is ever required

Use a dedicated credential whose repository permissions are read-only. Do not reuse the Human owner's GitHub credential, Personal Access Token, GitHub CLI login or writable GitHub App token inside the Codex runtime.

Minimum principle:

```text
Metadata: read
Contents: read
Pull requests: no write
Issues: no write unless explicitly required for a separate non-publication workflow
Administration: none
Workflows/Actions: no write
```

## Never expose to Codex

Do not expose credentials that can:

- write repository contents;
- update refs / branches / tags;
- create or merge PRs;
- change Actions workflows;
- change Pages settings;
- change repository administration / rulesets / protection;
- publish releases.

## Defense layers

AERIS uses multiple independent controls:

```text
Layer 1  AGENTS.md authority contract
Layer 2  aeris.policy.yaml machine policy
Layer 3  no writable GitHub credential in Codex runtime
Layer 4  disabled local origin push URL
Layer 5  deny pre-push hook
Layer 6  CODEOWNERS / Human publication ownership
Layer 7  GitHub Ruleset / branch protection (recommended server-side lock)
```

The target state is not merely “Codex should not push.” It is:

> **Codex should not possess a viable path that can mutate the official AERIS GitHub repository.**

```


## tools/validate-core-governance.py

```text
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

```
`aeris.retained-rules.json` 是精確取代與保留清單的機器契約；validator 同時核對原文token、mandatory links及固定安全斷言。
