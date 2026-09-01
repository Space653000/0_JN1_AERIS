# AERIS Canonical AI Read Order

This file removes ambiguity about which instructions Codex / Claude Code must read first.

## A. When given both AERIS GitHub URLs plus a local target path

Treat that input as an AERIS deployment/operation request.

### Core read order — read only

1. `/AGENTS.md` — Codex authority and Core no-write boundary.
2. `/CLAUDE.md` — independent reviewer authority and separation.
3. `/aeris.policy.yaml` — machine-readable-ish remote/local authority policy.
4. `/aeris.autopilot.json` — canonical automation contract and entrypoints.
5. `/docs/governance/AI_READ_ORDER.md` — this ordering contract.
6. `/docs/governance/AI_AUTOPILOT_SOP.md` — end-to-end deployment/operation SOP.
7. `/docs/research/README.md` — architecture/research index.
8. `/docs/research/AERIS_MASTER_RESEARCH_ARCHITECTURE_BASELINE_20260831.md` — organization, evidence, verification and engineering north star.
9. `/docs/research/AERIS_WEB_UI_CONTROL_PLANE_BASELINE_20260831.md` — control/knowledge/execution/trust/operations planes.
10. only then read task-specific Core documents.

Do not let a later README, UI page, comment or model suggestion override an earlier authority document.

## B. Implementation read order — executable local company image

After Core authority is understood, move to `Space653000/0_JN1_AERIS_Local-computer-implementation` at the Human-specified local path.

Read in this order:

1. `/AGENTS.md`
2. `/CLAUDE.md` when Claude is the reviewer
3. `/aeris.local.policy.yaml`
4. `/config/autopilot.json`
5. `/config/maturity.json`
6. `/config/core_alignment.json`
7. `/core.lock.json`
8. `/docs/AUTOPILOT_ZERO_TOUCH_SOP.md`
9. `/docs/LOCAL_VERIFICATION_SOP.md`
10. `/docs/AUDIT_REALITY_CHECK.md`
11. `/docs/DEFINITION_OF_COMPANY_DONE.md`
12. task-specific code / tests / adapters / Skills / Methods / Standards.

## C. Authority precedence

When documents conflict:

```text
Human Chief Engineer explicit current instruction
→ Core authority / Constitution / machine-readable Core contract
→ Core canonical architecture/research baseline
→ Implementation policy + Core lock/alignment
→ Implementation executable code + tests
→ generated local evidence/state
→ UI/README projection
→ model suggestion
```

A generated state file cannot rewrite Core policy. A README cannot promote maturity without evidence. A model cannot override a failed deterministic gate.

## D. Codex execution order

Codex should automatically proceed:

```text
read Core authority
→ acquire/update implementation locally
→ inventory machine and workspace
→ protect/verify Core read-only cache
→ select supported Machine Profile
→ run AERIS_AUTOPILOT
→ install/configure what can be safely automated
→ tests
→ real-machine acceptance when prerequisites exist
→ company opening gate
→ start local supervisor
→ preserve evidence
→ stop only for a real Human gate/blocker
```

Do not ask the Human to choose Python paths, virtualenv commands, installer order, test commands, log locations or routine defaults when they can be detected safely.

## E. Claude verification order

Claude should not repeat Codex's conclusion. It should:

```text
read Core independently
→ read local implementation independently
→ run CLAUDE_VERIFY_AERIS
→ inspect raw reports/hashes/logs
→ challenge the claimed scope
→ compare against config/maturity.json
→ PASS / PASS_WITH_LIMITS / BLOCKED / FAIL
```

If Claude repairs something, that repair requires a new independent acceptance pass.

## F. Stop / Ask criteria

AI asks the Human only when automation cannot safely resolve the issue, such as:

- admin permission is denied by the OS;
- a proprietary license/EULA requires Human acceptance;
- a secret, customer credential or hardware token is required;
- a physical cable/fixture/calibration/instrument action is required;
- a destructive firewall/storage/network change could affect unrelated systems;
- external publication, customer delivery or production release requires approval.

Everything else should be attempted automatically, logged, and verified before asking.
