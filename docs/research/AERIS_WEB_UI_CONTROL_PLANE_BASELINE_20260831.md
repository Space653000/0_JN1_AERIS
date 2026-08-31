# AERIS Web UI / Control Plane Baseline

**Date:** 2026-08-31 (Asia/Taipei)  
**Repository:** `Space653000/0_JN1_AERIS`  
**Status:** UI / information-architecture target baseline; not an implementation-complete claim  
**Purpose:** Merge the missing concrete web-interface design from the 2026-08-31 AERIS discussion into the research package.

---

# 0. Why this addendum exists

The existing three research files already contain most of the deep architecture:

- Kairos / LifeOS Agent Harness lessons
- model-neutral SSOT
- 100 Virtual Acoustic Engineering Seats
- Speaker / Microphone × six engineering disciplines
- 24 Product Chiefs
- Evidence / Verification / Reproducibility
- risk / approval controls
- standards lifecycle intelligence
- autonomous R&D loop
- observability and false-Done prevention

However, the prior baseline did **not** fully define the concrete AERIS web product surface. In particular, it lacked a committed specification for:

1. the **Dashboard / Mission Control** page,
2. the **Engineering Workspace** page used by the Human Chief Engineer,
3. the **Service Console** page for backend Harness / Trust / Operations,
4. a formal **Global AI Organization / Profession Benchmark 100** research module,
5. the exact relationship among UI state, backend truth, Evidence, Verification and Health.

This document fills those gaps and supersedes the earlier sequencing statement that treated Dashboard as a late P3-only concern.

The corrected decision is:

> **Build a thin, truthful three-page web shell early, but do not let UI completeness outrun Evidence / Verification / state-machine truth.**

The UI is therefore an early control surface, while engineering trust remains the primary backend priority.

---

# 1. AERIS Product Positioning

AERIS should be presented as:

> **AERIS — Acoustic Engineering & Research Intelligence System**
>
> **One Human Chief Engineer directing a 100-seat virtual acoustic engineering organization.**

The 100 seats are professional capability contracts, not 100 always-running processes.

Typical runtime target:

- ordinary task: **2–8 roles**
- complex task: **5–15 roles**
- all 100 roles remain available in the Role Library

Core formula:

> **AERIS = Kairos-style Agent Harness × 100-seat Acoustic Organization × Engineering Evidence System × Autonomous R&D Loop**

---

# 2. Three Canonical Web Entrances

The first official web information architecture is intentionally limited to three top-level pages.

| Page | Path | Primary question |
|---|---|---|
| Dashboard | `/index.html` | **What is happening across AERIS now?** |
| Engineering Workspace | `/workspace.html` | **What do I want AERIS to engineer?** |
| Service Console | `/services.html` | **Is the Harness / backend / trust infrastructure healthy?** |

Later detail pages may include:

- Projects
- Speaker
- Microphone
- Product Pods
- Simulation
- Algorithm
- Validation
- Tuning
- Autonomous Lab
- Skills
- Memory
- Knowledge Graph
- Standards
- Benchmark 100
- Evidence
- Verification
- Risk & Approval
- Reproduction
- Audit

But these must not fragment the first usable control surface.

---

# 3. Visual Language — Kairos-inspired, not a clone

The UI should borrow the public Kairos / LifeOS visual principles while remaining clearly AERIS:

- very light gray / warm white background
- fixed left navigation on desktop
- teal / aqua accent
- compact pastel status chips
- identity / mission hero card
- small KPI cards
- dense engineering detail only after drill-down
- calm, information-first hierarchy
- Traditional Chinese first; English engineering terminology retained where useful

The UI must **not** copy unknown Kairos implementation details such as framework, database, frontend library or proprietary components.

---

# 4. Dashboard — Mission Control

## 4.1 Purpose

The Dashboard answers:

> **What is AERIS doing, what is blocked, what needs human attention, and can every green state be proven?**

## 4.2 Required top-level blocks

### Identity Hero

Display:

