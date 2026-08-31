# Kairos（雷小蒙）Light / Dark UX & UI 深度研究 → AERIS UI v0.3 Baseline

**Research date:** 2026-09-01 (Asia/Taipei)  
**Target:** `os.lifehacker.tw` / Kairos（雷小蒙）公開 Dashboard、AI Expo 第一方展示、Skills Dashboard 案例  
**Repository:** `Space653000/0_JN1_AERIS`  
**Implementation status:** AERIS UI v0.3 — Kairos Interaction Baseline  

---

# 0. Executive Summary

這次研究不只抽象談「淺色、深色、Teal」，而是把 Kairos 公開 Dashboard 拆成真正的 UX 元件與資訊節奏。

核心結論：

> **Kairos 是 Calm Personal OS，而不是 Enterprise Analytics Dashboard。**

它的辨識度來自：

```text
窄型 persistent sidebar
→ 小型同步 / uptime context
→ Identity-first hero
→ compact capability cards
→ narrative explanation
→ pastel tags
→ 4-card summary
→ chapter-based drill-down
```

而不是：

```text
巨大 KPI
+ 大量圖表
+ 厚重陰影
+ 寬 sidebar
+ 高彩度 cyberpunk
```

因此 AERIS v0.3 將三個頁面統一成同一個 Kairos-inspired shell：

- Dashboard：Who / What / Current Engineering System
- Workspace：What do I want AERIS to engineer?
- Services：Can the Harness / Trust / Operations prove its state?

AERIS 仍然保留自己的工程差異化：

> **Kairos UX × Acoustic Engineering Evidence / Verification / Authority.**

---

# 1. Source / Evidence Boundary

## 1.1 第一方可直接觀察資料

### A. AI Expo — Kairos Dashboard 實際畫面

第一方 AI Expo 頁面：

`https://expo.lifehacker.tw/`

Dashboard 圖片資產：

`https://expo.lifehacker.tw/assets/AI%20Expo/v25.avif`

AI Expo 對畫面的第一方描述：

> 雷小蒙的系統主頁。專案進度、技能模組與每日自動化任務，集中在單一介面。

這張圖是目前最重要的 UI source fact。

### B. Skills Dashboard UX 案例

`https://works.lifehacker.tw/works/skills-dashboard.html`

公開案例明確記載：

- 40 Skills / 14 categories
- 首屏先看 summary metrics
- 關鍵字搜尋
- category filter
- drag ordering
- compact cards
- 點卡片才看完整說明
- 分類優先於最近更新排序

這提供 Kairos / LifeOS 生態系很清楚的 Progressive Disclosure pattern。

### C. os.lifehacker.tw

`https://os.lifehacker.tw/`

公開 crawler 目前只能直接讀到：

```text
啟動 Kairos 中...
```

所以不可依 crawler 結果聲稱知道 frontend framework、CSS source 或完整 runtime implementation。

---

# 2. Kairos Dashboard — Direct Visual Observation

以下只記錄第一方 Dashboard 截圖可以直接看到的視覺結構。

## 2.1 Sidebar 比一般 SaaS 更窄

可觀察到：

- 左側欄是窄型 persistent rail
- logo 約 30 px 級，而不是大型 brand block
- `KAIROS` 是小型 uppercase brand
- 下一行是更小的中文名稱
- sidebar 內資訊密度高，但字級非常克制

AERIS 決策：

```text
expanded sidebar ≈ 176 px
collapsed sidebar ≈ 64 px
```

目的：把畫面空間留給工程內容，不讓 navigation 成為主角。

## 2.2 Uptime / sync 是 secondary context

Kairos sidebar brand 下方可見小型 uptime 資訊；主內容 header 下方有 synced context。

這個 UX 的重點不是數值本身，而是：

> **Operational context 要看得到，但不搶內容注意力。**

AERIS 對應：

- 靜態 prototype 顯示 `UI Shell · Target Baseline`
- 未接 live telemetry 前，不假裝 uptime / synced / healthy 是真實資料
- 未來接 backend 後才可顯示 live `last_sync`, `heartbeat`, `artifact_freshness`

## 2.3 Navigation：一個主標籤 + 一個更小的副標籤

Kairos sidebar 可見：

- Kairos
- Activity
- Timeline
- Skills
- Projects
- Health
- Inbox

每個 navigation item 有 icon、主要文字與更小的 secondary label。

AERIS v0.3 對應：

