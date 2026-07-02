---
domain: software-craft
tags: [secrets, config, 12-factor, dotenv, credentials, llm-agent-security]
last-updated: 2026-07-02
---

# Secrets and Configuration

## Key Takeaways

- **Config is not secrets.** Twelve-factor env vars (Wiggins, 2011) are the right home for ordinary configuration — base URLs, feature flags, regions. Secrets (API keys, tokens, passwords) carry a different risk and need different handling: readable by any process under the user, leaked into `/proc/<pid>/environ`, crash dumps, and child processes, leaving no audit trail and no rotation without a redeploy (Heigh, 2023; Niessen, 2026).
- **The LLM agent is the threat surface this workflow adds.** An agent with Bash and Read tools that authors the probe and the adapter can read a workspace file, run `env` / `printenv`, introspect `os.environ`, read `/proc/<pid>/environ`, or `print()` a credential in code it writes — and anything it reads lands in the session transcript. Instruction alone does not bind it (a fetched page can prompt-inject past it). The defense is layered attack-surface reduction, not a guarantee.
- **Secrets live outside the workspace** at `~/.secrets/<project>.env`, never in the repo tree. opencode's `external_directory` permission set to `ask` on `~/.secrets/**` turns a silent read into a user prompt; the in-process `dotenv_values()` load the agent's own code performs does not trigger it (subprocess file I/O is not intercepted), so the legitimate path runs clean and only direct snooping is gated.
- **Read secrets with `dotenv_values()`, never `load_dotenv()`.** `load_dotenv()` mutates `os.environ` — the surface `env`, `printenv`, and `/proc` expose; `dotenv_values()` returns a dict and leaves the process environment untouched, feeding a frozen typed Settings directly and keeping secrets scoped to one object, never the global env (python-dotenv, theskumar).
- **The agent never creates, reads, or debugs a secret.** It instructs the user how to obtain and place each credential (provider, scope, the exact `~/.secrets/<project>.env` line), and on an auth failure it stops and asks with concrete suggestions instead of investigating the value. This applies to secrets only; ordinary debugging is unchanged.
- **A committed `.env.example` is the env contract.** It lists every variable name, fills non-secret defaults, and leaves secret lines empty with a pointer to `~/.secrets/`. The cassette scrub ([[software-craft/external-fixtures]]) is the explore-time guard; a gitleaks CI step is the push-time guard.

## Concepts

**Config is not secrets.** Twelve-factor (Wiggins, 2011) codified "store config in the environment" — everything that varies between deploys. That holds for ordinary configuration, but the industry has stepped back from treating secrets as just more env vars: a secret in `os.environ` is unencrypted, readable by every process under the same user, visible in `/proc/<pid>/environ`, captured by crash dumps and error trackers, inherited by every child process, and impossible to audit or rotate without a redeploy (Heigh, 2023; env.dev, 2026; Niessen, 2026). The fix is not to abandon twelve-factor but to split it: non-secret config stays in the workspace `.env`; secrets take a harder path.

**The LLM agent is the threat surface this workflow adds.** A human developer who mishandles a secret is a known problem with known defenses. This workflow adds a new actor: an LLM agent with Bash and Read tools that authors the probe script and the adapter implementation. Such an agent can `Read` a workspace file, `cat` a path, run `env` or `printenv`, execute `python -c "import os; print(os.environ)"`, read `/proc/self/environ`, or `print()` a credential in code it writes — and anything it reads lands in the transcript. Instruction ("do not print secrets") is a soft guard. The defense is layered surface reduction, and the honest caveat is that it is not a guarantee.

**Secrets live outside the workspace.** Placing the secrets file at `~/.secrets/<project>.env` — outside the repo tree — does three things at once: it cannot be committed accidentally (a path outside the repo is never staged); it sits outside the directory the agent normally enumerates; and it falls under opencode's `external_directory` permission, which an instance configures to `ask` on `~/.secrets/**`. The mechanical gate is the point: a direct `Read` or `bash: cat` of that path triggers a user prompt, while the legitimate `dotenv_values()` call inside the probe subprocess does not, so the probe runs clean and only direct snooping is gated.

**Read secrets with `dotenv_values()`, never `load_dotenv()`.** python-dotenv exposes two loaders (python-dotenv, theskumar). `load_dotenv()` parses the file and sets each value into `os.environ` — the exact surface that `env`, `printenv`, and `/proc/<pid>/environ` expose. `dotenv_values()` parses the same file and returns a dict without touching the environment. The two-file pattern composes them: `load_dotenv()` for the workspace `.env` (non-secret; `os.environ` exposure is acceptable) and `dotenv_values("~/.secrets/<project>.env")` for secrets, the result handed straight to a frozen Settings and never to `os.environ`. This is the single most effective mechanical change: even an agent that runs `env` sees nothing.

**The agent never creates, reads, or debugs a secret.** Because the agent cannot be fully bound by instruction, the procedural rule removes both the temptation and the need: the agent names each secret variable and tells the user how to obtain and place it (which provider, what scope, the exact line in `~/.secrets/<project>.env`); it never generates a credential, never writes a secrets file, never reads one to "check." When a probe or an auth-dependent test fails on credentials, the agent does not investigate the secret — it stops and asks, with concrete suggestions (the key may be wrong, expired, scoped too narrowly, or the variable may be unset). This applies to secrets only; ordinary connectivity or shape debugging is unchanged.

**Defense in depth, not a guarantee.** No single layer suffices. The layered set — out-of-workspace location, permission gate, `dotenv_values()` over `load_dotenv()`, frozen typed Settings, reference-by-name in code, cassette scrub at explore ([[software-craft/external-fixtures]]), and a gitleaks scanner at push — shrinks the surface at every stage. Process introspection (`env`, `/proc`) is the residual vector if a secret ever does reach `os.environ`; `dotenv_values()` is what keeps it from reaching there.

