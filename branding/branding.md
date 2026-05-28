# Branding: temple8

> *From zero to hero: Spec-driven agent orchestration. Any workflow. Any LLM. Zero lock-in.*

Agents read this file before generating release names, C4 diagrams, README banners, or any document with visual or copy identity. All fields are optional; absent or blank fields fall back to defaults (adjective-animal release names, Mermaid default colors, no wording constraints).

**Ownership**: The stakeholder owns this file. The designer proposes changes (color palettes, visual assets, wording updates); the stakeholder approves them. No other agent edits this file.

---

## Identity

- **Project name:** temple8
- **Tagline:** From zero to hero: Spec-driven agent orchestration. Any workflow. Any LLM. Zero lock-in.
- **Mission:** Eliminate overhead so engineers ship features, not setup.
- **Vision:** The standard starting point for any serious Python project: the bedrock every Python engineer reaches for first.
- **Tone of voice:** Direct, precise, minimal. The Greeks did not decorate the Parthenon with apologies. Neither do we.

## Visual

The palette is drawn from classical marble, parchment, and gold, materials that have carried ideas for millennia. Every colour choice serves legibility first; decoration is secondary.

- **Background/parchment:** `#faf7f2` → `#ede8e0`, warm off-white, the surface on which ideas are set down
- **Primary text:** `#5c3d1e` → `#3b2410`, deep warm brown, the ink that endures
- **Accent/gold:** `#c9a84c` → `#e8c96a`, antique gold, used for borders and structural lines only (never body text)
- **Secondary/blue:** `#7baabf` → `#4a7a96`, Aegean steel blue, for labels and secondary hierarchy
- **Stone/marble:** `#f0ece4` → `#c8c0b8`, the load-bearing colour; columns, shapes, structural chrome
- **Logo:** `docs/assets/logo.svg`
- **Banner:** `docs/assets/banner.svg`

> Deep brown `#3b2410` on parchment `#faf7f2` achieves >10:1 contrast (WCAG AAA). Gold is decorative; it never carries meaning that must be read.

### Logo

Greek temple façade: pediment, four columns, three-step stylobate. A horizontal lintel (crossbeam) spans between the two central columns at mid-height. The void above the lintel and the void below it, framed by the entablature and stylobate, together imply an 8 (structural, not decorative). Transparent background. Stone-light `#f0ece4` / `#c8c0b8` fill, `#5c3d1e` brown outlines.

**8-shape shadow consistency**: The four shadow edges defining the two loops of the 8 (ceiling, lintel-top, lintel-bottom, floor) are equal in height (2 px each) so both loops appear the same size. The ceiling and floor shadows use `#5c3d1e` at 0.45 opacity; the lintel has a bottom-only border (no full outline) with an underside shadow (`#5c3d1e` at 0.38) and a subtle top shadow strip (`#a09890` at 0.2 opacity, matching the column shadow style).

### Banner

Warm parchment `#faf7f2` background. Left zone: temple mark (same geometry as logo, scaled). Right zone: `TEMPLE·VIII` typeset with engraved two-layer effect: front layer `#f0ece4` (stone-light), shadow layer `#3b2410` (deep brown) offset +3px right / +4px down. Middle dot `·` in gold `#c9a84c`. Gold accent rules above and below the title. Gold top and bottom border bands. Vertical gold divider separating temple from title zone. No subtitle.

## Release Naming

- **Convention:** `adjective-greek-figure`
- **Theme:** Greek antiquity: philosophers, heroes, gods, mythological figures. Every release name should read like an epithet: something a figure *earned* through their defining quality (e.g. "Resolute Athena", "Precise Pythagoras", "Luminous Hypatia").
- **Rationale:** Ancient Greece is the origin of the intellectual tradition that underpins Western civilisation: democracy, systematic philosophy, formal logic, and scientific reasoning all trace their lineage to the Greek city-states. Plato and Aristotle invented political philosophy as a genre; Aristotle formalised logic and ethics; the Pythagoreans established that abstract reasoning could describe the physical world. This template stands on the same premise: rigorous method, applied from the beginning, produces something worth building on. The Greek figure in each release name is not decoration: it is a statement about what kind of work this is.
- **Excluded words:** *(none)*

## Wording

Every word carries weight. The Greeks had a name for ornament that obscures meaning: *kenophonia*: empty noise.

- **Avoid:** `easy`, `simple`, `just`, `quick`, `scaffold`, `superseded`, `boilerplate`
- **Prefer:** `minimal`, `precise`, `production-ready`, `rigorous`, `from zero to hero`

