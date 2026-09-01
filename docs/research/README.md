# AERIS Research Index

**Repository:** `Space653000/0_JN1_AERIS`  
**Current UI baseline:** **AERIS UI v0.5 — Direct Kairos User-Screenshot Correction**  
**Updated:** 2026-09-01

This folder separates research facts, synthesis, AERIS decisions and future targets so later AI does not treat inference as implemented fact.

## Canonical architecture/research reading order

1. [`AERIS_MASTER_RESEARCH_ARCHITECTURE_BASELINE_20260831.md`](AERIS_MASTER_RESEARCH_ARCHITECTURE_BASELINE_20260831.md)  
   100-seat Acoustic Engineering Organization, Speaker/Microphone × engineering disciplines, Evidence / Verification / Reproducibility, Risk, Standards and Tool Bus.

2. [`2026-08-31_Kairos_LifeOS_AERIS_Deep_Research.md`](2026-08-31_Kairos_LifeOS_AERIS_Deep_Research.md)  
   Kairos/LifeOS Agent Harness, Rules/Skills/Memory/Workflow, portable model runtime and Evidence-before-Done lessons.

3. [`AERIS_RESEARCH_DATA_INDEX_20260831.md`](AERIS_RESEARCH_DATA_INDEX_20260831.md)  
   SOURCE-FACT / SYNTHESIS / AERIS-DECISION / TARGET / VERIFY-LATER index.

4. [`AERIS_WEB_UI_CONTROL_PLANE_BASELINE_20260831.md`](AERIS_WEB_UI_CONTROL_PLANE_BASELINE_20260831.md)  
   Dashboard / Workspace / Services and the backend Control / Knowledge / Execution / Trust / Operations planes.

5. [`2026-09-01_Kairos_Dark_Light_UX_UI_Research.md`](2026-09-01_Kairos_Dark_Light_UX_UI_Research.md)  
   Earlier Kairos Light/Dark and progressive-disclosure research.

6. [`2026-09-01_Kairos_User_Screenshot_UI_Calibration_v0.4.md`](2026-09-01_Kairos_User_Screenshot_UI_Calibration_v0.4.md)  
   Historical screenshot-calibration attempt. **Its 228px labeled-sidebar / micro-typography assumptions are superseded where they conflict with v0.5 direct-screenshot review.**

7. [`2026-09-01_Kairos_User_Screenshot_UI_Calibration_v0.5.md`](2026-09-01_Kairos_User_Screenshot_UI_Calibration_v0.5.md)  
   **Current visual authority.** Human-supplied direct Light/Dark screenshots are treated as the strongest visual evidence: narrow ~70px icon rail, rounded-square identity tile, readable body scale, warm dark hierarchy/dotted texture direction and icon-only low-priority utilities.

## AI governance reading order

For Codex/Claude deployment work, architecture research is not the first authority. Read [`../governance/AI_READ_ORDER.md`](../governance/AI_READ_ORDER.md) first. It places `AGENTS.md`, `CLAUDE.md`, policy and Autopilot contracts before research/UI material.

## Current web entrances

- Dashboard: `https://space653000.github.io/0_JN1_AERIS/`
- Workspace: `https://space653000.github.io/0_JN1_AERIS/workspace.html`
- Services: `https://space653000.github.io/0_JN1_AERIS/services.html`

Repository HTML/CSS/JS existing does not prove GitHub Pages has been externally verified live. Public deployment needs HTTP/Pages evidence.

## UI truth rule

```text
Real execution / data
→ Evidence
→ Verification
→ Telemetry / State Store
→ Dashboard Projection
```

Forbidden:

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

Current direct-screenshot regressions include, unless newer Human evidence explicitly overrides them:

- default 228px always-expanded labeled sidebar instead of the narrow icon rail;
- circular identity avatar instead of rounded-square identity tile;
- 8–13px micro typography for ordinary readable content;
- heavy shadows / giant SaaS KPI styling;
- emoji-heavy navigation;
- high-saturation teal as a large page surface;
- cool pure-black/neon cyberpunk Dark mode instead of warm dark hierarchy;
- dashboard-first analytics wall before identity/context;
- fake operational health not backed by Evidence/Telemetry.

**Visual evidence precedence:** direct Human screenshot > first-party public image > AERIS visual inference > prior CSS/token guess.
