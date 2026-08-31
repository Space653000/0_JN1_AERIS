# AERIS Master Research & Architecture Baseline
## Kairos / AI-Native Solo Company / 100-Seat Acoustic Engineering Organization
**Repository:** `Space653000/0_JN1_AERIS`  
**Baseline date:** 2026-08-31 (Asia/Taipei)  
**Status:** Architecture / Research baseline; not an implementation-complete claim  
**Purpose:** Consolidate the research facts, quantitative data, acoustic scope, architecture decisions, standards intelligence, verification model, and implementation roadmap discussed for AERIS.

---

# 0. Executive Summary

AERIS — **Acoustic Engineering & Research Intelligence System** — should not be designed as a single chatbot, a single model, or 100 permanently running agents.

The target architecture is:

> **1 Human Chief Engineer + 100 Virtual Acoustic Engineering Seats + model-neutral orchestration + acoustic engineering tools + traceable knowledge + evidence + independent verification + physical measurement loop.**

The transferable operating model extracted from current AI-native organizations and agent systems is:

> **Rules → Skills → Memory → Workflows → Tools → Automation → Approval → Evaluation → Observability**

For professional acoustic engineering, AERIS must extend this to:

> **Evidence → Provenance → Traceability → Independent Verification → Engineering Reproducibility**

Five constitutional statements define the target:

1. **Model is not AERIS identity.**
2. **100 Seats are capabilities, not 100 always-running agents.**
3. **Memory is not Evidence.**
4. **Execution is not Completion.**
5. **Engineering truth is established by evidence and verification, not by Agent consensus.**

---

# 1. Research Boundary and Important Caveat

## 1.1 No credible official “world top 100 AI one-person companies/jobs” ranking

A web-wide review found many “Top 100 AI companies / one-person companies / AI jobs” pages, but no authoritative global ranking that can honestly be treated as the definitive “world top 100 AI-built one-person companies or AI-replaced professional roles.”

Therefore this document does **not** fabricate a ranking.

Instead, it extracts **transferable operating patterns** from frontier examples that demonstrate one or more of:

- one-person or very small AI-native teams,
- professional task automation,
- multi-agent scientific/engineering work,
- tool-using agents,
- autonomous experiment loops,
- measurable outcome automation,
- long-horizon agent failure modes,
- evaluation and observability practices.

The architecture is then mapped onto acoustic engineering.

---

# 2. Frontier AI-Native Organization / Profession Evidence

| # | Organization / System | Date / period | Quantitative / factual signal | Transferable pattern for AERIS |
|---|---|---|---|---|
| 1 | Coinbase AI-native operating model | 2026-05-05 memo | Explicitly discussed “one person teams”, leaders owning broader scopes, and people managing fleets of agents | Fewer humans + broader ownership; agent fleets are subordinate to accountable human ownership |
| 2 | Cisco MyAgent | 2026 reporting | Rolled personalized AI agents broadly across a workforce of roughly 90,000 employees | Per-user agent + policy server + routing + enterprise connectors |
| 3 | FutureHouse AI Scientist | 2025–2026 | AI Scientist concept: broad scientific direction → assistants/tools → experiments/analysis/paper | Hierarchical scientific organization rather than single chatbot |
| 4 | FutureHouse Robin | 2025–2026 | Multi-agent end-to-end scientific workflow; Nature-related publication update 2026-05-19 | Hypothesis → experiment strategy → analysis → follow-up insight |
| 5 | LILA Sciences AI Science Factory | 2025–2026 | Reasoning model + autonomous lab/instruments + verifiers + continuous learning | “Brain + body + verifier”; real experiments are truth signals |
| 6 | Autonomous materials labs | 2026-07-08 publication | Multi-agent AI manages autonomous-materials-lab campaigns and resource optimization | Engineering campaign orchestration |
| 7 | Siemens Eigen Engineering Agent | 2026-04-20 | Piloted with >100 customers across 19 countries | Autonomous engineering tasks tied to real engineering environments and customer standards |
| 8 | Harvey Legal AI | 2026 public metrics | 400K+ agentic queries/day; 20M+ terms extracted; 445K+ deep-analysis reports; 25,000+ custom workflows | Professional workflow library, structured review, repeatable domain work |
| 9 | Intercom Fin | 2026-06 public metric | ~76% average resolution rate; 7,000+ teams cited | Measure outcomes, not agent activity |
| 10 | Anthropic Project Vend | 2025–2026 | Real vending-business operation exposed long-horizon failures and economic mistakes | Autonomous operation needs state, constraints, monitoring and kill switches |
| 11 | Andon Labs / Vending-Bench | 2025–2026 | Long-horizon agent benchmarks show forgetting, delivery misreads, meltdown loops | Long-running jobs require explicit state machine and observability |
| 12 | Anthropic parallel Claude C compiler experiment | 2026-02-05 | 16 parallel Claude agents, nearly 2,000 Claude Code sessions, about US$20,000 API cost, ~100,000 lines of Rust compiler code | Tests/harness/isolated environments/task partitioning matter more than number of agents |
| 13 | SWE-bench / coding-agent harness evidence | 2025–2026 | Same model performance can move materially with scaffolding/harness; research reports large benchmark swings | Harness design is part of system capability |
| 14 | Meta AI-native pod restructuring reports | 2026-08 | Reported productivity ambitions were tempered by operational/technical disruption | Do not equate headcount reduction with reliable output |

## 2.1 Core synthesis

These cases converge on one architecture principle:

> **Do not build “a universal AI employee.” Build an accountable organization of capabilities, tools, workflows, verifiers, state, and evidence.**

For AERIS:

```text
Stephen
  ↓
Chief Acoustic Architect
  ↓
Task Router / Capability Registry
  ↓
Dynamic Engineering Pod
  ↓
Tools / Simulation / Measurement
  ↓
Evidence
  ↓
Independent Verification
  ↓
Stephen final engineering decision
```

