# Kairos／雷小蒙／LifeOS 深入研究與 AERIS 架構吸收建議

> 研究基準日：2026-08-31（Asia/Taipei）  
> 研究對象：Kairos（雷小蒙）、LifeOS、`os.lifehacker.tw`、Raymond-Agent 公開架構與工作紀錄  
> AERIS：Acoustic Engineering & Research Intelligence System  
> 文件目的：把公開可取得的架構、數據、事件、事故、演進與可移植設計，整理成可直接供 AERIS / Claude Code / Codex 使用的工程研究基線。

---

## 0. Executive Summary

Kairos 最值得 AERIS 吸收的，不是某一顆模型、不是 Dashboard，也不是「多 Agent」本身，而是 **Agent Harness**：把核心規則、Skills、Memory、Workflow、Tools、Automation、Observability、Evidence 與 Human Approval 變成可累積、可搬遷、可驗證的長期資產。

Kairos 的公開演進大致可以整理成：

```text
Prompt
→ Core Rules
→ Memory
→ Skills
→ Tools
→ Automation
→ Model Portability
→ Evaluation
→ Observability
→ Evidence-before-Done
→ Human Approval
→ Judgment Externalization
```

對 AERIS 而言，建議再往前推一階：

```text
Requirement
→ Method
→ Input Provenance
→ Execution
→ Evidence Bundle
→ Deterministic Verification
→ Independent Review
→ Human Approval
→ Release
→ Reproduction
```

**核心判斷：**

1. **Model is compute, not identity**：Claude Code、Codex、未來本機模型都應是可替換 runtime。
2. **Memory is not Evidence**：記憶可摘要、重組、淘汰；工程證據不可任意改寫。
3. **Execution is not Completion**：執行成功不等於工程結果完成；必須經過 Evidence、Verification、必要時的 Human Approval。
4. **Reviewer is a role, not a model brand**：不要把「Codex 做、Claude 驗」寫死；Executor / Reviewer 應由角色與權限定義。
5. **Dashboard is projection, not truth**：Dashboard 只能投影真實狀態；所有綠燈都必須能下鑽到可驗證證據。
6. **Reproducibility is a product feature**：AERIS 的競爭力應是半年後換模型、換工程師仍可重現結果。

---

## 1. 研究範圍與證據分級

### 1.1 證據等級

| 等級 | 定義 | 本報告處理方式 |
|---|---|---|
| **A：公開直接證實** | 第一方 Wiki、工作紀錄、作者文章、公開 GitHub 可直接找到 | 可當作「公開事實」引用 |
| **B：作者自述數據** | 作者或 Kairos 自己報告的使用量、速度、準確率、成本 | 明確標示「作者自述」，不當成第三方 benchmark |
| **C：工程推論** | 依公開事件與架構合理推導 | 明確標示為分析判斷 |
| **D：未知／未公開** | 無足夠公開資料 | 不猜實作細節 |

### 1.2 目前不能嚴謹證實的項目

以下內容公開資訊不足，不應自行腦補：

- `os.lifehacker.tw` Dashboard 的前端 framework。
- Dashboard 後端 framework、API gateway、資料庫種類與 schema。
- 目前所有 Memory 是否仍完全沿用 2026-02 的 `memory.json` 架構。
- 全部 Skills / Workflows 的完整 source code。
- 全部 MCP server、OAuth scope、secret policy。
- 正式 SLO / SLA / MTTR / incident rate。
- 完整 Backup RPO / RTO / DR topology。
- 完整 RBAC / ABAC 權限模型。
- 是否做過獨立 security audit / penetration test。
- 首頁目前提到「三棲助理狀態」，但公開技術資料只明確證實 Claude Code + Codex；第三 runtime 未公開指定。

---

## 2. Kairos 定位與公開系統架構

Kairos（對外多稱「雷小蒙」）是侯智薰（雷蒙）於 2026 年 2 月起，用 Claude Code 從零手刻的個人 AI Agent。公開 Wiki 將它定位成工作與生活助理、團隊數位分身，架在 Raymond-Agent / LifeOS 知識庫之上。

公開資料明確顯示，系統核心不是單一聊天機器人，而是：

