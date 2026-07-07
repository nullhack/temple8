# Delving into ChatGPT usage in academic writing through excess vocabulary (Kobak et al., 2024)

## Citation
Kobak, D., et al. (2024). "Delving into ChatGPT usage in academic writing through excess vocabulary." *arXiv:2406.07016* (published *Scientometrics*, 2025).
URL: https://arxiv.org/abs/2406.07016

## Method
Large-scale corpus analysis of ~14 million PubMed abstracts (2010–2024); "excess word" frequency analysis after a baseline, with comparative RLHF model testing.

## Confidence
High — peer-reviewed-scale bibliometric study; method and data described transparently.

## Key Insight
The arrival of LLMs caused an abrupt, unprecedented spike in the frequency of certain "style words" in scientific abstracts, and an excess-vocabulary lower bound estimates at least 10% of 2024 PubMed abstracts were processed by an LLM.

## Core Findings
1. Twenty-one "focal words" whose PubMed frequency spiked with LLM adoption (e.g. `delve`, `intricate`, `underscore`, `showcasing`, `pivotal`, `realm`, `meticulously`).
2. At least 10% of 2024 abstracts were LLM-processed; the lower bound reaches ~30% in some sub-corpora (by country, journal, discipline).
3. The vocabulary shift exceeds the effect of major events like the COVID-19 pandemic on scientific language.
4. Comparative model testing (Llama with/without RLHF) is consistent with RLHF contributing to the overuse — architecture and training data alone do not explain it.
5. Pre-LLM baselines show these words were rare; the spike is not a continuation of a prior trend.

## Mechanism
The authors compute per-word frequency trajectories across 14M abstracts, identify words whose post-2022 frequency far exceeds the pre-LLM baseline ("excess" vocabulary), and use the aggregate excess to estimate a lower bound on LLM-processed abstracts. The RLHF role is probed by comparing models with and without RLHF fine-tuning.

## Relevance
Grounds the vocabulary-overrepresentation claims in `writing/ai-language-markers`: the overused lexicon is empirically established (not anecdotal), the RLHF mechanism is named (not the unverified "regional annotator" story), and the scale (≥10% of 2024 abstracts) shows the instinct's reach.

## Related Research
medRxiv (2024) co-occurrence study (`delve`/`realm`/`underscore`, 85-fold rise); Jackson, 2026 (structural tells); arXiv:2412.11385 (the "puzzle of lexical overrepresentation" formalisation).
