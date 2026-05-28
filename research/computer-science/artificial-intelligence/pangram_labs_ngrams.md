# Pangram Labs N-gram AI Detection Research

## Citation

Pangram Labs. (2026). N-gram Analysis of AI-Generated vs Human Writing. Pangram Labs research.

## Source Type

Industry Research

## Method

N-gram Statistical Analysis

## Verification Status

Unverified (industry data, not peer-reviewed)

## Confidence

Medium

## Key Insight

N-gram level analysis reveals that AI writing is detectable not just through individual word frequencies but through characteristic word combinations and phrase structures that form statistically distinct patterns from human writing.

## Core Findings

1. **N-gram signatures**: AI text exhibits characteristic n-gram (2-3 word combination) patterns that differ statistically from human writing beyond what single-word analysis captures.
2. **Multifaceted as marker**: "multifaceted" identified as 28x overrepresented in AI text through n-gram analysis.
3. **Phrase-level detection**: Detection accuracy improves when analyzing word combinations rather than individual words alone.
4. **Complementary to single-word analysis**: N-gram analysis catches patterns that single-word frequency analysis misses, particularly hedging constructions and formulaic transitions.

## Mechanism

LLMs generate text through next-token prediction, which creates statistical regularities at the phrase level (bigrams, trigrams) that are more distinctive than individual word choices. The model's tendency to use "safe" transitional phrases and hedging constructions creates n-gram patterns that are statistically unusual in human writing but consistently present in AI output.

## Relevance

Provides the phrase-level detection methodology that complements single-word frequency analysis. Essential for building multi-level AI writing detection systems that look beyond vocabulary to structural patterns.

## Related Research

- WriteHuman 2026 analysis: large-scale pair dataset with trigram-level findings
- TextVisualization.app corpus analysis: single-word frequency ratios
- Scientometrics delve study (2024): RLHF annotation bias mechanism
