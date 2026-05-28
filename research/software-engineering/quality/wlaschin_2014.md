# Choosing Properties for Property-Based Testing (Wlaschin, 2014)

## Citation

Wlaschin, S. (2014). "Choosing properties for property-based testing" *F# for Fun and Profit*. https://fsharpforfunandprofit.com/posts/property-based-testing-2/

## Source Type

Blog/Article

## Method

Theoretical with practical examples

## Verification Status

Verified

## Confidence

High

## Key Insight

Seven recurring patterns help developers discover testable properties when they cannot think of any: "Different paths, same destination" (commutative diagram), "There and back again" (inverse function), "Some things never change" (invariant under transformation), "The more things change, the more they stay the same" (idempotence), "Solve a smaller problem first" (structural induction), "Hard to prove, easy to verify", and "The test oracle".

## Core Findings

1. The universal problem with property-based testing is not tooling but discovering what properties to test — developers stare at a blank screen unable to think of properties
2. Seven patterns cover most common cases: commutative operations, inverse pairs, invariants, idempotence, structural induction, easy-verification, and test oracles
3. "Different paths, same destination" applies when two operation sequences should produce the same result (e.g., addition is commutative)
4. "There and back again" applies when an operation and its inverse return to the starting state (e.g., serialize/deserialize)
5. "Some things never change" applies when a transformation preserves an invariant (e.g., sort preserves multiset of elements)
6. "Hard to prove, easy to verify" applies when finding the answer is complex but checking it is simple (e.g., prime factorisation — hard to find, easy to multiply back)
7. "The test oracle" applies when an alternate (simpler, slower) implementation exists to verify the production implementation
8. Model-based testing is a variant of the test oracle pattern: a simplified model runs in parallel with the system under test, and states are compared after each operation

## Mechanism

Rather than trying to enumerate all possible properties of a system, developers apply each of the seven patterns as lenses to examine the system's behaviour. Each pattern asks a different question: "Are there two ways to get the same result?" "Is there an inverse?" "What stays the same?" "What happens if I do it twice?" "Can I break it into smaller parts?" "Is the answer easy to check?" "Is there a reference implementation?" This structured approach overcomes the "blank screen" problem by providing concrete starting points for property discovery.

## Relevance

Essential for BDD example creation: the seven patterns provide a systematic method for deciding whether a Rule should use simple Examples or Scenario Outlines with parameterised inputs. When a pattern applies, it reveals which input combinations matter and whether the behaviour holds across a range of inputs. This directly informs the Example-vs-Scenario-Outline decision in the write-bdd-features skill. The patterns also surface missing Examples: if a pattern applies to a Rule but no Example covers the revealed combination, the specification is incomplete.

## Related Research

- (Claessen & Hughes, 2000) - QuickCheck: automatic testing of Haskell programs
- (MacIver, 2016) - Hypothesis library extending property-based testing to Python
- (Tillmann & Schulte, 2005) - PEX team at Microsoft compiled a complementary list of property patterns
