---
name: tdd
description: "Drive implementation with the red-green loop: agree the seams, write one failing test, watch it fail, write minimal code to pass, repeat. Use when building a feature or fixing a bug test-first, or when the user mentions TDD, red-green-refactor, or test-first. Do NOT use for planning a feature's overall test suite (test-strategy)."
type: component
domain: 3-delivery
---

# Test-Driven Development

TDD is the red → green loop. This skill is the reference that makes that loop produce tests worth keeping: what a good test is, where tests go, the anti-patterns, and the rules of the loop. Every section applies on every cycle — consult them before and during the loop, not after.

When exploring the codebase, read the project's agent/context docs (`AGENTS.md` / `CLAUDE.md` / `CONTEXT.md`, if present) so test names and interface vocabulary match the project's domain language, and respect ADRs in the area you're touching.

## Outputs

**Artifact:** the implementation plus its passing test suite, grown one red-green slice at a time — every behavior covered by a test that was seen to fail first
**Format:** code + tests, delivered inline in the target repo
**Location:** tests colocated with (or in the project's designated test dir for) the code under test
**Audience:** reviewers and CI

## What a good test is

Tests verify behavior through public interfaces, not implementation details. Code can change entirely; tests shouldn't. A good test reads like a specification — "user can checkout with valid cart" tells you exactly what capability exists — and survives refactors because it doesn't care about internal structure.

For examples of good and bad tests, read `references/tests.md`. For mocking guidelines (mock only at system boundaries; design for mockability), read `references/mocking.md`.

## Seams — where tests go

A **seam** is the public boundary you test at: the interface where you observe behavior without reaching inside. Tests live at seams, never against internals.

**Test only at pre-agreed seams.** Before writing any test, write down the seams under test and confirm them with the user. No test is written at an unconfirmed seam. You can't test everything — agreeing the seams up front is how testing effort lands on the critical paths and complex logic instead of every edge case.

Ask: "What's the public interface, and which seams should we test?"

## Anti-patterns

- **Implementation-coupled** — mocks internal collaborators, tests private methods, or verifies through a side channel (querying the database instead of using the interface). The tell: the test breaks when you refactor but behavior hasn't changed.
- **Tautological** — the assertion recomputes the expected value the way the code does (`expect(add(a, b)).toBe(a + b)`, a snapshot derived by hand the same way, a constant asserted equal to itself), so it passes by construction and can never disagree with the code. Expected values must come from an independent source of truth — a known-good literal, a worked example, the spec.
- **Horizontal slicing** — writing all tests first, then all implementation. Bulk tests verify _imagined_ behavior: you test the _shape_ of things rather than user-facing behavior, the tests go insensitive to real changes, and you commit to test structure before understanding the implementation. Work in **vertical slices** instead — one test → one implementation → repeat, each test a **tracer bullet** that responds to what the last cycle taught you.

## Rules of the loop

- **Red before green.** Write the failing test first, then only enough code to pass it. Don't anticipate future tests or add speculative features.
- **Watch it fail.** Run the new test and see it fail — for the expected reason (the feature is missing), not because of a typo or setup error — before writing any implementation. If you didn't watch the test fail, you don't know it tests the right thing: it isn't a real test. If it passes immediately, you're testing behavior that already exists — fix the test. If it errors rather than fails, fix the error and re-run until it fails correctly.
- **One slice at a time.** One seam, one test, one minimal implementation per cycle.
- **Refactoring is not part of the loop.** It belongs to the review stage (e.g. a `/code-review` pass), not the red → green implementation cycle.
