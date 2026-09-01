# AGENTS.md — AERIS Codex Full-Build Autopilot Contract

Repository: `Space653000/0_JN1_AERIS`  
Canonical branch: `main`  
Repository role: **REMOTE READ-ONLY DESIGN SSOT / TARGET BASELINE**

## 0. Non-negotiable Core boundary

During normal AERIS deployment/build, Codex may read/clone/fetch/compare this Core but MUST NOT push, PR, merge, change refs/settings/Rulesets, or otherwise write the canonical Core. Core publication is a separate Human-authorized governance action.

Core defines WHAT AERIS must become. `Space653000/0_JN1_AERIS_Local-computer-implementation` and the selected local workspace define HOW it is built and run.

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
