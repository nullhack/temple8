"""Strip docstrings from Python source files (surgical, line-range based).

Used by the tdd `select` state to naked a target source `.py` at cycle entry,
removing docstrings carried over from the last merge's generation pass. Tests
and stubs are never passed through here — they stay naked permanently.

The edit is line-range only: each docstring's `[lineno, end_lineno]` is removed
and every other line (formatting, comments, blank lines) is preserved, so the
file does not get reformatted as a side-effect. Assumes bodies are not
docstring-only (true for real rework `.py`); a docstring-only body would need a
`pass` substituted, which this script does not do.
"""

import ast
import sys
from pathlib import Path

_NODE_TYPES = (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)


def _docstring_ranges(source: str) -> list[tuple[int, int]]:
    tree = ast.parse(source)
    ranges: list[tuple[int, int]] = []
    for node in ast.walk(tree):
        if isinstance(node, _NODE_TYPES) and node.body:
            first = node.body[0]
            if (
                isinstance(first, ast.Expr)
                and isinstance(first.value, ast.Constant)
                and isinstance(first.value.value, str)
            ):
                ranges.append((first.lineno, first.end_lineno))
    return ranges


def strip_file(path: Path) -> int:
    source = path.read_text(encoding="utf-8")
    ranges = _docstring_ranges(source)
    if not ranges:
        return 0
    lines = source.splitlines(keepends=True)
    for start, end in sorted(ranges, reverse=True):
        del lines[start - 1 : end]
    path.write_text("".join(lines), encoding="utf-8")
    return len(ranges)


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("usage: strip_docstrings.py <file> [...]", file=sys.stderr)
        return 2
    stripped = 0
    for arg in argv[1:]:
        n = strip_file(Path(arg))
        if n:
            print(f"stripped {n} docstring(s) from {arg}")
            stripped += n
    return 0 if stripped >= 0 else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
