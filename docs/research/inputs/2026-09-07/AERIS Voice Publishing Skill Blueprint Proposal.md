# AERIS Voice Publishing Skill Blueprint Proposal

## 1. 提案名稱

**AERIS Voice Publishing Skill**

正式定位：

> 將 AERIS 既有的聲學工程知識、研究結果、量測報告、工廠巡檢報告、標準文件與一般 PDF / EPUB / Markdown / TXT，轉換成可追溯、可重現、可離線運作的語音內容與有聲出版品。

這不是單純 TTS 功能，而是一條完整的：

**Document → Understanding → Speech Normalization → Pronunciation → TTS → Audio Production → Chapter / Subtitle / Metadata → Evidence**

Pipeline。

---

# 2. 為什麼 AERIS 應該新增此能力

AERIS 的終極目標不是一般聊天機器人，而是一支可追溯的 AI 聲學工程專業團隊。

目前 AERIS 已經著重：

- 聲學研究
- 測試與量測
- 工廠問題分析
- Root Cause Analysis
- 規格與標準知識
- 報告生成
- Evidence
- 可重現性
- 本機運作

但「工程知識輸出」目前主要仍以文字、Markdown、PDF、Dashboard 為主。

Voice Publishing Skill 可以新增第四種正式輸出：

1. 結構化資料
2. Markdown / PDF 報告
3. Dashboard / Web UI
4. **Audio / Audiobook / Spoken Briefing**

因此它應被視為：

> AERIS 的正式 Knowledge Delivery / Publishing Capability。

---

# 3. 不應直接把 abogen 當成 AERIS 本體

abogen 可以作為重要 Reference Implementation，但不應成為 AERIS Architecture 的核心依賴。

正確原則：

> **AERIS owns the capability.  
> abogen is only one implementation adapter.**

原因：

現在可能使用：

- Kokoro
- Supertonic
- abogen

未來可能改成：

- Qwen TTS
- Fish Speech
- CosyVoice
- 新一代 local TTS
- 其他 OpenAI-compatible TTS

因此 Blueprint 不能寫成：

> AERIS = abogen + Kokoro

而應寫成：

> AERIS defines a model-neutral Voice Publishing Capability.

所有實際 TTS Model、第三方專案與 Backend 均屬 Implementation Layer。

---

# 4. AERIS Voice Publishing 核心 Pipeline

```text
PDF
EPUB
Markdown
TXT
AERIS Report
Measurement Report
Factory Inspection Report
Research Report
Standards Notes
Knowledge Base
Meeting Notes
        │
        ▼
[1] Document Ingestion
        │
        ▼
[2] Document Understanding
        │
        ▼
[3] Speech Normalization
        │
        ▼
[4] Pronunciation Resolution
        │
        ▼
[5] TTS Routing
        │
        ▼
[6] Audio Production
        │
        ▼
[7] Chapter / Subtitle / Metadata
        │
        ▼
[8] Publishing
        │
        ▼
[9] Evidence Bundle
```

---

# 5. Capability 01 — Document Ingestion

第一階段應支援：

- Markdown
- TXT
- PDF
- EPUB

未來可增加：

- DOCX
- HTML
- SRT
- ASS
- VTT
- AERIS native report JSON

要求：

### 必須保留文件結構

包括：

- Title
- Heading
- Chapter
- Section
- Paragraph
- Table
- Figure caption
- List
- Metadata

Voice Publishing 不應只是：

> PDF → extract text → TTS

而應做到：

> Document Structure → Speech Structure。

---

# 6. Capability 02 — Document Understanding

原始工程文件不一定適合直接朗讀。

例如：

```text
FR:
100 Hz = -2.1 dB
1 kHz = 0 dB
10 kHz = -5.4 dB
```

直接交給 TTS 會很難聽。

AERIS 應先轉成：

> 頻率響應結果顯示，一百赫茲相對參考值下降二點一分貝，一千赫茲為零分貝參考點，十千赫茲則下降五點四分貝。

因此中間必須有：

**Speech-oriented Document Understanding Layer**

用途：

- 表格轉口語敘述
- 圖表摘要
- 公式轉口語
- Bullet → narrative
- 無法朗讀的格式轉寫
- 過長句重新分句
- Technical abbreviation normalization
- Symbol normalization

