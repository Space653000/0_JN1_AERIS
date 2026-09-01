# AGENTS.md — AERIS Codex Autopilot Execution Contract

Repository: `Space653000/0_JN1_AERIS`  
Canonical branch: `main`  
Repository role: **REMOTE READ-ONLY DESIGN SSOT / TARGET BASELINE**

## 0. Non-negotiable Core boundary

**Codex MUST NOT modify this canonical GitHub repository or any of its remote refs during normal AERIS implementation/deployment.**

Core defines WHAT AERIS must be. Local implementation defines HOW it runs. Codex may read, clone, fetch, compare and inspect Core; all implementation/install/runtime changes occur in `Space653000/0_JN1_AERIS_Local-computer-implementation` and the Human-specified local target path.

This is an authority boundary, not a suggestion.

## 1. Autopilot trigger — do not make the Human operate the installer

If a Human supplies all three inputs below, treat them as an `AERIS_AUTOPILOT_REQUEST` even if no additional prose is supplied:

```text
https://github.com/Space653000/0_JN1_AERIS
https://github.com/Space653000/0_JN1_AERIS_Local-computer-implementation
<LOCAL_TARGET_PATH>
```

Then automatically:

1. read the canonical order in `aeris.autopilot.json` and `docs/governance/AI_READ_ORDER.md`;
2. protect/verify this Core as read-only locally;
3. acquire/update the Implementation repository at the requested local path;
4. read its `AGENTS.md`, `config/autopilot.json`, maturity and Core lock/alignment;
5. execute its platform-specific `AERIS_AUTOPILOT` entrypoint;
6. let the implementation detect OS/machine/network/runtime/model and perform every safe automated step;
7. run deterministic tests and real-machine acceptance when prerequisites exist;
8. open the company only to an evidence-supported operational scope;
9. preserve bootstrap/acceptance/opening/audit evidence;
10. stop and ask the Human only at a genuine Human gate.

Do **not** ask the Human to choose ordinary Python paths, virtualenv commands, package order, test commands, log locations, default local ports or other safely detectable implementation details.

## 2. Allowed Core remote operations

Codex may perform read-oriented operations only:

- read files/directories/issues/documentation;
- clone Core locally;
- `git fetch origin main`;
- inspect `origin/main` history and SHA;
- compare local Core cache to canonical `origin/main`;
- report Core drift.

## 3. Forbidden Core remote operations

During normal AERIS work Codex MUST NOT directly or indirectly:

- push / force-push;
- create/update/delete remote branches or tags;
- create/update/merge/close PRs against Core;
- use GitHub write APIs against Core;
- update refs/releases/Pages/settings/Rulesets/branch protection;
- bypass/re-enable a disabled Core push path;
- auto-update an Implementation Core lock merely to silence drift.

If Core changed, Implementation must fail closed until the new Core semantics are deliberately reviewed and implemented.

A separate Human-controlled Core publication process may exist outside normal Codex deployment. It must be explicitly commissioned by the Human and must not be inferred from an implementation task.

## 4. Canonical read order

Before execution read, in order:

1. `AGENTS.md`
2. `CLAUDE.md` for reviewer separation
3. `aeris.policy.yaml`
4. `aeris.autopilot.json`
5. `docs/governance/AI_READ_ORDER.md`
6. `docs/governance/AI_AUTOPILOT_SOP.md`
7. `docs/research/README.md`
8. `docs/research/AERIS_MASTER_RESEARCH_ARCHITECTURE_BASELINE_20260831.md`
9. `docs/research/AERIS_WEB_UI_CONTROL_PLANE_BASELINE_20260831.md`
10. task-specific Core material.

Earlier authority wins over later convenience documentation.

## 5. Local Core guard

Every Git-backed Core cache used by Codex must have defense in depth:

```text
canonical fetch URL
+ disabled push URL
+ deny pre-push hook
+ detached canonical checkout
+ clean worktree
+ HEAD == canonical/recorded SHA
```

A checksum-manifested air-gap snapshot is acceptable when Git is unavailable, but its manifest still needs a trusted source/authenticity story for high assurance.

## 6. Human–AI responsibility split

```text
Human Chief Engineer = final authority / irreversible and formal release approval
Codex               = primary local executor / installer / implementer
Claude Code         = independent reviewer / acceptance auditor
Core                = design authority
Evidence            = basis for engineering truth
```

Codex must not use model consensus as engineering evidence. Claude agreeing with Codex is not proof.

## 7. Truth and operating states

Capability maturity:

```text
NOT_IMPLEMENTED → IMPLEMENTED → TESTED → VERIFIED
                         ↘ BLOCKED_EXTERNAL where applicable
```

Operational state is separate:

```text
CLOSED
BOOTSTRAPPING
BLOCKED
OPEN_WITH_LIMITS
OPEN_VERIFIED_SCOPE
```

Installation success cannot directly promote a company/capability to VERIFIED.

## 8. Human gates — only ask when genuinely blocked

Codex should continue automatically until one of these is encountered:

- OS denies required administrator/elevation action;
- proprietary license/EULA requires Human acceptance;
- secret/customer credential/hardware token is required;
- physical cable/fixture/chamber/instrument/calibration action is required;
- a destructive disk/network/firewall change could affect unrelated systems;
- external publication/customer/formal/production release;
- changing canonical Core policy.

When blocked, preserve completed work and ask for the **minimum exact Human action**, not a generic troubleshooting session.

## 9. No destructive convenience

Autopilot must be idempotent and conservative:

- never delete customer/private data to make installation easier;
- never wipe an unrelated non-empty directory;
- back up before migrations that can overwrite local state;
- never weaken privacy/checksum/verification gates to obtain a green result;
- prefer resume/reuse over recreation.

## 10. Required Codex completion evidence

Every deployment/implementation run must report or point to machine-readable evidence containing:

```text
Canonical Core SHA
Core remote write performed: NO
Implementation SHA
Local target path
Machine Profile
Runtime mode
Private endpoint scope
Bootstrap result
Unit/security test result
Core integrity result
Local inference result
Offline result
Hard-offline result or NOT_TESTED
Company opening state
Supervisor/heartbeat state
Evidence/audit paths
Unverified capabilities
External blockers
Required Human action, if any
```

## 11. North-star invariant

The automation harness does not replace AERIS engineering maturity. Core priorities remain Evidence / Verification / Reproducibility, not installer cosmetics.

**GitHub Core is the blueprint. The local Implementation is the construction site. Codex builds locally; Claude challenges the evidence; the Human remains Chief Engineer.**
