# AERIS Research Data Index — 2026-08-31

**Companion to:** `AERIS_MASTER_RESEARCH_ARCHITECTURE_BASELINE_20260831.md`

This file is the structured research-data appendix. It separates externally observed facts from AERIS architecture decisions and future hypotheses.

---

# 1. Evidence Classes

| Class | Meaning |
|---|---|
| SOURCE-FACT | Directly supported by reviewed public source metadata/content |
| SYNTHESIS | Cross-source architectural conclusion |
| AERIS-DECISION | Proposed design decision for AERIS |
| TARGET | Future desired capability, not current implementation claim |
| VERIFY-LATER | Should be rechecked before regulatory/product release use |

---

# 2. Kairos / 雷小蒙 Dataset

| Item | Value / observation | Class |
|---|---|---|
| Kairos public positioning | Personal AI Agent / digital clone built around Claude Code and a knowledge/work system | SOURCE-FACT |
| Public era | 2026 | SOURCE-FACT |
| Operational memory-audit failure | Silent failure for about 5 days reported in public work log | SOURCE-FACT |
| Scheduling failure | Ghost/overwritten scheduling and multiple bot schedules silently failing were publicly described | SOURCE-FACT |
| Pre-travel work burst | 23 sessions in the final 48 hours before travel in an April work-log snippet | SOURCE-FACT |
| KW knowledge-base example | 73 reading notes, 352 concept cards in under two months | SOURCE-FACT |
| Skills dashboard example | 40 skills, 14 categories | SOURCE-FACT |
| Transferable principle | Tool neutrality + context compact + skills + memory + workflow + traceability | SYNTHESIS |
| AERIS adaptation | Add evidence, verification, calibration, standard lifecycle, reproducibility | AERIS-DECISION |

Primary URLs:
- https://os.lifehacker.tw/
- https://os.lifehacker.tw/posts/2026-03-20-ai-work-log-03
- https://os.lifehacker.tw/posts/2026-04-21-ai-work-log-07
- https://os.lifehacker.tw/posts/2026-05-09-ai-work-log-08
- https://os.lifehacker.tw/posts/2026-08-07-ai-work-log-12
- https://wiki.lifehacker.tw/knowledge-cards/工具中立與Context-Compact
- https://works.lifehacker.tw/works/kw-knowledge-base.html
- https://works.lifehacker.tw/works/skills-dashboard.html

---

# 3. AI-Native Organization / Agent Dataset

| Organization / system | Quantitative observation | AERIS significance | Class |
|---|---:|---|---|
| Coinbase | “one person teams” / fleets-of-agents operating model in 2026-05-05 memo | Human accountability above agent fleet | SOURCE-FACT + SYNTHESIS |
| Cisco MyAgent | rollout reported across workforce of roughly 90,000 | policy server + routing + personalized agents | SOURCE-FACT + SYNTHESIS |
| FutureHouse AI Scientist | human → AI scientist → science assistants → tools | hierarchical scientific workflow | SOURCE-FACT |
| FutureHouse Robin | end-to-end multi-agent scientific discovery loop | hypothesis → experiment → analysis → follow-up | SOURCE-FACT |
| LILA Sciences | reasoning model + autonomous lab/instruments + verifiers | brain/body/verifier pattern | SOURCE-FACT + SYNTHESIS |
| Autonomous materials labs | multi-agent management of research campaigns, 2026 publication | campaign orchestration | SOURCE-FACT |
| Siemens Eigen Engineering Agent | >100 customers, 19 countries in 2026 pilot reporting | real engineering integration + customer standards | SOURCE-FACT |
| Harvey | 400K+ agentic queries/day | professional workflow scale | SOURCE-FACT |
| Harvey | 20M+ terms extracted | domain data-processing scale | SOURCE-FACT |
| Harvey | 445K+ deep-analysis reports | repeatable professional-analysis workflow | SOURCE-FACT |
| Harvey | 25,000+ custom workflows | workflow library architecture | SOURCE-FACT |
| Intercom Fin | ~76% average resolution rate, 7,000+ teams cited | outcome KPI beats activity KPI | SOURCE-FACT + SYNTHESIS |
| Anthropic C compiler experiment | 16 parallel Claude agents | parallelism alone is not architecture | SOURCE-FACT |
| Anthropic C compiler experiment | nearly 2,000 Claude Code sessions | long-horizon harness requirement | SOURCE-FACT |
| Anthropic C compiler experiment | ~US$20,000 API cost | agent scale has material cost | SOURCE-FACT |
| Anthropic C compiler experiment | ~100,000 Rust LOC compiler result | large artifact possible with harness/tests | SOURCE-FACT |
| Project Vend / Vending-Bench | long-horizon errors, state/economic failures | state machine, monitoring, kill switch | SOURCE-FACT + SYNTHESIS |