```text
Human
  ↓
Interfaces
  ├─ CLI
  ├─ Mobile / Remote Control
  ├─ Discord
  └─ Dashboard
  ↓
Agent Harness
  ├─ Core Rules
  ├─ Skills
  ├─ Memory
  ├─ Workflows / Hooks
  ├─ Governance / Judgment Rules
  └─ Tool Permissions
  ↓
Replaceable Model Runtime
  ├─ Claude Code
  ├─ Codex
  └─ Future / Other Model
  ↓
Tools / MCP / API / CLI
  ↓
Gmail / Calendar / Notion / WordPress / Home Assistant / Web / Local Files
  ↓
Logs / State / Evidence / Dashboard
```

### 2.1 三層知識架構

公開 Wiki 將 Kairos 簡化成三層：

| 層 | Kairos 公開實作 | AERIS 對應建議 |
|---|---|---|
| L1 核心規則 | `CLAUDE.md` / core rules | `CONSTITUTION.md` + `CORE_RULES.md` + Risk Policy |
| L2 Skills | 任務 SOP，按需載入 | 聲學 Versioned Engineering Skills |
| L3 Dynamic Memory | 跨對話長期記憶 | Project / Experiment / Decision / Lesson Memory |

### 2.2 後期七層 Harness

2026 年中作者把 Agent 拆成七層：

1. 核心規則
2. 技能
3. 精煉記憶
4. 使用者畫像
5. 對話歷史
6. 生命週期自動化
7. 多平台門面

後期公開文章更提到 Kairos 已累積 **近 60 個個人化 Skills**。這與 2 月早期的 15 Skills 並不矛盾，而是反映系統規模持續成長。

---

## 3. Memory Architecture：從「記住」轉成「知道去哪裡找」

### 3.1 2026-02 公開的三層 Memory

| Memory Layer | 公開檔案 / 機制 | 用途 | 量化資料 |
|---|---|---|---:|
| 精煉記憶 | `MEMORY.md` | 偏好、專案進度、踩坑、當前狀態 | 每次載入前約 200 行 |
| 關係記憶 | `memory.json` + Memory MCP | Entity / Relationship 查詢 | 未公開完整 schema |
| 時序記憶 | `daily/*.md` | 每次 session 完成事項、決策、技術紀錄 | 每次 session 結束自動寫入 |

作者明確提出核心原則：

> AI 不需要記住所有細節，但需要知道去哪裡找。

### 3.2 AERIS 應保留原理，不必照抄檔名

AERIS 建議改成：

```text
Hot Context
= 現在最需要的少量狀態

Structured Knowledge
= Project / Component / Requirement / Method / Lesson 關聯資料

Immutable Event History
= 真實執行歷史與 audit event
```

**重要：Memory 不應承擔 Evidence 的責任。**

---

## 4. Context 分層與 Rules SSOT

### 4.1 `CLAUDE.md` 768 → 120 行

2026-02 第三週，公開文章記錄：

- `CLAUDE.md` 一度膨脹到 **768 行**。
- 瘦身後只保留 **120 行核心規則**。
- 領域知識搬進 **15 個 Skills**。
- `MEMORY.md` 控制在 **200 行以內**。
- 一次性決策只留在 daily log。

這是整套架構最重要的設計之一：**不要把所有知識塞進 system prompt / CLAUDE.md。**

### 4.2 Claude Code / Codex 共用 SSOT

作者後續明確提出：

```text
AGENTS.md      → Codex 入口
CLAUDE.md      → Claude Code 入口
core-rules.md  → 真正共用核心規則 SSOT
skills/        → 重複工作 SOP
memory/        → 長期記憶
workflows/     → 具體任務流程
projects/      → 專案與資料
```

三個原則：

1. 入口可以有多個，但核心規則最好只有一份。
2. 重複流程逐步整理成 Skill。
3. 重要記憶不要只存在平台聊天裡。

### 4.3 AERIS 直接採用

AERIS 建議：

```text
AGENTS.md    = Codex adapter / entrance
CLAUDE.md    = Claude Code adapter / entrance

真正規則：
core/CONSTITUTION.md
core/CORE_RULES.md
core/RISK_POLICY.yaml
core/APPROVAL_MATRIX.yaml
```

---

## 5. Skills：從 Prompt 進化成可測試模組

### 5.1 Kairos Skill 的成熟過程

早期：Skill = 任務 SOP。  
後期：Skill 已逐步具備軟體模組特性：

- `SKILL.md`
- `references/`
- `scripts/`
- `evals/`
- `CHANGELOG`
- 安裝 / 更新方式
- 跨 Claude Code / Codex / Cursor 等工具搬遷

