# AERIS 100-Specialist AI Company Blueprint Evaluation Pack

**Project:** AERIS — Acoustic Engineering & Research Intelligence System  
**Document Type:** Blueprint Evaluation / Architecture Input  
**Version:** v0.1  
**Date:** 2026-09-07  
**Language:** Traditional Chinese  
**Purpose:** 作為 AERIS 下一階段藍圖評估、架構審查、Claude Code / ChatGPT Codex 實作規劃的共同輸入文件。

---

# 0. Executive Summary

AERIS 的目標不是建立 100 個彼此獨立、同時常駐運行的聊天機器人，而是：

> **建立一間只有 1 位人類決策者，但具備 100 個可被調度之聲學專業職能的 AI Acoustic Engineering Company。**

AERIS 應該以：

- **100 Specialists = Capability Pool**
- **Skills = 真正能力**
- **Workflow = 工程 SOP**
- **Knowledge = 專業知識與可追溯記憶**
- **Tools = 工程計算、量測、分析能力**
- **Evidence = 可追溯工程證據**
- **Reviewer = 防止 AI 自說自話**
- **Human Gate = 最終人類決策權**

作為整體設計原則。

核心結論：

1. 市面上已經存在不少可直接 Clone / Fork / Adapt 的 AI Company / Multi-Agent OS。
2. 沒有一套現成系統直接等於「100 人聲學工程公司」。
3. 最合理方式不是複製單一產品，而是吸收不同專案的強項。
4. AERIS 前端可以借鏡雷小蒙 Kairos 的簡潔、高辨識度 Dashboard，但核心架構應更接近工程組織、任務治理、Evidence 與 Audit 系統。
5. **100 名專家不應等於 100 個常駐 LLM Process。**
6. AERIS 應採用 **Dispatcher / Chief Acoustic Engineer → 動態選人 → 任務組隊 → Evidence → Independent Review → Human Approval**。
7. 100 個 Specialist 應全部遵循統一 Contract，而不是只有 100 段 Prompt。

---

# 1. AERIS Long-Term Product Definition

## 1.1 AERIS 全名

**AERIS — Acoustic Engineering & Research Intelligence System**

## 1.2 核心願景

建立一支可在本機環境長期運作的聲學工程 AI 專業團隊，整合：

- 顧問
- 聲學研發
- 電聲
- 麥克風
- 喇叭
- DSP
- Beamforming
- Spatial Audio
- 聲源定位
- 量測
- 模擬
- NVH
- NPI
- 工廠測試
- 品質
- 標準
- 故障分析
- 技術報告
- Evidence
- Review
- Audit

長期目標：

> 建立一套具備接近大型專業工程團隊能力廣度、但只需要一位人類進行策略、風險與最終核准的 Acoustic Engineering AI Company。

---

# 2. 市面上可直接參考／套用的 AI Company 架構

以下專案不是聲學專用，但其架構可被 AERIS 拆解吸收。

## 2.1 候選專案比較

| 專案 | 可直接套用程度 | 主要強項 | AERIS 適配度 | 建議用途 |
|---|---:|---|---:|---|
| OneManCompany | ★★★★★ | AI 員工、組織、HR、COO、任務、Talent Market | 95% | 100 人 AI 公司組織模型 |
| FounderOS-DEMO | ★★★★★ | Dashboard、Agents、Tasks、Skills、Org、Brain、Workflow | 95% | AERIS 前端與資訊架構 |
| Mission Control | ★★★★☆ | Agent Health、Tasks、Memory、Cost、Eval、Security | 95% | AERIS 後台營運中心 |
| OPOS | ★★★★★ | Company-as-Code、Git、治理、Human Gate | 93% | AERIS Core / Governance |
| AI-First HQ OS | ★★★★☆ | deny-by-default、audit、approval、evidence | 93% | Security / Governance |
| OpenCompany | ★★★★☆ | Company roster declarative config | 85% | Specialist Registry 概念 |
| Dify | ★★★★★ | Agent / Workflow 視覺化、模板、匯入匯出 | 80% | Workflow Builder |

---

# 3. 各參考專案可吸收的核心設計

## 3.1 OneManCompany

OneManCompany 最有價值的地方不是 UI，而是：

> **CEO 是唯一人類，其他角色由 AI 員工組成。**

適合 AERIS 吸收：

- AI Employee Registry
- 組織結構
- Agent Profile
- Skills
- Tools
- Job Description
- Hiring / Talent Market
- Performance
- Task Assignment
- Role-based Responsibility

其 Talent Template 類型可轉化為：

```text
AERIS/
└── specialists/
    ├── A001_acoustic_system_architect/
    ├── A002_physical_acoustics/
    ├── A003_wave_propagation/
    ...
    └── A100_independent_acoustic_reviewer/
```

每一個 Specialist 建議包含：