```text
Dashboard   / 系統首頁
Workspace   / 工程工作台
Activity    / 工程流程
Roles       / 100 席能力庫
Research    / 研究與標準
Services    / 後端服務
Health      / Trust / Evidence
```

## 2.4 Active navigation 不是高飽和色塊

Kairos active item 使用的是：

- 極淡 cyan / teal surface
- 左側細 accent
- 文字與 icon 才提高 teal contrast

這比整塊 teal button 更安靜。

AERIS v0.3 已採：

```text
pale-teal gradient background
+ 2 px left active bar
+ teal text/icon
```

## 2.5 Sidebar bottom：Dark Mode + Collapse

第一方截圖可直接看到側欄最底部：

```text
🌙 Dark Mode
← Collapse
```

這是一個很重要的資訊架構訊號：

> Theme / layout control 是 persistent utility，但屬於低優先層，不應放在 topbar 搶工程內容。

AERIS v0.3 已改成同樣的 UX 位置：

- Light 狀態顯示 `☾ Dark Mode`
- Dark 狀態顯示 `☀ Light Mode`
- Sidebar `Collapse / Expand`
- Theme 與 sidebar state 都跨頁 persistence

---

# 3. Main Header Grammar

Kairos 主內容頂部很克制：

```text
◉ Kairos
雷小蒙 · synced ...
                         [刷新]
```

不是巨大 page title。

AERIS v0.3 對應：

```text
◉ AERIS
Acoustic Engineering & Research Intelligence System · static snapshot
                                                  [刷新]
```

字級策略：

- top title 約 14 px 級
- secondary context 約 8 px 級
- refresh 是小型 outline control

---

# 4. Identity-first Hero

Kairos Dashboard 最大的視覺 anchor 不是 KPI，而是「我是誰」。

第一方截圖可以直接看到：

1. `Kairos Online · ONLINE`
2. teal square avatar
3. `我是雷小蒙`
4. 一排能力定位文字
5. 多個 compact system cards
6. narrative paragraphs
7. quote / statement box
8. pastel tags

這是非常典型的 **identity → capability → context → detail**。

AERIS v0.3 對應：

```text
AERIS Shell · TARGET BASELINE

[A]
我是 AERIS
AI 聲學工程團隊 ｜ 研發設計 ｜ 量測驗證 ｜ 模擬調校 ｜ 演算法 ｜ 工廠品質

AI Runtime     Replaceable Models
Role Library   100 Virtual Seats
Knowledge      3-layer Context
Verification   G0 → G5
Dynamic Pod    5–15 Specialists
```

重要差異：

Kairos 可以顯示 `ONLINE`，但 AERIS 目前沒有 live backend，所以只顯示 `TARGET BASELINE`。

這是 Evidence-before-Done 在 UI 上的直接體現。

---

# 5. Hero Background

Kairos Identity card 並不是單一純色。

可觀察特徵：

- 很淡的 teal / warm / lavender gradient
- 低強度 texture / particle feeling
- 1 px soft border
- rounded corner
- shadow 幾乎不可察覺

AERIS v0.3 已改成：

```text
soft teal → warm white → lavender gradient
+ sparse 1 px radial particles
+ very low shadow
+ 14 px radius
```

目標不是 pixel clone，而是重現「calm identity surface」。

---

# 6. Typography / Density

這次最需要修正的地方是：舊 AERIS 字太大、card 太大、sidebar 太寬。

Kairos 截圖呈現的是高資訊密度，但不是擁擠。

AERIS v0.3 baseline：

| Element | Approx. UI scale |
|---|---:|
| Brand | 11 px |
| Sidebar primary | 9 px |
| Sidebar secondary | 7 px |
| Top title | 14 px |
| Identity title | 22 px |
| Body explanation | 9 px |
| Panel title | 10 px |
| Table / compact data | 7–8 px |
| Tag / state chip | 7 px |

原則：

> **小字不是目的；高 signal-to-noise 才是目的。**

工程詳細資料仍必須在可讀性與 accessibility 下調整，不可為了仿 Kairos 犧牲測試報告的可讀性。

---

# 7. Card Geometry

Kairos 公開畫面中的卡片不是大型 Material Design cards。

AERIS v0.3：

```text
small cards: 8–9 px radius
main panels: 12 px radius
identity hero: 14 px radius
border: 1 px very low contrast
shadow: minimal
```

舊版 AERIS 的 18–22 px radius 與較大陰影已降低。

---