作者公開的 `speak-human-tw` 是最直接的例子。

### 5.2 公開 benchmark 數據

`speak-human-tw` 公開 README 目前列出：

- **42 條 benchmark cases**
  - 27 條 SF：該改必中
  - 15 條 SNF：不可誤殺
- 38 種 AI 寫作痕跡。
- 公開 release 曾記錄雙模型交叉評測：改寫端 Codex CLI、判分端 Claude。

這代表 Skill 已不再只是「提示詞」，而是可以有：

```text
Specification
+ Reference
+ Script
+ Test Dataset
+ Regression Test
+ Negative Case
+ Version
```

### 5.3 AERIS Skill 標準建議

```text
skills/
└── frequency-response-analysis/
    ├── SKILL.md
    ├── skill.yaml
    ├── references/
    │   ├── method-notes.md
    │   └── standards-index.yaml
    ├── schemas/
    │   ├── input.schema.json
    │   └── result.schema.json
    ├── scripts/
    │   ├── analyze.py
    │   └── validate.py
    ├── tests/
    │   ├── unit/
    │   ├── golden/
    │   ├── regression/
    │   └── bad_cases/
    ├── fixtures/
    └── CHANGELOG.md
```

AERIS 的每個 Skill 必須同時回答：

1. **怎麼做？**
2. **如何證明做對？**

---

## 6. Model Portability：Claude / Codex 是可替換「大腦」

公開工作紀錄與搬家文章反覆強調：

- 重要記憶、Skills、Workflow、規則放在本地資料夾。
- Claude Code 與 Codex 可以讀同一套本地知識。
- 作者把模型比喻成「租來的大腦」。
- 系統資產不應綁在某一家 AI 平台。

### 6.1 2026-06 計費事件

作者自述：

- 當時 Kairos 有 **40+ 背景自動化**。
- 若 Anthropic 預告的計費變更照原方案執行，估計每月多 **USD 100–200**。
- 因此測試把外連「大腦」從 Claude 改接 Codex。
- 最終雖然計費改動喊卡，但完成了 Claude / Codex 雙棲驗證。

### 6.2 AERIS 決策

不要寫死：

```text
Codex = Builder
Claude = Reviewer
```

應寫成：

```text
ROLE = Executor / Reviewer / Researcher / Verifier
MODEL = replaceable implementation
```

模型只是 role adapter。

---

## 7. Quantitative Data：公開可量化資料總表

> 注意：多數為作者自述或 Kairos 工作週報，並非第三方 telemetry audit。

| 類別 | 數據 | 時點 / 語境 | 信賴分類 |
|---|---:|---|---|
| 初期建置時間 | 21 天 | 2026-02-08 起 | A |
| 初期 `CLAUDE.md` | 768 → 120 行 | 2026-02 第三週 | A |
| 初期 Skills | 15 個 | 2026-02 | A |
| 後期 Skills | 近 60 個 | 2026 年中後期文章 | A/B |
| `MEMORY.md` | 200 行以內 | 初期 Context 分層 | A |
| Workflow 觸發詞 | 12 個 | 21 天成果回顧 | A |
| Discord Bot 早報 | 09:00 | 早期配置 | A |
| Discord Bot 晚報 | 22:00 | 早期配置 | A |
| Bot watchdog | 每 15 分鐘 | 早期基礎設施 | A |
| Gmail 手動處理 | 30–60 分鐘/日 | 導入前 | B |
| AI 回信草稿 | 約 80% 草稿 | 人工最後審核 | B |
| Home Assistant 自動化 | 一次重寫 5 個 | 個案 | B |
| iCloud Vault | 14GB → 900MB | `.nosync` 效能手術 | B |
| Python | 3.9 → 3.13 | 2026-02 | A |
| Ghost 成本 | USD 20/月 → 11–12/月 | 自述約降 40% | B |
| 專屬主機 | USD 12/月 | Linode Tokyo / Zeabur | B |
| 部落格掃描 | 368 篇 | 2026-03 | B |
| 核心概念頁 | 16 個 | 368 篇整理結果 | B |
| 反向連結 | 155 篇 | 同上 | B |
| Discord 歷史訊息 | 87 則 | 生日資料抽取 | B |
| 生日資料 | 44 位 | 同上 | B |
| Dashboard 整合平台 | 7 個 | GA4 / Kit / Ghost / Meta Ads / GSC / Bing / Threads | B |
| Kit 訂閱者 | 25,074 | 2026-03 工作紀錄當下 | B |
| Ghost 會員 | 11,223 | 2026-03 工作紀錄當下 | B |
| API Keys | 18 個接 Dashboard | 2026-03 | B |
| 1Password Keys | 31 筆 | 2026-03 | B |
| AI 快訊 | 576 → 84 → 12 → 3 | 關鍵字→AI判斷→精選 | B |
| Memory audit 故障 | 5 天無人發現 | 2026-03 incident | A/B |
| Bot schedules | 4 個全部 silent fail | 2026-03 incident | A/B |
| WordPress 外掛 | 47 → 36 | 2026-03 | B |
| WordPress 圖片 Alt | 39 張 / 4 篇文章 | 2026-03 | B |
| 個人百科 | 109 條 | 2026-06 | B |
| 個人百科分類 | 14 大類 | 2026-06 | B |
| 背景自動化 | 40+ | 2026-06 | B |
| 預估額外 AI 成本 | USD 100–200/月 | 當時計費假設 | B |
| Agent wake-up | 1,481 次 / 26 天 | 2026-06-29 ~ 08-05 | B |
| Agent 互動 | 30,000+ turns / 26 天 | 同上 | B |
| 公開 Skill benchmark | 42 cases | `speak-human-tw` | A |