```text
agent/
├── profile.yaml
├── DESCRIPTION.md
├── skills/
│   ├── skill_01/
│   │   └── SKILL.md
│   └── skill_02/
│       └── SKILL.md
├── tools/
│   └── TOOL.md
├── manifest.json
├── tests/
├── evals/
└── evidence_contract.yaml
```

參考：

- https://github.com/1mancompany/OneManCompany
- https://github.com/1mancompany/talent-template

---

## 3.2 OPOS

OPOS 最適合 AERIS 吸收的是：

> **Company-as-Code**

即：

- Mission
- Policy
- Department
- Role
- Task
- Backlog
- Governance

全部透過可版本控制的文件描述。

推薦 AERIS 保留：

```text
company/
departments/
specialists/
skills/
workflows/
knowledge/
standards/
tasks/
evidence/
reviews/
policies/
```

AERIS 不應只是一個應用程式，而應該是一個：

> **可用 Git 追蹤與稽核的 Engineering Organization Repository。**

參考：

- https://github.com/Koroqe/OPOS

---

## 3.3 FounderOS-DEMO

FounderOS 最適合借鏡 AERIS 的是資訊架構：

```text
/
├── agents
├── tasks
├── skills
├── org
├── brain
├── workflows
├── integrations
├── analytics
├── roadmap
└── reference
```

推薦 AERIS 對應：

```text
/
├── specialists
├── missions
├── skills
├── organization
├── knowledge
├── workflows
├── integrations
├── analytics
├── standards
├── measurements
├── hardware
├── evidence
└── system
```

參考：

- https://github.com/Bennettxai/FounderOS-DEMO

---

## 3.4 Mission Control

Mission Control 類型系統最值得 AERIS 學習：

- Agent Health
- Task Status
- Model
- Token
- Cost
- Memory
- Tool Calls
- Security
- Evaluation
- Golden Dataset
- Drift Detection
- Alert
- Cron
- Pipeline
- Logs

AERIS 需要的不只是聊天，而是可以回答：

> 「這個 AI Engineer 目前是否可信？」

建議 AERIS 每個 Specialist 都至少可查看：

```text
STATUS
MODEL
VERSION
CURRENT TASK
TOOLS USED
KNOWLEDGE SOURCES
LAST EVAL SCORE
TRUST SCORE
KNOWN LIMITATIONS
EVIDENCE GENERATED
REVIEW STATUS
```

參考：

- https://github.com/builderz-labs/mission-control

---

## 3.5 Dify

Dify 的價值主要不是 Specialist，而是：

> **Workflow Builder**

可參考：

- Node-based Workflow
- Variable Passing
- Conditional Routing
- Human-in-the-loop
- Tool Integration
- Knowledge Retrieval
- Workflow Template

AERIS 未來可發展成：

```text
Acoustic Workflow Library

Speaker FR Diagnosis
Mic Sensitivity Analysis
Rub & Buzz FA
Factory Golden Sample Verification
Beamforming Evaluation
Sound Source Localization
NVH Investigation
IEC / ISO Compliance Review
Acoustic Report Generation
```

---

# 4. 雷小蒙 Kairos 對 AERIS 的價值

雷小蒙最值得 AERIS 吸收的，不應只有 UI。

可吸收的主要概念：

- 簡潔首頁
- 即時系統狀態
- AI Brain
- Memory
- Skills / Tools
- Automation
- Integration
- 快速導向任務
- 將複雜能力隱藏在簡單介面下

AERIS 不應複製 Kairos 本身，而應吸收其：

> **Simple Outside, Structured Inside**

概念。

---

# 5. AERIS 不應同時跑 100 個 Agent

## 5.1 錯誤架構

```text
User
 ├── Agent 001
 ├── Agent 002
 ├── Agent 003
 ...
 └── Agent 100
```

問題：

- Token / Compute 無限制膨脹
- Memory 不一致
- Specialist 間互相矛盾
- Persona 漂移
- 跨角色知識難同步
- 難以 Audit
- 難以測試
- 難以管理版本
- Edge Runtime 不合理
- 16 GB 系統不可長期承受

---

## 5.2 建議架構

```text
Stephen
   ↓
AERIS Front Desk
   ↓
Problem Classifier
   ↓
Dispatcher / Chief Acoustic Engineer
   ↓
Specialist Registry
   ↓
選擇 1~N 個必要角色
   ↓
Lead Engineer
+ Specialist(s)
+ Measurement / Simulation
+ Independent Reviewer
   ↓
Evidence Package
   ↓
Human Approval
```

核心原則：

> **100 人是 Capability Pool，不是 100 個 Runtime Process。**

---

# 6. AERIS 100-Specialist Organization

建議正式定義：

> **10 Divisions × 10 Specialists = 100 Specialists**

---

# D01 — Acoustic Science & Modeling
## 聲學科學與建模

