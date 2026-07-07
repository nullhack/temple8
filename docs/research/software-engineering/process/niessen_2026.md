# The 12-Factor App, 15 Years Later (Niessen, 2026)

## Citation
Niessen, L. (2026). "The 12-Factor App — 15 Years Later. Does it Still Hold Up in 2026?" *ITNEXT*, 12 February 2026.
URL: https://itnext.io/the-12-factor-app-15-years-later-does-it-still-hold-up-in-2026-c8af494e8465

## Method
Practitioner reassessment (independent retrospective on the twelve-factor methodology).

## Confidence
Medium-High — the author's claims corroborate Heigh (2023) and the Kubernetes SIG guidance.

## Key Insight
The core principle — separate configuration from code, with the same artifact plus config equalling a deployment — remains sound; the literal prescription to use environment variables exclusively shows its age, because env vars leak into logs, crash dumps, child processes, and `/proc`.

## Core Findings
1. The config factor is overly specific about environment variables as the mechanism.
2. For sensitive configuration, files mounted outside the process environment are preferable to env vars.
3. Kubernetes models this as ConfigMaps and Secrets, mountable as either env vars or files.
4. GitOps keeps the configuration-of-record in a separate Git repository; injection still happens at deploy time.
5. The underlying idea (separate config from code) is as solid as ever; only the "env vars only" literalism dates it.

## Mechanism
Env vars share exposure paths the original twelve-factor author did not weigh: process-tree inheritance, `/proc/<pid>/environ`, and capture by observability tooling. A file mounted into the container/filesystem without being placed in the process environment — or a secrets manager returning a value on demand — removes those paths while preserving the config/code separation that is the actual point of the factor.

## Relevance
Grounds the "files over env vars" insight and the "twelve-factor predates the critique" framing in `secrets-and-config`. It legitimizes the out-of-workspace `~/.secrets/<project>.env` file (a config file mounted outside the process environment, read with `dotenv_values`) as the modern reading of the config factor for the secret case.

## Related Research
Wiggins, 2011; Heigh, 2023; env.dev, 2026.