---

# 7. Capability 03 — Engineering Speech Normalizer

這應該成為 AERIS 最有差異化的能力之一。

一般 Audiobook 工具不懂聲學工程語言。

AERIS 必須建立：

> **Engineering Speech Normalizer**

例如：

```text
94 dB SPL
→ 九十四分貝聲壓級

20 Hz
→ 二十赫茲

20 kHz
→ 二十千赫茲

1/3 octave
→ 三分之一倍頻程

THD
→ T H D

THD+N
→ T H D plus N

ANC
→ A N C

FFT
→ F F T

SNR
→ S N R

-3 dB
→ 負三分貝

20 Hz–20 kHz
→ 二十赫茲到二十千赫茲
```

還需涵蓋：

- IEC 標準
- ISO 標準
- ANSI 標準
- APx
- SoundCheck
- HEAD acoustics
- GRAS
- Brüel & Kjær
- Klippel
- ReSpeaker
- XMOS
- XVF3800
- MEMS
- SPL
- Leq
- dBA
- dBC
- LUFS
- PSD
- FFT
- FR
- THD
- THD+N
- Rub & Buzz
- Beamforming
- DoA
- ANC
- AEC
- AGC

未來應形成：

```text
engineering_pronunciation_dictionary/
```

並且可版本化。

---

# 8. Capability 04 — Pronunciation Dictionary

需要建立獨立 Pronunciation Layer。

不能把發音規則 hard-code 在某個 TTS 模型。

資料可以包含：

```text
term
language
category
spoken_form
ipa_optional
tts_override
source
confidence
version
```

例如：

```text
XVF3800
→ X V F 三八零零

APx555
→ A P x 五五五

B&K
→ B and K

IEC 60268-21
→ I E C 六零二六八之二十一
```

並需支援：

- 中文
- 英文
- 中英混合
- 廠牌
- 公司名
- 人名
- 標準名稱
- 型號
- 自訂詞

---

# 9. Capability 05 — TTS Router

AERIS 不綁定單一 TTS。

應建立：

```text
TTSProvider
```

統一 Interface。

例如：

```text
synthesize(
    text,
    language,
    voice,
    speed,
    style,
    output_format
)
```

Adapter 可以包含：

```text
adapters/
└── tts/
    ├── interface.py
    ├── kokoro.py
    ├── supertonic.py
    ├── local_generic.py
    └── openai_compatible.py
```

Routing 可依：

- Language
- Quality
- Latency
- GPU RAM
- License
- Offline availability
- Voice availability
- User preference

決定 Backend。

---

# 10. 中文與英文必須分開選型

Blueprint 不應假設同一模型同時是中文與英文最佳方案。

建議：

```text
English
→ Kokoro / future best local English TTS

Traditional Chinese
→ 可替換的高品質中文 TTS Backend
```

必須保留：

> `language-specific backend routing`

原因是小型英文 TTS 在中文自然度通常不等價。

因此 Architecture 必須從一開始就允許：

```text
zh-TW → Model A

en-US → Model B
```

而不是被單一模型綁死。

---

# 11. Capability 06 — Audio Production

TTS Output 不能直接算完成。

需要 Production Layer：

- Sentence segmentation
- Chunk generation
- Pause control
- Silence insertion
- Normalization
- Loudness normalization
- Sample rate control
- Channel format
- Fade in/out
- Chapter transition
- Audio concatenation
- Retry failed segment
- Resume interrupted job

並需要避免：

> 任何一段失敗就整本重新生成。

因此每個 Segment 應該是可快取、可重用、可追蹤的 Artifact。

---

# 12. Capability 07 — Chapter

必須支援 Chapter。

例如一份工廠聲學報告：

```text
Chapter 1
Executive Summary

Chapter 2
Test Setup

Chapter 3
Measurement Results

Chapter 4
Frequency Response

Chapter 5
THD Analysis

Chapter 6
Root Cause

Chapter 7
Risk Assessment

Chapter 8
Recommendation
```

Chapter Source 應優先取自：

1. 原文件 heading
2. AERIS report schema
3. LLM inference

而不能完全依賴 LLM 猜測。

---