| ID | Specialist | 主要用途 |
|---|---|---|
| A001 | Chief Acoustic Scientist | 聲學問題的物理模型、理論與分析方向 |
| A002 | Physical Acoustics Specialist | 波動、反射、繞射、干涉 |
| A003 | Wave Propagation Specialist | 傳播路徑、衰減、媒介 |
| A004 | Computational Acoustics Engineer | 數值聲學方法 |
| A005 | FEM Acoustic Specialist | 有限元素聲場 |
| A006 | BEM Acoustic Specialist | 邊界元素、外場輻射 |
| A007 | Statistical Energy Analysis Specialist | 中高頻 SEA |
| A008 | Vibro-Acoustic Coupling Specialist | 結構與聲場耦合 |
| A009 | Acoustic Material Specialist | 吸音、阻尼、多孔材料 |
| A010 | Acoustic Simulation Validation Engineer | Simulation vs Measurement correlation |

---

# D02 — Measurement & Metrology
## 量測與計量

| ID | Specialist | 主要用途 |
|---|---|---|
| A011 | Acoustic Measurement Architect | 整體量測方案設計 |
| A012 | Microphone Measurement Specialist | Microphone 選型、量測 |
| A013 | Sound Level Meter Specialist | SPL、Leq、Weighting |
| A014 | Acoustic Calibration Engineer | Calibrator、Sensitivity |
| A015 | Measurement Uncertainty Specialist | Uncertainty Budget |
| A016 | FFT Analyzer Specialist | FFT / Spectrum |
| A017 | 1/1 & 1/3 Octave Specialist | Octave Analysis |
| A018 | Acoustic Data Acquisition Engineer | DAQ、Sampling |
| A019 | Anechoic Chamber Specialist | 消音室 |
| A020 | Reverberation Chamber Specialist | Diffuse Field、Sound Power |

---

# D03 — Electroacoustics & Transducer
## 電聲與換能器

| ID | Specialist | 主要用途 |
|---|---|---|
| A021 | Electroacoustic System Architect | Speaker / Mic 系統架構 |
| A022 | Loudspeaker Driver Engineer | Speaker Driver |
| A023 | Microphone Transducer Engineer | Microphone Transducer |
| A024 | Speaker Enclosure Engineer | Enclosure、Port、Cavity |
| A025 | Thiele-Small Specialist | T/S Parameters |
| A026 | Microspeaker Engineer | Notebook / Phone Microspeaker |
| A027 | Receiver Engineer | Earpiece Receiver |
| A028 | MEMS Microphone Specialist | MEMS Mic |
| A029 | Amplifier & Speaker Matching Engineer | Amplifier / Driver Matching |
| A030 | Electroacoustic Distortion Specialist | THD / IMD / Rub & Buzz |

---

# D04 — Audio DSP & Algorithms
## 音訊 DSP 與演算法

| ID | Specialist | 主要用途 |
|---|---|---|
| A031 | Audio DSP Architect | DSP Pipeline |
| A032 | Digital Filter Specialist | FIR / IIR |
| A033 | FFT/STFT Specialist | Time-Frequency |
| A034 | Equalization Specialist | EQ Tuning |
| A035 | Dynamic Range Processing Specialist | Compressor / Limiter / AGC |
| A036 | Acoustic Echo Cancellation Engineer | AEC |
| A037 | Noise Suppression Engineer | Noise Suppression |
| A038 | Dereverberation Specialist | Dereverb |
| A039 | Adaptive Filtering Specialist | LMS / NLMS / RLS |
| A040 | Real-Time Audio Optimization Engineer | Latency / CPU / Memory |

---

# D05 — Array, Beamforming & Spatial Acoustic
## 陣列、波束形成與空間聲學

| ID | Specialist | 主要用途 |
|---|---|---|
| A041 | Microphone Array Architect | Mic Array Geometry |
| A042 | Beamforming Engineer | Beamforming |
| A043 | Delay-and-Sum Specialist | DAS |
| A044 | MVDR Beamforming Specialist | MVDR |
| A045 | GCC-PHAT Specialist | TDOA |
| A046 | SRP-PHAT Specialist | Acoustic Localization |
| A047 | Direction-of-Arrival Engineer | DoA |
| A048 | Acoustic Source Localization Engineer | Sound Source Position |
| A049 | Acoustic Camera Engineer | Acoustic Heatmap / Camera Registration |
| A050 | Spatial Audio Engineer | Binaural / Multichannel / 3D Audio |

---

# D06 — Speech, Hearing & Psychoacoustics
## 語音、聽覺與心理聲學

