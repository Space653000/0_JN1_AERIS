# Kairos User-Screenshot UI Calibration → AERIS UI v0.4

**Date:** 2026-09-01 (Asia/Taipei)  
**Repository:** `Space653000/0_JN1_AERIS`  
**Status:** Current visual calibration baseline  
**Supersedes for visual geometry:** the looser `Kairos-inspired` styling in AERIS UI v0.2/v0.3.

---

## 0. Why v0.4 exists

The earlier AERIS pages adopted Kairos concepts — teal accent, persistent sidebar, Light/Dark, cards and progressive disclosure — but still looked too much like a generic SaaS / engineering analytics dashboard.

On 2026-09-01 the Human Chief Engineer supplied direct Light and Dark screenshots while operating `https://os.lifehacker.tw/`. Those screenshots are treated as the strongest available visual reference for layout calibration.

The correction is:

> **Do not merely borrow Kairos colors. Borrow its visual density, geometry, hierarchy and restraint.**

AERIS keeps its own acoustic-engineering content and truth model, while using Kairos-like Personal OS visual grammar.

---

## 1. Evidence classes for this calibration

### SOURCE-FACT / direct visual observation

From the Human-supplied screenshots of `os.lifehacker.tw` and first-party Kairos dashboard material:

- persistent left navigation;
- compact navigation rows rather than large app-menu tiles;
- Light canvas is neutral gray / near-white, with white sidebar and white cards;
- Dark canvas uses layered charcoal / dark gray rather than pure black;
- teal/aqua is a restrained identity / active-state accent;
- active navigation is soft-filled and visually quiet;
- primary typography is compact, not oversized marketing typography;
- metadata/status text has a terminal / monospace feeling;
- cards use thin borders and minimal or no obvious shadow;
- the system identity appears before detailed operational data;
- Dark Mode and sidebar Collapse are low-priority persistent utilities near the bottom of navigation;
- information progresses from identity/summary toward detail instead of showing a dense analytics wall immediately.

First-party corroboration:

- `https://os.lifehacker.tw/`
- `https://lifehacker.tw/courses/24hr-claude-code-tutorial`
- the course page labels its Kairos image as a real dashboard screenshot showing memory, skill modules and project tracking;
- Kairos work logs describe Dashboard as an operational surface and record real system/automation status work.

### AERIS-DECISION

Exact CSS values below are AERIS implementation tokens calibrated from the observed screenshots. They are **not claimed to be Kairos source-code values**.

---

## 2. Geometry baseline

### Desktop

```text
Sidebar width          ≈ 228 px
Collapsed sidebar      ≈ 62 px
Main content max width ≈ 1180 px
Main horizontal pad    ≈ 26 px
Card radius            ≈ 12 px
Control/nav radius     ≈ 8–9 px
Card gap               ≈ 8–10 px
Border                 1 px, low contrast
Large decorative shadow: prohibited
```

The goal is a quiet Personal OS, not floating Material cards.

---

## 3. Typography baseline

The screenshots show restrained hierarchy. AERIS v0.4 therefore uses approximately:

```text
Body / normal UI       10–13 px depending on information level
Sidebar primary        11 px
Sidebar secondary       8 px
Metadata / status       8–9 px monospace-style
Section heading        13 px
Page heading           16 px
Identity name          22 px
Summary numeric        18 px
```

Principles:

1. Do not use 28–36 px SaaS dashboard headings for ordinary operational pages.
2. Use system UI fonts first so Windows/macOS render naturally.
3. Traditional Chinese and English engineering terminology share the same hierarchy.
4. Status and machine-state metadata may use `ui-monospace` to preserve the Kairos terminal/OS feel.

---

## 4. Light palette — v0.4

```text
Canvas        #F5F6F7
Sidebar       #FFFFFF
Surface       #FFFFFF
Surface 2     #FAFBFB
Surface 3     #F1F3F4
Primary text  #22272B
Secondary     #525A61
Muted         #8B9298
Border        #E4E7E9
Accent teal   #62C5BA
Accent strong #348F87
Accent soft   #E7F6F3
```

Light mode must feel slightly gray overall. White cards are separated primarily by 1 px borders, not shadow.

---

