# TextVisualization.app Corpus Analysis (AI vs Human Word Frequency)

## Citation

TextVisualization.app. (2026). AI vs Human Writing: Large-Scale Corpus Frequency Analysis. TextVisualization.app tool and corpus.

## Source Type

Corpus Analysis Tool

## Method

Corpus Statistical Analysis

## Verification Status

Unverified (tool-generated data, methodology not peer-reviewed)

## Confidence

Medium

## Key Insight

Large-scale corpus comparison reveals extreme single-word frequency ratios between AI and human writing, with the most overrepresented words (breathtaking: 36,261x; vibrant: 1,260x; intricate: 115x; testament: 228x; tapestry: 25-35x) being virtually diagnostic of AI generation.

## Core Findings

1. **breathtaking**: 36,261x more common in AI corpus than human corpus. The single most overrepresented word in the analysis.
2. **vibrant**: 1,260x more common in AI corpus.
3. **testament**: 228x more common in AI corpus.
4. **intricate**: 115x more common in AI corpus.
5. **tapestry**: 25-35x more common in AI corpus.
6. **Frequency distribution**: The overrepresentation follows a power-law distribution. A small number of words have extreme ratios (1000x+) while most markers cluster in the 9-50x range.

## Mechanism

The extreme ratios suggest these words appear in specific genres (tourism, marketing, academic writing) that are heavily represented in LLM training data. When the model draws from these genres for general-purpose writing, the vocabulary leaks into contexts where humans would use simpler alternatives. The 36,261x ratio for "breathtaking" suggests near-zero human usage in the comparison corpus but consistent AI deployment as a positive intensifier.

## Relevance

Provides the most extreme single-word frequency ratios available, establishing the upper bound of AI vocabulary overrepresentation. These ratios are useful as high-confidence individual markers. Any text containing "breathtaking" used as a general intensifier is almost certainly AI-generated.

## Related Research

- WriteHuman 2026 analysis: phrase and construction-level patterns from 80K+ pairs
- Pangram Labs n-gram research: n-gram level detection methodology
- Scientometrics delve study (2024): RLHF annotation bias as root cause
