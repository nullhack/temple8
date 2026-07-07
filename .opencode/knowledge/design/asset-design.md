---
domain: design
tags: [asset-design, logo, banner, social-card, favicon, svg, dev-branding, open-graph]
last-updated: 2026-07-02
---

# Asset Design

## Key Takeaways

- A Python project ships a small, fixed set of visuals — **one per use case**: a GitHub social card, a README banner, a logo/avatar, a favicon. Design each for where it lives; do not invent a brand system around them.
- The **GitHub social card** (open-graph image) is 1280×640 px; it is the project's face in link previews, so it carries the name + one line of intent + the mark, composed for the 2:1 frame.
- Produce assets as **self-contained SVG** (presentation attributes, no external references, no `<style>` blocks GitHub will strip) with an accessible `aria-label`/`<title>`; rasterise (PNG) only where the target requires it (the `.ico`, the apple-touch-icon).
- Honour **accessible contrast** in every asset (WCAG 2.2 floors) and provide a **dark-mode variant** where the asset will appear on both light and dark surfaces (README, GitHub).
- The dev-branding norm is **minimal**: one mark, generous whitespace, one accent. Vercel, Stripe, Linear, and the GitHub-ecosystem house style are the reference points — not heavy illustrative branding.
- A favicon or avatar must read at the size it is shown (32–64 px for avatars; 16 px for tab favicons); verify legibility at that size for those two assets only. It is a check, not a design philosophy.

## Concepts

**One asset per use case.** A developer project's visual surface is a fixed inventory — the social card, the README banner, the logo/avatar, and (optionally) a favicon. Each lives in a specific context at a specific size and is composed for that context, not for a hypothetical "brand system" that would scale from a tab favicon to a billboard. Designing a four-tier production apparatus around four images is the over-engineering this project rejects.

**The social card is the project's face.** GitHub renders the repository's open-graph image (1280×640) in link previews on GitHub itself, in Slack, in social media, and in search. It is the single most-seen asset. It carries the project name, one line of intent (the tagline or purpose), and the mark — composed for the 2:1 frame, with the critical content inside the central 60–70% (some platforms crop the edges).

**Self-contained, accessible SVG.** SVG is the source format: it scales, it is small, and it diffs cleanly in version control. The production SVG uses presentation attributes (`fill="#1a1a2e"`) rather than inline `<style>` (which some hosts strip), references nothing external (no `<use href="external">`, no web fonts), declares a square `viewBox` with padding, and carries an accessible name via `<title>` + `aria-labelledby` (or `role="img"` + `aria-label`). Raster formats (PNG, ICO) are exported from the SVG where a target demands them.

**Accessible + dark-mode-aware.** Contrast floors (WCAG 2.2) apply to assets, not just UI text — a logo on a low-contrast background is inaccessible. Where the asset appears on both light and dark surfaces (a README that honours `prefers-color-scheme`, GitHub's theme-aware rendering), provide a variant per surface, or design a mark that holds on both (a monochrome mark with a transparent background is the simplest path).

**The minimal dev-branding norm.** The reference aesthetic across respected developer projects is restraint: one mark (often a single geometric form or a wordmark), generous whitespace, one accent color, a single typeface. Heavy illustrative branding, gradients, and mascots read as over-invested for a library or a CLI. Match the norm unless the project's identity genuinely calls for more.

**Legibility at the shown size — a check, not a philosophy.** The avatar (32–64 px in GitHub UIs) and the favicon (16 px in a browser tab) are the only assets that appear small. Verify they are legible at that size — simplify the mark if a thin stroke vanishes, drop a subtitle if it becomes unreadable. This is a final verification on two assets, not a multi-tier production process applied to all of them.

## Content

### The asset inventory for a Python project

| Asset | Size | Where it lives | Key constraint |
|---|---|---|---|
| social card (open-graph) | 1280×640 | link previews (GitHub, Slack, social) | name + intent + mark in the central 60–70% |
| README banner | wide (e.g. 1280×320 or full-width) | top of the README | reads at README width; honours dark mode |
| logo / avatar | square (e.g. 512×512) | GitHub repo avatar, package page | legible at 32–64 px |
| favicon | square (16→512) | browser tab, bookmark | legible at 16 px; provide PNG + an `.ico` if required |

### SVG production rules

- presentation attributes (`fill`, `stroke`) over inline `<style>` — hosts strip `<style>`.
- self-contained: no `<use href>` to external, no web fonts, no base64 blobs.
- square `viewBox` (e.g. `0 0 512 512`) with 5–10% internal padding.
- accessible name: `<title>` + `aria-labelledby`, or `role="img"` + `aria-label`.
- convert strokes to filled paths for the production file; optimise (SVGO-style: strip metadata, collapse numeric precision).

### Dark mode

Provide a dark-surface variant for any asset shown on a theme-aware surface (README, GitHub), OR design a monochrome mark on a transparent background that holds on both. The `prefers-color-scheme` media query works in SVG rendered inline in HTML; for raster exports, ship two files.

## Related

- [[design/visual-design]] — hierarchy, contrast, typography apply to assets as much as to UI
- [[design/accessibility]] — contrast floors + accessible naming apply to every asset