Important architectural synthesis:

> Agent count is not a maturity metric. Reliable state, tests, evidence, task partition, observability and verification are stronger maturity indicators.

---

# 4. Acoustic Job-Market Dataset

## 4.1 Amazon Ring Acoustic Engineer — Taiwan

Observed scope includes:
- acoustic system design
- audio platform / circuitry
- component evaluation
- acoustic simulation
- validation / reliability
- sound-quality tuning
- platform bring-up
- manufacturing criteria / test matrix
- factory-test troubleshooting
- sound-quality analysis
- test libraries
- algorithm evaluation / integration / validation
- AP / SoundCheck / ACQUA
- MATLAB / Python

AERIS mapping:
- validates six-domain model: Acoustic / Audio / Validation / Tuning / Simulation / Algorithm
- requires additional cross-cutting NPI / manufacturing / software / automation / quality capability

Source:
- https://amazon.jobs/en/jobs/10447431/acoustic-engineer-ring-hardware

## 4.2 Apple Acoustic Technologies

Observed current role families include:
- Acoustic Transducer Engineer
- Acoustics DSP Engineer
- Automation Engineer

AERIS mapping:
- transducer, DSP and automation should be explicit capabilities rather than one broad “acoustic engineer” persona.

---

# 5. Engineering Tool Dataset

| Tool / family | Observed scope relevant to AERIS |
|---|---|
| COMSOL Acoustics Module | speakers, microphones, rooms, structural acoustics, thermoviscous, porous media, multiphysics |
| Siemens Simcenter | vibroacoustics, aeroacoustics, ray acoustics, system simulation |
| KLIPPEL R&D | T/S, nonlinear parameters, distortion, power/life, simulation, auralization, scanning vibrometry |
| KLIPPEL QC | fast production / end-of-line testing |
| Audio Precision APx | R&D and production electroacoustic test, automated sequences, limits, calibration, logging |
| Listen SoundCheck | modular R&D / production electroacoustic measurement, wireless / voice devices |
| HEAD acoustics ACQUA | voice/audio-quality and communication-device testing |
| HEAD HQS / MDAQS | perceptual / objective quality metrics, including Timbre / Immersiveness / Distortion dimensions |
| GRAS | ear simulators / headphone / hearing-aid measurement loads |

AERIS architecture decision:

> These should become Tool Bus execution adapters where practical, not merely documents embedded into retrieval.

---

# 6. Standards / Regulatory Dataset

## 6.1 IEC / AES / CTA

| Standard | Key reviewed metadata | Class |
|---|---|---|
| IEC 60268-4:2018 | microphone measurement; reviewed as valid; stability metadata showed 2027 | SOURCE-FACT |
| IEC 60268-5:2003 | **withdrawn 2026-04-17** | SOURCE-FACT |
| IEC 60268-21:2018 | acoustic output measurement framework; stability metadata showed 2026 | SOURCE-FACT |
| IEC 60268-22:2020 | electrical/mechanical measurement on transducers | SOURCE-FACT |
| IEC 60268-23:2023 | TVs and monitors — loudspeaker systems; stability metadata showed 2030 | SOURCE-FACT |
| IEC 60268-24:2023 | ANC headphones / earphones characteristics | SOURCE-FACT |
| IEC 60268-7:2025 | published 2025-06-27; newer headphone/earphone edition | SOURCE-FACT |
| ANSI/CTA-2034-B | published July 2024; in-home loudspeaker measurement | SOURCE-FACT |
| AES75-2023 | maximum linear sound level using Music-Noise | SOURCE-FACT |

