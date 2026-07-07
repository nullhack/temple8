---
name: design-interaction
description: "Design the interaction + feedback + error flows for a user-facing surface (CLI, API, or web). On-demand — run when the ux-engineer is consulted on an interaction contract."
---

# Design Interaction

1. Load [[design/interaction-design]], [[design/accessibility]] — the conversation model, the two gulfs, feedback + error design, and the accessibility floors that apply to every interaction.
2. Identify the surface (CLI / HTTP API / web UI) and load its surface-specific knowledge: [[design/cli-design]] for a terminal, [[design/api-design]] for an HTTP service, [[design/visual-design]] for a graphical surface.
3. State the user's goal for the surface in one sentence, then list the flows that reach it — including the recovery path from each error. A flow is a contract, not a happy path; the error paths are designed here, not deferred.
4. Design the feedback for every action: received, in progress, succeeded, failed — within a latency the user can associate with the action. Close the gulfs of execution (signified affordances, the user's vocabulary, one primary action) and evaluation (legible state, results in the user's terms).
5. Design the errors along prevent → detect → recover: constrain input to prevent; validate early to detect; write an actionable, in-the-user's-terms message with a fix path to recover. Never ship a flow whose error paths have not been designed.
6. Verify the accessibility floor: keyboard reachability + visible focus (graphical), contrast per WCAG 2.2, color never the sole signal, semantic markup. IF a flow fails the floor THEN fix the design before handoff.
7. Document the interaction contract: the flows, the feedback at each step, and the error catalog. Hand to the implementer; the contract, not a Figma file, is the source.
