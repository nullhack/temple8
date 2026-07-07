# Environment Variables Don't Keep Secrets (Heigh, 2023)

## Citation
Heigh, S. (2023). "Environment Variables Don't Keep Secrets: Best Practices for Plugging Application Credential Leaks." *CyberArk Developer Blog*, 25 January 2023.
URL: https://developer.cyberark.com/blog/environment-variables-dont-keep-secrets-best-practices-for-plugging-application-credential-leaks/

## Method
Practitioner article (security-vendor engineering blog).

## Confidence
High — the leak vectors it names are mechanically verifiable on any Linux host.

## Key Insight
Environment variables are a convenient but structurally leaky secret store; a credential reachable as an env var is exposed through several well-known, unavoidable vectors, so env vars should not be treated as a secrets-management solution.

## Core Findings
1. Every process running under the same user can read another's environment.
2. `/proc/<pid>/environ` exposes a process's full environment to the same-user reader.
3. Child processes inherit the entire environment by default.
4. Crash dumps, APM agents, and error trackers routinely capture the environment.
5. Env vars offer no access control, no audit trail, and rotation requires a redeploy.

## Mechanism
A secret placed in `os.environ` ceases to be scoped to the code that needs it; it is now a property of the process, visible to anything that can introspect the process or any descendant it spawns. The exposure is not a bug in any one tool but a property of the environment-variable mechanism itself. The mitigation is to narrow the surface — keep secrets out of the process environment (a file mounted outside it, or a secrets manager that returns the value on demand) so the vectors above do not apply.

## Relevance
Grounds the "why environment variables leak" mechanics and the threat-model vectors V1–V5 in `secrets-and-config`. The out-of-workspace file + `dotenv_values()` (dict, not `os.environ`) approach is a direct application of the article's narrowing prescription.

## Related Research
Wiggins, 2011; Niessen, 2026; env.dev, 2026.
