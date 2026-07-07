---
domain: design
tags: [visual-design, hierarchy, contrast, typography, color, wcag-contrast, layout]
last-updated: 2026-07-02
---

# Visual Design

## Key Takeaways

- Visual design's job is communication, not decoration: it tells the user what matters, what goes together, and what they can do — through **hierarchy**, **contrast**, **spacing**, and **alignment**.
- **Hierarchy** is built from four levers — size, weight, position, and spacing — and the user reads the page in the order they establish. If everything is emphasised, nothing is.
- **Contrast** carries meaning and legibility; text-against-background contrast has a hard floor (WCAG 2.2: 4.5:1 for normal text, 3:1 for large) below which the design is inaccessible, not just ugly (W3C, 2023).
- **Color is semantic**, not ornamental: it signals state (success/warning/danger), identity (brand), and structure (grouping). Reserve it for those jobs; the layout should hold without it (so the design still works for color-blind users and in dark mode).
- **Typography** is a small set of decisions with outsized effect: one or two typefaces, a defined weight/size scale (not arbitrary), generous line-height, and measure (line length) under ~75 characters for body text.
- **Whitespace and alignment** do the quiet work: alignment creates order the eye reads as "designed"; whitespace groups (proximity) and gives the content room to breathe.

## Concepts

**Communication, not decoration.** A visual surface that the user scans for 2 seconds must convey what matters, what groups with what, and what is actionable. Visual design is the discipline that engineers that scan. The decorative lens ("make it look nice") produces arbitrary choices; the communication lens produces a hierarchy the user reads correctly under time pressure.

**Hierarchy from four levers.** Size (larger = more important), weight (bolder = more important), position (top-left in left-to-right reading order = seen first), and spacing (more space around = more important; less space between = grouped). The user's eye follows the gradient these create. The failure mode is flat hierarchy — every heading the same size, every element equally weighted — which forces the user to read everything to find anything.

**Contrast has a floor.** Contrast is the perceptual distance between an element and its background. For text it has an accessibility floor set by WCAG 2.2 (4.5:1 for normal text, 3:1 for large text and for meaningful graphics), below which the text is unreadable for low-vision users and in adverse lighting (W3C, 2023). Contrast is also a hierarchy lever — a high-contrast primary heading against a low-contrast secondary one creates order without size changes.

**Color as semantics.** Color signals state (green/success, yellow/warning, red/danger), identity (the brand accent), and structure (a tinted group). It should not be the only signal — color-blind users (and dark-mode inversions) defeat color-only coding, so pair color with a shape, label, or weight. Modern color systems layer tokens (primitive hex → semantic role → component), so `surface-action-primary` resolves to the brand accent and can be re-skinned without touching components.

**Typography decisions.** One typeface (or two — a body + a display) is plenty. Define a type scale (a fixed set of sizes/weights) and use only those tokens. Body line-height around 1.5; measure (line length) 45–75 characters. Avoid the decorative — condensed faces, all-caps body, low-weight low-contrast text — for anything the user must read.

**Whitespace and alignment.** Proximity groups: items close together are read as related, items far apart as separate. Alignment creates the order the eye reads as deliberate — a strong axis (left-aligned text, a grid) reads as "designed"; misalignment reads as "sloppy" and slows comprehension. Whitespace is not wasted space; it is the cheapest hierarchy lever available.

## Content

### Hierarchy levers and what each signals

| Lever | Signals | Failure mode |
|---|---|---|
| size | relative importance | everything large → flat |
| weight | relative importance; emphasis | everything bold → no emphasis |
| position | reading order | primary action buried → lost |
| spacing | grouping (proximity) and importance | uniform spacing → nothing groups |

### WCAG 2.2 contrast floors

| Use | Minimum ratio |
|---|---|
| normal text (< 18pt / 24px, or < 14pt bold) | 4.5:1 |
| large text (≥ 18pt / 24px, or ≥ 14pt bold) | 3:1 |
| meaningful graphics + UI components | 3:0 |

Verify pairs with a contrast checker, not by eye; perceived contrast shifts with surrounding color and screen calibration (W3C, 2023).

### A minimal type scale

Define sizes as tokens (e.g. `text-sm`, `text-base`, `text-lg`, `text-xl`, `text-2xl`) and weights (`font-regular`, `font-medium`, `font-semibold`, `font-bold`); use only those. Body at `text-base`/`font-regular`; headings step up size + weight together. One typeface family with a full weight range outperforms several decorative families.

### Color roles (semantic, not visual)

Primitive tokens (raw hex) feed semantic tokens (`text-primary`, `surface-action`, `border-muted`, `state-success/warning/danger`) that feed component tokens. Components consume semantics, never primitives — so a re-skin (brand change, dark mode) is a token-layer change, not a component rewrite.

## Related

- [[design/interaction-design]] — signifiers and hierarchy are how the user reads what they can do
- [[design/accessibility]] — contrast floors + color-not-sole-signal are accessibility rules
- [[design/asset-design]] — the same hierarchy/contrast/typography apply to banners + logos