---

# 3. Kairos / 雷小蒙: Data and Transferable Lessons

Kairos is useful to AERIS primarily as a **portable agent harness / personal operating system pattern**, not as a direct acoustic architecture.

Public evidence reviewed includes:

- Kairos / 雷小蒙 started as a personal AI Agent built with Claude Code in 2026.
- The public knowledge ecosystem emphasizes:
  - tool neutrality,
  - context compacting,
  - skills,
  - memory,
  - work logs,
  - human-review publication flow,
  - repo / PR traceability.
- A public work log recorded operational failures including:
  - memory audit silently broken for about **5 days**,
  - overwritten / removed scheduling,
  - multiple bot schedules silently failing.
- A public April work-log snippet states that in the final **48 hours** before travel, **23 sessions** were used to close remaining work.
- A public knowledge-base case reports approximately:
  - **73 reading notes**
  - **352 concept cards**
  - accumulated in under two months.
- A public skills-dashboard case reports:
  - **40 skills**
  - **14 categories**.

## 3.1 The important lesson is not the UI

The strongest transferable pattern is:

```text
Rules
↓
Skills
↓
Memory
↓
Workflow
↓
Tools
↓
Automation
↓
Approval
↓
Evaluation
↓
Observability
```

The most important operational lesson is:

> A background job that “should be running” is not the same as a job that actually ran and produced the expected artifact.

Therefore AERIS must monitor:

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

---

# 4. Real-World Acoustic / Audio Role Evidence

## 4.1 Amazon Ring Acoustic Engineer (Taiwan)

A current Amazon Ring acoustic-engineering listing was used as a reality check. The job scope includes or strongly implies:

- acoustic system design,
- audio platform / circuitry,
- component evaluation,
- acoustic simulation,
- validation / reliability,
- sound-quality tuning,
- new-platform bring-up,
- test matrix and internal manufacturing criteria,
- factory-test troubleshooting,
- sound-quality analysis,
- test libraries,
- algorithm evaluation / integration / validation,
- Audio Precision / SoundCheck / ACQUA,
- MATLAB / Python.

This validates the user's six-domain framework while also showing that an industrial role must cross into:

- manufacturing,
- automation,
- software,
- embedded platform,
- quality,
- system integration.

## 4.2 Apple Acoustic Technologies

Current Apple acoustic roles include examples such as:

- Acoustic Transducer Engineer
- Acoustics DSP Engineer
- Automation Engineer

The transferable lesson is that “acoustics” in top product companies is a multidisciplinary organization, not only enclosure design or frequency-response testing.

## 4.3 Embedded / platform audio responsibilities observed in current industry roles

Typical adjacent requirements include:

- ALSA / PulseAudio,
- Android / QNX audio stacks,
- ARM / DSP,
- Dolby / DTS,
- A/V sync,
- Audio Precision,
- DSP firmware / middleware,
- wake word / audio intelligence,
- on-device privacy / latency / memory / power constraints.

---

# 5. AERIS Final Positioning

> **AERIS = Acoustic Engineering Organization-in-a-Box**

Alternative precise formulation:

> **AERIS = Portable Agent Harness × 100-Seat Acoustic Capability Organization × Engineering Evidence & Verification System**

Long-term target:

> **A 100% locally survivable professional acoustic-engineering AI organization that can use replaceable models, accumulate verified engineering knowledge, control real engineering tools, reproduce results, and remain auditable across years.**

A useful analogy, not a claim of equivalent capability:

> **“Acoustic-engineering version of LILA AI Science Factory + Siemens Engineering Agent + Apple/Amazon Audio Organization + KLIPPEL/AP/HEAD Lab.”**

---

# 6. Five-Dimensional Engineering Matrix

Every engineering task should be addressable across five axes.

## 6.1 Transducer axis
- Speaker
- Microphone

## 6.2 Engineering-discipline axis
1. Acoustic
2. Audio
3. Validation
4. Tuning
5. Simulation
6. Algorithm

## 6.3 Product axis
- Medical hearing aid
- OTC hearing aid
- PSAP / assistive listening
- Auracast assistive system
- TWS earbuds
- ANC over-ear headphone
- gaming / communication headset
- smartphone
- tablet
- laptop
- monitor / all-in-one
- smart speaker
- soundbar
- home theater
- TV / display audio
- doorbell / security camera
- IoT / smart appliance
- AR glasses
- VR / XR headset
- automotive audio / hands-free
- AMR / robot vehicle
- quadruped robot
- humanoid / service robot
- conference / UC device
- directional / array microphone system

## 6.4 Lifecycle axis
```text
Concept
→ Architecture
→ Feasibility
→ Prototype
→ EVT
→ DVT
→ PVT
→ MP
→ EOL
→ Field Return
→ Next Generation
```

## 6.5 Evidence axis
- Requirement
- Theory
- Calculation
- Simulation
- Measurement
- Listening
- Standard
- Factory data
- Reliability data
- Field data

---

# 7. Speaker: Six-Domain Scope

## 7.1 Acoustic
- transducer selection
- Thiele/Small parameters
- nonlinear parameters
- front volume / back volume
- sealed / vented / passive-radiator topology
- port / vent resonance
- leak path
- gasket
- mesh / grille
- waveguide / horn
- cavity modes
- structural radiation
- acoustic impedance
- diffraction
- near-field / far-field
- enclosure interaction

## 7.2 Audio
- DAC
- codec
- Class-D amplifier
- smart amp
- gain structure
- power integrity
- ground
- THD+N
- SNR
- crosstalk
- I2S
- TDM
- clocking
- latency
- embedded audio route

## 7.3 Validation
- frequency response
- phase
- impulse response
- impedance
- T/S
- THD
- IMD
- Rub & Buzz
- compression
- maximum SPL
- directivity
- power handling
- thermal
- reliability
- production margin

