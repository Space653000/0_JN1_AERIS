# Kairos（雷小蒙）Light / Dark UX & UI 深度研究 → AERIS Theme Baseline

**Research date:** 2026-09-01 (Asia/Taipei)  
**Target:** `os.lifehacker.tw` / Kairos（雷小蒙）公開 Dashboard 與相關第一方公開展示  
**Repository:** `Space653000/0_JN1_AERIS`  
**Status:** Research + AERIS implementation baseline  

---

# 0. Executive Summary

本次研究的目標不是「抄一張 Kairos 截圖」，而是抽取雷小蒙公開 UI 中真正可移植的 UX 規則，再映射到 AERIS 的 Dashboard / Workspace / Services。

研究後的核心結論：

> **Kairos 的視覺優勢不是高密度炫技，而是 Calm Control Surface：固定側欄、Identity-first、低對比卡片、少量 pastel semantic colors、摘要先行、需要時才 drill-down。**

AERIS 應保留這個哲學，但把內容換成工程級資訊：

```text
Identity
→ North-Star KPI
→ Current Engineering State
→ Human Attention
→ Search / Filter
→ Drill-down Evidence
```

Theme 決策：

> **Light / Dark 必須是同一套資訊架構與 semantic hierarchy 的兩種觀看模式，而不是兩套不同 UI。**

AERIS 已實作：

- `System / Light / Dark` 三態切換
- 預設 `System`
- 手動選擇寫入 `localStorage`
- OS theme 變更時，System 模式即時跟隨
- Theme control 固定在側欄底部，呼應 Kairos 公開截圖的 `Dark Mode / Collapse` 低優先層級位置
- 深色模式保留 Teal identity 與 Green / Amber / Rose / Purple semantic colors
- 支援 `prefers-reduced-motion`
- 桌面 / 窄桌機 / 手機皆保留 theme control

---

# 1. Evidence Boundary：哪些是公開可證實，哪些不是

## 1.1 可直接證實

### A. Kairos 公開實際 Dashboard 截圖

第一方課程頁公開的 Kairos Dashboard 截圖可以直接觀察到：

- 左側固定 navigation rail
- 白 / 暖白 canvas
- 極淡灰 border
- Teal / aqua 作為 AI identity 主色
- 大型 soft-gradient identity card
- 多個淡色 pastel tag / chip
- 主要資訊由大標題 → 摘要 → tags → KPI cards 向下展開
- 側欄底部有 `Dark Mode`
- 側欄底部另有 `Collapse`
- 左側 navigation 至少可見 Kairos / Activity / Timeline / Skills / Projects / Health / Inbox 等分類

第一方截圖 URL：

`https://s.teachifycdn.com/image/width%3D1920%2Cquality%3D80/attachment/public_image/95279a3a-e796-4778-842a-053cc152bcf4/c4f70870-8a70-419d-93d9-b6df6cdc25f5.jpg`

來源頁：

`https://lifehacker.tw/courses/24hr-claude-code-tutorial`

### B. AI Expo 對 Dashboard 用途的第一方描述

AI Expo 2026 頁面直接描述：

> 雷小蒙的系統主頁把「專案進度、技能模組與每日自動化任務」集中在單一介面。

這確認 Dashboard 的核心目的不是裝飾，而是 **single operational overview**。

來源：

`https://expo.lifehacker.tw/`

### C. Skills Dashboard 的 UX 取捨

雷蒙作品平台的 Skills Dashboard 案例公開描述：

- 頁面頂部先顯示 Skill 總數、分類數、平均文件大小、參考文件數
- 下方再提供搜尋與分類標籤
- 卡片只顯示最重要摘要
- 點卡片後才看完整說明
- 分類優先於「最近更新」排序

這對 AERIS 非常重要，因為 100-seat Role Library / Skill Registry / Standards Registry 都會面臨同樣的資訊規模問題。

來源：

`https://works.lifehacker.tw/works/skills-dashboard.html`

## 1.2 目前不能直接證實

截至本次研究，公開索引中沒有找到與 Light 截圖同等可信度、可直接檢視的 Kairos Dark Mode 全頁實拍。

