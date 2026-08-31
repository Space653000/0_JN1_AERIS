# AERIS Research Index

**Repository:** `Space653000/0_JN1_AERIS`  
**Current UI baseline:** **AERIS UI v0.4 — Kairos User-Screenshot Calibration**  
**Updated:** 2026-09-01

此資料夾區分「研究事實」「AERIS 架構決策」「未來 Target」，避免後續 AI 把推論當成已完成實作。

## Canonical reading order

1. [`AERIS_MASTER_RESEARCH_ARCHITECTURE_BASELINE_20260831.md`](AERIS_MASTER_RESEARCH_ARCHITECTURE_BASELINE_20260831.md)  
   AERIS 100-seat Acoustic Engineering Organization、Speaker / Microphone × 六工程領域、Evidence / Verification / Reproducibility、Risk / Standards / Tool Bus。

2. [`2026-08-31_Kairos_LifeOS_AERIS_Deep_Research.md`](2026-08-31_Kairos_LifeOS_AERIS_Deep_Research.md)  
   Kairos / LifeOS Agent Harness、Rules / Skills / Memory / Workflow、portable model runtime、事故與 Evidence-before-Done lessons。

3. [`AERIS_RESEARCH_DATA_INDEX_20260831.md`](AERIS_RESEARCH_DATA_INDEX_20260831.md)  
   SOURCE-FACT / SYNTHESIS / AERIS-DECISION / TARGET / VERIFY-LATER 的研究資料索引。

4. [`AERIS_WEB_UI_CONTROL_PLANE_BASELINE_20260831.md`](AERIS_WEB_UI_CONTROL_PLANE_BASELINE_20260831.md)  
   Dashboard / Workspace / Services 三個 canonical web entrances 與 backend five-plane control surface。

5. [`2026-09-01_Kairos_Dark_Light_UX_UI_Research.md`](2026-09-01_Kairos_Dark_Light_UX_UI_Research.md)  
   Kairos 第一方 Dashboard、Light/Dark、Collapse、Progressive Disclosure 的前一版 UI/UX 深度研究。

6. [`2026-09-01_Kairos_User_Screenshot_UI_Calibration_v0.4.md`](2026-09-01_Kairos_User_Screenshot_UI_Calibration_v0.4.md)  
   **目前最新視覺規格。** 依 Human Chief Engineer 直接操作 `os.lifehacker.tw` 時提供的 Light / Dark 實際截圖重新校準：228px sidebar、低對比灰階 canvas、12px card radius、幾乎無陰影、8–13px compact UI typography、monochrome icons、soft-teal active state、Dark charcoal hierarchy，以及 Identity-first dashboard rhythm。

## Current web entrances

- Dashboard: `https://space653000.github.io/0_JN1_AERIS/`
- Workspace: `https://space653000.github.io/0_JN1_AERIS/workspace.html`
- Services: `https://space653000.github.io/0_JN1_AERIS/services.html`

> GitHub repository 中 HTML / CSS / JS 存在，不等於 GitHub Pages deployment 已被外部驗證。公開網址必須另外以 HTTP / Pages deployment evidence 驗收。

## UI truth rule

```text
Real execution / data
→ Evidence
→ Verification
→ Telemetry / State Store
→ Dashboard Projection
```

禁止：

```text
Pretty UI
→ therefore system is healthy
```

## Current visual rule

```text
Kairos Personal OS restraint
×
AERIS Acoustic Engineering evidence rigor
```

UI regressions include, unless explicitly approved by the Human:

- heavy shadows;
- oversized round cards;
- giant SaaS KPI typography;
- emoji-heavy navigation;
- high-saturation teal used as large page surfaces;
- pure-black / neon cyberpunk Dark mode;
- dashboard-first analytics wall before identity/context;
- remote visual redesign that ignores the v0.4 screenshot calibration.