## 7.4 Tuning
- target response
- EQ
- crossover
- DRC
- limiter
- bass enhancement
- loudness
- tonal balance
- dynamics
- spatial rendering
- sub integration

## 7.5 Simulation
- lumped-parameter model
- FEM
- BEM
- vibro-acoustic
- thermoviscous acoustics
- porous media
- structural coupling
- room acoustics
- ray acoustics
- DOE / optimization

## 7.6 Algorithm
- EQ
- crossover
- DRC
- excursion protection
- thermal protection
- smart-amp control
- adaptive EQ
- room correction
- spatial audio
- loudness management

---

# 8. Microphone: Six-Domain Scope

## 8.1 Acoustic
- MEMS / ECM capsule
- microphone port
- cavity
- mesh
- waterproof membrane
- array geometry
- leakage
- wind noise
- handling noise
- vibration isolation
- structure-borne paths

## 8.2 Audio
- bias
- preamp
- ADC
- PDM
- I2S / TDM
- clock
- PSRR
- SNR
- EIN
- AOP
- crosstalk
- gain

## 8.3 Validation
- sensitivity
- frequency response
- phase
- unit matching
- self noise
- SNR
- THD
- AOP
- directivity
- far-field behavior
- wind
- handling
- vibration
- scenario testing

## 8.4 Tuning
- gain
- EQ
- matching
- beam width
- voice target
- noise target
- far-field tuning
- array pattern

## 8.5 Simulation
- microphone port model
- thermoviscous model
- array propagation
- BEM
- room
- wind
- structure-borne vibration

## 8.6 Algorithm
- AEC
- beamforming
- DOA
- NR
- AGC
- dereverberation
- VAD
- KWS
- source separation
- ASR front end
- speech enhancement

---

# 9. 100 Virtual Acoustic Engineering Seats

**Important:** These are logical professional capability contracts, not 100 continuously running processes.

## A. Chief Engineering Council — 8 seats

1. Chief Acoustic Architect
2. Speaker Engineering Director
3. Microphone Engineering Director
4. Product Audio System Architect
5. DSP & Algorithm Director
6. Validation & Quality Director
7. NPI & Manufacturing Director
8. Research / Standards / Knowledge Director

## B. Speaker Center of Excellence — 18 seats

9. Speaker Acoustic System Architect
10. Transducer / T-S / Nonlinear Specialist
11. Enclosure / Port / Waveguide Specialist
12. Audio Circuit Architect
13. Amp / Codec / Power Integrity Specialist
14. Embedded Audio Interface Specialist
15. Speaker Measurement Engineer
16. Nonlinear / Power / Reliability Validation Engineer
17. Directivity / Spatial Validation Engineer
18. Tonal Tuning Engineer
19. Dynamics / Bass / Protection Tuning Engineer
20. Psychoacoustic Speaker Tuning Engineer
21. Lumped / FEM Acoustic Simulation Engineer
22. BEM / Vibro-acoustic Simulation Engineer
23. Room / Ray / System Simulation Engineer
24. Speaker DSP Engineer
25. Smart-Amp / Protection Algorithm Engineer
26. Spatial / Room-Correction Algorithm Engineer

## C. Microphone Center of Excellence — 18 seats

27. Microphone Acoustic Architect
28. MEMS / ECM Capsule Specialist
29. Port / Mesh / Wind / Isolation Specialist
30. Microphone Audio Circuit Architect
31. ADC / PDM / Clock / Noise Specialist
32. Embedded Capture Pipeline Engineer
33. Microphone Measurement Engineer
34. Array / Directivity Validation Engineer
35. Far-field / Noise Scenario Validation Engineer
36. Microphone Tonal Tuning Engineer
37. Array Pattern Tuning Engineer
38. Speech Quality Tuning Engineer
39. Mic-Port / Thermoviscous Simulation Engineer
40. Array / Wave Propagation Simulation Engineer
41. Room / Wind / Structure Simulation Engineer
42. AEC / Echo Control Engineer
43. Beamforming / DOA Engineer
44. NR / AGC / Dereverb / Speech Enhancement Engineer

## D. Product Chief Engineers — 24 seats

45. Medical Hearing Aid
46. OTC Hearing Aid / PSAP
47. Assistive Listening / Auracast
48. TWS Earbuds
49. ANC Over-Ear Headphone
50. Gaming / Communication Headset
51. Smartphone
52. Tablet
53. Laptop
54. Monitor / All-in-One
55. Smart Speaker
56. Soundbar
57. Home Theater / Multichannel
58. TV / Display Audio
59. Doorbell / Security Camera
60. IoT / Smart Appliance
61. AR Glasses
62. VR / XR Headset
63. Automotive Audio / Hands-Free
64. AMR / Robot Vehicle
65. Quadruped Robot
66. Humanoid / Service Robot
67. Conference / UC Device
68. Directional / Array Microphone System

## E. Cross-Disciplinary Distinguished Engineers — 20 seats

69. Psychoacoustics
70. Objective Perceptual Metrics / MOS
71. Spatial Audio / Binaural / HRTF
72. Room Acoustics
73. Vibration / NVH
74. Acoustic Materials / Foam / Mesh / Porous Media
75. Thermal / Power / Reliability
76. EMC / EMI / Ground Noise
77. Mechanical Tolerance / Leakage / Assembly
78. DOE / Statistics / Monte Carlo
79. Metrology / Measurement Uncertainty
80. Sensor Fusion / IMU / Head Tracking
81. Bluetooth / LE Audio / Wireless Audio
82. OS Audio Stack / Latency / Sync
83. Codec / Transport / Network Audio
84. Audio Machine Learning
85. Acoustic Data Engineering
86. Competitive Benchmark / Teardown
87. Patent / Prior-Art Intelligence
88. Frontier Acoustic Research Scientist

## F. Engineering Operations / Verification — 12 seats

