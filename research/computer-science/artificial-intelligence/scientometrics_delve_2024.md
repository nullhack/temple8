# Scientometrics "Delve" Study (2024)

## Citation

Lund, B. D., Wang, T., Mannuru, N. R., Nie, B., Shimray, S., & Wang, Z. (2024). "The history and future of AI-generated text: A bibliometric analysis of PubMed abstracts." *Scientometrics*, Springer. (PubMed frequency spike analysis)

## Source Type

Academic Paper

## Method

Bibliometric Analysis

## Verification Status

Verified

## Confidence

High

## Key Insight

The word "delve" appeared 48x more often in AI-generated text than human-written text, with a measurable spike in PubMed abstracts post-2023 traceable to RLHF annotation bias from Nigerian annotators where "delve" is common in business English.

## Core Findings

1. **48x overrepresentation**: "delve" appears 48 times more frequently in AI-generated text compared to human baselines.
2. **PubMed spike**: Measurable increase in "delve" usage in PubMed abstracts after 2023, corresponding to widespread LLM adoption in academic writing.
3. **RLHF annotation origin**: The overrepresentation was traced to RLHF annotation bias. Many annotators were from Nigeria where "delve" is common in business English, creating a selection bias that amplified the word globally across LLM output.
4. **Bibliometric methodology**: The study used large-scale bibliometric analysis of academic abstracts to quantify the vocabulary shift, providing concrete evidence of LLM influence on academic writing.

## Mechanism

RLHF (Reinforcement Learning from Human Feedback) trains models to prefer outputs rated highly by human annotators. When the annotator pool has regional language patterns (e.g., Nigerian business English favoring "delve"), the model learns to produce those patterns regardless of context. The selection bias is then amplified through the reward model, making the pattern universal across all LLM output rather than regionally confined.

## Relevance

Provides the canonical case study for how RLHF annotation bias creates vocabulary overrepresentation in LLM output. The "delve" story illustrates the broader mechanism: training data composition + annotator demographics + reward model amplification = statistically detectable vocabulary markers. This mechanism generalizes to all Tier 1 AI writing markers.

## Related Research

- WriteHuman 2026 analysis: current-generation overrepresentation patterns from 80K+ pair dataset
- TextVisualization.app corpus analysis: quantified many additional single-word ratios (breathtaking: 36,261x; vibrant: 1,260x)
- Pangram Labs n-gram research: n-gram level detection methodology
