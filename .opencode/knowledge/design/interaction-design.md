---
domain: design
tags: [interaction-design, ixd, feedback, affordance, error-design, mental-model, heuristics]
last-updated: 2026-07-02
---

# Interaction Design

## Key Takeaways

- Interaction is a conversation: the user states an intent, the system replies with feedback, and every silent failure or opaque error is the system breaking its turn (Norman, 2013).
- Two gulfs divide user and system — the **gulf of execution** (can the user figure out what to do?) and the **gulf of evaluation** (can the user tell what happened?). Design closes both (Norman, 2013).
- **Affordances** are what an element suggests it can do; **signifiers** signal where the affordance lives. A button-shaped thing affords pressing; its label + style signify it. Without signifiers, affordances are invisible.
- **Feedback** confirms every action — received, in progress, succeeded, or failed — within a time the user can associate with the action. No feedback is itself a (broken) message.
- Errors are designed, not afterthoughted: **prevent** (constrain, confirm, default safely), **detect** (validate early, clearly), **recover** (an actionable message + a path forward). A good error often matters more than a smooth success.
- **Consistency** + **one primary action per screen** + **progressive disclosure** (show the common case, hide the rest behind a deliberate reveal) are the load-bearing heuristics; Nielsen's ten is the fuller canon (Nielsen, 1994).

## Concepts

**The conversation model.** Norman (2013) frames interaction as a dialogue: the user acts on a mental model of the system, the system responds, and the user updates the model from the response. A silent failure breaks the dialogue — the user's turn goes unanswered. An opaque error breaks it too — the reply is in a language the user cannot act on. The designer's job is to keep the dialogue coherent: every user action gets a system reply the user can interpret.

**The two gulfs.** The gulf of execution is the distance between the user's intent and the actions the system offers — closed by discoverable, signified affordances and by matching the interface to the user's vocabulary, not the developer's. The gulf of evaluation is the distance between the system's state and the user's understanding of it — closed by legible state, continuous feedback, and results that read in the user's terms. Most "usability" problems sit in one gulf or the other (Norman, 2013).

**Affordance and signifier.** An affordance is the possible action an object suggests (a flat plate affords pushing; a link affords clicking). A signifier is the perceptible cue that tells the user where the affordance is — the word "Push," the underlined blue text, the button shape. Digital interfaces have weak natural affordances, so signifiers carry the load; removing them (a flat grey rectangle that is somehow a button) is a common failure.

**Feedback.** Every action deserves a reply, and the reply's latency sets its form: under ~100 ms feels immediate; ~1 s needs a "working" signal; over ~10 s needs progress + cancellation. The failure mode is not slowness but silence — a click that produces no visible change leaves the user unsure whether the system heard, is working, has failed, or has succeeded.

**Designed errors.** The prevent→detect→recover sequence is the discipline. Prevent by constraining input (a date picker over free text), confirming destructive acts, and choosing safe defaults. Detect by validating as early as possible (client-side, at the field, not after a round trip) and reporting precisely. Recover by making the message actionable — name the problem in the user's terms, show the path to fix it, and preserve the user's work. A "something went wrong" toast is a designed error that failed its design.

**Heuristics and structure.** Nielsen's ten heuristics (visibility of system status, match between system and real world, user control and freedom, consistency and standards, error prevention, recognition over recall, flexibility and efficiency, aesthetic and minimalist design, help users recognise and recover from errors, help and documentation) remain the working canon (Nielsen, 1994). In practice the load-bearing three are consistency (the same action looks and behaves the same way everywhere), one primary action per screen (the user always knows what to do next), and progressive disclosure (the common path is uncluttered; the rest is reachable but not in the way).

## Content

### Closing the two gulfs

| Gulf | Question | Closed by |
|---|---|---|
| execution | "can I figure out what to do?" | signified affordances; the user's vocabulary; one clear primary action |
| evaluation | "can I tell what happened?" | legible state; feedback on every action; results in the user's terms |

### Nielsen's ten heuristics (the canon)

Visibility of system status · match between system and real world · user control and freedom · consistency and standards · error prevention · recognition rather than recall · flexibility and efficiency of use · aesthetic and minimalist design · help users recognise, diagnose, and recover from errors · help and documentation (Nielsen, 1994).

### Error design — prevent, detect, recover

| Layer | What the designer does |
|---|---|
| prevent | constrain input; confirm destructive acts; safe defaults; make the wrong action hard |
| detect | validate early and precisely; report at the point of error, not after a round trip |
| recover | actionable message in the user's terms; a visible path to fix; preserve the user's work |

### Progressive disclosure

Show the common case by default; reveal complexity only when the user asks for it (a "show advanced" toggle, a `--verbose` flag, a secondary panel). The principle is parsimony at the surface: the user pays attention only to what their current goal needs.

## Related

- [[design/visual-design]] — signifiers and hierarchy are visual; the two work together
- [[design/accessibility]] — a gulf the user cannot cross alone (perception, motor, cognition) is closed by accessible design
- [[design/cli-design]] · [[design/api-design]] — interaction for the terminal and HTTP surfaces
