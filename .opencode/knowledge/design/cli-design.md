---
domain: design
tags: [cli-design, terminal-ux, stdout-stderr, exit-codes, progressive-disclosure, no-color]
last-updated: 2026-07-02
---

# CLI Design

## Key Takeaways

- A CLI has two audiences — a **human at a terminal** and a **script down a pipe** — and the default optimises for the human while giving the script an opt-in structured mode (`--json`) (clig.dev, 2024).
- **stdout carries payload; stderr carries diagnostics.** A pipeline that pipes stdout into another tool must never receive progress bars, log lines, or decoration (clig.dev, 2024).
- **Exit codes are first-class signals**: `0` for success; distinct non-zero codes for distinct failure modes, documented in `--help`. Scripts branch on them.
- **Errors are informative**: exit non-zero, write the message to stderr, and include the error code/title, what went wrong, and a suggested fix or URL — never a stack trace for a human audience.
- **Progressive disclosure**: strong defaults for the common case, every default overridable, simple things simple and hard things possible. The quiet default is the parsimony tie-in — a successful run prints little; verbosity is opt-in (`-v`, `--verbose`, `--debug`).
- **Color is for emphasis, not decoration**, stripped automatically when stdout is not a TTY or when `NO_COLOR` is set; symbols and emoji only where they aid scanning.

## Concepts

**Two audiences.** The same command is run interactively by a human and invoked by a script. The human wants formatted, colored, progressive output; the script wants a stable, parseable, minimal contract. The resolution is a default for the human and an opt-in for the machine: detect `isatty(stdout)`; emit formatted output to a terminal, structured output when `--json` (or `--output json`) is passed; strip ANSI codes either way when stdout is piped (clig.dev, 2024).

**The output contract.** stdout is the payload — the data the user asked for or the success message a script checks for. stderr is everything else: progress, warnings, diagnostics, errors. Mixing them puts decoration in the payload and breaks pipelines. Long human output goes through a pager (`less`); the machine path never does.

**Exit codes signal outcome.** A script's only reliable channel for branching is the exit code. `0` is success; non-zero is failure, and distinct non-zero codes for distinct failures (a usage error vs a permission error vs a not-found) let the script respond differently. Document the codes in `--help` so script authors can rely on them.

**Informative errors.** A CLI error is the user's only feedback channel — there is no GUI to expand a dialog. So the message carries the code/title, a one-line explanation in the user's terms, and a suggested fix or a documentation URL; it goes to stderr; the process exits non-zero. A raw Python traceback is a debugging aid for the author, not an error for the user.

**Progressive disclosure + parsimony.** The common case should work with no flags (strong defaults); every default is overridable; the `--help` shows the common case first and the advanced options later. Successful default runs are quiet — they print the result, or nothing, not a log of every step. Verbosity is a ladder: default (terse) → `-v` (what it did) → `--debug` (everything, for bug reports). This is the CLI form of the project's parsimony rule.

**Color, symbols, TTY.** Color directs attention (green success, red error) but is stripped when stdout is not a TTY or when `NO_COLOR` is set (the `NO_COLOR` convention is an industry standard). Symbols and emoji (✓, ✗) aid scanning in a terminal but must not be the only signal (screen readers, font fallback). Never block on color — the output must read in plain monochrome too.

## Content

### Output channels

| Channel | Carries | When |
|---|---|---|
| stdout | payload (the data; the success line) | always; the contract a script consumes |
| stderr | progress, warnings, errors, diagnostics | always; never piped into the next tool |
| exit code | outcome (`0` success; non-zero failure) | always; how scripts branch |

### The verbosity ladder

| Mode | Trigger | Output |
|---|---|---|
| quiet (default) | — | the result, or nothing on success |
| verbose | `-v` / `--verbose` | what the command did, one line per step |
| debug | `--debug` | everything, including internals, for bug reports |
| machine | `--json` / `--output json` | stable structured schema, no decoration |

### Error anatomy (to stderr, exit non-zero)

```
error: cannot connect to <host>: connection refused
  hint: check the host is reachable, or set API_BASE in ~/.secrets/<project>.env
  docs: https://<project>/docs/errors#connection
exit: 2 (network)
```

### Machine-readable mode

`--json` emits a documented, versioned schema; changing a field name is a breaking change. Strip ANSI + progress + symbols in this mode — the consumer is a parser, not an eye.

## Related

- [[design/interaction-design]] — feedback, errors, and progressive disclosure apply to the terminal surface
- [[design/accessibility]] — color-not-sole-signal, `NO_COLOR`, screen-reader-readable output
- [[software-craft/secrets-and-config]] — error hints point at `~/.secrets/`, never echo a value
