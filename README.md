# 0_JN1_AERIS

**AERIS — Acoustic Engineering & Research Intelligence System**

本 repository 用於建立一套可長期保存、模型可替換、證據可追溯、工程結果可驗證的 AI 聲學工程組織系統。

## Web UI — AERIS UI v0.4

目前最新視覺 baseline：

> **Kairos Personal OS visual restraint × AERIS Acoustic Engineering evidence rigor**

2026-09-01 依 Human Chief Engineer 直接操作 `os.lifehacker.tw` 時提供的 Light / Dark 實際截圖重新校準，不再只做泛化的「Kairos-inspired」SaaS Dashboard。

三個 canonical entrances：

1. [Dashboard / Mission Control](index.html)  
   `AERIS 在線_` → Identity → 5 個 compact capability metrics → About → Engineering Overview → Engineering Flow → Temporary Pod / Trust → 100-seat Role Library。

2. [Engineering Workspace](workspace.html)  
   Human Chief Engineer 的單一工程入口；Product / Transducer / Lifecycle / Risk / Evidence → Dynamic Temporary Pod。

3. [Service Console](services.html)  
   Control / Knowledge / Execution / Trust / Operations 五個 planes；Verification G0–G5、Risk R0–R4、Evidence Bundle、Health semantics。

### v0.4 screenshot-calibrated visual contract

三頁共用：

- 約 `228px` persistent desktop sidebar；collapsed 約 `62px`
- Light：neutral gray canvas + white sidebar/cards
- Dark：layered charcoal surfaces，不使用 pure black / neon cyberpunk
- 主要卡片約 `12px` radius；controls 約 `8–9px`
- 幾乎無大型 drop shadow；以低對比 `1px` border 分層
- compact `8–13px` operational typography；Identity name 約 `22px`
- system UI fonts + monospace-like machine/status metadata
- monochrome restrained navigation symbols；不使用 emoji-heavy sidebar
- pale-teal active navigation + left `2px` accent
- Teal 只做 identity / active / focus，不做大面積背景
- sidebar bottom：`Dark Mode ↔ Light Mode`、`Collapse ↔ Expand`
- theme 與 sidebar state 透過 `localStorage` 跨頁保留
- first visit follows OS `prefers-color-scheme`
- summary-first / progressive-disclosure hierarchy
- responsive + `prefers-reduced-motion`

> **重要：**目前三頁仍是 Target-state static prototype。任何 `HEALTHY` / 完成狀態在未連接真實 telemetry、Evidence 與 Verification backend 前，都不得視為正式工程事實。

### GitHub Pages target URLs

- Dashboard: `https://space653000.github.io/0_JN1_AERIS/`
- Workspace: `https://space653000.github.io/0_JN1_AERIS/workspace.html`
- Services: `https://space653000.github.io/0_JN1_AERIS/services.html`

Repository 中檔案存在 ≠ Pages 已被外部 HTTP 驗證上線；公開部署狀態必須另外驗收。

## Research / Architecture

完整索引：[`docs/research/README.md`](docs/research/README.md)

目前主要文件：

1. [AERIS Master Research & Architecture Baseline](docs/research/AERIS_MASTER_RESEARCH_ARCHITECTURE_BASELINE_20260831.md)
2. [Kairos / LifeOS Deep Research](docs/research/2026-08-31_Kairos_LifeOS_AERIS_Deep_Research.md)
3. [AERIS Research Data Index](docs/research/AERIS_RESEARCH_DATA_INDEX_20260831.md)
4. [AERIS Web UI / Control Plane Baseline](docs/research/AERIS_WEB_UI_CONTROL_PLANE_BASELINE_20260831.md)
5. [Kairos Light / Dark UX & UI Deep Research — AERIS UI v0.3](docs/research/2026-09-01_Kairos_Dark_Light_UX_UI_Research.md)
6. [Kairos User-Screenshot UI Calibration — AERIS UI v0.4](docs/research/2026-09-01_Kairos_User_Screenshot_UI_Calibration_v0.4.md)

## Core Architecture

> **1 Human Chief Engineer + 100 Virtual Acoustic Engineering Seats + model-neutral orchestration + real engineering tools + Evidence + Independent Verification + Human Approval + Reproducibility.**

100 seats are capabilities, not 100 always-running agents. Typical active pod size is **2–8 roles**, or **5–15 roles** for complex work.

## North Star

> **AERIS is not an AI-agent demo. It is an Acoustic Engineering Organization OS whose engineering conclusions remain traceable, verifiable and reproducible even after today’s models are replaced.**