89. International Standards & Regulation Engineer
90. OEM / Customer Certification Engineer
91. Test Automation Engineer
92. Laboratory Instrument Controller
93. Factory EOL / QC Engineer
94. Failure Analysis / FACA Engineer
95. Supplier Quality / Incoming Quality Engineer
96. Reliability / HALT / Environmental Engineer
97. Requirement / Traceability / Configuration Manager
98. Acoustic Red-Team / DFMEA Reviewer
99. Technical Report / Evidence / Knowledge Curator
100. Autonomous Experiment & Optimization Engineer

## 9.1 Seat count verification

```text
Chief Council                8
Speaker CoE                 18
Microphone CoE              18
Product Chief Engineers     24
Distinguished Engineers     20
Operations / Verification   12
--------------------------------
TOTAL                      100
```

---

# 10. Role #100: Autonomous Experiment & Optimization

This is a likely long-term moat.

Example closed loop:

```text
Requirement agent
→ captures SPL / THD / Xmax / power / thermal / enclosure / battery / target FR
↓
Acoustic design agents
→ propose mechanical / acoustic alternatives
↓
Simulation agents
→ lumped / FEM / BEM / DOE
↓
Optimization
→ Pareto candidates
↓
Prototype / Measurement controller
→ real test
↓
Validation
→ simulation-measurement correlation
↓
Tuning agents
→ EQ / limiter / crossover
↓
Psychoacoustic evaluation
→ objective + perceptual scoring
↓
Red Team
→ heat / distortion / rub-buzz / tolerance / aging / battery
↓
Chief Architect
→ recommendation
↓
Human approval
```

This is an **Acoustic Autonomous R&D Loop**, not chat.

---

# 11. Dynamic Pod Runtime

Do **not** run all 100 seats.

Recommended:

```text
100-seat Role Library
      ↓
Task Router
      ↓
Select relevant capabilities
      ↓
Temporary Engineering Pod
      ↓
Execute
      ↓
Independent Review
      ↓
Pod dissolved
```

Typical concurrency:

- ordinary task: **2–8 roles**
- complex task: **5–15 roles**

Three runtime tiers:

- **Tier A Directors:** ~8
- **Tier B Principal Specialists:** ~20–30 available capabilities
- **Tier C Ephemeral Workers:** spawn for analysis, research, plotting, data parsing, CAE, report generation

Example TWS / ANC pod can include:

- Product Audio System Architect
- MEMS Specialist
- Port / Mesh Specialist
- Array Validation
- Array Tuning
- AEC
- Beamforming
- NR
- ANC Headphone Product Chief
- Psychoacoustics
- Metrology
- Bluetooth
- Standards
- Test Automation
- Red Team

---

# 12. Model Strategy

AERIS must be model-neutral.

## 12.1 Claude Code — current default role
- architecture review
- high-risk design review
- acceptance / verification
- difficult debugging
- refactoring strategy
- security review
- constitution / architecture guard

## 12.2 ChatGPT Codex — current default role
- implementation
- bulk coding
- test creation
- refactoring execution
- documentation generation
- repository maintenance
- repeatable engineering automation

## 12.3 Local LLM — current default role
- permanent offline fallback
- local routing
- low-risk repetitive support
- local retrieval / indexing
- basic dialog and fallback

## 12.4 SSOT principle

```text
AERIS_CORE_RULES.md = source of truth

CLAUDE.md  ─┐
AGENTS.md   ─┼─ thin model adapters
LOCAL.md    ─┘
```

No model-specific file may become the only source of core engineering rules.

---

# 13. Knowledge Architecture

AERIS should not be “just a vector DB.”

## L1. Fundamental Knowledge
- acoustics
- electroacoustics
- DSP
- psychoacoustics
- vibration
- statistics
- measurement science

## L2. Standards
- IEC
- ISO
- AES
- CTA
- ITU-T
- Bluetooth
- FDA / eCFR
- customer specifications

## L3. Product Knowledge
- architecture patterns
- component behavior
- topology tradeoffs
- product constraints

## L4. Internal Engineering
- design reviews
- measurement results
- simulations
- FA / FACA
- DOE
- supplier data
- tuning history
- manufacturing data

## L5. Raw Data
- WAV
- FRD
- MAT
- CSV
- UFF
- HDF5
- APx project/output
- SoundCheck sequences/results
- Klippel data
- CAE files

## L6. Engineering Knowledge Graph

Canonical relation:

```text
Problem
→ Cause
→ Evidence
→ Fix
→ Result
```

Example:

```text
800 Hz dip
→ gasket leakage
→ pressure scan + teardown
→ gasket +0.15 mm
→ +4.2 dB
→ DVT verified
```

---

# 14. Memory vs Knowledge vs Evidence vs Audit vs Provenance

| Asset | Definition | AI may rewrite? |
|---|---|---|
| Memory | recent context / preference / operational experience | may summarize |
| Knowledge | reviewed and reusable engineering knowledge | controlled |
| Evidence | raw data and outputs from real engineering activity | generally immutable |
| Audit | who did what and when | append-only |
| Provenance | lineage from input/method/tool/activity to result | must remain traceable |

Knowledge-promotion flow:

```text
Raw Observation
↓
Finding
↓
Verified Finding
↓
Lesson Candidate
↓
Engineering Review
↓
Canonical Knowledge
```

Forbidden:

```text
LLM inference
↓
directly overwrite permanent knowledge
```

---

# 15. Evidence-Weighted Engineering

Agent voting is not truth.

Recommended trust hierarchy:

| Evidence type | Relative trust |
|---|---|
| single LLM inference | low |
| textbook / paper | medium |
| current applicable standard | high |
| CAE simulation | medium–high, condition-dependent |
| calibrated measurement | very high |
| repeated calibrated measurement | very high |
| MP production statistics | extremely high for production behavior |
| field-return data | extremely high for real-world failure evidence |

Recommended engineering answer schema:

```text
Finding:
Confidence:
Evidence:
Counter-hypothesis:
Missing Evidence:
Recommended Test:
Decision impact:
```

---

# 16. Engineering Project Flow

```text
Customer / User
→ Chief Acoustic Architect
→ Requirement decomposition
→ Standards + historical cases + benchmark + constraints
→ Hypothesis generation
→ Speaker / Mic / Audio / Algorithm / Simulation specialists
→ Calculation / Simulation
→ Design Review Gate
→ Measurement Plan
→ Physical Measurement
→ Simulation ↔ Measurement correlation
→ Tuning / Optimization
→ Validation
→ Reliability / Factory
→ Red Team
→ Final Engineering Decision
→ Technical Report
→ Knowledge Graph Update
```

---

# 17. Skill Standard

A Skill is not merely a prompt.

Recommended package:

```text
skills/
└── acoustic/
    └── leakage-diagnosis/
        ├── SKILL.md
        ├── manifest.yaml
        ├── references/
        ├── scripts/
        ├── tests/
        ├── evals/
        └── golden/
```

Each skill should define:

- purpose
- inputs
- outputs
- prerequisites
- allowed tools
- forbidden actions
- assumptions
- units
- required evidence
- acceptance criteria
- failure modes
- tests
- golden cases
- version
- owner
- reviewer

---

# 18. Workflow vs Agent Rule

Use deterministic systems for deterministic work.

```text
fixed / repeatable / predictable
→ script / cron / state machine / workflow engine

uncertain reasoning / diagnosis / synthesis
→ LLM / agent
```

Example:

Bad:

```text
Ask the LLM every day whether a backup should run.
```

Better:

```text
Scheduler runs backup deterministically.
Agent only investigates failures or anomalies.
```

---

# 19. DONE Definition

AERIS must reject:

```text
Agent says “done”
= DONE
```

Formal completion:

```text
Claim
↓
Task ID exists
↓
Tool reports completion
↓
Artifact physically exists
↓
Hash valid
↓
DUT / Fixture / Configuration match
↓
Calibration valid
↓
Required metrics exist
↓
Acceptance test executed
↓
Evidence Bundle complete
↓
Independent Verification PASS
↓
Human Approval if required
↓
DONE
```

---

# 20. Independent Verification Boundary

Creator and reviewer must be separated.

```text
Implementation Agent / Codex
       ↓
artifact + tests + evidence
       ↓
================================
INDEPENDENT VERIFICATION BOUNDARY
================================
       ↓
Reviewer / Claude Code
       ↓
Acceptance Criteria
Reference Data
Golden Samples
Unit consistency
Numerical tolerance
Regression tests
Evidence completeness
       ↓
PASS / FAIL
       ↓
FAIL → implementation fixes
PASS → human approval when required
```

A reviewer must not simply say “looks reasonable.”

---

# 21. Engineering Reproducibility

Every important result should be rerunnable.

```text
Requirement
↓
Input
↓
Raw Data
↓
Method
↓
Tool + Version
↓
Parameters
↓
Calculation / Simulation
↓
Result
↓
Evidence Package
↓
Independent Reviewer
↓
Acceptance Criteria
↓
PASS / FAIL
↓
Human Approval
```

Recommended result manifest:

```yaml
task_id:
project_id:
input_hash:
tool:
tool_version:
script_commit:
parameters:
units:
dut:
fixture:
calibration_id:
raw_data:
output_files:
result_hash:
reviewer:
review_status:
timestamp:
```

---

# 22. Risk / Approval Levels

## R0
Read-only / query / summary / sandbox calculation  
→ automatic allowed.

## R1
Reversible low-risk local modification  
→ automatic with full log.

## R2
Important repository / project / measurement modification  
→ reviewer gate required.

## R3
External impact / publish / email / delete / hardware control / official test conclusion  
→ human approval mandatory.

> Capability does not imply authority.

---

# 23. Long-Running Job State Machine

Required states:

```text
QUEUED
RUNNING
WAITING
SUCCEEDED
FAILED
CANCELLED
TIMED_OUT
```

Required metadata:

- task_id
- owner
- started_at
- last_heartbeat
- timeout
- retry_count
- cancellation support
- expected artifacts
- output location
- error code
- evidence link

This applies to:

- COMSOL
- MATLAB batch
- APx / SoundCheck automation
- measurement runs
- data indexing
- report generation
- long research tasks

---

# 24. Observability / Health Model

A process being alive is insufficient.

Minimum health indicators:

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

Operational controls:

- retry
- timeout
- rate limit
- circuit breaker
- kill switch
- rollback
- alert
- audit trail

Recommended telemetry principle:

> Maintain a stable internal AERIS telemetry schema, then map it outward to OpenTelemetry rather than binding long-term storage directly to changing GenAI semantic conventions.

---

# 25. Golden Acoustic Cases

Start with real failure history rather than synthetic volume.

Recommended first 20:

1. Leakage misdiagnosis
2. Gasket issue
3. Port resonance
4. Driver breakup
5. Thermal compression
6. Excursion over-limit
7. Rub & Buzz
8. Mic port resonance
9. Wind noise
10. Handling noise
11. Ground noise
12. PDM clock issue
13. AEC convergence failure
14. Beamforming steering error
15. Simulation / Measurement mismatch
16. Wrong standard revision
17. Wrong fixture
18. Wrong calibration
19. Wrong unit
20. Wrong SPL reference

Each case requires:

```text
Input
Expected reasoning checkpoints
Expected result
Forbidden result
Tolerance
Required evidence
Reviewer rubric
```

An early target of **20–50 real cases** is more valuable than creating hundreds of weak synthetic tests.

---

# 26. Acoustic / Audio Tool Bus

These tools should be execution adapters, not merely documents in RAG.

## 26.1 COMSOL Acoustics Module
Use cases:
- speakers
- mobile devices
- microphones
- mufflers
- sensors
- rooms
- structural coupling
- piezo
- flow
- thermoviscous
- porous media