# 13. Capability 08 — Subtitle

應支援：

- SRT
- VTT
- ASS

最低要求：

### Sentence-level timestamp

未來可增加：

- Word-level timestamp
- Sentence highlighting
- Karaoke-style highlighting

字幕用途：

- YouTube
- 教學影片
- 技術簡報
- Audiobook
- AERIS Web Player
- 工廠訓練教材

---

# 14. Capability 09 — Metadata

正式 Audio Artifact 應附帶：

```text
title
author
organization
project
created_at
document_version
language
voice
tts_backend
chapter_list
source_document
report_id
```

對 Audiobook 類輸出，可增加：

- Cover
- Description
- Series
- Publisher
- Track
- Chapter metadata

---

# 15. Capability 10 — Output Formats

Phase 1：

```text
WAV
MP3
```

Phase 2：

```text
OPUS
FLAC
SRT
VTT
```

Phase 3：

```text
M4B
Chapter Metadata
Cover
Audiobook Package
```

---

# 16. AERIS 最重要的特殊能力：Evidence

AERIS 與一般有聲書軟體最大的差異，不應是 Voice 比較多。

而是：

> **Every audio output must be traceable.**

每次產生 Voice Artifact，至少保存：

```text
source_document
source_sha256

document_parser
document_parser_version

normalizer
normalizer_version

llm_model
llm_prompt_version

pronunciation_dictionary_version

tts_backend
tts_model
tts_model_version
voice_id

language
speed
sample_rate

chapter_map

subtitle_mode

generated_at

output_sha256
```

因此可以回答：

> 這段聲音是根據哪一份報告？

> 當時用什麼模型？

> 哪個 Prompt？

> 哪版 Pronunciation Dictionary？

> 原始文件後來有沒有被修改？

> 是否可以重新產生完全相同的輸出？

---

# 17. Provenance Chain

應形成：

```text
Source Document
    │
    ├─ SHA256
    │
    ▼
Parsed Document
    │
    ├─ parser version
    │
    ▼
Normalized Speech Text
    │
    ├─ normalizer version
    ├─ LLM model
    ├─ prompt version
    │
    ▼
Pronunciation-resolved Text
    │
    ├─ dictionary version
    │
    ▼
TTS Segments
    │
    ├─ backend
    ├─ voice
    ├─ model
    │
    ▼
Final Audio
    │
    ├─ SHA256
    │
    ▼
Evidence Bundle
```

這應符合 AERIS 原本 Evidence-first 的設計原則。

---

# 18. Core 與 Implementation 必須分開

AERIS 現有架構應繼續遵守：

```text
0_JN1_AERIS
=
WHAT
=
Canonical Core / Blueprint

0_JN1_AERIS_Local-computer-implementation
=
HOW
=
Executable Implementation
```

## Core 只定義 Capability

例如：

```text
VOICE_PUBLISHING_CAPABILITY_V1
```

定義：

- Purpose
- Input
- Output
- Contract
- Evidence
- Security
- Privacy
- Offline requirement
- Acceptance Gate

Core 不指定：

- pip package
- Docker
- Kokoro version
- GPU runtime
- abogen repo
- Python implementation detail

---

# 19. Implementation Repo 才負責實作

推薦：

```text
skills/
└── voice_publishing/
    ├── SKILL.md
    ├── manifest.yaml
    ├── README.md
    ├── schemas/
    ├── tests/
    ├── golden/
    └── examples/

services/
└── voice_publishing/

adapters/
├── document/
│   ├── pdf/
│   ├── epub/
│   └── markdown/
│
├── tts/
│   ├── interface/
│   ├── kokoro/
│   └── other/
│
└── abogen/
    └── adapter/
```

---

# 20. abogen 在 AERIS 的正式角色

推薦定位：

```text
External Reference Implementation
+
Optional Adapter
```

不是：

```text
AERIS Core dependency
```

可借用能力：

- EPUB parsing
- PDF handling
- Chapter handling
- M4B packaging
- Subtitle
- Pronunciation Override
- Voice assignment
- Voice Mixer concept
- Audiobookshelf integration
- Job processing
- Audio concatenation

但 AERIS 必須保留自己的：

