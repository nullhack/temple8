# python-dotenv (theskumar)

## Citation
python-dotenv (maintained by Saurabh Kumar, GitHub `theskumar`; originally by Théo Attalah, `bbc2`). Current release v1.2.0.
URL: https://github.com/theskumar/python-dotenv · Reference: https://bbc2.github.io/python-dotenv/reference/

## Method
Library documentation / source (the canonical API reference for the load functions this workflow depends on).

## Confidence
High — the function semantics below are quoted from the library's own docstrings.

## Key Insight
`python-dotenv` exposes two distinct loaders: `load_dotenv()` mutates `os.environ`, while `dotenv_values()` returns a dict and leaves the environment untouched — the second is the correct loader when the values are secrets.

## Core Findings
1. `load_dotenv(dotenv_path=None, ..., override=False) -> bool` — parses a `.env` file and loads every variable found **as an environment variable**.
2. `dotenv_values(dotenv_path=None, ...) -> Dict[str, Optional[str]]` — parses a `.env` file and returns its content **as a dict**, without touching the environment.
3. By default `load_dotenv()` does not override variables already present in the environment (`override=False`).
4. The two compose: `dotenv_values(".env.shared")` + `dotenv_values(".env.secret")` + `os.environ` for a layered, override-ordered config dict (the library README's own example).
5. A key with no value (`FOO`) parses to `{"FOO": None}` under `dotenv_values`; `load_dotenv` ignores such keys.

## Mechanism
Both functions parse the same file format (key=value lines, optional quoting, POSIX expansion, comments). They diverge at the output boundary: `load_dotenv` writes into the live process environment (inherited by every child, visible in `/proc`, capturable by crash dumps); `dotenv_values` returns a fresh mapping that the caller controls — it can be handed to a frozen dataclass and never reach `os.environ`. The choice of loader is therefore a choice of exposure surface.

## Relevance
Grounds the load-bearing API distinction in `secrets-and-config`: `dotenv_values()` (not `load_dotenv()`) for secrets, because it keeps the value out of the process environment the agent could introspect. The library's own README demonstrates exactly the two-file layered-dict pattern the knowledge prescribes.

## Related Research
Heigh, 2023 (why the distinction matters); env.dev, 2026 (the typed-config wrapper that consumes the dict).