# 8. Four-card Summary Rhythm

Kairos Identity card 下方緊接一排 4 個 summary cards。

這種節奏非常適合 Dashboard：

```text
Identity / explanation
↓
4 fast metrics
↓
Chapter detail
```

AERIS Dashboard 現在使用：

- 100 Virtual Roles
- 24 Product Chiefs
- 2 × 6 core matrix
- False-Done target = 0

這些是 architecture facts / targets，不冒充 runtime telemetry。

---

# 9. Chapter-based Progressive Disclosure

第一方截圖在 summary cards 下方開始出現：

```text
CHAPTER 01
為什麼叫 Kairos？
```

代表 Dashboard 不只是一組 tile，而是帶有 narrative / chapter structure。

AERIS 對應：

```text
CHAPTER 01
AERIS 怎麼把一個工程問題變成可驗證結論？
```

Services：

```text
CHAPTER 01 Five-Plane Architecture
CHAPTER 02 Verification G0–G5
```

Workspace：

```text
TASK INTAKE
CHAPTER 01 Engineering Contract
```

這讓複雜工程系統仍然可以用「先理解，再深入」的方式閱讀。

---

# 10. Skills Dashboard Pattern → AERIS Role / Skill / Standards UX

第一方案例提供完整 UX：

```text
Summary
→ Search
→ Filter
→ Compact Card
→ Detail on demand
```

AERIS 直接採用：

## Role Library

```text
100 roles
→ keyword search
→ group filter
→ compact role cards
→ future role contract drawer
```

## Skills

```text
skill count / failing evals
→ domain filter
→ compact skill card
→ SKILL.md / method / test / golden detail
```

## Standards

```text
current / stale / withdrawn
→ search
→ product / body / lifecycle filter
→ standard summary
→ edition / applicability / method mapping
```

因此 Dashboard 不應變成資料庫全部攤開。

---

# 11. Light Mode — Observable Direction + AERIS Tokens

Light Mode 的視覺方向：

```text
near-white canvas
+ white cards
+ extremely subtle gray dividers
+ teal identity / active state
+ pastel semantic surfaces
```

AERIS v0.3 baseline：

| Token | Value |
|---|---|
| Canvas | `#FBFBF9` |
| Sidebar | `#FAFAF8` |
| Panel | `#FFFFFF` |
| Text | `#202524` |
| Soft text | `#5F6967` |
| Border | `#ECEEEB` |
| Teal | `#43B8B2` |
| Teal soft | `#EDF9F7` |
| Green soft | `#EFF8F1` |
| Amber soft | `#FFF8E9` |
| Rose soft | `#FFF1F4` |
| Purple soft | `#F5F1FF` |

這些是 **AERIS token decisions**，不是宣稱 Kairos exact CSS。

---

# 12. Dark Mode — Evidence Boundary

第一方公開截圖明確證明 Kairos 有 `Dark Mode` control，但目前沒有取得與 Light screenshot 同等可信度、可引用的完整 Dark screenshot / CSS source。

因此不能把任何 dark hex 宣稱為 Kairos original token。

AERIS 原則：

> **Dark 是 Light semantic hierarchy 的對稱映射，不變成另一套 cyberpunk UI。**

AERIS v0.3：

| Token | Value |
|---|---|
| Canvas | `#0E1110` |
| Sidebar | `#0C0F0E` |
| Panel | `#141816` |
| Control | `#171C1A` |
| Text | `#E8ECEA` |
| Soft text | `#B7C0BD` |
| Border | `#252D2A` |
| Teal | `#64D1C8` |
| Teal soft | `#16302D` |
| Green soft | `#192A1F` |
| Amber soft | `#332817` |
| Rose soft | `#342026` |
| Purple soft | `#28233A` |

禁止：

- pure black everywhere
- neon cyan / neon green flood
- heavy glow
- glassmorphism everywhere
- Dark Mode 改變資訊架構

---

# 13. Theme Interaction Contract — v0.3

前一版使用三段式：

```text
System / Light / Dark
```

深入研究實際 Kairos sidebar 後，v0.3 改成更接近其 interaction pattern：

```text
☾ Dark Mode
← Collapse
```

在 Dark Mode：

```text
☀ Light Mode
← Collapse
```

技術行為：

1. 第一次沒有 explicit preference 時，跟隨 OS `prefers-color-scheme`。
2. 使用者按 theme toggle 後，寫入 `localStorage`。
3. 三頁共用同一 preference。
4. `Collapse / Expand` 也寫入 `localStorage`。
5. Collapse 後只保留 logo / icons / utility icons。
6. mobile 不強迫 desktop collapse model。

