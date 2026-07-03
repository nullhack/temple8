# The Real Signature of AI Writing Isn't the Em-Dash Anymore (Jackson, 2026)

## Citation
Jackson, I. (2026). "The Real Signature of AI Writing Isn't the Em-Dash Anymore." *WriteHuman* blog, 21 April 2026.
URL: https://writehuman.ai/blog/ai-tells-in-2026

## Method
Corpus analysis of 80,141 humanization pairs (AI input vs humanized output) from the WriteHuman service, scored with the G² log-likelihood ratio (Dunning, 1993); positive G² = over-represented in AI input.

## Confidence
Medium-High — a vendor blog, but the method, sample size (80,141 pairs), and per-feature statistics are stated; corroborated by independent sources on burstiness and hedging.

## Key Insight
The strongest 2026 AI tells are structural (hedging verbs and formulaic sentence shapes), not the em-dash of 2024 reputation; `ensuring` and `rather than` are the single strongest word and multi-word signals.

## Core Findings
1. `ensuring` / `ensures` over-represented 4.3× — the strongest single-word tell; joined by a hedging-verb family (`highlights`, `supports`, `reflects`).
2. `rather than` over-represented 2.5× (17,251 occurrences in AI inputs vs 6,859 in humanized) — the strongest multi-word tell.
3. Em-dashes: 18.5% of AI inputs contain ≥1 vs 7.1% of humanized (2.6×) — a real but weaker signal than its reputation.
4. "Relational connectors" (`rather`, `broader`, `reducing`) act as glue the model uses to avoid making a direct claim.
5. The G² log-likelihood ratio (Dunning, 1993) is the scoring statistic — the standard corpus-vs-corpus comparison.

## Mechanism
Each feature's occurrence is compared between AI inputs and humanized outputs across 80,141 pairs; G² quantifies over-representation. Hedging verbs and significance-inflation emerge because the model optimises for "considered-sounding" prose (RLHF preference), padding claims rather than stating them. The humanizer strips these, exposing them as the differential.

## Relevance
Grounds the hedging-verb, filler, and structural-marker claims in `writing/ai-language-markers` with concrete multipliers, and downgrades the em-dash from its caricatured status. The actionable edits (cut `rather than`; restate the comparison directly; drop significance-inflation) come straight from the data.

## Related Research
Kobak et al., 2024 (vocabulary overrepresentation); Duey, 2026 and Leap AI, 2026 (burstiness / cadence uniformity as the persistent structural signal).