## 6.2 Automotive communication

| Recommendation | Approval/status signal | Scope |
|---|---|---|
| ITU-T P.1100 (10/2025) | approved 2025-10-29; in force | narrowband motor-vehicle hands-free |
| ITU-T P.1110 (10/2025) | approved 2025-10-29; in force | wideband motor-vehicle hands-free |
| ITU-T P.1120 (10/2025) | approved 2025-10-29; in force | super-wideband/fullband motor-vehicle hands-free |

## 6.3 Hearing aid / medical

| Regulation / standard | Key reviewed signal |
|---|---|
| 21 CFR 800.30 | OTC hearing-aid latency requirement remains ≤15 ms in reviewed current eCFR |
| FDA QMSR | effective 2026-02-02 |
| ISO/IEC 17025:2017 | laboratory competence / valid-results framework |
| ISO/IEC 42001:2023 | AI management-system framework |

## 6.4 EU AI governance

Reviewed 2026 information indicates:
- broader AI Act enforcement/application phase from 2026-08-02;
- actual high-risk classification depends on deployment/use case;
- documentation, logging, human oversight and traceability are low-regret architecture choices.

## 6.5 Bluetooth LE Audio

Key public feature set:
- LC3
- isochronous transport
- multi-stream audio
- hearing-aid support
- Auracast broadcast audio

AERIS implication:
- explicit Bluetooth / LE Audio / latency / sync / transport capability is required.

---

# 7. 100-Seat Count Dataset

| Organization block | Seats |
|---|---:|
| Chief Engineering Council | 8 |
| Speaker Center of Excellence | 18 |
| Microphone Center of Excellence | 18 |
| Product Chief Engineers | 24 |
| Cross-Disciplinary Distinguished Engineers | 20 |
| Engineering Operations / Verification | 12 |
| **TOTAL** | **100** |

Runtime decision:
- typical pod: 2–8 roles
- complex pod: 5–15 roles
- do not instantiate all 100 continuously.

---

# 8. Product Coverage Dataset

Minimum product families currently defined:

1. Medical Hearing Aid
2. OTC Hearing Aid / PSAP
3. Assistive Listening / Auracast
4. TWS Earbuds
5. ANC Over-Ear Headphone
6. Gaming / Communication Headset
7. Smartphone
8. Tablet
9. Laptop
10. Monitor / All-in-One
11. Smart Speaker
12. Soundbar
13. Home Theater / Multichannel
14. TV / Display Audio
15. Doorbell / Security Camera
16. IoT / Smart Appliance
17. AR Glasses
18. VR / XR Headset
19. Automotive Audio / Hands-Free
20. AMR / Robot Vehicle
21. Quadruped Robot
22. Humanoid / Service Robot
23. Conference / UC Device
24. Directional / Array Microphone System

---

# 9. Six-Domain Dataset

For both Speaker and Microphone, AERIS uses six primary engineering disciplines:

1. Acoustic
2. Audio
3. Validation
4. Tuning
5. Simulation
6. Algorithm

This creates a base 2 × 6 engineering matrix before product and lifecycle dimensions are applied.

---

# 10. Lifecycle Dataset

```text
Concept
Architecture
Feasibility
Prototype
EVT
DVT
PVT
MP
EOL
Field Return
Next Generation
```

---

# 11. Evidence Dataset

Evidence categories:
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

Trust policy is not a pure numeric score; it is context-dependent. General ordering proposed:

```text
single LLM inference
< reviewed literature
< applicable current standards
< well-defined simulation
< calibrated measurement
< repeated calibrated measurement
< large production / field evidence for production behavior
```