Storage：

```text
aeris-theme-preference
aeris-sidebar-state
```

---

# 14. Semantic Color Contract

| Family | Meaning |
|---|---|
| Teal | identity / active / primary context |
| Green | verified / deterministic pass |
| Amber | attention / reviewer / pending |
| Rose | risk / failed / unverified / Human gate |
| Purple | meta / routing / model-neutral / blocked context |
| Blue | knowledge / data / informational subsystem |
| Neutral | inactive / unknown / target-only |

Hard rule：

> **Color is redundant encoding, never the only encoding.**

畫面仍必須寫 `FAILED`, `UNKNOWN`, `VERIFIED`, `DESIGN TARGET`。

---

# 15. Dashboard UX v0.3

Canonical hierarchy：

```text
Compact topbar
↓
Identity hero
  ├─ target status
  ├─ avatar + identity
  ├─ 5 capability cards
  ├─ explanation
  ├─ statement box
  └─ tags
↓
4 summary cards
↓
CHAPTER 01 Autonomous R&D loop
↓
Temporary Pod + Engineering Trust
↓
Role Library search/filter
↓
Research / Knowledge modules
```

這比舊版更接近 Kairos 的閱讀節奏。

---

# 16. Workspace UX v0.3

Workspace 不複製 Dashboard 內容，而是沿用 shell / density / visual grammar。

Canonical flow：

```text
Human intent
↓
Product / Transducer / Lifecycle / Risk
↓
Objective / Constraints
↓
Evidence + Standards strategy
↓
Role Router
↓
Temporary Pod
↓
STOP / ASK / REROUTE / VERIFY
```

使用者不需要選 100 個 Agent。

---

# 17. Services UX v0.3

Services 保留相同 shell，但允許較高資訊密度。

Canonical flow：

```text
Harness identity
↓
5 plane quick summary
↓
Five-Plane Architecture
↓
Service Registry
↓
Verification G0–G5
↓
Risk / Authority
↓
Evidence Bundle
↓
Health semantics
```

最重要 UX guard：

> `DESIGN TARGET` 絕不等於 `HEALTHY`。

---

# 18. Responsive / Accessibility

Desktop：

- expanded sidebar 176 px
- optional 64 px collapsed rail
- main content max-width 1480 px

Narrow desktop：

- sidebar 150 px
- multi-column cards reduce columns

Mobile：

- navigation becomes horizontal compact strip
- desktop collapse utilities hidden
- primary page content becomes one-column where needed

Accessibility：

- keyboard focus ring
- theme / collapse are buttons, not clickable divs
- `aria-label`
- theme color not sole state signal
- `prefers-reduced-motion`
- input focus visible

---

# 19. What AERIS deliberately does NOT copy

AERIS 不複製：

- Kairos proprietary text / branding
- unknown frontend framework
- unknown CSS source
- exact private dashboard data
- any unverified dark-mode source token

AERIS 吸收的是：

```text
visual hierarchy
interaction priority
information density
progressive disclosure
persistent utility placement
identity-first control surface
```

---

# 20. Source Registry

Primary first-party sources：

1. `https://os.lifehacker.tw/`
2. `https://expo.lifehacker.tw/`
3. `https://expo.lifehacker.tw/assets/AI%20Expo/v25.avif`
4. `https://works.lifehacker.tw/works/skills-dashboard.html`
5. `https://os.lifehacker.tw/posts/2026-03-20-ai-work-log-03`
6. `https://os.lifehacker.tw/posts/2026-08-07-ai-work-log-12`

Relevant Kairos operations lessons：

- Dashboard consolidates projects / Skills / daily automations.
- Silent failures demonstrate why a dashboard cannot manufacture truth.
- Evidence-before-Done must override visually pleasant status states.

---

# 21. Final AERIS UI Decision

Current canonical UI version：

> **AERIS UI v0.3 — Kairos Interaction Baseline**

Formula：

> **Kairos Calm Personal OS UX × AERIS Engineering Evidence System.**

Visual target：

> **安靜、精準、小而密、容易掃描；複雜度在需要時才展開。**

Engineering target：

> **畫面可以像 Kairos 一樣輕，但每一個工程狀態必須比一般 Dashboard 更重視 Evidence、Verification、Authority 與 Reproducibility。**