| ID | Specialist | 主要用途 |
|---|---|---|
| A051 | Speech Acoustics Engineer | Speech Spectrum / Intelligibility |
| A052 | Speech Enhancement Engineer | Noisy Speech |
| A053 | ASR Front-End Engineer | ASR 前處理 |
| A054 | Voice Capture Engineer | Far-Field Voice |
| A055 | Psychoacoustics Specialist | 人耳感知 |
| A056 | Sound Quality Engineer | Loudness / Sharpness / Roughness |
| A057 | Listening Test Engineer | AB / ABC / MUSHRA 類測試 |
| A058 | Speech Intelligibility Specialist | STI / STIPA |
| A059 | Hearing & Auditory Perception Specialist | Hearing Model |
| A060 | Voice UX Acoustic Engineer | Voice Interaction UX |

---

# D07 — Product Audio & Consumer Electronics
## 產品聲學與消費電子

| ID | Specialist | 主要用途 |
|---|---|---|
| A061 | Product Acoustic Architect | 整機聲學架構 |
| A062 | Notebook Acoustic Engineer | Notebook |
| A063 | Smartphone Acoustic Engineer | Smartphone |
| A064 | Tablet Acoustic Engineer | Tablet |
| A065 | Smart Speaker Acoustic Engineer | Smart Speaker |
| A066 | Headphone Acoustic Engineer | Headphone |
| A067 | TWS Acoustic Engineer | TWS |
| A068 | Wearable Acoustic Engineer | Wearable |
| A069 | Gaming Audio Engineer | Gaming Device |
| A070 | Product Acoustic Integration Engineer | ME / EE / Acoustic Integration |

---

# D08 — NVH, Machinery & Structural Acoustic
## NVH、機械與結構聲學

| ID | Specialist | 主要用途 |
|---|---|---|
| A071 | NVH System Engineer | Noise / Vibration / Harshness |
| A072 | Structural Vibration Engineer | Vibration |
| A073 | Modal Analysis Specialist | Modal |
| A074 | Operational Deflection Shape Engineer | ODS |
| A075 | Order Analysis Specialist | Rotating Machinery |
| A076 | Machinery Noise Engineer | Fan / Motor / Pump |
| A077 | Fan Noise Specialist | Tonal / Broadband Fan Noise |
| A078 | Motor Acoustic Engineer | Electromagnetic / Mechanical Noise |
| A079 | Structure-Borne Noise Specialist | Structure-Borne Transmission |
| A080 | Transfer Path Analysis Engineer | TPA |

---

# D09 — Building, Environmental & Industrial Acoustics
## 建築、環境與工業聲學

| ID | Specialist | 主要用途 |
|---|---|---|
| A081 | Architectural Acoustic Engineer | 建築 / 空間聲學 |
| A082 | Room Acoustic Specialist | RT / Room Response |
| A083 | Sound Isolation Engineer | Airborne / Impact Isolation |
| A084 | HVAC Acoustic Engineer | HVAC Noise |
| A085 | Environmental Noise Engineer | Environmental Noise |
| A086 | Occupational Noise Specialist | Workplace Exposure |
| A087 | Industrial Noise Control Engineer | Factory Noise |
| A088 | Acoustic Barrier & Silencer Engineer | Barrier / Silencer / Muffler |
| A089 | Community Noise Assessment Engineer | Community Noise |
| A090 | Building Acoustic Compliance Engineer | 建築聲學 Compliance |

---

# D10 — Factory, Standards & Acoustic Intelligence
## 工廠、標準與聲學智能

| ID | Specialist | 主要用途 |
|---|---|---|
| A091 | Acoustic NPI Engineer | EVT / DVT / PVT / NPI |
| A092 | Factory Acoustic Test Engineer | Production Acoustic Test |
| A093 | Acoustic Test Fixture Engineer | Test Fixture |
| A094 | Acoustic GR&R / MSA Engineer | Measurement System Capability |
| A095 | Acoustic Failure Analysis Engineer | Failure Analysis / RCA |
| A096 | Acoustic Quality Engineer | Spec / Yield / SPC |
| A097 | Acoustic Standards Engineer | ISO / IEC / AES / Industry Standards |
| A098 | Acoustic AI/ML Engineer | Classification / Anomaly Detection |
| A099 | Acoustic Data & Evidence Engineer | Raw Data / Provenance / Evidence |
| A100 | Independent Acoustic Review & Report Auditor | 最終技術審查 |

---

# 7. Specialist 不只是 Prompt

100 位 Specialist 都應遵循相同 Contract。

建議最少包含：

```yaml
id:
name:
division:
title:

mission:

expertise:
  -

inputs:
  -

outputs:
  -

must_not:
  -

tools:
  -

knowledge_sources:
  -

required_evidence:
  -

review_by:
  -

prompt_starters:
  -

evals:
  -

version:
status:
```

---

# 8. Specialist Contract Example — A049 Acoustic Camera Engineer