- AERIS name
- `Acoustic Engineering & Research Intelligence System`
- `100-seat AI Acoustic Engineering Organization`
- Local-first / model-neutral positioning
- quick tags: Speaker, Microphone, Acoustic, Audio, Validation, Tuning, Simulation, Algorithm, Autonomous Lab, Evidence-first

### North-Star KPI cards

Minimum cards:

| KPI | Target / meaning |
|---|---|
| Virtual Engineering Roles | 100 |
| Core Acoustic Matrix | 2 × 6 |
| Product Chiefs | 24 |
| Verification Gates | G0–G5 |
| Typical Active Specialists | 5–15 |
| False-Done | 0 target |
| Unauthorized R3/R4 | 0 target |
| Tier-A Evidence Completeness | 100% target |
| Calibration Validity | 100% applicable runs |
| Tier-A Reproduction | 100% target |

### Acoustic Autonomous R&D Loop

```text
Requirement
→ Method
→ Execution
→ Evidence
→ Verification
→ Approval
→ Reproduction
→ Knowledge Promotion
```

The UI must make the following state distinction explicit:

```text
DRAFT
→ READY
→ EXECUTING
→ EXECUTED
→ EVIDENCED
→ VERIFIED
→ APPROVED
→ RELEASED
```

Forbidden shortcut:

```text
EXECUTED → DONE
```

### Active Engineering Pods

Show current project pods with:

- project / product
- lifecycle stage
- selected roles
- risk tier
- current workflow state
- blocker
- evidence completeness
- approval required / not required

### Human Attention Queue

Priority examples:

- R3 / R4 approval waiting
- Verification FAIL
- standard stale / withdrawn
- calibration expired
- expected scheduled run missed
- artifact stale
- simulation-measurement correlation below acceptance threshold

### 100-Seat Role Library

Searchable by:

- role name
- organization block
- Speaker / Microphone / All
- discipline
- product

Role Library is a capability registry, not a chat-contact list.

---

# 5. Engineering Workspace — Human Chief Engineer Work Surface

## 5.1 Core UX decision

The Human Chief Engineer should **not** manually choose among 100 chatbots.

The canonical interaction is:

```text
Human engineering objective
↓
Requirement Parser
↓
Task / Risk Classification
↓
Role Router
↓
Temporary Engineering Pod
↓
Workflow / Skill / Tool plan
```

## 5.2 Required task form

Minimum fields:

- Product
- Speaker / Microphone / Both
- Lifecycle stage
- Engineering objective
- constraints
- available inputs / raw data
- Evidence level
- standards strategy
- risk tier
- desired output
- acceptance / stop condition

### Example

```text
Product: Laptop
System: Speaker
Lifecycle: EVT
Risk: R2 Controlled Engineering Execution

Objective:
100–250 Hz speaker energy is insufficient.
Enclosure volume cannot increase.
Xmax, THD, power and thermal limits must remain compliant.
Do not use EQ to mask an unverified mechanical root cause.
```

## 5.3 Temporary Pod example

For the example above, AERIS may select roles such as:

- #001 Chief Acoustic Architect
- #004 Product Audio System Architect
- #006 Validation & Quality Director
- #009 Speaker Acoustic System Architect
- #010 Transducer / T-S / Nonlinear Specialist
- #011 Enclosure / Port / Waveguide Specialist
- #015 Speaker Measurement Engineer
- #016 Nonlinear / Power / Reliability Validation Engineer
- #019 Dynamics / Bass / Protection Tuning Engineer
- #021 Lumped / FEM Acoustic Simulation Engineer
- #025 Smart-Amp / Protection Algorithm Engineer
- #053 Laptop Product Chief
- #075 Thermal / Power / Reliability
- #079 Metrology / Measurement Uncertainty
- #098 Acoustic Red-Team / DFMEA Reviewer

The exact pod must be generated from capability fit, risk, evidence requirements and tool needs.

## 5.4 Workspace panels

### Requirement Board

Track:

- target
- upper/lower limit
- margin
- unit
- condition
- source
- applicable standard / customer spec

### Hypothesis Board

Each hypothesis must be explicitly marked:

- UNVERIFIED
- PARTIALLY SUPPORTED
- REJECTED
- VERIFIED ROOT CAUSE

