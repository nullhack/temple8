---
name: write-probe
description: "Author the minimal authenticated probe script that exercises one success path and one error path against the real service, without executing it."
---

# Write Probe

1. Load [[software-craft/external-fixtures]] — probe patterns and the kind-dispatch table.
2. Translate the researched access shape into the real working call sequence. Cover one success path and at least one representative error path.
3. Pull secrets from `~/.secrets/<project>.env` via `dotenv_values()` — never `load_dotenv()` into `os.environ` (secrets stay scoped to the probe, off the process env); non-secret config (base URLs) comes from the workspace `.env`. Reference every secret by name; never print or log it. IF a secret the probe needs is not yet set up THEN instruct the user how to obtain and place it — do not create it. Per [[software-craft/secrets-and-config]].
4. Keep the script throwaway — reference for the capture step and the later implementer. IF the package or tests could import it THEN move it out — it is never imported.
5. Do not execute the script here; capturing the exchange is the next step's job.