此外 `https://os.lifehacker.tw/` 對公開 crawler 目前只回傳：

```text
啟動 Kairos 中...
```

因此不能嚴謹反推：

- Kairos frontend framework
- Tailwind / React / Next / Vue 等實作
- 原始 design token
- Dark Mode 精確 hex
- theme storage implementation
- component library

**AERIS 不把推論偽裝成 source fact。**

所以本文件的 Dark token 是：

> **AERIS implementation decision inspired by the observable Kairos hierarchy, not a claim that these are Kairos original CSS values.**

---

# 2. Kairos Observable Visual Grammar

## 2.1 Canvas

Light UI 的感覺不是純白 SaaS，也不是高彩度科技風，而是：

```text
warm / neutral near-white canvas
+
white cards
+
very low-contrast dividers
```

效果：

- 長時間觀看負擔較低
- 多卡片同時出現時不會產生「表格牆」壓力
- identity color 可以很突出，但不需要大面積高飽和

## 2.2 Identity-first Hero

Kairos 首頁先回答：

> 「我是誰、現在是否在線、我有哪些核心能力？」

而不是先丟 project table。

AERIS 對應：

```text
AERIS
Acoustic Engineering OS
100-seat AI Acoustic Engineering Organization
Local-first / Model-neutral / Evidence-first
```

這是產品 identity，也是資訊架構 anchor。

## 2.3 Sidebar

可觀察原則：

- persistent desktop sidebar
- active item 用淡 teal background，不使用高飽和整塊色
- navigation 文字偏小
- icon + label
- theme / collapse 放在最底部，避免搶工程任務的主要注意力

AERIS 對應：

```text
CONTROL
Dashboard
Workspace
Services

INTELLIGENCE / TRUST / WORKFLOW
...

(bottom)
Appearance
System / Light / Dark
```

## 2.4 Cards

Kairos 的 card grammar：

- 大圓角
- 極輕陰影或幾乎無陰影
- 細 border
- 內容摘要優先
- card 間距規律
- 不用大量強烈 outline

AERIS 對應：

- KPI card = one metric + one sentence
- Role card = ID + name + group
- Service card = service + one-line purpose
- Evidence / verification detail留到下鑽頁

## 2.5 Semantic Chips

公開截圖可觀察到多種柔和色 chip。

AERIS 定義 semantic mapping：

| Color family | AERIS meaning |
|---|---|
| Teal | Identity / active / primary system context |
| Green | Verified / positive / deterministic pass |
| Amber | Attention / reviewer / pending |
| Rose | Risk / failed / unverified / Human gate |
| Purple | Meta / model-neutral / loop / blocked context |
| Neutral gray | Informational / inactive / target-only |

原則：

> **Color supplements state; color never becomes the only carrier of state.**

文字仍必須顯示 `VERIFIED`, `FAILED`, `UNKNOWN`, `DESIGN TARGET` 等。

---

# 3. UX Pattern：Summary → Search → Filter → Detail

Skills Dashboard 公開案例最值得複製的是資訊探索順序：

```text
Summary metrics
↓
Search
↓
Category filter
↓
Compact cards
↓
Detail on demand
```

這個 pattern 直接套用到 AERIS：

### Role Library

```text
100 roles
↓
Search role
↓
Filter by organization block
↓
Role card
↓
Role contract / tools / evidence / authority
```

### Skill Registry

```text
Skill count / categories / failing evals
↓
Search
↓
Domain filter
↓
Skill card
↓
SKILL.md / method / tests / golden cases
```

### Standards Registry

```text
current / stale / withdrawn count
↓
Search standard
↓
Product / body / status filter
↓
Standard card
↓
Edition / applicability / method mapping
```

**AERIS 不應把首頁做成完整工程資料庫。**

---

# 4. Light Theme — AERIS Token Baseline

Light Mode 高度貼近公開 Kairos 的可觀察視覺方向，但不是 pixel clone。