- Contract
- Data model
- Evidence
- Adapter layer
- Testing
- Error handling
- Security policy

---

# 21. Security / Privacy Requirement

Voice Publishing 必須優先支援：

> **100% Local / Offline**

因為 AERIS 可能處理：

- 公司內部文件
- 客戶資料
- 未公開產品
- 聲學量測報告
- Failure Analysis
- NPI 資訊
- Factory issue
- Design specification

因此預設：

```text
local_only = true
```

任何 Cloud Provider：

```text
must require explicit policy approval
```

不能因為某個 TTS Adapter 支援 API，就默認上傳文件。

---

# 22. Job 架構

長文件生成必須是 Job-based，而不是單 request。

```text
VoicePublishingJob
```

狀態：

```text
QUEUED
PARSING
NORMALIZING
SYNTHESIZING
PACKAGING
VALIDATING
COMPLETED
FAILED
CANCELLED
```

並保存：

```text
progress
current_chapter
current_segment
retry_count
error
timestamps
```

---

# 23. Cache

TTS 應該支援 Segment Cache。

Cache Key：

```text
hash(
    normalized_text
    + model
    + voice
    + speed
    + pronunciation_version
)
```

好處：

修改 Chapter 8 時：

> 不必重新產生 Chapter 1～7。

這會大幅降低：

- 時間
- GPU loading
- 能耗
- 重複運算

---

# 24. Quality Gates

不能只驗證：

> 有成功生成 MP3。

最低 Gate 應包含：

### Gate VP-01
Document Parsing

- Heading 正確
- Chapter 正確
- 文字沒有大量遺漏

### Gate VP-02
Speech Normalization

測試至少：

- dB
- Hz
- kHz
- THD
- THD+N
- IEC
- 型號
- 負數
- 小數
- 百分比

### Gate VP-03
Pronunciation

建立 Golden Dataset。

例如：

```text
100+ acoustic terms
50+ model names
50+ standards / abbreviations
```

### Gate VP-04
Audio

驗證：

- file valid
- duration > 0
- no NaN
- sample rate correct
- no corrupted segments

### Gate VP-05
Chapter

Chapter 數量、順序、名稱需與來源吻合。

### Gate VP-06
Evidence

每個正式 Artifact 必須具備完整 Provenance。

---

# 25. Golden Test Set

建議建立：

```text
golden/
├── acoustic_terms_zh_tw.yaml
├── acoustic_terms_en.yaml
├── standards.yaml
├── units.yaml
├── mixed_language.yaml
├── report_sample.md
├── factory_report_sample.md
└── measurement_report_sample.md
```

之後換 TTS Model 時，可以直接跑 regression。

---

# 26. Phase 規劃

## Phase 1 — MVP

目標：

> AERIS Report → MP3

支援：

- Markdown
- TXT
- Engineering Normalizer
- Pronunciation dictionary
- English TTS
- Chinese TTS abstraction
- WAV / MP3
- Evidence

這階段先證明 architecture。

---

## Phase 2 — Document Publishing

增加：

- PDF
- EPUB
- Chapter
- Subtitle
- Metadata
- Job Queue
- Cache

---

## Phase 3 — Audiobook Production

增加：

- M4B
- Cover
- Voice Roles
- Voice Mixer
- Audiobook packaging
- Audiobookshelf adapter

---

## Phase 4 — Advanced AERIS Engineering Voice

增加：

- Table → spoken summary
- Chart → spoken interpretation
- Measurement result narration
- Multilingual technical narration
- Different voices by engineer role
- Executive summary voice mode
- Engineering detailed voice mode
- Training / teaching voice mode

---

# 27. 未來可形成不同 Voice Profiles

例如：

```text
AERIS Executive Voice
```

只講：

- Summary
- Risk
- Decision
- Recommendation

---

```text
AERIS Engineer Voice
```

講：

- Measurement
- FR
- THD
- SPL
- Setup
- Root Cause

---

```text
AERIS Training Voice
```

講：

- Concepts
- Explanation
- Examples
- Standards

---

```text
AERIS Factory Voice
```

講：

- Issue
- Location
- Severity
- Immediate Action
- Follow-up

因此 Voice Publishing 最後不是單純：

> 同一份文字換不同聲音。

