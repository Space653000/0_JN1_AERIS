# Kairos User-Screenshot UI Calibration → AERIS UI v0.5

**Date:** 2026-09-01 (Asia/Taipei)  
**Evidence authority:** Human Chief Engineer direct Light/Dark screenshots while operating `os.lifehacker.tw`  
**Status:** Current screenshot-calibrated visual baseline  
**Supersedes:** v0.4 geometry, typography, avatar and navigation-control assumptions where they conflict with the direct screenshots.

## 1. Why v0.5 is necessary

v0.4 correctly captured the restrained teal/neutral Personal-OS feeling, but over-interpreted the screenshots into a conventional `~228px` labeled sidebar and extremely small `8–13px` operational typography. Direct screenshot review does not support those as the primary desktop geometry.

The strongest evidence is the Human-supplied screenshot itself. Therefore this document corrects the canonical target instead of defending an earlier implementation.

## 2. Direct visual observations — Light

Approximate screenshot geometry, not claimed Kairos source CSS:

- very light warm-neutral canvas;
- thin dark green/near-black line across the top, roughly a few pixels;
- **floating narrow left icon rail around 70px**, not a 228px text navigation panel;
- rail uses white rounded surface with restrained shadow/border;
- teal `K` logo tile near the top with a small green online indicator;
- active navigation is a teal rounded-square/icon tile;
- remaining navigation is monochrome iconography;
- main content begins to the right of the rail with generous whitespace;
- page identity/header shows an outlined icon + name and synced metadata;
- refresh control sits at upper right;
- main identity card is large, white, subtly bordered and highly rounded but not a generic SaaS KPI wall;
- `Kairos 在線_` appears with a restrained teal ONLINE pill;
- avatar is a **rounded-square teal tile**, not a circle;
- identity name is visually large, approximately high-20s/low-30s px at screenshot scale;
- normal readable body copy is closer to ordinary web reading size, roughly 17–18px at screenshot scale, not 8–10px microcopy;
- capability mini-cards are compact but still readable;
- quote/callout surface is pale gray;
- bottom chips are quiet and compact.

## 3. Direct visual observations — Dark

- near-#101111 warm dark canvas rather than blue-black;
- subtle dotted texture/pattern on the page background;
- floating rail uses a warm dark surface;
- main card uses warm charcoal/brown-black hierarchy, not cool neutral slate;
- text is warm off-white;
- teal remains vivid but not neon;
- refresh is bordered/transparent rather than a large filled control;
- theme control is an **icon-only sun/light control near the rail bottom**;
- no evidence requires a text `Dark Mode / Collapse` control in the primary screenshot geometry.

## 4. Canonical desktop geometry target

```text
Navigation rail        ≈ 68–76 px
Main gap after rail    ≈ 22–34 px
Main content width     responsive / screenshot-proportional
Major card radius      visually generous, calibrated by screenshot
Icon tile radius       rounded square, not circular
Avatar                 rounded square
Top accent line        ≈ 2–4 px
```

Do not turn the rail into a permanent 228px labeled menu unless a later Human screenshot explicitly shows that state.

Expanded navigation may exist as a responsive/secondary state, but it is not the primary screenshot baseline.

## 5. Typography target

Approximate screenshot-scale hierarchy:

```text
Readable body/UI       ≈ 16–18 px
Metadata/status        smaller but legible
Section heading        ≈ 18–22 px
Identity name          ≈ 28–32 px
Capability labels      compact, not microscopic
```

Exact browser/device scaling can change apparent pixels; preserve **relative hierarchy and readability**, not blindly hard-code these numbers.

Forbidden regression:

```text
8px body text
9px primary controls
11px normal content
```

on a standard desktop simply because v0.4 used those values.

## 6. Navigation contract

Primary screenshot state:

```text
[K logo]
[active icon]
[icon]
[icon]
[icon]
...

(bottom)
[theme icon]
```

Rules:

- icon-first rail;
- selected item uses restrained teal surface;
- labels should appear through tooltip, accessible name, secondary expansion or responsive state rather than consuming primary rail width;
- preserve keyboard focus and screen-reader labels;
- no emoji-heavy navigation.

## 7. Surface/palette direction

v0.4's general palette direction remains useful, but the direct screenshot outranks exact token guesses.

Light:

```text
warm near-white/very-light neutral canvas
white cards/rail
low-contrast borders
restrained dark-green/teal identity
```

Dark:

```text
warm near-black canvas
warm charcoal cards
subtle dotted background texture
warm off-white text
teal identity accent
```

Avoid cool generic SaaS slate if it makes the screenshot visibly less similar.

## 8. Dashboard rhythm

Preserve the first-hand structure:

```text
page identity + sync metadata + refresh
↓
large identity/status card
  Kairos/AERIS online wording
  rounded-square identity tile
  identity statement
  capability links/mini-cards
  readable narrative/about content
  callout/quote/chips
↓
progressive detail
```

AERIS content remains its own engineering system; only visual grammar is calibrated from the screenshot.

## 9. AERIS truth overlay

Visual similarity must never fake backend state.

```text
real execution/data
→ Evidence
→ Verification
→ Telemetry/State Store
→ Dashboard projection
```

If there is no heartbeat/telemetry, show `UNKNOWN`, `NO HEARTBEAT`, `STALE` or `NOT CONFIGURED`, not `HEALTHY`.

## 10. Acceptance for future UI changes

A UI change is a screenshot-calibration regression if, without newer Human evidence, it:

- restores a 228px always-expanded labeled sidebar as the default desktop state;
- uses circular identity avatar where screenshot target is rounded-square;
- makes ordinary body content microscopic;
- removes the warm dark hierarchy/dotted texture direction;
- turns the theme utility into prominent text controls inconsistent with the screenshot;
- adds heavy shadows, neon cyan or oversized SaaS KPI visuals;
- ignores identity-first progressive disclosure;
- displays operational truth unsupported by live Evidence/Telemetry.

**Evidence precedence:** direct Human screenshot > first-party public image > AERIS visual inference > prior token guess.
