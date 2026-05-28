# WriteHuman AI Writing Analysis (80,141 Pairs) (2026)

## Citation

WriteHuman. (2026). AI Writing Detection and Humanization Analysis: 80,141 AI-to-Human Text Pairs. WriteHuman platform analysis.

## Source Type

Industry Analysis

## Method

Corpus Analysis

## Verification Status

Unverified (industry data, not peer-reviewed)

## Confidence

Medium

## Key Insight

Analysis of 80,141 AI-to-human text pairs reveals that hedging verbs ("ensuring/ensures", "highlights", "supports", "reflects") and specific constructions ("rather than" at 2.5x, "capable of" as highest-leverage swap) are the strongest 2026 signals of AI-generated text.

## Core Findings

1. **Hedging verb overrepresentation**: "ensuring/ensures" appears 4.3x more often in AI text. "highlights", "supports", "reflects" are the top hedging verbs distinguishing AI from human writing.
2. **"rather than" as discriminator**: 17,251 occurrences in AI text vs 6,859 in human text (2.5x overrepresentation), making it one of the strongest single-phrase signals.
3. **"capable of" vs "able to"**: The single highest-leverage humanization swap in the dataset. AI consistently uses "capable of" where humans use "able to".
4. **Formulaic trigram**: "X plays a crucial/critical/important role in shaping Y" is statistically the most formulaic trigram in the dataset.
5. **Em dash overuse**: 18.5% of AI inputs contain ≥1 em dash vs 7.1% of human text (2.6x). AI uses 1 per 50-80 words vs human 1 per 500 words.
6. **Intensifier adverbs**: "significantly", "effectively", "directly", "increasingly" are top-tier signals in 2026 data.

## Mechanism

The overrepresentation patterns emerge from RLHF training where human reviewers consistently prefer formal, hedged, "balanced" language. Each round of preference training amplifies these patterns. The "capable of" preference likely stems from academic and formal training corpus dominance, while hedging verbs reflect the model's tendency to qualify and soften claims rather than state them directly.

## Relevance

Provides the empirical foundation for identifying AI-generated text in 2026. The 80,141 pair dataset is one of the largest humanization benchmarks available and captures current-generation LLM output patterns. Essential for any system that needs to distinguish AI from human writing or that generates text intended to read naturally.

## Related Research

- TextVisualization.app corpus analysis: single-word frequency ratios from large-scale corpus comparison
- Pangram Labs n-gram research: n-gram level AI writing detection
- Scientometrics delve study (2024): origin of specific vocabulary overrepresentation through RLHF bias
- Wikipedia "Signs of AI writing": community-maintained catalogue of AI writing markers