```yaml
id: A049
name: Acoustic Camera Engineer
division: D05
title: Acoustic Camera & Source Imaging Specialist

mission:
  Build, analyze and validate acoustic source imaging systems.

expertise:
  - microphone arrays
  - STFT
  - GCC-PHAT
  - SRP-PHAT
  - Delay-and-Sum
  - MVDR
  - acoustic heatmap
  - RGB/RGB-D registration

inputs:
  - multichannel WAV
  - microphone coordinates
  - sample rate
  - camera calibration
  - target frequency band

outputs:
  - localization result
  - acoustic heatmap
  - confidence score
  - assumptions
  - error sources
  - evidence package

must_not:
  - invent microphone calibration
  - invent array geometry
  - invent camera calibration
  - declare PASS without evidence
  - alter raw measurement data
  - hide uncertainty

tools:
  - numpy
  - scipy
  - FFT/STFT
  - acoustic array toolkit
  - visualization
  - calibration database

required_evidence:
  - raw-data hash
  - algorithm version
  - parameter set
  - microphone geometry version
  - calibration version
  - result confidence
  - reviewer result

review_by:
  - A015
  - A048
  - A100

prompt_starters:
  - 分析這份 4ch WAV 的聲源方向
  - 比較 GCC-PHAT 與 SRP-PHAT
  - 把聲源熱圖投影到 RGB 畫面
  - 評估這個 localization 是否可信
```

---

# 9. 使用者不應自己記住 A001～A100

AERIS UI 不應要求使用者說：

> 「我要 A046。」

UI 應問：

> **你現在想解決什麼問題？**

建議首頁提供：

```text
🔊 Speaker 聽起來不對
🎤 Microphone 收音不好
📈 頻響異常
🔉 有異音 / Buzz / Rattle
🏭 產線測試異常
📊 幫我分析量測資料
🌀 Fan / Motor 有噪音
🧱 房間 / 隔音問題
🗣️ 語音辨識效果不好
📡 找聲音從哪裡來
📷 做 Acoustic Camera
📐 幫我設計量測方法
📚 查 ISO / IEC 標準
📝 幫我產生聲學報告
❓ 我不知道，幫我診斷
```

---

# 10. Dynamic Team Assembly

例如使用者選擇：

> **Fan 有怪聲**

AERIS 自動組隊：

```text
Lead
A071 NVH System Engineer

Specialists
A077 Fan Noise Specialist
A075 Order Analysis Specialist
A033 FFT/STFT Specialist

Measurement
A011 Acoustic Measurement Architect

Failure Analysis
A095 Acoustic Failure Analysis Engineer

Independent Reviewer
A100 Independent Acoustic Review & Report Auditor
```

這比固定一個「Fan Agent」更合理。

---

# 11. Mission-Based Runtime

AERIS Runtime 建議以 Mission 為核心，而不是 Agent Chat 為核心。

一個 Mission：

```yaml
mission_id: M-2026-0001

problem:
  Fan 出現週期性 tonal noise

objective:
  找出主要噪音來源與 root cause

lead:
  A071

specialists:
  - A077
  - A075
  - A033
  - A011

reviewer:
  - A095
  - A100

required_inputs:
  - WAV
  - RPM
  - fan model
  - microphone distance

required_outputs:
  - spectrum
  - order map
  - tonal frequencies
  - root cause hypothesis
  - confidence
  - evidence

status:
  IN_PROGRESS
```

---

# 12. AERIS 首頁建議

```text
┌─────────────────────────────────────────────────────────┐
│ AERIS                         SYSTEM HEALTH ● NORMAL     │
│ Acoustic Engineering & Research Intelligence System     │
├─────────────────────────────────────────────────────────┤
│                                                         │
│     What acoustic problem are we solving today?         │
│                                                         │
│ [ Describe Problem................................. ]    │
│                                      [ Start Mission ]  │
├───────────────────┬─────────────────────────────────────┤
│ SPECIALISTS       │ ACTIVE MISSIONS                     │
│                   │                                     │
│ 100 Available     │ XVF3800 Localization           72%  │
│ 3 Working         │ Fan Noise Investigation        35%  │
│ 1 Reviewing       │ NB Speaker FA                  91%  │
│                   │                                     │
├───────────────────┼─────────────────────────────────────┤
│ KNOWLEDGE         │ EVIDENCE / APPROVAL                 │
│ Standards  1,842  │ ⚠ 2 Awaiting Human Approval        │
│ Papers     12,631 │ ✓ 18 Verified                       │
│ Reports     3,482 │ ✕ 1 Verification Failed             │
├───────────────────┴─────────────────────────────────────┤
│ Lab │ Measurements │ Specialists │ Missions │ Standards │
│ Evidence │ Workflows │ Knowledge │ Hardware │ System    │
└─────────────────────────────────────────────────────────┘
```

---

# 13. AERIS Main Navigation

建議正式定義為：

```text
01 Dashboard
02 Missions
03 Specialists
04 Skills
05 Workflows
06 Measurements
07 Simulations
08 Knowledge
09 Standards
10 Evidence
11 Reviews
12 Reports
13 Hardware
14 Integrations
15 Analytics
16 System
```