## Content

### Config is not secrets: the split and the maturity ladder

Non-secret configuration belongs in the workspace `.env`, gitignored, loaded with `load_dotenv()` so ordinary code can read it through `os.environ` or a typed Settings. The maturity ladder for the harder case — secrets — runs from a local `.env` (acceptable for local development only), through encrypted files (SOPS, git-crypt, dotenvx) for version-controlled team sharing, to a dedicated secrets manager (Vault, AWS/GCP/Azure Secrets Manager, Doppler, Infisical) for production (env.dev, 2026; young_gao, 2026). This workflow's concern is the local-development tier the explore and build phases run in: real credentials hit real services once, locally, and the rest is replay. Production secret provisioning is the platform's job, not the pipeline's.

### Why environment variables leak

The mechanics are concrete. On Linux every process's environment is exposed at `/proc/<pid>/environ`, readable by the same user; child processes inherit the full set by default; crash dumps, APM agents, and error trackers routinely capture it; and any command the agent runs (`env`, `printenv`, `python -c "import os; ..."`) reads it (Heigh, 2023; Niessen, 2026). The twelve-factor prescription predates these concerns and was always about separation of config from code, not about secrecy (Niessen, 2026). For sensitive values, a file mounted outside the process environment — or a secrets manager — is the recommended shape, because it does not share these exposure paths (Niessen, 2026).

### The LLM-agent threat model

| # | Vector | Example | Primary defense |
|---|---|---|---|
| V1 | Direct file read | `Read .env`, `cat ~/.secrets/x.env` | out-of-workspace location + `external_directory` ask |
| V2 | Code exfil | `print(os.environ["KEY"])` in probe/adapter | `dotenv_values()` (secret never in `os.environ`); reference-by-name; cassette scrub |
| V3 | Process introspection | `env`, `printenv`, `/proc/<pid>/environ` | `dotenv_values()` (secret never in `os.environ`) |
| V4 | Commit leak | secret in `.env`, cassette, or source → pushed | `.gitignore`; cassette scrub (explore); gitleaks (CI) |
| V5 | Log / error leak | secret in a stack trace or fail message | fail-fast validation; no secret in the message |

V3 is the residual risk if a secret ever reaches `os.environ`; `dotenv_values()` is the layer that keeps it from reaching there.

### The layered defense

| Layer | Closes | How |
|---|---|---|
| Out-of-workspace `~/.secrets/<project>.env` | V1, V4 (file) | outside the repo tree; never staged |
| opencode `external_directory: {"~/.secrets/**": "ask"}` | V1 | direct Read / bash-cat triggers a user prompt |
| `dotenv_values()` for secrets | V2, V3 | secret stays in a scoped dict, never `os.environ` |
| Frozen typed Settings, loaded once, passed explicitly | V2, V5 | one immutable object; no scattered `os.environ` access (young_gao, 2026) |
| Reference-by-name in code | V2 | the agent's code names the variable, never the value |
| Cassette scrub ([[software-craft/external-fixtures]]) | V4 (cassette) | secrets stripped before commit at explore |
| gitleaks in CI | V4 (push) | last-line scan on every push |
| Agent rule: instruct / ask, never create or debug | V2 (debug path) | the agent never needs the value to troubleshoot |

### The dotenv mechanics: two files, two loaders

```python
from dataclasses import dataclass
from dotenv import dotenv_values, load_dotenv
import os

@dataclass(frozen=True)
class Settings:
    api_base: str
    api_key: str

    @classmethod
    def from_env(cls) -> "Settings":
        load_dotenv()  # workspace .env: non-secret config into os.environ
        secrets = dotenv_values(os.path.expanduser("~/.secrets/<project>.env"))
        api_base = os.environ.get("API_BASE", "https://default.example.com")
        api_key = secrets["API_KEY"]  # straight from the dict, never os.environ
        if not api_key:
            raise RuntimeError("API_KEY unset in ~/.secrets/<project>.env")
        return cls(api_base=api_base, api_key=api_key)
```

`load_dotenv()` is acceptable for the non-secret workspace file because exposure through `os.environ` is harmless for a base URL. `dotenv_values()` is mandatory for secrets: the value moves file → dict → frozen field, never through the process environment. The fail-fast check produces a message that names the variable and its location, never the value.

### The agent–secrets protocol

The rule is procedural and applies to secrets only. **Creating:** when a probe or adapter needs a credential, the agent states what to obtain (provider, scope), the exact line to add to `~/.secrets/<project>.env` (`VAR_NAME=`), and stops — it does not generate a key, does not write the file, does not read it to verify. **Failing:** when a probe run or an auth-dependent test fails on credentials, the agent does not read the secret, does not echo it, does not try alternate values — it stops and asks, with concrete suggestions (the key may be wrong, expired, scoped too narrowly, or the variable unset). The protocol exists because the agent cannot be fully bound by "do not look," so the workflow removes both the need and the opportunity.

### The committed `.env.example`

The discoverable contract for "what environment does this project need" is `.env.example`, committed: every variable NAME listed, non-secret defaults filled (`API_BASE=https://default.example.com`), secret lines empty with a pointer (`API_KEY=  # obtain from <provider>; place in ~/.secrets/<project>.env`). It carries no value that unlocks anything, so it is safe in version control, and a new contributor reads it once to know the full env shape.

## Related

- [[software-craft/external-fixtures]] — the cassette scrub is the explore-time commit guard; this knowledge is the lifecycle guard around it
- [[software-craft/source-stubs]] — the typed Settings is a normal source stub; its `from_env()` is where the two-file load lives
- [[software-craft/test-design]] — auth-dependent tests replay cassettes offline; they never need the live secret at test time