---

# 12. Golden-Test Dataset

Initial 20 real-failure-oriented cases:

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

Initial desired corpus size:
- **20–50 real cases** before pursuing large synthetic benchmark volume.

---

# 13. Verification / Acceptance Dataset

Formal DONE chain:

```text
Claim
→ Task ID exists
→ Tool reports completion
→ Artifact physically exists
→ Hash valid
→ DUT / Fixture / Configuration match
→ Calibration valid
→ Required metrics exist
→ Acceptance test executed
→ Evidence Bundle complete
→ Independent Verification PASS
→ Human Approval if required
→ DONE
```

Risk levels:
- R0 read-only / sandbox
- R1 reversible low-risk local modification
- R2 important project / measurement modification; reviewer gate
- R3 external impact / publish / delete / hardware control / official conclusion; human approval

---

# 14. Quantitative P0 Target Dataset

| Metric | Target |
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

# 15. Status of Claims

This research package deliberately distinguishes current facts from future goals.

## Current externally observed facts
- public AI-native operating patterns
- public Kairos operating data
- current job-role descriptions
- public tool capabilities
- reviewed standard/regulatory metadata

## AERIS architecture decisions
- 100 virtual seats
- dynamic pods
- creator/reviewer separation
- Evidence Bundle
- role contracts
- P0–P3 roadmap
- model-neutral SSOT

## Future targets, not present-tense claims
- autonomous lab operation
- autonomous end-to-end acoustic R&D
- complete 100-seat runtime
- regulated-product compliance
- full instrument control
- Level 6 autonomous discovery

---

# 16. Source URLs

### Kairos
- https://os.lifehacker.tw/
- https://wiki.lifehacker.tw/projects/Kairos雷小蒙AI分身
- https://os.lifehacker.tw/posts/2026-03-20-ai-work-log-03
- https://os.lifehacker.tw/posts/2026-04-21-ai-work-log-07
- https://os.lifehacker.tw/posts/2026-05-09-ai-work-log-08
- https://os.lifehacker.tw/posts/2026-08-07-ai-work-log-12
- https://works.lifehacker.tw/works/kw-knowledge-base.html
- https://works.lifehacker.tw/works/skills-dashboard.html

### Agent engineering
- https://www.anthropic.com/engineering/building-effective-agents
- https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- https://www.anthropic.com/engineering/building-c-compiler
- https://www.anthropic.com/engineering/harness-design-long-running-apps
- https://www.anthropic.com/engineering/how-we-contain-claude
- https://openai.com/index/unrolling-the-codex-agent-loop/

### AI-native professional systems
- https://www.coinbase.com/blog/building-a-leaner-and-faster-coinbase
- https://www.futurehouse.org/ai-scientist
- https://www.futurehouse.org/research/demonstrating-end-to-end-scientific-discovery-with-robin-a-multi-agent-system
- https://www.lila.ai/
- https://www.lila.ai/tech
- https://www.harvey.ai/blog/introducing-agent-builder
- https://www.anthropic.com/research/project-vend-1
- https://andonlabs.com/

### Acoustic role / tools
- https://amazon.jobs/en/jobs/10447431/acoustic-engineer-ring-hardware
- https://www.comsol.com/acoustics-module
- https://www.klippel.de/products/rd-system.html
- https://www.audioprecision.com/applications/production-test
- https://www.head-acoustics.com/products/analysis-software/acqua

### Standards / governance
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
- https://www.w3.org/TR/prov-dm/
- https://json-schema.org/draft/2020-12
- https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization
- https://modelcontextprotocol.io/specification/2025-11-25/basic/utilities/tasks
- https://opentelemetry.io/docs/specs/semconv/

---

# 17. Data Maintenance Rule

All time-sensitive rows must eventually carry:

```yaml
source_url:
checked_at:
source_type:
claim:
status:
confidence:
next_review_at:
```

Standards/regulatory data must be revalidated before a design is formally released or certified.
