# 0_JN1_AERIS

**AERIS — Acoustic Engineering & Research Intelligence System**

> **Canonical Core / Remote Read-Only SSOT**  
> This repository defines **WHAT AERIS must be**. Normal Codex/Claude deployment may READ / CLONE / FETCH / COMPARE it, but must not write this Core remotely.

## Zero-experience AERIS Autopilot entry

The intended Human input is only:

```text
https://github.com/Space653000/0_JN1_AERIS
https://github.com/Space653000/0_JN1_AERIS_Local-computer-implementation
<LOCAL_TARGET_PATH>
```

An agent with GitHub + terminal access must interpret that as an AERIS Autopilot request and continue automatically until a genuine Human gate is reached.

Canonical automation contract:

- Codex: [`AGENTS.md`](AGENTS.md) — primary local executor/installer/implementer.
- Claude Code: [`CLAUDE.md`](CLAUDE.md) — independent reviewer/acceptance auditor.
- Machine-readable contract: [`aeris.autopilot.json`](aeris.autopilot.json).
- Authority policy: [`aeris.policy.yaml`](aeris.policy.yaml).
- Exact read order: [`docs/governance/AI_READ_ORDER.md`](docs/governance/AI_READ_ORDER.md).
- End-to-end SOP: [`docs/governance/AI_AUTOPILOT_SOP.md`](docs/governance/AI_AUTOPILOT_SOP.md).

The automation target is:

```text
Core main (read-only blueprint)
        ↓
Implementation repo (executable company image)
        ↓
Human-specified local path
        ↓
Detect / inventory / install / configure
        ↓
Tests / Core integrity / real-machine acceptance
        ↓
Evidence-supported company opening
        ↓
Local supervisor + heartbeat + audit/evidence
        ↓
Independent Claude acceptance
```

It is **not** legitimate to bypass a license, secret, physical calibration, unsupported machine, failed test, privacy rule, checksum/signature failure, Core drift or formal release approval merely to make the process zero-touch.

## Human + AI authority model

```text
Human Chief Engineer = final authority
Canonical Core       = design authority
Codex                = primary local executor
Claude Code          = independent reviewer
Evidence             = engineering decision basis
```

Agent consensus is not evidence. The reviewer is expected to challenge the executor.

## Core read-only protection

For a Git-backed local Core cache, the required state is:

```text
fetch URL = canonical Core
push URL  = DISABLED
pre-push  = DENY
detached canonical checkout
clean working tree
HEAD == recorded canonical Core SHA
```

Legacy/manual PowerShell helpers remain under [`tools/local-only/`](tools/local-only/). In the normal two-repo Autopilot path, the Implementation repository owns the executable synchronization/verification flow.

Normal direction:

```text
GitHub Core main ─────► Local AERIS
```

Not:

```text
Normal Codex deployment ─X─► GitHub Core main
```

A Core publication is a separate Human-controlled governance process.

## Core Architecture

> **1 Human Chief Engineer + 100 Virtual Acoustic Engineering capability seats + model-neutral orchestration + real engineering tools + Evidence + Independent Verification + Human Approval + Reproducibility.**

100 seats are capability/authority/evidence/review boundaries, not 100 permanently running LLM processes. Ordinary Temporary Pods target **2–8 roles**; complex work targets **5–15 roles**.

Permanent truth rules:

```text
Model != Identity
Memory != Evidence
Execution != Completion
Dashboard != Truth
Agent consensus != engineering truth
Implemented != Tested != Verified
```

## Engineering priority

AERIS is not primarily an installer or dashboard project. The deployment harness exists to make the engineering organization reproducible. Core trust priorities remain:

```text
Task identity/state
→ Evidence Bundle
→ G0–G5 verification
→ Independent Reviewer
→ R0–R4 authority / Human approval
→ Golden acoustic cases
→ Audit / Health / Reproduction
→ mature Skills / Methods / Standards
→ professional tool adapters
→ Dynamic Pods
```

## Web UI

The three canonical static target entrances are:

1. [Dashboard / Mission Control](index.html)
2. [Engineering Workspace](workspace.html)
3. [Service Console](services.html)

Target Pages URLs:

- `https://space653000.github.io/0_JN1_AERIS/`
- `https://space653000.github.io/0_JN1_AERIS/workspace.html`
- `https://space653000.github.io/0_JN1_AERIS/services.html`

Repository files existing does not prove Pages is externally deployed or live. UI status is always a projection of real Evidence/Telemetry, never the source of truth.

The current direct-screenshot visual calibration is indexed in [`docs/research/README.md`](docs/research/README.md). If an older visual document conflicts with the latest screenshot calibration, the latest Human-supplied screenshot evidence wins.

## Research / Architecture

Canonical index: [`docs/research/README.md`](docs/research/README.md)

Primary architecture documents:

1. [AERIS Master Research & Architecture Baseline](docs/research/AERIS_MASTER_RESEARCH_ARCHITECTURE_BASELINE_20260831.md)
2. [Kairos / LifeOS Deep Research](docs/research/2026-08-31_Kairos_LifeOS_AERIS_Deep_Research.md)
3. [AERIS Research Data Index](docs/research/AERIS_RESEARCH_DATA_INDEX_20260831.md)
4. [AERIS Web UI / Control Plane Baseline](docs/research/AERIS_WEB_UI_CONTROL_PLANE_BASELINE_20260831.md)

## North Star

> **AERIS is not an AI-agent demo. It is an Acoustic Engineering Organization OS whose conclusions remain traceable, verifiable and reproducible even after today's models are replaced.**