## 26.2 Siemens Simcenter
Use cases:
- vibroacoustics
- aeroacoustics
- ray acoustics
- system acoustic simulation

## 26.3 KLIPPEL R&D System
Use cases:
- T/S
- nonlinear parameters
- distortion
- power / life
- simulation
- auralization
- scanning vibrometry
- micro-speaker through subwoofer

## 26.4 KLIPPEL QC
Use cases:
- fast production testing
- linear / nonlinear measures
- linked test sequences
- end-of-line quality

## 26.5 Audio Precision APx
Use cases:
- electro-acoustic validation
- production test
- automated sequences
- golden unit
- limits
- calibration
- logging
- speakers
- microphones
- headphones
- hearing aids

## 26.6 Listen SoundCheck
Use cases:
- modular R&D electroacoustic measurement
- production test
- wireless / voice devices
- high-channel-count systems

## 26.7 HEAD acoustics ACQUA
Use cases:
- voice / audio quality testing
- automated electroacoustic chain
- communication standards
- headsets
- ANC
- smart speakers

## 26.8 HEAD perceptual metrics
Examples:
- HQS
- MDAQS
- Timbre
- Immersiveness
- Distortion

## 26.9 GRAS
Use cases:
- IEC 60318 ear simulators
- headphones
- hearing aids
- realistic ear-load measurement

---

# 27. Standards Intelligence — Verified 2026-08-31 Baseline

**Important:** This section stores metadata and scope summaries only. It does not reproduce copyrighted standard text.

| Standard / regulation | 2026-08-31 status / date signal | AERIS relevance |
|---|---|---|
| IEC 60268-4:2018 | Valid in reviewed IEC metadata; stability date shown as 2027 | Microphone measurement |
| IEC 60268-5:2003 | **Withdrawn 2026-04-17** | Legacy loudspeaker reference; excellent stale-standard Golden Test |
| IEC 60268-21:2018 | Current measurement framework reviewed; stability metadata showed 2026 | Acoustic output measurements |
| IEC 60268-22:2020 | Current publication found | Electrical/mechanical transducer measurements |
| IEC 60268-23:2023 | Current; stability metadata showed 2030 | TV / monitor loudspeaker systems |
| IEC 60268-24:2023 | Current | ANC headphone/earphone characteristics and measurement |
| IEC 60268-7:2025 | Published **2025-06-27**; replaces older 2010 + AMD1:2020 lineage | Headphones / earphones / headsets |
| ANSI/CTA-2034-B | Published July 2024 | In-home loudspeaker FR / directivity / max-output measurement |
| AES75-2023 | Current public AES standard page | Maximum linear sound level using Music-Noise |
| ITU-T P.1100 (10/2025) | Approved **2025-10-29**, in force | Narrowband automotive hands-free |
| ITU-T P.1110 (10/2025) | Approved **2025-10-29**, in force | Wideband automotive hands-free |
| ITU-T P.1120 (10/2025) | Approved **2025-10-29**, in force | Super-wideband / fullband automotive hands-free |
| 21 CFR 800.30 | eCFR reviewed current through late Aug 2026; OTC hearing-aid latency limit remains **≤15 ms** | OTC hearing-aid controls |
| FDA QMSR | Effective **2026-02-02** | Medical-device quality system; important for hearing-aid product mode |
| ISO/IEC 17025:2017 | Current lab competence baseline | Calibration / measurement competence architecture |
| ISO/IEC 42001:2023 | Current AI management-system baseline | AI governance / risk / continual improvement |
| EU AI Act | broader enforcement/application stage active from **2026-08-02**; classification depends on use case | AI governance / deployment risk |
| Bluetooth LE Audio | Complete spec suite available; LC3, isochronous transport, multi-stream, hearing-aid support, Auracast | TWS / assistive / hearing / wireless audio |

## 27.1 Standards Registry schema

```yaml
standard_id:
title:
edition:
publication_date:
status:
supersedes:
superseded_by:
withdrawn_date:
stability_date:
product_scope:
source_url:
last_checked_at:
```

## 27.2 Standards lifecycle requirement

AERIS must never assume:

```text
PDF exists in RAG
= standard is current
```

Instead:

```text
retrieved standard
↓
check lifecycle metadata
↓
check edition / amendment / withdrawal
↓
record current status
↓
use applicable version
```

---

# 28. Hearing-Aid / Medical “Regulated Product Mode”

Because FDA QMSR became effective on **2026-02-02**, medical / OTC hearing-aid work should use a stricter mode than ordinary consumer-audio projects.

Recommended additions:

- controlled requirements
- design-history traceability
- risk-control linkage
- verification / validation separation
- controlled tool versions
- calibration trace
- change-control
- signed evidence
- review / approval segregation
- regulation applicability check
- retained audit trail

AERIS should not claim regulatory compliance merely because it implements these patterns; this is an architecture baseline.

---

# 29. Bluetooth / Wireless Audio Scope

AERIS wireless-audio capability should cover:

- Classic Bluetooth audio where relevant
- LE Audio
- LC3
- isochronous channels
- multi-stream
- hearing-aid support
- Auracast
- latency
- synchronization
- codec transport
- RF coexistence effects on audio behavior
- power / battery tradeoffs

---

# 30. Acoustic Engineering Constitution

1. Do not present inference as measured fact.
2. All numeric values require unit, condition, and source.
3. Simulation requires boundary conditions.
4. Measurement requires calibration state.
5. Standards must check revision and lifecycle status.
6. Do not hide poor simulation-measurement correlation with tuning.
7. Algorithm improvement must also check latency, MIPS, memory, and power.
8. Speaker tuning must check excursion, temperature, and distortion.
9. Microphone algorithms must be evaluated across noise, distance, azimuth, speaker, and language conditions.
10. Do not only store pass/fail; track margin.
11. Major design decisions preserve evidence and provenance.
12. AI cannot self-declare engineering completion; a Verification Gate is required.

