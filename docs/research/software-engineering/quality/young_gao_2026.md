# Production Secrets Management: From .env to Vault (young_gao, 2026)

## Citation
young_gao (2026). "Production Secrets Management: From .env Files to HashiCorp Vault (and Beyond) (2026 Guide)." *DEV Community*, 21 March 2026.
URL: https://dev.to/young_gao/production-secrets-management-from-env-files-to-vault-and-beyond-cp1

## Method
Practitioner guide (engineering blog, dev.to).

## Confidence
Medium-High — the bootstrap-once / explicit-dependency pattern recurs across the source set.

## Key Insight
`.env` for development, a secrets manager for production; the application bootstraps secrets once at startup into an immutable config object and passes it as an explicit dependency — it never reaches for a global `process.env`/`os.environ` accessor throughout the codebase.

## Core Findings
1. `.env` is a developer-machine convenience and a production liability (unencrypted, no ACL, no audit trail, no rotation).
2. Read secrets once at startup into a frozen config object; pass it explicitly to the components that need it.
3. Scattering `process.env.X` / `os.environ["X"]` across the codebase defeats audit, rotation, and testing.
4. Build-time secret baking (into an image or bundle) is forbidden; runtime injection is the rule.
5. Dual-credential rotation (old stays valid while new propagates) lets the app retry on auth failure without restart.
6. Namespace secrets per environment; never reuse a credential across staging and production.

## Mechanism
A bootstrap function resolves every secret the process needs (from `.env` locally, a manager in production), constructs a frozen config object, and the rest of the application receives that object as a constructor argument. Because the object is the single read site, every place a secret is used is greppable; because it is immutable, it cannot be mutated mid-flight; because nothing reads the global env ad hoc, rotating a secret is a bootstrap-time change, not a codebase-wide chase.

## Relevance
Grounds the typed-frozen-Settings-loaded-once-passed-explicitly pattern and the maturity ladder in `secrets-and-config`. The frozen `Settings` constructed in `from_env()` is the object form of this article's bootstrap config.

## Related Research
env.dev, 2026; Heigh, 2023; Niessen, 2026.
