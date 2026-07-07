# The Twelve-Factor App — Config (Wiggins, 2011)

## Citation
Wiggins, A. (2011). "The Twelve-Factor App — III. Config." 12factor.net.
URL: https://12factor.net/config

## Method
Methodology / practitioner guideline (the Heroku-era twelve-factor codification).

## Confidence
High — foundational and widely cited across languages and platforms.

## Key Insight
Configuration that varies between deploys belongs in environment variables, kept strictly separate from code; the same code artifact runs across every deploy, with config injected at run time.

## Core Findings
1. An app factors as code (the same across deploys) plus config (what varies).
2. Environment variables are the universal, language- and OS-agnostic config interface.
3. Config must never be checked into version control alongside code.
4. The separation preserves deploy portability and lets the same artifact run dev/staging/prod.

## Mechanism
The config factor draws the boundary at the process environment: the deploy platform (or the developer's shell) injects variables, and the application reads them through the standard library (`os.environ`, `process.env`). Code stays deploy-agnostic; deploy-specifics live entirely in the surrounding environment. This predates and enables the entire modern config-injection surface (Docker `-e`, Kubernetes ConfigMaps/Secrets, serverless env).

## Relevance
Grounds the twelve-factor baseline in `secrets-and-config`: the principle that non-secret configuration belongs in environment variables. The knowledge splits this from secrets because the original prescription predates the modern critique of `os.environ` as a secret store (see Heigh, 2023; Niessen, 2026) — the principle (separate config from code) holds; the literal mechanism (everything in env vars) does not, for secrets.

## Related Research
Heigh, 2023; Niessen, 2026; env.dev, 2026.