---

## 8. 事故時間線：真正值得 AERIS 學的部分

### 8.1 2026-03：Authentication 三連坑

事件：

1. API mode 導致 Remote Control 消失，SSH 認證失敗。
2. 雙 Token 架構中的環境 token 24 小時後失效。
3. 舊文件用 SSH 重啟，但 SSH session 沒 Keychain。

最後收斂：

```text
認證統一走 Keychain，不要有第二條路。
```

**AERIS 對策：**

- Secret Provider SSOT。
- 啟動前 credential health check。
- 禁止多套 fallback secret path 無限增生。

### 8.2 2026-03：Silent Failure

公開工作紀錄：

- Memory audit 壞了 **5 天** 無人發現。
- Ghost schedule 被覆蓋刪除。
- Bot 的 **4 個排程全部靜默失敗**。

作者後續明確判斷：下一步不是建更多系統，而是現有系統要有更好的健康監控。

**AERIS 必須監控：**

```text
last_expected_run
last_successful_run
expected_artifact_exists
artifact_is_fresh
verification_passed
approval_pending_age
```

不能只監控：

```text
process_alive = true
```

### 8.3 WordPress 升級 500

- 先升 Elementor → 全站 500。
- rollback。
- 改成先升 PHP 再升 Elementor。

**教訓：** dependency sequencing、preflight、rollback checkpoint 都要制度化。

### 8.4 Email 自動分類錯誤

作者曾讓 AI 自己判斷「回覆 / 忽略 / 轉交」，結果重要合作信被判成不需回覆。

後續改法：

```text
Gmail Label = SSOT
AI = 只負責草稿內容
Human = 最後審核與寄出
```

**AERIS 對應：**

Pass / Fail、測試等級、Requirement status、正式 release 條件，不得靠 LLM 自由猜測。

### 8.5 2026-07/08：False-Done / Authority 過界

後期公開工作紀錄出現幾類更成熟的治理問題：

- AI 宣稱背景 upload 已開始，但實際 task 根本不存在。
- 未經核准提前開通權限／課程。
- 修正通知限制後仍發生通知轟炸。

因此形成兩個重要控制：

1. **Evidence-before-Done**：AI 說完成前必須拿出證據。
2. **Human Approval**：寄信、發布、開權限、外部 release 等高影響動作要先問人。

### 8.6 事故的共同根因

```text
LLM says DONE
≠
Real-world DONE
```

更完整應該是：

```text
Claim
→ Observable State
→ Evidence
→ Acceptance Criteria
→ Independent Verification
→ Approval when required
→ DONE
```

---

## 9. Judgment Externalization：把高階工程師腦內判斷變規則

Kairos 後期 Wiki 把成熟 Agent 的核心概念整理成：

- **Stop**：什麼條件算完成。
- **Ask**：什麼情況必須問人。
- **Reroute**：什麼訊號代表方向錯了，要換路徑。
- **Verify**：完成前必須提供什麼證據。