| Token | AERIS Light | Purpose |
|---|---|---|
| Canvas | `#F7F8F7` | global background |
| Sidebar | `#FBFCFB` | persistent navigation |
| Panel | `#FFFFFF` | cards / work surface |
| Main text | `#172322` | primary content |
| Soft text | `#52615F` | explanatory text |
| Accent teal | `#35B7AA` | identity / focus |
| Teal soft | `#E9F8F5` | active nav / semantic background |
| Green soft | `#EDF8F1` | positive state |
| Amber soft | `#FFF7E7` | attention state |
| Rose soft | `#FFF0F3` | risk state |
| Purple soft | `#F4F0FF` | meta state |

UI strategy：

- 大面積不使用高飽和 teal
- teal 只做 identity、active state、focus
- white card 與 near-white canvas 只用 1 px 淺 border 分層
- shadow 保持極低

---

# 5. Dark Theme — Symmetric Engineering Mapping

Dark Mode 不應變成「黑底 neon cyberpunk」。

如果 Light 是 calm productivity UI，Dark 也應是 calm engineering UI。

AERIS Dark baseline：

| Token | AERIS Dark | Purpose |
|---|---|---|
| Canvas | `#0D1211` | global background |
| Sidebar | `#0F1514` | navigation |
| Panel | `#121918` | cards |
| Control | `#151D1B` | button / input |
| Main text | `#E7EFED` | primary content |
| Soft text | `#B4C0BD` | explanatory text |
| Accent teal | `#5ED2C3` | identity / focus |
| Teal soft | `#15302C` | active / selected |
| Green soft | `#182D21` | verified |
| Amber soft | `#352A17` | attention |
| Rose soft | `#371F25` | risk |
| Purple soft | `#28223D` | meta |

Dark principles：

1. 不是 `#000000` pure black。
2. Panel 只比 canvas 亮一階，避免「浮動卡片像白色洞」。
3. Accent brightness 提高，但使用面積不增加。
4. Pastel semantic colors 改為 dark-tinted surface + brighter text。
5. Border 仍存在，以免只靠 shadow 分層。
6. Chart / measurement color 在後續 Plot Theme 必須另外定義，不直接照 UI chip 色。

---

# 6. Theme Interaction Contract

AERIS theme controls：

```text
◐ System
☀ Light
☾ Dark
```

## Default

`System`

理由：

- 不強迫使用者選擇
- Windows / macOS / mobile 已有成熟日夜偏好
- 使用者手動指定後才 override OS

## Persistence

```text
localStorage key:
aeris-theme-preference
```

Values：

```text
system
light
dark
```

## OS change behavior

若 preference = `system`：

```text
prefers-color-scheme changes
→ AERIS immediately maps to new theme
```

若 preference = `light` / `dark`：

```text
OS change
→ no override
```

這避免使用者明明選了 Dark，AERIS 卻被 OS 自行切回 Light。

---

# 7. Responsive UX

Kairos 公開截圖主要是 desktop；AERIS 需要明確定義跨裝置策略。

## Desktop > 1100 px

```text
236 px persistent sidebar
+
full labels
+
3-way theme dock at bottom
```

## Compact desktop / tablet

```text
74 px icon rail
+
labels collapse
+
theme buttons become icon-only vertical controls
```

## Mobile <= 720 px

```text
sidebar becomes horizontal top rail
+
navigation horizontally scrollable
+
theme buttons remain visible
+
content grids collapse to 1–2 columns
```

這與 Kairos 公開 `Collapse` 控制的思想一致：

> Navigation density 可以縮小，但核心入口不能消失。

---

# 8. Accessibility / Human Factors

AERIS 是長時間工程工作台，不應只追求「看起來像 Kairos」。

## Required baseline

- keyboard focus visible
- theme control uses button + `aria-pressed`
- color state also has text label
- `prefers-reduced-motion` disables nonessential motion
- form controls inherit theme
- `color-scheme` communicates current theme to browser-native controls
- mobile theme switch remains reachable

## Contrast note

AERIS theme 使用高對比 main text：

