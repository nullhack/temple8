# Blameless Post-Mortems (Beyer et al., 2016)

## Citation

Beyer, B., Jones, R., Petoff, J., & Murphy, N. R. (2016). *Site Reliability Engineering: How Google Runs Production Systems*. O'Reilly Media. Chapter 15: "Postmortem Culture: Learning from Failure."

## Source Type

Practitioner Book

## Method

Observational

## Verification Status

Verified

## Confidence

High

## Key Insight

Blameless post-mortems focus on process and system failures (not individual mistakes) to produce more actionable improvements than blame-oriented reviews.

## Core Findings

1. **Fundamental Principle**: Every failure is a process failure, not a people failure
2. **Psychological Safety Effect**: Blameless approach enables honest disclosure of full context including mistakes and near-misses
3. **Process-Level Framing**: "What process gap allowed this to happen?" vs "Who made the mistake?" shifts improvement target from individual behavior to systemic reliability
4. **Complete Root Cause Analysis**: Participants share more information when not threatened with punishment
5. **Google SRE Origin**: Developed as core practice in Site Reliability Engineering at Google, founded by Benjamin Treynor Sloss in 2003

## Mechanism

Blameless post-mortems work through psychological safety enabling honest disclosure. When participants know they will not be punished, they share complete context including their own mistakes. This produces more comprehensive root cause analysis than blame-oriented reviews where participants hide information for self-protection. Process-level framing shifts focus to systemic improvements.

## Relevance

Essential for incident response, organizational learning, reliability engineering. Applied in SRE practices, DevOps culture, continuous improvement. Fundamental for building high-reliability organizations and preventing repeat failures through systemic fixes rather than individual blame.

## Related Research

Connects to (Amy Edmondson) on psychological safety, (Sidney Dekker) on Just Culture, (John Allspaw) on post-mortem practices. Part of broader SRE methodology alongside error budgets, monitoring, automation. Related to learning organization principles and continuous improvement frameworks.