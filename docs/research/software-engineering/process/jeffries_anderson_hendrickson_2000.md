# Extreme Programming Installed (Jeffries, Anderson & Hendrickson, 2000)

## Citation

Jeffries, R., Anderson, A. & Hendrickson, C. (2000). *Extreme Programming Installed.* Addison-Wesley Professional (XP Series), published 16 Oct 2000 (copyright 2001). ISBN 0-201-70842-6 (ISBN-13 978-0-201-70842-4). 288 pages. Foreword by Kent Beck.
URL: https://www.informit.com/store/extreme-programming-installed-9780201708424

## Method

Practitioner book; connected collection of essays by three participants in the DaimlerChrysler (C3) XP project.

## Confidence

High — a primary XP source.

## Key Insight

XP's practices — test-first, simple design, continuous refactoring, small releases, pair programming — co-evolve; the simplest design that could possibly work, built test-first and refactored as understanding grows, beats speculative generality bought against an uncertain future.

## Core Findings

1. Write the test first, by intention; it drives both the interface and the confidence to change the code later.
2. Implement the simplest thing that could possibly pass the test.
3. Refactor continuously — improve structure under green tests, every cycle.
4. You Aren't Gonna Need It: do not build for a future the present test does not justify.

## Mechanism

Test-first forces a statement of intent before the implementation, which produces interfaces a caller actually wants; simple design keeps the code legible so the next change is cheap; continuous refactoring pays down the design debt that simple-design-for-today accrues; YAGNI blocks the speculative structure that would otherwise accumulate. The practices reinforce one another, so dropping one weakens the rest.

## Relevance

Grounds the YAGNI and simple-design discipline cited in the workflow's design decisions: KISS/YAGNI first, the simplest structure that removes the smell, no speculative patterns.

## Note on the citation

Earlier knowledge citations read "Beck & Jeffries 1999", which is inaccurate: Kent Beck is not an author of this book (he wrote the foreword). Beck's own XP work is *Extreme Programming Explained: Embrace Change* (Addison-Wesley, 1999, ISBN 0-201-61641-6) — a different book. Citations in the knowledge files should read "Jeffries, Anderson & Hendrickson 2000" for this work, or "Beck 1999" if *XP Explained* was the intended source.

## Related Research

- Beck 2002 (test-driven development)
- Fowler 1999 (refactoring)
