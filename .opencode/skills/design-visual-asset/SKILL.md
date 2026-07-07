---
name: design-visual-asset
description: "Produce a project visual asset — social card, README banner, logo/avatar, or favicon — as self-contained, accessible SVG. On-demand."
---

# Design Visual Asset

1. Load [[design/asset-design]], [[design/visual-design]], [[design/accessibility]] — the per-use-case asset inventory, the visual-design levers (hierarchy, contrast, typography), and the accessibility floors every asset must meet.
2. Identify the asset + where it lives — social card (1280×640, open-graph previews), README banner (wide, dark-mode-aware), logo/avatar (square, reads at 32–64 px), favicon (square, reads at 16 px). Compose for that context, not for a generic brand system.
3. Establish hierarchy with the four levers — size, weight, position, spacing — so the user reads the name first, the intent second, the mark third. Apply parsimony: one mark, generous whitespace, one accent; the dev-branding norm is restraint.
4. Author the asset as self-contained SVG: presentation attributes (no inline `<style>` hosts strip), no external `<use href>` or web fonts, a square `viewBox` with padding, strokes converted to filled paths for production, metadata stripped.
5. Make it accessible: give the SVG an accessible name (`<title>` + `aria-labelledby`, or `role="img"` + `aria-label`); meet WCAG 2.2 contrast floors against every background it will appear on; pair color with a shape or label so it survives color-blind + dark-mode.
6. Provide a dark-surface variant where the asset appears on a theme-aware surface (README, GitHub), OR design a monochrome mark on a transparent background that holds on both.
7. Verify legibility at the shown size for the avatar (32–64 px) and favicon (16 px) only — simplify the mark if a thin stroke vanishes. Export PNG / `.ico` only where a target demands it; the SVG is the source.