這對 AERIS 特別重要，因為聲學工程最有價值的知識往往不是公式本身，而是：

- 哪個測試方法適合哪個 DUT。
- 什麼 anomaly 是 setup 問題、什麼是 DUT 問題。
- 什麼條件下數據不可用。
- 何時該重測。
- 何時需要校正。
- 何時需要第二種量測方法交叉驗證。
- 哪些結果可以自動判斷，哪些一定要 senior engineer review。

AERIS 的護城河，應該就是把這些「判斷力」結構化。

---

## 10. Notion / n8n / Agent 的分工原則

作者的實戰分工方向值得直接吸收：

```text
Deterministic work
→ deterministic executor / workflow

Semantic / engineering judgment
→ Agent

Irreversible / high-risk action
→ Human Gate
```

AERIS 不應讓 LLM 決定所有事情。

例如：

### 應 deterministic

- FFT / filter / unit conversion。
- 檔案 checksum。
- schema validation。
- Requirement numerical comparison。
- schedule / backup / retry。
- instrument command sequence（通過安全 gate 後）。

### 應由 Agent 判斷

- anomaly root cause hypothesis。
- 應載入哪個聲學 Skill。
- Requirement / Method 是否語義上衝突。
- 報告的工程解釋與例外說明。

### 必須 Human Gate

- 可能傷害 DUT 的高功率測試。
- 正式 Pass / Fail release。
- 對客戶的正式規格承諾。
- destructive firmware / config change。

---

## 11. Dashboard / Observability

Kairos 的 LifeOS Dashboard 是很好的 UI / operation surface 參考，但 AERIS 不應把 Dashboard 當成 truth source。

### 11.1 AERIS 應看的 Dashboard 資訊

```text
PROJECT STATUS
REQUIREMENT STATUS
RUN STATUS
SKILL VERSION
METHOD VERSION
INSTRUMENT / CALIBRATION STATUS
EVIDENCE COMPLETENESS
VERIFICATION STATUS
APPROVAL STATUS
REPRODUCTION STATUS
FAILED / STALE / BLOCKED JOBS
```

### 11.2 Observability 三種信號

建議底層採 vendor-neutral observability：

```text
TRACE
Project → Workflow → Skill → Tool Call → Verification → Approval

METRIC
success_rate
evidence_completeness
verification_failure_rate
job_lag
data_freshness
reproduction_success
model_cost
human_escalation_rate

LOG
who / what / when / input / action / output / evidence / decision
```

可考慮 OpenTelemetry 作為 traces / metrics / logs 的底層 instrumentation。

---

## 12. AERIS 應吸收 vs 不應照搬

### 12.1 高度值得吸收

| Kairos 模式 | AERIS 採用方式 |
|---|---|
| Local-first knowledge | 規則、Skills、Memory、Methods、Evidence 優先本機持有 |
| Model portability | Claude / Codex / Local Model 只做 adapter |
| Core Rules SSOT | Constitution + Core Rules 單一真實來源 |
| Hierarchical Memory | Hot Context / Structured Knowledge / History 分層 |
| Skill modularization | 每個聲學方法做成 versioned skill package |
| Skill eval | Golden / regression / negative / safety tests |
| Deterministic + Agent 分工 | 固定流程不浪費 LLM token |
| Workflow hooks | session / job lifecycle 自動化 |
| Watchdog | critical job heartbeat / freshness monitoring |
| Evidence-before-Done | 沒 evidence 不進 VERIFIED |
| Human Approval | 高風險與 external release 必須人工批准 |
| Judgment Externalization | Stop / Ask / Reroute / Verify 工程化 |

### 12.2 不應直接照搬

1. **不要只追求更多 Skills / Agents。**
   - AERIS 應先建立 Verification / Evidence / Reproduction，再擴張 Skill 數量。

2. **不要把個人助理的 Bypass 權限直接搬進工程系統。**
   - 聲學儀器、DUT、firmware、正式報告的風險高很多。

3. **不要把 Memory 當正式實驗紀錄。**
   - Memory 可重寫；Evidence 不可。

4. **不要把 Agent 自評當唯一驗收。**
   - 必須有 deterministic validator + independent review。

5. **不要把 Dashboard 綠燈當工程完成。**
   - 每個狀態必須能下鑽到 artifact / hash / log / validation result。

6. **不要綁 Claude 或 Codex。**
   - AERIS 的永久資產是 Harness 與 Domain Knowledge，不是模型品牌。