而是：

> 同一份 Evidence 生成不同 Audience 的 Voice Artifact。

---

# 28. 與 AERIS Agent / Engineer 的關係

未來任何 Engineer Agent 可以呼叫：

```text
voice_publish()
```

例如：

```text
Acoustic Consultant
→ Executive audio summary

Measurement Engineer
→ Test-result narration

Factory Engineer
→ Factory issue voice report

Standards Engineer
→ Standard learning audiobook

Research Engineer
→ Paper audio summary
```

所以它應該是：

> **Shared Platform Skill**

而不是第 101 個 Engineer。

---

# 29. Blueprint Architectural Decision

建議正式 Decision：

> **APPROVE — Add Voice Publishing as a shared AERIS platform capability.**

但附帶條件：

1. Model-neutral
2. Backend-neutral
3. Offline-first
4. Evidence-first
5. Adapter-based
6. Engineering pronunciation aware
7. Reproducible
8. Testable
9. No hard dependency on abogen
10. No hard dependency on Kokoro

---

# 30. 一句話 Blueprint 定義

> **AERIS Voice Publishing is a model-neutral, offline-first and evidence-traceable platform capability that transforms engineering documents, reports and knowledge into structured spoken content, subtitles and audiobook-grade artifacts while preserving document provenance, technical pronunciation and reproducibility.**

---

# 31. 中文版 Blueprint 定義

> **AERIS Voice Publishing 是一套模型中立、本機優先、可追溯且可重現的共用平台能力，負責將聲學工程文件、研究、量測結果、工廠報告、標準知識與一般文件，經過文件理解、工程語音正規化、專業發音解析、TTS 與音訊製作後，輸出成 MP3、WAV、字幕、章節化內容與 M4B 等正式語音 Artifact，並完整保留來源、模型、版本與輸出 Evidence。**

---

# 32. Blueprint 評估時最重要的問題

Blueprint Reviewer 應回答：

### Architecture
- 此能力是否應屬 Shared Platform Skill？
- 是否與既有 AERIS Knowledge / Report Pipeline 重疊？
- Input / Output contract 應放在哪一層？

### Dependency
- abogen 應 clone、fork、submodule、adapter 還是僅 reference？
- 哪些程式值得直接採用？
- 哪些應由 AERIS 自己重寫？

### Model
- 英文 TTS Backend 選型？
- zh-TW Backend 選型？
- 是否需要多模型 Router？

### Evidence
- Voice Artifact 的 minimum evidence schema 是什麼？
- 如何與 AERIS 現有 Evidence Bundle 整合？

### Security
- 是否能完全 offline？
- 哪些 dependency 會自動下載模型？
- 如何避免文件意外送往 Cloud？

### Performance
- 一小時音訊生成時間
- RAM
- VRAM
- Disk
- Startup time
- Cache efficiency

### Quality
- 中文自然度
- 英文自然度
- Engineering pronunciation accuracy
- Chapter correctness
- Subtitle correctness

---

# 33. 建議 Codex 不要直接開始安裝

Blueprint 通過前，Codex 第一階段只做：

```text
RESEARCH
↓
INVENTORY
↓
ARCHITECTURE IMPACT ANALYSIS
↓
ADR
↓
SPEC
↓
IMPLEMENTATION PLAN
```

不能一看到 abogen 就：

```text
git clone
pip install
開始改 AERIS
```

先判斷：

> 它是不是符合 AERIS Blueprint。

再決定：

> 怎麼施工。

這樣才能避免「功能越做越多，但 AERIS Architecture 慢慢改歪」。

---

# 最終建議

**建議納入 AERIS Blueprint。**

優先級建議：

**P1：**

- TTS abstraction
- Engineering Speech Normalizer
- Pronunciation Dictionary
- AERIS Report → Speech
- Evidence

**P2：**

- PDF / EPUB
- Chapter
- Subtitle
- Job
- Cache

**P3：**

- M4B
- Voice Mixer
- Multi-role Voice
- Audiobookshelf

核心原則：

> **先建立 AERIS 自己的 Voice Publishing Architecture，再吸收 abogen。**

而不是：

> **把 abogen 裝進 AERIS，然後讓 AERIS 適應 abogen。**