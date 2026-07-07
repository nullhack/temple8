---
domain: requirements
tags: [discovery, interview, elicitation, CIT, laddering, active-listening]
last-updated: 2026-07-01
---

# Interview Techniques

## Key Takeaways

- Five techniques combine in every discovery interview: CIT, Laddering, CI Perspective Change, the Funnel, and the three-level Active Listening protocol.
- CIT (Flanagan, 1954): probe concrete past incidents, not generalities — schema-based recall hides edge cases.
- Laddering (Reynolds & Gutman, 1988): after each answer, climb means→ends until the answer names a writable constraint.
- CI Perspective Change (Fisher & Geiselman, 1987): when recall stalls, re-frame from another actor's seat.
- Funnel (Tversky & Kahneman, 1974): start open, narrow only after the broad layer is exhausted — never lead with categories (priming bias).
- Active Listening (Rogers & Farson, 1957) operates at three depths: paraphrase per answer (L1), synthesise per group (L2), full synthesis at session end (L3).
- The techniques are constant; the question-set and the active-listening depth change per funnel level — see each `interview-*` skill for the level-specific procedure.

## Concepts

**CIT — concrete incidents over generalities.** Schema-based recall ("usually we...") hides workarounds and edge cases; a concrete incident forces actual memory. Probe with "Walk me through the last time this happened", then "What happened next? What made it effective or ineffective?".

**Laddering — climb to the constraint.** The first answer is rarely the real constraint. After each answer ask "Why did that matter?" / "What does that enable?" / "What breaks without it?". Stop when the stakeholder reaches a value they cannot explain further — a writable design constraint.

**CI Perspective Change — re-frame on stall.** When recall stalls, ask the same situation from another actor's seat: "What does the end user experience here?", "What would your team lead's concern be?". Peripheral details and cross-role concerns surface that the primary perspective conceals.

**Funnel — broad before specific.** Any category name the interviewer introduces activates a schema that filters what the interviewee reports (priming bias). Sequence questions so the stakeholder's own categories emerge first; narrow only after the broad layer is exhausted.

**Active Listening — three depths.** L1 (per answer): paraphrase each answer before the next question. L2 (per group): a brief synthesis when transitioning between behaviour groups — confirms completeness, offers a recovery point. L3 (end of session): full synthesis across everything discussed, presented for stakeholder approval — the accuracy gate. Never introduce topic labels during active listening; the summary reflects what the stakeholder said.

## Content

### CIT (Flanagan, 1954)

Ask about a specific past event, not a general description.

- "Tell me about a specific time [X] worked exactly as you needed."
- "Tell me about a specific time [X] broke down or frustrated you."
- Probe: "What task were you doing? What happened next? What made it effective / ineffective?"

### Laddering / Means-End Chain (Reynolds & Gutman, 1988)

Climb from surface attribute to underlying consequence to terminal value.

- "Why is that important to you?"
- "What does that enable?"
- "What would break if that were not available?"
- Stop at a value the stakeholder cannot explain further — a writable constraint.

### CI Perspective Change (Fisher & Geiselman, 1987)

Describe the same situation from another actor's viewpoint.

- "What does the end user experience in that situation?"
- "What would your team lead's concern be here?"
- "From the perspective of someone encountering this for the first time, what would they need to know?"

### Funnel — question ordering (Tversky & Kahneman, 1974)

Broad open-ended questions before specifics. The interviewer's category names prime the interviewee; the funnel lets the stakeholder's own categories emerge first.

### Active Listening protocol (Rogers & Farson, 1957)

- **L1 (per answer)** — paraphrase each answer before the next question: "So if I understand correctly, X happens when Y?".
- **L2 (per group)** — brief synthesis on transitioning between behaviour groups: "We've covered A and B. Before C, here's what I understood: [summary]. Does that capture it?".
- **L3 (end of session)** — full synthesis of everything discussed, presented for approval. The accuracy gate and the input to contract authoring.

Do not introduce topic labels during active listening; the summary reflects what the stakeholder said, not new framing.

## Related

- [[requirements/ubiquitous-language]] — term extraction feeding the glossary authored at consolidation
- [[requirements/domain-decomposition]] — gap analysis applied at building-block identification
- [[requirements/aggregate-boundaries]] — sizing block boundaries