---

# 31. Maturity Model

| Level | Name | Meaning |
|---|---|---|
| 1 | Ask | Explain what something is |
| 2 | Analyze | Diagnose where the problem is |
| 3 | Engineer | Recommend how to modify |
| 4 | Execute | Actually run script/simulation/measurement plan |
| 5 | Verify | Correlate evidence and narrow hypotheses |
| 6 | Discover | Propose designs, run DOE/experiments, recommend Pareto-optimal option |

Target:

> **AI Principal Acoustic Engineer Team**

---

# 32. Repository Architecture Proposal

```text
AERIS/
├── AERIS_CONSTITUTION.md
├── AERIS_CORE_RULES.md
├── CLAUDE.md
├── AGENTS.md
│
├── governance/
│   ├── risk_policy.yaml
│   ├── approval_policy.yaml
│   ├── tool_permissions.yaml
│   └── review_conflicts.yaml
│
├── capabilities/
│   ├── registry.yaml
│   ├── speaker/
│   ├── microphone/
│   ├── simulation/
│   ├── measurement/
│   ├── factory/
│   ├── quality/
│   ├── standards/
│   └── reporting/
│
├── skills/
├── workflows/
├── evals/
│   ├── capability/
│   ├── regression/
│   └── golden/
│
├── knowledge/
├── memory/
│   ├── project/
│   ├── session/
│   └── lessons/
│
├── evidence/
│   └── <project>/<task_id>/
│
├── provenance/
├── audit/
├── standards/
│   ├── registry/
│   ├── lifecycle/
│   └── source_metadata/
│
├── tools/
├── adapters/
│   ├── claude/
│   ├── codex/
│   └── local/
│
├── runtime/
│   ├── orchestrator/
│   ├── scheduler/
│   ├── state_machine/
│   └── health/
│
├── telemetry/
└── dashboard/
```

---

# 33. Machine-Readable Role Contract

Example:

```yaml
role_id: SPK_ACOUSTIC_ARCHITECT

domains:
  - speaker
  - acoustic

skills:
  - enclosure_analysis
  - leakage_diagnosis
  - port_design

allowed_tools:
  - python_readonly
  - comsol_read
  - measurement_db_read

risk_ceiling: R1

required_evidence:
  - input_provenance
  - calculation_manifest
  - units
  - conditions

review_conflicts:
  - cannot_self_approve
```

The purpose of the 100-seat architecture is:

> **Capability + Authority + Evidence + Review Boundary**

not persona decoration.

---

# 34. Core Control Plane

```text
Intent / Task Classifier
↓
Requirement Parser
↓
Role Router
↓
Project Pod Builder
↓
Workflow Engine / DAG
↓
Tool Execution
↓
Evidence Store
↓
Reviewer / Verifier
↓
Confidence Engine
↓
Human Gate
↓
Report
↓
Knowledge Promotion
```

Canonical project object:

```text
Project
→ Requirements
→ Hypotheses
→ Tasks
→ Artifacts
→ Evidence
→ Decisions
→ Verification
→ Lessons
```

---

# 35. Architecture Simplicity Rule

Do not add infrastructure because it sounds advanced.

Claude Code should challenge:

- Do we really need a Graph DB?
- Is SQLite / DuckDB enough?
- Do we need an Event Bus?
- Is an explicit state machine enough?
- Do we need 100 role files?
- Is one capability registry better?
- Do we need microservices?
- Is a local modular monolith safer?
- Do we need a vector DB?
- Are FTS / simple retrieval sufficient initially?
- Do we need a complex model router now?
- Is instrument integration mature enough for Autonomous Lab?

Default bias:

> **Local Modular Monolith + Explicit State Machine + Files / SQLite / DuckDB**

until evidence justifies heavier infrastructure.

---

# 36. P0–P3 Implementation Roadmap

## P0 — Build the part that prevents AERIS from becoming unreliable

1. Repository inventory
2. Current architecture map
3. Constitution / Core Rules SSOT
4. Memory / Knowledge / Evidence separation
5. Capability Registry schema
6. Skill standard
7. Evidence Bundle standard
8. Task state machine
9. Acceptance Gate
10. First 20–50 Golden / failure cases
11. Audit log
12. Basic health monitoring

### P0 exit criteria

- 100% important tasks have task_id
- important gated outputs have evidence
- creator/reviewer separation works
- DONE can be machine-verified
- changing model does not destroy core rules

## P1 — Models and engineering tools

1. Claude / Codex / Local thin adapters
2. Tool permission model
3. Python / MATLAB / Git adapters
4. Measurement data interface
5. Tool-version capture
6. Calibration metadata
7. Standards Registry
8. OpenTelemetry-compatible telemetry
9. Job cancellation / retry / timeout
10. Security baseline

## P2 — Dynamic engineering organization

1. 100-seat Capability Registry
2. Dynamic Pod assembly
3. Task routing
4. Specialist Skill loading
5. Cross-role evidence contracts
6. Independent reviewer allocation
7. Regression eval automation
8. Knowledge-promotion workflow

## P3 — Mature control plane

1. Dashboard
2. Remote interfaces
3. More automation
4. More instruments
5. Hardware / lab control
6. Regulated Product Mode
7. Advanced multi-agent optimization

---

# 37. Things Not to Build First

Do not prioritize:

- pretty dashboard
- 100 permanent agents
- microservices
- event bus
- graph database
- complex vector infrastructure
- complex model router
- autonomous-lab control
- large persona prompt library

before:

- task identity
- state
- evidence
- tests
- verification
- reproducibility
- health monitoring

---

# 38. Claude Code Review Contract

Claude Code first phase should **not modify code**.

Required outputs:

