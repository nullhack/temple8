---
domain: design
tags: [accessibility, wcag-2-2, aria, keyboard, screen-readers, contrast, pour]
last-updated: 2026-07-02
---

# Accessibility

## Key Takeaways

- **WCAG 2.2 is the current W3C Recommendation** (2023) — the standard to design and cite against. WCAG 3.0 is a working draft; it does not replace 2.x, and its contrast algorithm is undetermined (APCA was exploratory and was removed in 2023 — it is not "WCAG 3") (W3C, 2023; W3C, 2026).
- The principles are **POUR**: content must be Perceivable, Operable, Understandable, and Robust — every success criterion sits under one of these.
- **Semantic markup** is the foundation: the right HTML element (`<button>`, `<nav>`, `<label>`) carries meaning assistive tech reads for free; `aria-*` fills gaps, it does not replace semantics.
- **Keyboard navigation is non-negotiable**: every interactive element reachable in a logical order, a visible focus indicator, no keyboard traps. If it works only with a mouse, it is broken.
- **Contrast** has WCAG 2.2 floors (4.5:1 normal text; 3:1 large text + meaningful graphics); **color is never the only signal** (color-blind users + dark mode defeat it).
- Accessibility is a design decision made early, not a compliance pass at the end; retrofitting is more expensive than building it in, and WCAG 2.2 AA is increasingly a legal floor, not a nicety.

## Concepts

**The POUR spine.** Perceivable (the user can perceive the content — alternatives for sensory information). Operable (the user can navigate + interact — keyboard, no traps, enough time). Understandable (the content + operation are comprehensible — readable, predictable, error-tolerant). Robust (the content works with current + future assistive tech — parseable, compatible). Every WCAG success criterion nests under one of these; together they are the working definition of "accessible" (W3C, 2023).

**WCAG 2.2 is the standard.** WCAG 2.2 (W3C Recommendation, October 2023) extends 2.1 and is the current conformance target. WCAG 3.0 is a multi-year working draft (March 2026); it does not deprecate 2.x, and conformance to 2.2 AA is expected to satisfy most of WCAG 3's minimum level once it finalises. Crucially, the WCAG 3 contrast algorithm is undecided — APCA was exploratory and was removed from the draft in 2023, so citing "APCA as WCAG 3" is wrong; design against the WCAG 2.2 ratios today (W3C, 2023; Roselli, 2026).

**Semantic markup first.** The right native element is the cheapest accessibility win: a real `<button>` is keyboard-focusable, announces as "button," and fires on click + Enter + Space without any extra code; a `<div onclick>` is none of those. ARIA's rule of thumb: if you can use a native element or attribute with the semantics + behavior you need, do that; use `aria-*` only to fill what native HTML cannot express. ARIA cannot rescue non-semantic markup — a `role="button"` on a div still needs manual focus + keyboard handling that a real button gets free.

**Keyboard, focus, traps.** Every interactive element must be reachable via Tab in a logical order, with a visible focus indicator (never `outline: none` without a replacement). The user must be able to escape any modal or widget with keyboard alone — a focus trap is a defect. Modal dialogs move focus into the dialog and return it on close; `Esc` dismisses.

**Contrast + color-not-sole-signal.** Text/background contrast must meet the WCAG 2.2 floors (4.5:1 normal; 3:1 large). Color must not be the only carrier of meaning — an error state shown only in red is invisible to color-blind users; pair it with an icon, a word, or a shape. The same applies to links-in-prose (underline or a clear non-color differentiator).

**A design decision, not a pass.** Accessibility built into the design (semantic structure, keyboard flows, contrast budget, error recovery) is cheap; retrofit is expensive and often incomplete. Treat WCAG 2.2 AA as the floor and design to it from the contract stage — the same stage at which error flows and feedback are designed.

## Content

### WCAG 2.2 contrast floors

| Use | Minimum ratio |
|---|---|
| normal text (< 18pt / 24px regular; < 14pt bold) | 4.5:1 |
| large text (≥ 18pt / 24px regular; ≥ 14pt bold) | 3.0:1 |
| meaningful graphics + UI component boundaries | 3.0:1 |

### The POUR quick-check

| Principle | Ask |
|---|---|
| Perceivable | is there a text alternative for every non-text element? |
| Operable | can every interaction be completed with a keyboard, with a visible focus? |
| Understandable | is the language defined; are inputs + errors identified + actionable? |
| Robust | does the markup parse cleanly + expose correct roles/names/states to AT? |

### ARIA's first rule

Use native HTML when it can carry the semantics + behavior you need. Reach for `aria-*` only to fill a gap native HTML cannot — and then pair it with the keyboard handling a native element would have given you for free.

### The WCAG 3 / APCA caveat

WCAG 3.0 is a working draft; it does not replace 2.x. Its contrast algorithm is undecided — APCA was exploratory and was removed from the draft in 2023. Design against WCAG 2.2 ratios today; track WCAG 3 as it matures, but do not cite APCA as a standard (Roselli, 2026).

## Related

- [[design/visual-design]] — contrast floors + color-not-sole-signal are shared rules
- [[design/interaction-design]] — keyboard nav + error recovery are interaction-design concerns accessibility sharpens
- [[design/asset-design]] — assets carry accessible names + meet contrast floors
- [[design/cli-design]] — terminal accessibility (color-not-sole-signal, `NO_COLOR`, screen-reader-readable output)
