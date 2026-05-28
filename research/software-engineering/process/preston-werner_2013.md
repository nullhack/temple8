# Semantic Versioning 2.0.0 (Preston-Werner, 2013)

## Citation

Preston-Werner, T. (2013). Semantic Versioning 2.0.0. https://semver.org

## Source Type

Specification

## Method

Theoretical

## Verification Status

Verified

## Confidence

High

## Key Insight

Version numbers follow MAJOR.MINOR.PATCH format encoding compatibility intent to enable automated dependency resolution and prevent dependency hell.

## Core Findings

1. **Three-Part Versioning**: MAJOR.MINOR.PATCH where MAJOR for incompatible API changes, MINOR for backward-compatible additions, PATCH for backward-compatible bug fixes
2. **Build Metadata Independence**: Build metadata (after `+`) provides arbitrary information without affecting version precedence - `1.0.0+20260430` and `1.0.0` have same precedence
3. **Pre-release Ordering**: Pre-release versions (after `-`) have lower precedence than normal versions: `1.0.0-alpha < 1.0.0`
4. **Dependency Resolution**: Enables automated package management with range specifications like `>=3.1.0 <4.0.0` preventing dependency hell
5. **Public API Declaration**: Requires clear, precise public API definition as foundation for meaningful version communication

## Mechanism

SemVer encodes compatibility intent in version number itself. MAJOR increments signal breaking changes requiring consumer updates; MINOR increments signal safe additions; PATCH increments signal safe fixes. Build metadata suffix (§10) allows arbitrary data (dates, commit hashes) without affecting dependency solver precedence calculations.

## Relevance

De facto standard for software versioning, essential for package management systems (npm, pip, Maven), continuous integration, API evolution communication. Foundational for dependency resolution algorithms, semantic release automation, software distribution strategies.

## Related Research

Created by Tom Preston-Werner (GitHub co-founder, Gravatar inventor) in 2013. Based on widespread existing practices in open/closed-source software. Influences modern package managers, CI/CD systems, release automation tools. Licensed under Creative Commons CC BY 3.0, maintained as open specification.