No LLM confidence alone may promote a hypothesis to verified root cause.

### Evidence Needed

Examples:

- impedance
- near-field FR
- T/S / nonlinear parameters
- Xmax
- temperature
- leakage / sealing
- assembly tolerance
- geometry
- lumped simulation
- FEM / BEM
- DOE
- listening / perceptual data

### Engineering Contract

Every task externalizes:

- **STOP** — what qualifies as complete
- **ASK** — when Human authority is required
- **REROUTE** — when the workflow must return to a prior stage
- **VERIFY** — evidence and acceptance gates required before release

---

# 6. Service Console — Backend / Harness / Trust Surface

The Service Console is for system health and architecture operations, not normal engineering conversation.

AERIS backend is grouped into five planes.

## 6.1 Control Plane

- AERIS Orchestrator
- Intent / Task Classifier
- Requirement Parser
- Role / Pod Router
- Workflow State Machine

## 6.2 Knowledge Plane

- Engineering Constitution
- Core Rules SSOT
- Skill Registry
- Method Registry
- Standards Registry
- Engineering Memory
- Knowledge Graph

## 6.3 Execution Plane

- Model Router
- model adapters
- Python / MATLAB
- COMSOL / Ansys / Simcenter
- KLIPPEL / APx / SoundCheck / ACQUA
- instrument / DAQ / chamber adapters

## 6.4 Trust Plane

- Evidence Store
- Verification Engine
- Independent Reviewer
- Approval Service
- Reproduction Runner

## 6.5 Operations Plane

- Observability
- Audit Ledger
- Health Monitor
- Expected-Run Ledger
- Artifact Freshness Monitor
- Alerting / retry / timeout / cancellation

---

# 7. Service Health Semantics

The UI must never invent a green light from missing telemetry.

Allowed health states should include:

```text
HEALTHY
DEGRADED
FAILED
UNKNOWN
NO_HEARTBEAT
STALE
NOT_CONFIGURED
BLOCKED
```

This is mandatory because:

> **process_alive != system_healthy**

Minimum backend health evidence:

```text
process_alive
expected_run_exists
last_success_at
last_heartbeat
scheduled_job_missed
expected_artifact_exists
artifact_freshness
verification_completed
calibration_valid
standard_revision_current
approval_pending_age
```

A static or mock frontend must display **DESIGN TARGET / DEMO DATA**, never `HEALTHY`, unless live telemetry exists.

---

# 8. Verification Gate shown in the Service Console

| Gate | Purpose | Primary executor |
|---|---|---|
| G0 Contract | schema, unit, hash, required files | deterministic |
| G1 Numerical | unit tests, NaN/Inf, ranges, dimensional consistency | deterministic |
| G2 Domain | acoustic / physical sanity, calibration, method prerequisites | deterministic rules + domain logic |
| G3 Regression | Golden cases, approved baseline, negative cases | deterministic |
| G4 Independent Review | requirement interpretation, suitability, exceptions | reviewer role |
| G5 Approval | high-impact execution / formal external release | Human |

Rule:

> G0–G3 must never be reduced to LLM subjective opinion.

---

# 9. Risk Authority Matrix shown in the Service Console

| Tier | Example | Agent authority | Gate |
|---|---|---|---|
| R0 | read / search / analysis | automatic | evidence log |
| R1 | reversible local change | automatic with tests | diff + tests |
| R2 | controlled project / measurement change | limited | reviewer / preconditions |
| R3 | possible DUT damage / hardware risk | not autonomous | explicit Human approval |
| R4 | customer report / official Pass-Fail / external release | no autonomous release | independent review + Human signature |

Principle:

> **Capability does not imply authority.**

---

# 10. Dashboard is projection, not truth

This rule must be visible in the architecture and implementation documentation:

```text
Real execution / data
↓
Evidence
↓
Verification
↓
Telemetry / state store
↓
Dashboard projection
```

Not:

```text
Dashboard state
↓
therefore engineering truth
```

Every important green state should be drillable to:

- run_id / task_id
- artifact
- hash
- raw / processed data
- method version
- tool version
- calibration state
- standard edition
- verification result
- reviewer
- approval record

