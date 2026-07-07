---
name: select-external-target
description: "Pick the next external service to probe by subtracting already-captured services from those the interview named."
---

# Select External Target

1. Enumerate every external service the interview named; cross-check against services that already have a committed cassette.
2. Subtract the captured set from the named set. IF the interview named none THEN pass straight through (no external services). IF any remain THEN pick the single one at the lowest layer (external boundary before adapter) and record the choice as the handoff; IF none remain THEN signal completion.
3. Enumerate only true external dependencies — third-party APIs/SaaS and external managed stores — not databases designed in-project or UI defined in-project. This state does no probing and captures no cassette; it only selects.