- Light `#172322` on `#F7F8F7` 約 **15.2:1**
- Dark `#E7EFED` on `#0D1211` 約 **16.2:1**

正式 release 前仍應用 axe / Lighthouse / Playwright 做完整 WCAG audit；本次不是 accessibility certification。

---

# 9. AERIS Three-Page Mapping

## Dashboard

Kairos pattern：

```text
Identity
→ summary counts
→ current capability / activity
→ searchable modules
```

AERIS：

```text
Identity Hero
→ 100 seats / 2×6 / 24 products / G0–G5
→ Autonomous R&D Loop
→ Trust KPI
→ Role Library
→ Benchmark 100
```

## Workspace

不照搬 Dashboard 卡片，而保留 Kairos 的「簡單入口、後面系統展開」哲學：

```text
Human objective
→ minimal structured inputs
→ Temporary Pod
→ Requirement / Hypothesis / Evidence
→ Workflow states
```

## Services

採同一 visual system，但資訊密度提高：

```text
Five Planes
→ service registry
→ verification
→ risk
→ evidence
→ health semantics
```

重要：Services 即使是 Dark Mode，也不得用炫目的綠燈造成 false confidence。

---

# 10. What AERIS Deliberately Does NOT Copy

不複製：

- Kairos 名稱與品牌 identity
- 未公開 source code
- 未公開 theme hex
- 未公開 framework
- 未公開 backend
- 個人生活導向的 navigation vocabulary

保留：

- calm visual hierarchy
- persistent navigation
- identity-first dashboard
- pastel semantic chips
- summary-before-detail
- search / category-first discovery
- dark-mode control in low-priority persistent area
- collapsible / responsive navigation philosophy

---

# 11. Current GitHub Implementation

Files：

```text
/index.html
/workspace.html
/services.html
/aeris.css
/aeris-theme.js
/aeris-data.js
```

Live target URLs：

```text
https://space653000.github.io/0_JN1_AERIS/
https://space653000.github.io/0_JN1_AERIS/workspace.html
https://space653000.github.io/0_JN1_AERIS/services.html
```

Theme state is shared among all three pages through the same `localStorage` key, therefore：

```text
Dashboard → choose Dark
↓
Workspace → remains Dark
↓
Services → remains Dark
```

這是「一個 OS」，不是三個彼此無關的 microsites。

---

# 12. Sources

## Primary / first-party

1. Kairos current public loader / dashboard endpoint  
   `https://os.lifehacker.tw/`

2. AI Expo 2026 — 一人公司 AI 工作術  
   `https://expo.lifehacker.tw/`

3. 雷小蒙 actual Dashboard screenshot on first-party course page  
   `https://lifehacker.tw/courses/24hr-claude-code-tutorial`

4. Actual dashboard image CDN asset  
   `https://s.teachifycdn.com/image/width%3D1920%2Cquality%3D80/attachment/public_image/95279a3a-e796-4778-842a-053cc152bcf4/c4f70870-8a70-419d-93d9-b6df6cdc25f5.jpg`

5. Skills Dashboard — summary / search / categories / cards UX case  
   `https://works.lifehacker.tw/works/skills-dashboard.html`

6. Kairos work log — Dashboard / automation operational context  
   `https://os.lifehacker.tw/posts/2026-03-20-ai-work-log-03`

7. Kairos work log — model portability / agent identity  
   `https://os.lifehacker.tw/posts/2026-06-18-ai-work-log-10`

8. Kairos work log — false-Done / long-running operational lessons  
   `https://os.lifehacker.tw/posts/2026-08-07-ai-work-log-12`

---

# 13. Final UX Decision

> **AERIS should feel like Kairos grew into an engineering operating system — not like an ERP, not like Grafana, and not like a cyberpunk AI demo.**

The visual priority is：

```text
Calm
→ Scannable
→ Searchable
→ Trustworthy
→ Drillable
```

not：

```text
More panels
→ more colors
→ more animations
→ more apparent complexity
```

Final theme principle：

> **Light for clarity, Dark for sustained focus, System for zero-friction default — same truth, same information hierarchy, same engineering state semantics.**