---

# 11. Global AI Organization / Profession Benchmark 100

There is no credible single global official ranking of “Top 100 AI one-person companies / AI-replaced professions.” AERIS must not fabricate one.

Instead, maintain a living dataset named:

> **Global AI Organization / Profession Benchmark 100**

Its purpose is not ranking by fame. It is to capture **100 reusable operating models** relevant to building AERIS.

Each record should contain:

```yaml
benchmark_id:
organization_or_system:
industry:
ai_role:
operating_model:
human_role:
tools:
workflow_loop:
quantitative_signal:
evidence_class:
source_urls:
last_verified_at:
aeris_transfer_pattern:
risk_or_failure_lesson:
```

Initial seed categories:

- AI Scientist / autonomous research
- engineering agents
- legal professional AI
- customer-service resolution AI
- AI-native one-person / small-team operation
- long-horizon autonomous operation
- coding / software agent harnesses
- manufacturing / industrial automation agents
- data / research / analyst roles
- governance / evaluation / observability systems

The existing research package already includes seed examples such as FutureHouse, LILA, Siemens Eigen, Harvey, Intercom Fin, Coinbase, Cisco, Project Vend / Vending-Bench and multi-agent software experiments.

The Dashboard may display this as a research module, but the canonical data belongs in the research / knowledge layer.

---

# 12. Navigation Baseline

Recommended left navigation:

```text
AERIS

● SYSTEM STATUS

◉ Dashboard
⌁ Workspace

ENGINEERING
◈ Projects
Speaker
Microphone
Product Pods
Simulation
Algorithm
Validation
Tuning
Autonomous Lab

INTELLIGENCE
Skills
Memory
Knowledge Graph
Standards
Benchmark 100
Research

TRUST
Evidence
Verification
Risk & Approval
Reproduction

SYSTEM
Services
Health
Activity
Audit
```

The initial repository implementation may expose only the first three pages while the remaining destinations are disabled / future modules.

---

# 13. Corrected implementation priority

The previous Master Baseline placed Dashboard in P3 and advised “Dashboard later.” That remains valid **only for a mature telemetry-rich control plane**.

The corrected distinction is:

## Early Thin UI — now

Build:

- Dashboard shell
- Engineering Workspace shell
- Service Console shell
- truthful `DESIGN TARGET` / `NOT CONNECTED` status semantics
- static Role Library / architecture projection

Purpose:

- establish information architecture
- give the Human Chief Engineer one canonical entrance
- make the target system understandable
- prevent future backend work from fragmenting the UX

## Mature Control Plane — later

Only after Evidence / state / health backends exist, add:

- live project status
- real agent / pod runtime state
- real instrument status
- real telemetry
- real health SLOs
- approval queue
- evidence drill-down
- standards freshness alerts
- automatic incident detection

Therefore:

> **Build the UI shell early; build the claim of “health” only after backend truth exists.**

---

# 14. Acceptance criteria for the first three pages

## Dashboard

- clearly states AERIS north star
- shows 100-seat organization concept
- explains 2 × 6 acoustic matrix
- shows Autonomous R&D loop
- distinguishes target/mock status from live truth
- provides navigation to Workspace and Services

## Workspace

- one Human task surface, not 100 chat windows
- captures Product / Transducer / Risk / Objective / Evidence target
- demonstrates dynamic Temporary Pod formation
- shows STOP / ASK / REROUTE / VERIFY contract

## Services

- shows five-plane backend architecture
- shows Verification G0–G5
- shows Risk R0–R4
- shows Evidence / Reproduction / Observability concepts
- uses `DESIGN TARGET` or equivalent until live telemetry is connected

---

# 15. Final UI architecture decision

The UI north star is:

> **One Human Command Surface, many specialized capabilities, one evidence contract.**

The permanent system asset remains:

```text
Constitution
+ Rules
+ Skills
+ Methods
+ Standards
+ Memory
+ Knowledge Graph
+ Workflows
+ Tool Adapters
+ Evidence
+ Verification
+ Audit
+ Reproduction
```

The web interface exists to make those assets operable and observable; it must never become a source of unverified engineering truth.