---

# 14. AERIS Front-End Design Principle

AERIS UI 不應像一般 ChatGPT Clone。

應該融合：

## Kairos
- 簡潔
- 易理解
- 系統感
- AI Presence

## FounderOS
- Agents
- Tasks
- Skills
- Org
- Brain
- Workflow
- Analytics

## Mission Control
- Health
- Eval
- Logs
- Security
- Drift
- Token
- Cost

## OneManCompany
- AI Organization
- Specialist Pool
- Team Assembly

## OPOS / AI-First HQ
- Governance
- Policy
- Evidence
- Approval
- Git
- Audit

---

# 15. AERIS System Architecture Proposal

```text
                   ┌───────────────────┐
                   │     Stephen       │
                   │   Human Owner     │
                   └─────────┬─────────┘
                             │
                    Human Gate / Approval
                             │
                   ┌─────────▼─────────┐
                   │    AERIS UI       │
                   │ Problem / Mission │
                   └─────────┬─────────┘
                             │
                   ┌─────────▼─────────┐
                   │ Problem Classifier│
                   └─────────┬─────────┘
                             │
                   ┌─────────▼─────────┐
                   │ Dispatcher / CAE  │
                   └─────────┬─────────┘
                             │
              ┌──────────────▼──────────────┐
              │   Specialist Registry      │
              │        A001-A100            │
              └──────────────┬──────────────┘
                             │
                   Dynamic Team Assembly
                             │
       ┌─────────────────────┼─────────────────────┐
       │                     │                     │
    Lead Engineer        Specialists          Reviewer
       │                     │                     │
       └───────────────┬─────┴─────┬──────────────┘
                       │           │
                    Skills       Tools
                       │           │
                       └─────┬─────┘
                             │
                        Knowledge
                             │
                       Measurement
                       Simulation
                       Standards
                             │
                             ▼
                         Evidence
                             │
                             ▼
                     Independent Review
                             │
                             ▼
                        Human Approval
```

---

# 16. Engineering Evidence Principle

AERIS 的每個工程結論都應回答：

```text
1. 你用了什麼輸入？
2. 輸入來源是什麼？
3. 使用哪個版本的資料？
4. 使用哪個演算法？
5. 演算法版本？
6. 使用哪些參數？
7. 使用哪些 Calibration？
8. 使用哪些 Standard？
9. 產出哪一份證據？
10. 信心度多少？
11. 有哪些 Assumption？
12. 有哪些 Limitation？
13. 哪位 Specialist 產出？
14. 哪位 Reviewer 審查？
15. 人類是否批准？
```

---

# 17. AERIS Recommended Engineering Pipeline

```text
Problem
↓
Requirement
↓
Specialist Selection
↓
Method
↓
Inputs
↓
Tools
↓
Analysis
↓
Evidence
↓
Verification
↓
Independent Review
↓
Human Approval
↓
Report
```

建議定義為 AERIS 核心工程流程：

> **Requirement → Method → Evidence → Verification → Human Approval**

---

# 18. Standards Agent Requirement

A097 Acoustic Standards Engineer 不能把 ISO / IEC / AES 規範內容直接永久寫死在 Prompt。

應採：

```text
Standards Registry
↓
Standard Metadata
↓
Version
↓
Publication Date
↓
Current / Superseded / Withdrawn
↓
Applicable Product
↓
Test Method
↓
Referenced Evidence
```

A097 必須優先確認：

- Standard Number
- Edition
- Publication Date
- Amendment
- Corrigendum
- Status
- Current / Withdrawn
- Product Applicability

避免引用過期標準。

---

# 19. AERIS Specialist Lifecycle

每個 Specialist 建議有：

```text
DRAFT
↓
IMPLEMENTED
↓
UNIT TESTED
↓
EVAL TESTED
↓
REVIEWED
↓
APPROVED
↓
ACTIVE
↓
MONITORED
↓
UPDATED / DEPRECATED
```

---

# 20. Specialist Quality Gate

每個 Specialist 最低需要：

- Profile
- Scope
- Inputs
- Outputs
- Must-Not
- Tools
- Knowledge
- Evidence Contract
- Reviewer
- Golden Questions
- Golden Dataset
- Unit Test
- Eval
- Drift Test
- Version

否則不得標為：

> **PRODUCTION READY**

---

# 21. Blueprint 評估時應回答的問題

## P0 — Architecture

1. Specialist Registry 是否應作為 AERIS Core 一級模組？
2. 100 Specialist 是否應一次建好骨架，但分階段 Enable？
3. Dispatcher 應如何選 Specialist？
4. Specialist 是否需要獨立 Memory？
5. 哪些知識應 Shared？
6. 哪些知識應 Role-specific？
7. Runtime 是否採單模型動態角色注入？
8. 是否需要多模型 routing？