---

## 13. AERIS vNext Target Architecture

```text
Human Engineering Authority
        ↓
AERIS CLI / IDE / Dashboard / Chat
        ↓
AERIS Orchestrator
        ├─ Constitution / Core Rules SSOT
        ├─ Standards Registry
        ├─ Versioned Acoustic Skills
        ├─ Engineering Memory
        └─ Workflow State Machine
        ↓
Model Router
        ├─ Claude
        ├─ Codex
        └─ Local / Future Models
        ↓
Typed Tool Adapters
        ├─ Python / MATLAB
        ├─ APx / Klippel / Measurement HW
        ├─ COMSOL / Simulation
        └─ Raw / Reference Data
        ↓
Execution Run
        ↓
Evidence Layer
        ↓
G0 Contract Verification
        ↓
G1 Numerical Verification
        ↓
G2 Domain / Physics Verification
        ↓
G3 Golden / Regression Verification
        ↓
G4 Independent Reviewer
        ↓
G5 Human Approval when required
        ↓
Approved Engineering Artifact
        ↓
Reproduction Runner
```

---

## 14. Evidence Layer：AERIS 與一般 AI Agent 最大差異

建議每次正式 run 建立：

```text
evidence/<run_id>/
├── run_manifest.json
├── requirement_snapshot.yaml
├── method_snapshot.yaml
├── input_manifest.json
├── checksums.sha256
├── raw/
├── processed/
├── results.parquet
├── plots/
├── execution.log
├── validation.json
├── environment.lock
├── standards.json
├── reviewer.json
└── approval.json
```

### 14.1 建議 `run_manifest.json` 最小欄位

```json
{
  "run_id": "AERIS-2026-000184",
  "project_id": "PROJECT-X",
  "requirement_id": "REQ-FR-003",
  "skill": {
    "id": "frequency-response-analysis",
    "version": "1.4.2"
  },
  "method": {
    "id": "FR-METHOD-002",
    "version": "3.1"
  },
  "inputs": [
    {
      "artifact_id": "raw_measurement_001",
      "sha256": "...",
      "units": "Pa"
    }
  ],
  "verification": {
    "deterministic": "PASS",
    "domain": "PASS",
    "regression": "PASS",
    "independent_review": "PENDING"
  }
}
```

---

## 15. Memory / Evidence / Audit / Provenance 必須分家

```text
Memory
= 我們從工作中學到了什麼

Evidence
= 這一次工程結果究竟發生了什麼

Audit
= 誰在什麼時間做了什麼

Provenance
= 結果由哪些資料、方法、工具、版本推導而來
```

這四個概念如果全部塞進「AI Memory」，未來將很難做正式 traceability。

---

## 16. AERIS 建議狀態機

正式工程 Run 不應只有 `TODO / DOING / DONE`。

建議：

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

錯誤狀態至少：

```text
FAILED_EXECUTION
FAILED_EVIDENCE
FAILED_VERIFICATION
REJECTED
STALE
BLOCKED
CANCELLED
```

**硬規則：禁止 `EXECUTED → DONE`。**

---

## 17. Verification Gate 建議

| Gate | 驗證內容 | 執行方式 | Fail |
|---|---|---|---|
| G0 Contract | schema、required fields、unit、hash、file existence | deterministic | block |
| G1 Numerical | unit test、NaN/Inf、range、dimension | deterministic | block |
| G2 Domain | 聲學 / 物理 sanity、calibration、method precondition | deterministic + domain rules | block |
| G3 Regression | Golden Data、approved baseline、negative case | deterministic | block |
| G4 Independent Review | requirement interpretation、method suitability、exception | Reviewer Agent | return |
| G5 Approval | 高風險執行 / 正式 release | Human | approve / reject |

**G0–G3 不應由 LLM「感覺」決定。**

---

## 18. Risk Policy 建議

| Risk Tier | 例子 | Agent Authority | Gate |
|---|---|---|---|
| R0 Read-only | 查資料、讀結果、搜尋標準 | Auto | logging |
| R1 Reversible | 建 branch、改分析 script、draft report | Auto-with-tests | Git diff + CI |
| R2 Controlled Execution | 執行量測、改 instrument config、寫 project DB | Limited | Preconditions + confirm |
| R3 High-impact | 高 SPL / 高功率、可能傷 DUT、destructive change | No autonomous | Explicit Human Approval |
| R4 External Release | 客戶報告、正式 Pass/Fail、對外規格承諾 | No autonomous release | Independent Review + Human signature |