## 5. Dark palette — v0.4

```text
Canvas        #17191A
Sidebar       #111314
Surface       #1E2022
Surface 2     #1A1C1E
Surface 3     #24272A
Primary text  #E8EAEC
Secondary     #B6BCC1
Muted         #8E969C
Border        #2C2F32
Accent teal   #72D0C5
Accent strong #98E3DA
Accent soft   #18332F
```

Rules:

- no pure black global canvas;
- no neon cyan cyberpunk treatment;
- keep visible border hierarchy;
- semantic color families remain muted dark surfaces;
- panel/surface contrast should be subtle but readable.

---

## 6. Sidebar contract

Sidebar is the strongest Kairos-like structural feature.

AERIS v0.4:

```text
Brand
Small system / baseline status

AERIS
  Dashboard
  Workspace
  Activity / workflow
  Roles

INTELLIGENCE
  Research
  Skills
  Standards

TRUST / SYSTEM
  Evidence
  Services

(bottom)
  Dark Mode / Light Mode
  Collapse / Expand
```

### Active item

- soft teal background;
- teal text;
- 2 px vertical accent on the left;
- no large solid teal rectangle.

### Icons

Use restrained monochrome symbols / line-style visual language.

Avoid colorful emoji navigation because it breaks the visual grammar observed in Kairos.

---

## 7. Dashboard content rhythm

AERIS Dashboard v0.4 follows this order:

```text
Page name / Refresh
↓
AERIS 在線_ / status
↓
Identity panel
  Avatar
  我是 AERIS
  role description
  5 compact capability metrics
  small context chips
↓
About AERIS
↓
4 compact Engineering Overview cards
↓
Core Systems / chapters
↓
Engineering Flow
↓
Temporary Pod / Trust
↓
Searchable 100-seat Role Library
```

This is deliberately different from a BI dashboard that starts with giant KPIs and charts.

---

## 8. Card contract

AERIS cards now use:

- 1 px low-contrast border;
- 12 px radius for major cards;
- 8–9 px radius for controls/subcards;
- no heavy shadow;
- compact padding;
- short title + short explanation;
- detail on demand.

Forbidden default styling:

```text
large 18–24 px radius everywhere
heavy drop shadows
oversized KPI typography
bright gradient dashboard tiles
emoji-heavy icon system
```

---

## 9. Three-page application

### Dashboard

Most visually similar to Kairos: identity-first, calm summary and chapter progression.

### Workspace

Uses the same shell and density, but the main identity is `Human Chief Engineer`; task form and Temporary Pod are the operational focus.

### Services

Uses the same shell and density, with more structured backend information. It must still remain visually quiet even when showing Five Planes, G0–G5 and R0–R4.

---

## 10. Theme / collapse persistence

Shared controller:

```text
aeris-theme.js
```

Local storage:

```text
aeris-theme-preference = light | dark
aeris-sidebar-state    = expanded | collapsed
```

Behavior:

- first visit follows OS Light/Dark preference;
- explicit Light/Dark choice persists across all three pages;
- sidebar collapse state persists across all three pages;
- OS theme changes continue to apply only until the user explicitly selects a theme.

---

## 11. AERIS differentiation remains mandatory

Visual calibration does not change the engineering constitution.

AERIS must still surface:

```text
Memory ≠ Evidence
Execution ≠ Completion
Reviewer = independent role, not model brand
Dashboard = projection, not truth
Capability ≠ Authority
```

The design objective is therefore:

> **Kairos Personal OS visual restraint × AERIS Acoustic Engineering evidence rigor.**

---

## 12. Acceptance criteria for future UI changes

Any future Codex / Claude Code UI change must check:

- Does it preserve compact Personal OS density?
- Does it retain the 228 px / compact sidebar geometry unless there is evidence for a better responsive state?
- Does it avoid heavy shadows and oversized rounding?
- Does it keep the neutral gray Light hierarchy and charcoal Dark hierarchy?
- Does teal remain an accent rather than becoming the page background?
- Are navigation icons monochrome and restrained?
- Is identity / context presented before detailed operational data?
- Does Dashboard still avoid claiming backend truth without evidence?

If a redesign violates these without explicit Human approval, treat it as a regression.
