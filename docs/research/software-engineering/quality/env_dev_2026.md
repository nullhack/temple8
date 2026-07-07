# Environment Variable Best Practices & Security (env.dev, 2026)

## Citation
env.dev (2026). "Environment Variable Best Practices" (29 April 2026) and "Env Variables Security: Secrets, Leaks & Best Practices" (12 April 2026).
URL: https://env.dev/guides/env-vars-best-practices · https://env.dev/guides/env-vars-security

## Method
Editorial / practitioner reference (site), grounded in cited incidents (Toyota 2017–2022, Uber 2022) and the GitGuardian 2024 State of Secrets Sprawl report.

## Confidence
High — concrete, incident-referenced; the hygiene rules recur across independent sources.

## Key Insight
Environment variables are the universal configuration interface and one of the largest single sources of production secret leaks; a small set of unglamorous, well-documented hygiene rules prevents most incidents.

## Core Findings
1. `.gitignore` `.env`, `.env.local`, `*.pem`, `*.key` from the first commit, not after.
2. Run a pre-commit secret scanner (gitleaks, detect-secrets, git-secrets) as a mandatory hook.
3. Validate every required variable at startup (fail-fast with a clear error).
4. Wrap env access in a typed configuration object; do not scatter raw `os.environ` reads.
4. `.env` is for local development only — no encryption at rest, no ACL, no audit, no rotation.
5. `chmod 600 .env`; never `COPY .env .` into a build artifact.
6. If a secret was committed, rotate immediately — history scrubbing cannot un-leak.
7. The maturity ladder: plain `.env` → encrypted files (SOPS, git-crypt) → dedicated secrets manager.

## Mechanism
Each rule maps to a real failure mode: the gitignore rule to the committed-key incident; the scanner to the same; fail-fast to the cryptic late-stage crash; the typed wrapper to un-auditable scattered access; the no-production rule to the plaintext-on-disk liability. Together they shrink the surface at every stage from authoring to deployment.

## Relevance
Grounds the hygiene layer (fail-fast validation, typed Settings, `.env.example` as the committed contract, the gitleaks CI step) and the maturity ladder in `secrets-and-config`.

## Related Research
Heigh, 2023; Wiggins, 2011; young_gao, 2026; Niessen, 2026.