---

## 19. Standards / Engineering Baseline

AERIS 是聲學工程系統，不能只吸收 Agent patterns，還要加工程標準層。

建議建立 versioned Standards Registry，至少可映射：

- IEC 60268-21：electro-acoustical transducers / sound systems acoustical output measurement。
- IEC 60268-23：TV、monitor with built-in loudspeakers 等設備 acoustical measurement。
- AES75：loudspeaker maximum linear acoustic output。
- AES69 / SOFA：spatial acoustic data exchange。
- ISO/IEC 17025 思維：measurement competence、impartiality、consistent operation、traceability。

**標準版本不得寫死在 Skill prose；必須以 registry + edition/version 管理。**

---

## 20. AERIS 建議 Repo 結構

```text
aeris/
├── AGENTS.md
├── CLAUDE.md
├── core/
│   ├── CONSTITUTION.md
│   ├── CORE_RULES.md
│   ├── RISK_POLICY.yaml
│   └── APPROVAL_MATRIX.yaml
├── schemas/
│   ├── run.schema.json
│   ├── evidence.schema.json
│   ├── artifact.schema.json
│   ├── measurement.schema.json
│   └── verification.schema.json
├── standards/
├── methods/
├── skills/
├── workflows/
├── adapters/
├── memory/
├── tests/
│   ├── unit/
│   ├── golden/
│   ├── regression/
│   ├── negative/
│   └── safety/
├── evidence/
└── audit/
```

`CLAUDE.md` / `AGENTS.md` 應保持薄；真正規則走 shared SSOT。

---

## 21. P0 / P1 / P2 優先級

### P0 — Trustworthy Core

優先完成：

- Constitution
- Core Rules SSOT
- Skill Spec v1
- Evidence Schema
- Run Manifest
- Risk Matrix
- Verification Gate v1
- 3 個端到端 acoustic pilot Skills
- Golden Dataset

建議 3 個 Pilot：

1. Measurement Import / Validation
2. Frequency Response Analysis
3. Comparison / Requirement Verification

目的是一次打通：

```text
raw data
→ schema
→ unit
→ calibration metadata
→ processing
→ plot
→ metric
→ requirement
→ evidence
→ reviewer
→ report
```

### P1 — Reliable Execution Platform

- Orchestrator
- Model Adapters
- Workflow State Machine
- Tool Adapter SDK
- Observability
- Health Monitor
- Approval Service
- Reproduction Runner
- 30–50 eval cases

### P2 — Scale & Intelligence

- Engineering Dashboard
- Skill Registry
- Standards Registry
- Advanced Memory Retrieval
- 10–15 核心聲學 Skills
- Reviewer Pool
- Trend / Regression Analytics

---

## 22. KPI / SLO 建議

> 以下是 AERIS 建議目標，不是 IEC / ISO 強制門檻。

| 指標 | 建議目標 |
|---|---:|
| False-Done Count | **0** |
| Unauthorized High-Risk Action | **0** |
| Tier-A Evidence Completeness | **100%** |
| Input Artifact Hash Coverage | **100%** |
| Method Version Coverage | **100%** |
| Tool Version Coverage（Tier-A） | **100%** |
| Standards Edition Traceability（formal run） | **100%** |
| Calibration Validity Check（applicable run） | **100%** |
| Safety Invariants | **100% PASS** |
| Scheduled Critical Job Heartbeat | **100%** |
| Tier-A Reproduction Success | **100%** |
| Reviewer Independence（Tier-A） | **100%** |
| Privileged Action Audit Coverage | **100%** |

---

## 23. 最終架構原則

### 原則 1：模型可替換

```text
Claude / Codex / Local Model
= Compute Runtime
```

不是 AERIS 的身份。

### 原則 2：Harness 才是永久資產

```text
AERIS Permanent Assets
├── Engineering Constitution
├── Core Rules SSOT
├── Standards Registry
├── Versioned Skills
├── Methods
├── Engineering Memory
├── Requirement Graph
├── Raw Data & Provenance
├── Tool Adapters
├── Workflow State Machine
├── Evidence Bundles
├── Golden Datasets
├── Verification Rubrics
├── Audit History
└── Reproduction Manifests
```

### 原則 3：完成必須可證明