```text
Current Repository Inventory
↓
Current Architecture Diagram
↓
Kairos Pattern Mapping
↓
100-Seat Capability Mapping
↓
Gap Matrix
↓
Conflict / Duplication Matrix
↓
Security Review
↓
Evidence / Verification Review
↓
Memory / Knowledge / Evidence Separation Review
↓
Standards / Regulatory Data Review
↓
Runtime / Multi-Agent Review
↓
P0 / P1 / P2 Plan
↓
Things NOT to build
↓
Human approval
```

Claude Code must be instructed to **challenge this RFC**, not merely implement it.

---

# 39. Codex Implementation Contract

After architecture approval, Codex can implement.

Every implementation delivery must include:

```text
Code
Tests
Evidence
Changed files
Risk
Rollback
Acceptance result
```

Never only:

```text
Done
```

---

# 40. Quantitative P0 Acceptance Metrics

| Metric | P0 target |
|---|---:|
| Critical tasks with task_id | 100% |
| Important gated outputs with Evidence Bundle | 100% |
| High-risk tasks with independent review | 100% |
| Human-required actions bypassed | 0 |
| Silent failed scheduled jobs | 0 |
| Golden regression pass rate | ≥95% |
| Reproducible engineering outputs | ≥90% first phase |
| Gated results missing tool/version/parameters | 0 |
| Model-specific duplicated core rules | 0 |

---

# 41. Source Registry

## 41.1 Kairos / 雷小蒙
- https://wiki.lifehacker.tw/projects/Kairos雷小蒙AI分身
- https://os.lifehacker.tw/
- https://os.lifehacker.tw/posts/2026-03-20-ai-work-log-03
- https://os.lifehacker.tw/posts/2026-04-21-ai-work-log-07
- https://os.lifehacker.tw/posts/2026-05-09-ai-work-log-08
- https://os.lifehacker.tw/posts/2026-08-07-ai-work-log-12
- https://wiki.lifehacker.tw/knowledge-cards/工具中立與Context-Compact
- https://works.lifehacker.tw/works/kw-knowledge-base.html
- https://works.lifehacker.tw/works/skills-dashboard.html
- https://works.lifehacker.tw/submit.html

## 41.2 Agent engineering / evaluations
- https://www.anthropic.com/engineering/building-effective-agents
- https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- https://www.anthropic.com/engineering/building-c-compiler
- https://www.anthropic.com/engineering/harness-design-long-running-apps
- https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- https://www.anthropic.com/engineering/how-we-contain-claude
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- https://openai.com/index/unrolling-the-codex-agent-loop/

## 41.3 AI-native organizations / scientific agents
- https://www.coinbase.com/blog/building-a-leaner-and-faster-coinbase
- https://www.futurehouse.org/ai-scientist
- https://www.futurehouse.org/research/demonstrating-end-to-end-scientific-discovery-with-robin-a-multi-agent-system
- https://www.lila.ai/
- https://www.lila.ai/tech
- https://www.harvey.ai/blog/introducing-agent-builder
- https://www.anthropic.com/research/project-vend-1
- https://andonlabs.com/

## 41.4 Provenance / interoperability / observability
- https://www.w3.org/TR/prov-dm/
- https://json-schema.org/draft/2020-12
- https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization
- https://modelcontextprotocol.io/specification/2025-11-25/basic/utilities/tasks
- https://blog.modelcontextprotocol.io/posts/2026-07-28/
- https://opentelemetry.io/docs/specs/semconv/
- https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/
- https://opentelemetry.io/blog/2026/genai-observability/

## 41.5 Acoustic / audio tools
- https://www.comsol.com/acoustics-module
- https://www.klippel.de/products/rd-system.html
- https://www.audioprecision.com/applications/production-test
- https://www.head-acoustics.com/products/analysis-software/acqua

## 41.6 Standards / regulations
- https://webstore.iec.ch/en/publication/32039
- https://webstore.iec.ch/en/publication/1223
- https://webstore.iec.ch/en/publication/28687
- https://webstore.iec.ch/en/publication/60560
- https://webstore.iec.ch/en/publication/66651
- https://webstore.iec.ch/en/publication/67683
- https://webstore.iec.ch/en/publication/86573
- https://www.cta.tech/standards/ansicta-2034-b/
- https://aes.org/standards/aes75/
- https://www.itu.int/rec/T-REC-P.1100/en
- https://www.itu.int/rec/T-REC-P.1110/en
- https://www.itu.int/rec/T-REC-P.1120/en
- https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-800/subpart-B/section-800.30
- https://www.fda.gov/medical-devices/postmarket-requirements-devices/quality-management-system-regulation-qmsr
- https://www.iso.org/standard/66912.html
- https://www.iso.org/standard/42001
- https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- https://www.bluetooth.com/learn-about-bluetooth/feature-enhancements/le-audio/

---

# 42. Final Architecture Decision

AERIS should be built as:

> **One human-directed, 100-seat virtual acoustic engineering organization with local-first survivability, replaceable models, real tool execution, evidence-backed engineering truth, independent verification, standards lifecycle intelligence, and reproducible physical measurement loops.**

The durable asset is not the current model generation.

The durable assets are:

- Constitution
- Core Rules
- Capability Registry
- Skills
- Engineering Knowledge
- Standards metadata
- Measurements
- Project Memory
- Workflows
- Evals
- Golden Tests
- Evidence
- Provenance
- Audit Logs
- Acceptance Gates
- Tool Integrations
- Engineering Decisions

The implementation order is:

```text
STEP 1  Claude Code: inventory only, no modification
STEP 2  Gap / Conflict / Risk / Keep / Change / Delete
STEP 3  Human approves target architecture
STEP 4  Codex implements P0
STEP 5  Claude Code independently verifies
STEP 6  Build Golden Regression
STEP 7  Move to P1 / P2
STEP 8  Dashboard later
```

The final north-star sentence:

> **AERIS is not an AI-agent demo. It is an Acoustic Engineering Organization OS whose engineering conclusions remain traceable, verifiable and reproducible even after today’s models are replaced.**
