---
domain: writing
tags: [ai-language-markers, ai-tells, rlhf-bias, prose-quality, parsimony]
last-updated: 2026-07-02
---

# AI Language Markers

## Key Takeaways

- LLMs overuse a stable set of words: corpus analysis of 14M PubMed abstracts found certain "style words" spiked abruptly with LLM adoption — `delve`, `intricate`, `underscore`, `showcasing`, `pivotal`, `realm`, `meticulously`, `multifaceted` — and at least 10% of 2024 abstracts were LLM-processed (Kobak et al., 2024).
- The strongest single-word tell is a hedging verb: `ensuring` is over-represented 4.3× in AI text, joined by a family (`highlights`, `supports`, `reflects`) the model reaches for when padding an idea to sound considered (Jackson, 2026).
- The strongest multi-word tell is `rather than` (2.5×; 17,251 vs 6,859 occurrences in an 80,141-pair corpus) — how the model hedges a comparison instead of making one (Jackson, 2026).
- Structural tells survive prompt rewrites longer than vocabulary: low **burstiness** (uniform 18–24-word sentences), the rule-of-three, and over-qualified claims ("can be a useful tool for many writers in certain situations"). Em-dashes are a weaker signal than their reputation (2.6×, not the caricature) (Jackson, 2026; Duey, 2026).
- The mechanism is RLHF bias, not architecture or training data alone — human preference feedback amplifies "neutral-competent" formal prose, the same instinct that reaches for docstrings unprompted (Kobak et al., 2024; [[software-craft/docstring-lifecycle]]).
- This is the prose analog of the docstring strip: a backstop against the training instinct. When authoring knowledge, ADRs, the glossary, or skills, scrub these markers — no single one is diagnostic, but several in one passage reads as unthinking generation.

## Concepts

**Vocabulary overrepresentation.** LLMs overuse a stable lexicon. Kobak et al. (2024) studied 14 million PubMed abstracts (2010–2024) and identified 21 "focal words" whose frequency spiked with LLM adoption — `delve`, `intricate`, `underscore`, `showcasing`, `pivotal`, `realm`, `meticulously` among them — estimating at least 10% of 2024 abstracts were processed by an LLM (up to 30% in some sub-corpora). A co-occurrence study found `delve`/`realm`/`underscore` rising up to 85-fold in 2023–2024 versus pre-2022 (medRxiv, 2024). These words appear in formal writing the models were trained on, then RLHF amplifies them because reviewers rate the formal-sounding variant higher.

**Hedging verbs and filler.** The model inflates significance: every topic is `pivotal`, every change `shapes` something, every feature `serves as` something. In an 80,141-pair humanization corpus, `ensuring` is over-represented 4.3× and `rather than` 2.5× (17,251 vs 6,859 occurrences) — the single strongest word and multi-word tells respectively (Jackson, 2026). The copula-avoidance pattern (`serves as` instead of `is`) and significance-inflation (`crucial`, `vital`, `key`) are the same reflex: padding an idea to sound considered rather than stating it.

**Structural formulaicity.** Vocabulary is the visible signal; structure is the persistent one. AI text has low burstiness — sentences settle into a 18–24-word metronome — and leans on the rule-of-three, the `Not X, but Y` construction, and over-qualified claims ("can be a useful tool for many writers in certain situations") that optimise for plausible deniability over meaning (Jackson, 2026; Duey, 2026). Em-dashes are a real but weaker tell (18.5% of AI inputs contain ≥1 vs 7.1% humanised, a 2.6× effect) — downgraded from their 2024 reputation (Jackson, 2026).

**Chatbot artifacts.** Conversational voice markers — `Absolutely!`, `Great question!`, `Let me break this down`, excessive bold formatting — index the "helpful assistant" role rather than content. They are distinct from the content markers above and persist in any conversational output.

**Multi-signal, RLHF-driven.** No single marker is diagnostic; detection scores vocabulary, structure, hedging, and cadence together, with cadence uniformity surviving longest across rewrites (Duey, 2026). The root cause is reinforcement learning from human feedback: reviewers consistently prefer the formal, hedged, "neutral-competent" variant, which narrows style toward technically-correct but distinctive-free prose (Kobak et al., 2024). This is the same instinct that reaches for docstrings unprompted — and the reason the backstop is a scrub, not an instruction.

## Content

### Vocabulary to scrub (overrepresented in AI text)

`delve`, `tapestry`, `intricate`, `multifaceted`, `pivotal`, `realm`, `underscore`, `showcasing`, `meticulous(ly)`, `testament`, `vibrant`, `breathtaking`, `robust`, `seamless`, `leverage`, `navigate`, `landscape`, `journey`. None is banned — each occurs in good human writing — but several in one passage signal unthinking generation (Kobak et al., 2024; Jackson, 2026).

### Hedging, filler, and significance-inflation

- `ensuring` / `ensures` (4.3× — the strongest word tell), `highlights`, `supports`, `reflects`, `underscores`.
- `rather than` (2.5× — the strongest phrase tell); rewrite the comparison directly or drop the qualifier.
- `plays a crucial/vital/key role in shaping`, `serves as`, `It's worth noting that`, `It's important to note`.
- Intensifier adverbs that inflate without evidence: `significantly`, `effectively`, `increasingly`, `remarkably`.

### Structural tells (persistent across rewrites)

- Low burstiness — uniform 18–24-word sentences; vary length deliberately.
- The rule-of-three; `Not X, but Y`; formulaic trigrams.
- Over-qualified claims that hedge toward plausible deniability — make the claim or drop it.
- Em-dashes — keep only where genuine; do not let them become the default appender.

### Chatbot artifacts (drop entirely in authored prose)

`Absolutely!`, `Great question!`, `Let me break this down`, `I'd be happy to help`, `I hope this helps`, excessive bold. These index the assistant role, not content.

### The scrub rule

When authoring knowledge, ADRs, the glossary, the README, or skill prose, treat the lists above as a find-and-replace pass: each marker present is a prompt to rewrite for directness. This is the prose form of the docstring strip — the same RLHF instinct surfaces in both, and the answer in both is a mechanical scrub at authoring time, not a reliance on the model to self-regulate.

## Related

- [[software-craft/docstring-lifecycle]] — the code-side analog: the same RLHF instinct, the same strip-not-instruct answer
- [[methodology/knowledge-files]] — the authoring bar this catalog enforces on knowledge prose
- [[methodology/research-files]] — the same bar for research-card prose