```text
Execution ≠ Completion
```

### 原則 4：判斷力必須外化

讓未參與原始討論的工程師 / Agent，也能根據條件、反例、驗收清單做出一致判斷。

### 原則 5：AERIS 要比 Kairos 多一層「工程真實性」

Kairos 主要解決：

```text
如何讓 AI 長期像一個人工作
```

AERIS 還必須解決：

```text
如何證明工程結果是對的、可追溯、可重現、可審核
```

---

## 24. 建議直接寫進 AERIS Constitution 的硬規則

```text
1. No Evidence, No Done.
2. No Verification, No Release.
3. Memory is not Evidence.
4. Dashboard is not Truth.
5. Model is Replaceable.
6. Reviewer is a Role, not a Brand.
7. High-Risk Action Requires Explicit Authority.
8. Deterministic Work Must Prefer Deterministic Execution.
9. Every Formal Result Must Have Provenance.
10. Every Tier-A Result Must Be Reproducible.
```

---

## 25. Source Registry

### Kairos / LifeOS 第一方資料

1. Kairos Dashboard  
   https://os.lifehacker.tw/

2. Kairos / 雷小蒙 AI 分身 Wiki  
   https://wiki.lifehacker.tw/projects/Kairos%E9%9B%B7%E5%B0%8F%E8%92%99AI%E5%88%86%E8%BA%AB

3. 21 天，我用 Claude Code 打造了一整套 AI 分身助理記錄  
   https://raymondhouch.com/lifehacker/digital-workflow/21-days-claude-code-ai-agent/

4. AI Agent 搬家教學：Claude Code 轉 Codex？AGENTS.md、CLAUDE.md 與記憶系統設計  
   https://raymondhouch.com/lifehacker/digital-workflow/claude-code-codex-migration/

5. AI Agent 7 層 Harness  
   https://raymondhouch.com/lifehacker/digital-workflow/ai-agent-7-layer-architecture/

6. Kairos W10–12 工作紀錄（2026/03/08–03/19）  
   https://os.lifehacker.tw/posts/2026-03-20-ai-work-log-03

7. Kairos W17–19 工作紀錄（2026/04/22–05/08）  
   https://os.lifehacker.tw/posts/2026-05-09-ai-work-log-08

8. Kairos W22–25 工作紀錄（2026/05/27–06/15）  
   https://os.lifehacker.tw/posts/2026-06-18-ai-work-log-10

9. Kairos W26 工作紀錄（2026/06/16–06/26）  
   https://os.lifehacker.tw/posts/2026-06-26-ai-work-log-11

10. Kairos W27–32 工作紀錄（2026/06/29–08/05）  
    https://os.lifehacker.tw/posts/2026-08-07-ai-work-log-12

11. `speak-human-tw` 公開 Skill repo  
    https://github.com/Raymondhou0917/speak-human-tw

### 工程與標準參考

12. ISO/IEC 17025  
    https://www.iso.org/ISO-IEC-17025-testing-and-calibration-laboratories.html

13. IEC 60268-21  
    https://webstore.iec.ch/en/publication/28687

14. IEC 60268-23  
    https://webstore.iec.ch/en/publication/66651

15. AES75  
    https://aes.org/standards/aes75/

16. AES69 / SOFA  
    https://www.sofaconventions.org/mediawiki/index.php/SOFA_%28Spatially_Oriented_Format_for_Acoustics%29

17. OpenTelemetry  
    https://opentelemetry.io/docs/what-is-opentelemetry/

18. JSON Schema  
    https://json-schema.org/specification

---

## 26. Final Decision for AERIS

AERIS 不應複製 Kairos 的外觀；應吸收 Kairos 經六個月真實使用、失敗、修正後證明有價值的 Harness pattern，然後把它升級成 **Engineering Verification Architecture**。

最保守、風險報酬比最高的順序是：

```text
先做可信
→ 再做可靠
→ 最後做規模
```

也就是：

```text
P0 Trustworthy Core
→ P1 Reliable Execution
→ P2 Scale & Intelligence
```

AERIS 真正的長期競爭優勢，不應是「今天接了哪個最強模型」，而應是：

> **模型可換、工具可換、工程師可換；但 AERIS 累積下來的工程知識、方法、證據、驗證標準與可重現性不會消失。**

這才是 Acoustic Engineering OS，而不是另一個 AI Assistant。