---

## P0 — Governance

1. 哪些輸出必須 Reviewer？
2. 哪些輸出必須 Human Gate？
3. 哪些操作禁止 Agent 執行？
4. Raw Data 是否只能 Read-only？
5. Report 是否需要 Evidence ID？
6. Standard 是否必須驗證版本？

---

## P0 — Evidence

1. Evidence Package Schema？
2. Raw Data Hash Schema？
3. Tool / Algorithm Version 怎麼記錄？
4. Calibration Version 怎麼追蹤？
5. Reviewer Sign-off 怎麼儲存？
6. Report 如何反向追到 Evidence？

---

## P1 — UI

1. Dashboard 是否採 Mission-first？
2. Specialist 是否放第二層？
3. 是否避免 100 個 Agent 卡片全部塞首頁？
4. 問題導向分類如何設計？
5. 是否支援 Advanced Mode 手動選 Specialist？

---

## P1 — Runtime

1. J4012 16 GB 如何調度模型？
2. 常駐模型只有幾個？
3. Specialist 是否透過 Prompt / Skill Injection 動態建立？
4. Specialist 結束後 Memory 如何保存？
5. 是否需要 queue？
6. 是否需要 GPU / RAM Budget Manager？

---

## P1 — Evaluation

1. 每個 Specialist 是否有 Golden Questions？
2. 是否建立 Acoustic Golden Dataset？
3. 是否記錄 Accuracy / Hallucination / Evidence Completeness？
4. 是否有 Cross-Specialist Conflict Test？
5. 是否有 Regression Test？

---

# 22. 建議實作優先級

## Phase 0 — Blueprint

只建立：

- Organization
- 100 Specialist Registry
- Specialist Contract
- Mission Contract
- Evidence Contract
- Review Contract
- Dispatcher Design
- UI IA
- Governance

**不急著建立 100 個完整 Agent。**

---

## Phase 1 — Foundation

先建立：

```text
AERIS Front Desk
Dispatcher
Mission Engine
Specialist Registry
Skill Registry
Knowledge Registry
Evidence Engine
Review Engine
```

---

## Phase 2 — 10 Anchor Specialists

先做每個 Division 一名 Anchor Specialist：

```text
A001
A011
A021
A031
A041
A051
A061
A071
A081
A091
```

目的：

- 驗證 Contract
- 驗證 Dispatcher
- 驗證 UI
- 驗證 Evidence
- 驗證 Reviewer
- 驗證 Runtime

---

## Phase 3 — 高價值 Specialist

優先補足目前最符合 AERIS 近期任務的角色：

```text
A015 Measurement Uncertainty
A022 Loudspeaker Driver
A028 MEMS Microphone
A030 Distortion
A033 FFT/STFT
A042 Beamforming
A045 GCC-PHAT
A046 SRP-PHAT
A048 Acoustic Source Localization
A049 Acoustic Camera
A062 Notebook Acoustic
A071 NVH
A075 Order Analysis
A077 Fan Noise
A091 NPI
A092 Factory Test
A094 GR&R / MSA
A095 Failure Analysis
A097 Standards
A099 Evidence
A100 Independent Reviewer
```

---

## Phase 4 — Full 100 Capability Pool

補足 A001-A100。

但仍保持：

> **按需啟動，而不是常駐。**

---

# 23. Recommended Repository Structure

```text
AERIS/
├── company/
│   ├── mission.md
│   ├── organization.yaml
│   └── governance.yaml
│
├── specialists/
│   ├── D01/
│   │   ├── A001/
│   │   ├── A002/
│   │   └── ...
│   ├── D02/
│   └── ...
│
├── skills/
├── workflows/
├── missions/
├── knowledge/
├── standards/
├── measurements/
├── simulations/
├── evidence/
├── reviews/
├── reports/
├── integrations/
├── hardware/
├── evals/
├── policies/
└── ui/
```

---

# 24. Recommended Specialist Directory

```text
A049_acoustic_camera_engineer/
├── profile.yaml
├── DESCRIPTION.md
├── system_prompt.md
├── skills/
│   ├── array_geometry/
│   ├── gcc_phat/
│   ├── srp_phat/
│   └── acoustic_heatmap/
├── tools/
├── workflows/
├── tests/
├── evals/
├── golden_questions.yaml
├── evidence_contract.yaml
├── review_contract.yaml
└── VERSION
```

---

# 25. Recommended UI Information Architecture

```text
Dashboard
│
├── Start Mission
│
├── Missions
│   ├── Active
│   ├── Review
│   ├── Approved
│   └── Archived
│
├── Specialists
│   ├── Division
│   ├── Capability
│   ├── Health
│   └── Evaluation
│
├── Measurements
├── Simulations
├── Standards
├── Knowledge
├── Evidence
├── Reviews
├── Reports
├── Hardware
├── Analytics
└── System
```

