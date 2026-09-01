# AERIS Human + AI Autopilot SOP

## Objective

The Human should be able to provide only:

```text
https://github.com/Space653000/0_JN1_AERIS
https://github.com/Space653000/0_JN1_AERIS_Local-computer-implementation
<LOCAL_TARGET_PATH>
```

to an agent with repository + terminal access. The agent should infer the AERIS Autopilot contract, perform all safe deterministic work automatically, and stop only at a real Human gate.

This is a **zero-experience target**, not permission to fake success. External licenses, credentials, physical calibration and operating-system privilege boundaries may still require Human action.

## 1. Repository roles

```text
0_JN1_AERIS
= WHAT AERIS must be
= canonical read-only Core / SSOT

0_JN1_AERIS_Local-computer-implementation
= HOW AERIS is installed/executed locally
= writable construction + Portable Company Image

Local target path
= actual company premises / runtime / evidence
```

Core must never be used as the construction directory.

## 2. Normal Human–AI operating model

```text
Human Chief Engineer
        │ final authority
        ▼
Canonical Core SSOT
        │ design truth
        ├───────────────┐
        ▼               ▼
Codex executor      Claude reviewer
        │               │
        └──── Evidence ──┘
                │
                ▼
        Local AERIS instance
```

Codex and Claude are intentionally separated. The reviewer should try to disprove the executor's claims.

## 3. Codex automatic bootstrap sequence

When the trigger inputs are present, Codex should execute without asking optional questions:

### Phase A — workspace safety

1. canonicalize the Human-specified target path;
2. refuse system roots, the user's entire home/profile directory, or a non-empty unrelated directory unless a safe subdirectory can be created;
3. detect existing AERIS checkout/state and prefer idempotent upgrade over destructive recreation;
4. record OS, architecture, current user, disk, RAM, GPU/accelerator, network availability and available package managers/tools.

### Phase B — acquire sources

1. fetch/clone Core only as a read-only reference;
2. disable Core push URL and install deny pre-push guard;
3. clone/update Implementation at the target path;
4. record both commit SHAs;
5. verify Implementation `core.lock.json` / semantic alignment against canonical Core before installation.

If Core has moved and Implementation has not deliberately reviewed the new Core, stop with `BLOCKED_CORE_DRIFT`. Never auto-update the lock merely to make CI green.

### Phase C — inventory and plan

Run the implementation Autopilot in plan/preflight mode. Determine:

- supported Machine Profile;
- Python/runtime availability;
- local inference runtime/model availability;
- required disk/RAM/headroom checks that are implemented;
- online/offline path;
- staged assets;
- external/proprietary dependencies;
- privacy/network scope;
- existing AERIS state/backup needs.

Write the plan before mutation.

### Phase D — safe installation/configuration

Automatically perform only reversible/controlled actions supported by the implementation:

- create isolated AERIS directories/venv;
- install redistributable prerequisites through supported package mechanisms;
- install/start local inference runtime where supported;
- acquire/import the configured local model when network/policy permits;
- create `.env` from versioned template without committing secrets;
- synchronize and verify Core read-only cache;
- build local Knowledge index;
- initialize audit/evidence/runtime state;
- preserve previous local state before any migration that could overwrite it.

Never auto-accept proprietary EULAs, invent credentials, weaken firewall/privacy controls, or bypass checksum/signature failures.

### Phase E — deterministic tests

Mandatory before real-machine acceptance:

```text
compile/syntax checks
unit/security tests
100-seat manifest checks
Core semantic alignment
Core cache integrity
privacy/endpoint policy tests
Knowledge build
Machine Profile detection
package/config sanity
```

Any failure = stop promotion. Fix only within authorized implementation/local scope, then rerun from the failed gate and all dependent gates.

### Phase F — real-machine acceptance

When prerequisites exist, run the real local acceptance path. It must preserve evidence for:

- real local model reachability;
- real inference response;
- offline-mode inference;
- Core integrity;
- supported machine profile;
- tests;
- applicable network/offline checks;
- applicable tool/driver/license/calibration checks.

A CI runner cannot substitute for this phase.

### Phase G — company opening

Installation alone is not opening.

Opening gate must produce one of:

```text
BLOCKED
OPEN_WITH_LIMITS
OPEN_VERIFIED_SCOPE
```

`OPEN_VERIFIED_SCOPE` may be used only for the exact capability scope whose required acceptance has passed.

Opening should start the versioned local supervisor/heartbeat where implemented and write a machine-readable opening report. Missing future P0 acoustic capabilities remain explicitly listed; they do not disappear because the kernel is operational.

### Phase H — handoff

Codex must finish with paths, not reassurance:

```text
Core SHA
Implementation SHA
Target path
Machine Profile
Runtime mode
Opening state
Local supervisor state
Acceptance report path
Bootstrap report path
Audit/evidence paths
Unverified capabilities
External blockers
Exact Human action required, if any
```

## 4. Claude automatic independent acceptance

After Codex completes, Claude Code receives the same two repositories + target path and automatically:

1. reads Core authority independently;
2. runs the implementation `CLAUDE_VERIFY_AERIS` entrypoint;
3. validates commit/core lock/hash relationships;
4. reruns deterministic checks that are safe to repeat;
5. reads raw acceptance/opening reports rather than Codex prose;
6. checks maturity claims against actual evidence;
7. identifies counter-hypotheses and missing evidence;
8. returns `PASS`, `PASS_WITH_LIMITS`, `BLOCKED`, or `FAIL`.

Claude must not approve a silent repair performed during the same acceptance context. Repair → fresh review.

## 5. Human gates

AERIS aims for minimal Human burden, not removal of legitimate authority.

Human action is still required for cases such as:

- OS elevation that the agent cannot lawfully obtain;
- proprietary license/EULA acceptance;
- API key, private credential, customer secret or hardware token;
- physical fixture/cable/chamber/instrument/calibration action;
- destructive disk/network/firewall change outside the isolated AERIS scope;
- customer/formal/production release;
- changing canonical Core policy itself.

The agent must state exactly one minimal next action and preserve all completed work so rerun is idempotent.

## 6. Recovery / idempotency

Autopilot must be safe to rerun.

Preferred behavior:

```text
Detect existing good state → reuse
Detect stale generated state → rebuild
Detect incompatible version → back up + migrate or BLOCK
Detect failed partial install → resume from deterministic checkpoint
Never delete customer/private data to make setup easier
```

Each run receives a run ID and writes durable reports.

## 7. No-fantasy opening rule

These statements are forbidden unless their exact scope is verified:

```text
100 engineers ready
all tools supported
all computers supported
privacy guaranteed
hard offline guaranteed
production ready
company complete
```

A truthful opening can instead say:

> AERIS local company kernel is OPEN for the verified baseline scope on this machine; listed acoustic P0 capabilities and external professional-tool integrations remain unverified/not implemented as recorded in maturity evidence.

## 8. Long-term target

The Autopilot is only the deployment/operations harness. AERIS's main engineering priority remains the Core trust foundation:

```text
Task identity/state
→ Evidence Bundle
→ G0–G5 verification
→ independent reviewer
→ R0–R4 authority/Human approval
→ Golden acoustic cases
→ audit/health/reproduction
→ mature Skills/Methods/Standards
→ professional tool adapters
→ Dynamic Pods
```

A more automatic installer must never substitute for this engineering maturity.
