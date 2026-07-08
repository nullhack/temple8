"""Strip docstrings from Python source files.

Deletes each docstring's `[lineno, end_lineno]` from the bottom up; every other
line (formatting, comments, blanks) is preserved — no reformat. Accepts many
files, edits each in place. Stubs (`.pyi`) are skipped by the caller's
`-name '*.py'` glob; `PYI021` handles them in lint. Assumes bodies are not
docstring-only.
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