---

# 26. Recommended AERIS Design Combination

AERIS 不建議完整 Copy 單一專案。

建議組合如下：

| AERIS 模組 | 最值得參考 |
|---|---|
| 100 人 AI 組織 | OneManCompany |
| Specialist Template | OneManCompany Talent Template |
| 前端 IA | FounderOS |
| 系統 Dashboard | Kairos |
| Agent Health / Eval | Mission Control |
| Workflow | Dify |
| Company-as-Code | OPOS |
| Governance / Human Gate | OPOS / AI-First HQ |
| Evidence | AERIS 自建 |
| Acoustic Specialist Taxonomy | AERIS 自建 |
| Standards Registry | AERIS 自建 |
| Acoustic Engineering QA | AERIS 自建 |

---

# 27. Final Architecture Decision Recommendation

建議 Blueprint 以以下方向作為基線：

> **AERIS = One Human + 100 Acoustic Capabilities + Dynamic Team Assembly + Engineering Evidence + Independent Review + Human Approval**

不是：

> 100 個聊天機器人。

也不是：

> 一個全能 Prompt。

而是：

> **一套工程組織作業系統。**

---

# 28. Final Definition

AERIS 最終應該被定義為：

> **AERIS is a local-first Acoustic Engineering AI Company Operating System that exposes 100 specialized acoustic engineering capabilities through dynamically assembled mission teams, shared engineering knowledge, controlled tools, traceable evidence, independent technical review, and explicit human approval.**

中文：

> **AERIS 是一套 Local-first 的聲學工程 AI 公司作業系統，以 100 個專業聲學職能形成能力池，依任務動態組隊，透過共享工程知識、受控工具、可追溯證據、獨立技術審查與人類最終核准完成專業工程工作。**

---

# 29. Blueprint 評估建議決策

建議 Blueprint 最終明確回答以下 10 件事：

1. **是否正式採用 100-Specialist Capability Pool？**
2. **是否禁止 100 個 Specialist 同時常駐？**
3. **是否採 Dynamic Team Assembly？**
4. **是否建立 Specialist Contract Schema？**
5. **是否建立 Mission Contract Schema？**
6. **是否建立 Evidence Contract Schema？**
7. **是否所有重要工程輸出都需 Independent Review？**
8. **是否建立 Human Approval Gate？**
9. **是否將 Standards Version Control 列入 P0？**
10. **是否採 Phase 0 → Phase 4 漸進實作，而非一次完成 100 人？**

---

# 30. 建議 Blueprint 最終核准基線

建議將下列項目列為 **P0 Architecture Decision**：

```text
[ ] 100-Specialist Registry
[ ] 10-Division Organization
[ ] Dynamic Team Assembly
[ ] Dispatcher / Chief Acoustic Engineer
[ ] Mission Contract
[ ] Specialist Contract
[ ] Skill Registry
[ ] Tool Registry
[ ] Knowledge Registry
[ ] Standards Registry
[ ] Evidence Engine
[ ] Independent Review
[ ] Human Approval Gate
[ ] Evaluation Framework
[ ] Version / Audit / Git Traceability
```

若以上未定義完成，不建議直接大量開發 100 個 Specialist。

---

# 31. External Reference List

## AI Company / Agent OS

- OneManCompany  
  https://github.com/1mancompany/OneManCompany

- OneManCompany Talent Template  
  https://github.com/1mancompany/talent-template

- OPOS  
  https://github.com/Koroqe/OPOS

- FounderOS-DEMO  
  https://github.com/Bennettxai/FounderOS-DEMO

- Mission Control  
  https://github.com/builderz-labs/mission-control

- Dify  
  https://dify.ai/

## AERIS 專業分類可參考組織

- Acoustical Society of America — Technical Committees  
  https://acousticalsociety.org/technical-committees-and-administrative-committees/

- Audio Engineering Society  
  https://aes2.org/

- ISO/TC 43 Acoustics  
  https://www.iso.org/committee/48458.html

- IEC TC 29 Electroacoustics  
  https://tc29.iec.ch/

---

# 32. Note for Blueprint / Claude Code / Codex

本文件是 **Architecture Input**，不是 Implementation Authorization。

後續 AI 在開始程式實作之前，應先：

1. 讀取目前 AERIS Core。
2. 比對現有 Architecture / Policy。
3. 判定本文件與現有 Blueprint 是否衝突。
4. 只提出 Architecture Delta。
5. 列出：
   - KEEP
   - MODIFY
   - ADD
   - REMOVE
   - DEFER
6. 先完成 P0 Architecture Decision。
7. 未經批准，不應直接大量生成 100 個 Specialist。
8. 不應破壞現有 AERIS Core Governance。
9. 不應繞過 Evidence / Review / Human Gate。
10. 所有實作應保持可回滾、可追溯、可驗收。

---

# END OF DOCUMENT
