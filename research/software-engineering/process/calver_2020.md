# Calendar Versioning (CalVer, 2020)

## Citation

CalVer (2020). Calendar Versioning. https://calver.org

## Source Type

Specification

## Method

Theoretical

## Verification Status

Verified

## Confidence

High

## Key Insight

Date-based version segments communicate release timing directly, suitable for projects with large/constantly-changing scope or time-sensitive releases.

## Core Findings

1. **Family of Schemes**: Not single scheme but flexible framework - YY.MINOR.MICRO (pip), YYYY.MM.DD (certifi), YY.0M (OpenSCAD)
2. **Standard Terminology**: YYYY/YY/0Y (year), MM/0M (month), WW/0W (week), DD/0D (day) segments
3. **Wide Adoption**: Ubuntu, Twisted, youtube-dl, pip, PyCharm, Unity, LibreOffice, OpenSCAD, Stripe API
4. **Compatibility Limitation**: CalVer alone doesn't signal breaking changes - some projects use hybrid SemVer+CalVer approach
5. **Three Key Use Cases**: Large/changing scope systems, time-sensitive releases, external-change-driven projects

## Mechanism

CalVer replaces arbitrary version increments with calendar-derived segments using Gregorian calendar and UTC convention. Date segments are 1-based (unlike traditional 0-based incremented versions) with short/zero-padded years relative to year 2000. Projects choose appropriate scheme based on release patterns and communication needs.

## Relevance

Essential for projects with time-based releases, security updates, business support schedules, large system coordination. Applied in operating systems, frameworks, security libraries, API versioning. Alternative to SemVer when semantic meaning is less relevant than temporal context.

## Related Research

Connects to (Preston-Werner, 2013) on Semantic Versioning as alternative approach. Part of broader software versioning strategies including hybrid approaches. Related to release management, dependency management, and software lifecycle practices.