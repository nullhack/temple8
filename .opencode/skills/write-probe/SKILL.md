---
name: write-probe
description: "Author the minimal authenticated probe script that exercises one success path and one error path against the real service, without executing it."
---

# Write Probe

1. Load [[software-craft/external-fixtures]] — probe patterns and the kind-dispatch table.
2. Translate the researched access shape into the real working call sequence. Cover one success path and at least one representative error path.
3. Pull credentials from the 12-factor environment (a dotenv `.env` locally); never hardcode them.
4. Keep the script throwaway — reference for the capture step and the later implementer. IF the package or tests could import it THEN move it out — it is never imported.
5. Do not execute the script here; capturing the exchange is the next step's job.
