# Software and Systems Traceability (Cleland-Huang, Gotel & Zisman, 2012)

## Citation

Cleland-Huang, J., Gotel, O. & Zisman, A. (eds.) (2012). *Software and Systems Traceability.* Springer. ISBN 978-1-4471-2238-8 (print) / 978-1-4471-2239-5 (ebook). 494 pages. DOI 10.1007/978-1-4471-2239-5.
URL: https://link.springer.com/book/10.1007/978-1-4471-2239-5

## Method

Edited academic reference volume.

## Confidence

High — the canonical reference on software traceability.

## Key Insight

A traceability matrix correlates two baselined artifacts many-to-many by marking intersecting cells; an empty row or column is a gap (no relationship), and a densely filled cell is over-complexity to simplify — and it must be built as the work proceeds, not reconstructed at the end.

## Core Findings

1. A trace is a relationship between two artifacts (a requirement and its test, a design and its code).
2. The matrix maps requirements forward to design, code, and test; coverage is read off the marked cells.
3. An empty row (a requirement with no test) is a gap; an empty column (a test with no requirement) is an orphan; a dense cell signals over-complexity.
4. Traceability captured during the work survives; traceability reconstructed afterward does not.

## Mechanism

The matrix is a grid whose rows and columns are two artifact sets and whose cells record the existence of a relationship; reading the grid's empties surfaces what was forgotten, and reading its density surfaces what was over-built. Because the traces degrade the moment they are divorced from the act of building, the matrix is maintained as a by-product of the work rather than as a separate documentation task.

## Relevance

Grounds gap analysis as a coverage matrix at the building-blocks funnel level: every bounded context maps to at least one building block, every quality attribute to at least one — the empties are elicited into rather than silently filled.

## Related Research

- Wiegers (Software Requirements — the RTM as a requirements-management tool)
