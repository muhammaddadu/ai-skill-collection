---
name: api-design
description: "Design or review an API contract — REST, GraphQL, or event/message. Use when designing endpoints, a schema, or events; reviewing an API; choosing a versioning strategy; checking for breaking changes; or asking 'is this API well designed'. Do NOT use for implementing endpoints in a specific framework or for internal function signatures."
type: component
domain: 2-discovery
---

# API Design & Review

## Purpose

Produce an API contract that consumers can build against safely — or audit an
existing one with a scored, weighted checklist. The contract comes first: the
shape of resources, errors, versioning, and evolution rules is agreed before
any endpoint is implemented, because the contract is the part you cannot
change once consumers exist. Covers three contract styles with one method:
REST/HTTP APIs, GraphQL schemas, and event/message contracts.

Two modes:

- **Design mode** — a new API (or a new surface on an existing one). Output is
  a contract document ready for review, with the checklist applied as you
  design rather than after.
- **Review mode** — an existing contract, spec, or live API. Output is a
  scored review report (0-100, letter grade) with prioritized findings and a
  quick-wins list.

Pick review mode whenever a contract already exists in any form (OpenAPI, SDL,
AsyncAPI, route handlers, or just deployed behavior). Pick design mode when
the surface doesn't exist yet. A redesign is both: review the old surface
first, then design the new one against the findings.

## Outputs

**Design mode**
- **Artifact:** contract document — `docs/api/<name>.md` in the target repo,
  containing the contract sketch (OpenAPI stub, GraphQL SDL, or AsyncAPI stub
  as fits the style), the decisions made (versioning strategy, error model,
  pagination style, auth model) with one-line rationale each, and open
  questions for reviewers.
- **Format:** markdown with embedded spec stub (YAML/SDL fenced blocks).
- **Audience:** the implementing team and the humans who must approve the
  contract before implementation starts.

**Review mode**
- **Artifact:** `API-REVIEW.md` in the target repo (or working directory) —
  per-category scores, overall 0-100 score with letter grade, prioritized
  findings referencing check IDs, and a Quick Wins list.
- **Format:** markdown report (template below).
- **Audience:** the API's owning team; findings are written so each one is
  independently actionable.

## Prerequisites

- A tech-spec or, at minimum, a clear consumer list: who calls this API, from
  where, and for what use-cases (see `../tech-spec`). If neither exists,
  extract the consumer list from the user before designing — a contract with
  no named consumers is a guess.
- Review mode additionally needs the contract itself: a spec file, schema,
  route definitions, or enough of the live API to evaluate.

## Workflow

### Design mode

Work through these steps in order; each produces a section of the contract
document. Apply the checklist (`references/api-review-checklist.md`) *during*
each step, not as a final pass — it is cheaper to design a check in than to
retrofit it.

1. **Consumers and use-cases first.** List every consumer (web client, mobile,
   partner, internal service, data pipeline) and the top use-cases each needs.
   Every element of the contract must trace to one of these. If you cannot
   name the consumer for an endpoint, cut the endpoint (checks A01, A07).

2. **Resource/entity modeling — or event taxonomy.**
   - REST: identify the resources (nouns), their relationships, and which are
     first-class (own URL) vs embedded. Model from the consumer's mental
     model, not from the tables (A01-A08).
   - GraphQL: model the type graph the same way; decide nullability per field
     deliberately and design list fields as connections from the start
     (A09, A10, A31).
   - Events: build the event taxonomy — past-tense facts, one catalog, owners,
     and what each payload must self-contain (A11, A12).

3. **Contract sketch.** Write the machine-readable stub: OpenAPI paths +
   schemas, GraphQL SDL, or AsyncAPI channels + messages. Realistic examples
   for every operation — placeholder-free (A44, A45). Keep it a stub: enough
   precision to review, not a full implementation spec.

4. **Apply the checklist as you go.** After sketching, run the relevant
   categories from `references/api-review-checklist.md` against the sketch and
   fix failures now. The three hard gates (A20, A29, A37) and the Critical
   checks are non-negotiable at this stage.

5. **Versioning & evolution policy.** Decide and write down, before v1: the
   versioning scheme (URL / header / additive-only), the definition of a
   breaking change for this API, additive-evolution rules, and the deprecation
   process with sunset expectations (A20-A28). For events: registry choice and
   compatibility mode (A26, A27).

6. **Error model.** One error envelope for the whole API, a stable error-code
   enum, correct status-code semantics, retryability rules (A13-A19). Write
   the envelope schema into the stub.

7. **Publish the contract for review.** Assemble `docs/api/<name>.md`:
   consumer list, contract stub, decisions with rationale, checklist result,
   open questions. Humans approve the contract before implementation begins;
   contested decisions go to an ADR (see Next steps).

### Contract document template (design mode)

```
# API Contract: <name>

Status: DRAFT — awaiting review        Style: REST | GraphQL | Events
Owner: <team>                          Reviewers: <named consumers' reps>

## Consumers & use-cases
| Consumer | Where it runs | Top use-cases |
|----------|---------------|---------------|

## Contract sketch
<fenced OpenAPI YAML | GraphQL SDL | AsyncAPI YAML stub, with realistic
examples for every operation/type/event>

## Decisions
| Decision | Choice | Rationale (one line) |
|----------|--------|----------------------|
| Versioning scheme      | URL /v1/ · header · additive-only | |
| Breaking-change def.   | <link or inline list>             | |
| Error envelope         | RFC 9457 · custom                 | |
| Pagination style       | cursor · offset · connections     | |
| Auth model             | <scheme + authZ granularity>      | |
| (events) Registry/mode | <registry> · backward/forward/full| |

## Checklist result
Applied references/api-review-checklist.md on <date>:
gates PASS/FAIL, Critical/High items resolved or listed below.

## Open questions
- <question> — blocking? <yes/no> — proposed default: <answer>
```

### Review mode

1. **Collect the contract.** Spec file (OpenAPI/SDL/AsyncAPI) preferred;
   otherwise route definitions, schema code, or observed behavior. Note which
   style(s) apply — REST, GraphQL, event — so non-applicable checks can be
   marked N/A. Confirm with the user which consumers exist and whether the API
   is already live (a live API raises the cost of every breaking-change
   finding).
2. **Read `references/api-review-checklist.md`** — all 48 checks, weights,
   severities, and the scoring algorithm live there.
3. **Evaluate every applicable check** as PASS, WARNING, or FAIL, with a
   one-line evidence note per non-PASS (what you saw, where).
4. **Check the hard gates first.** A20 (breaking change without version bump +
   migration note), A29 (unbounded list), A37 (unauthenticated mutation). Any
   gate failure caps the grade at D and leads the report.
5. **Score.** Category score = weighted pass rate within the category; overall
   score per the formula in the reference. Grades: A ≥90, B 75-89, C 60-74,
   D 40-59, F <40.
6. **Write `API-REVIEW.md`** using the template below: findings sorted by
   severity then category weight, each referencing its check ID; Quick Wins =
   severity Critical/High AND fix < 15 minutes, sorted by
   (severity × estimated impact) descending.

### Review report template

```
# API Review: <name>

API Design Score: XX/100 (Grade: X)
Hard gates: PASS | FAILED (A__) — <one line>

Resource & schema design:            XX/100  ████████░░  (25%)
Versioning & compatibility:          XX/100  ██████░░░░  (20%)
Errors & status semantics:           XX/100  ███████░░░  (15%)
Pagination, filtering & consistency: XX/100  █████░░░░░  (15%)
Security & auth:                     XX/100  ████████░░  (15%)
DX & docs:                           XX/100  ██████████  (10%)

## Quick Wins
1. [A__] <finding> — <fix> (Critical, ~N min)
...

## Findings by priority
### Critical
- [A__] <what fails, where, why it matters, recommended fix>
### High
...

## Passed highlights
<2-3 things the contract does well — keeps the report credible>
```

## Scoring at a glance

Full algorithm, severity multipliers, and per-check definitions live in
`references/api-review-checklist.md`; this is the shape of it. Category score
is the weighted pass rate of its checks (PASS = 1, WARNING = 0.5, FAIL = 0,
N/A excluded); each check's contribution is scaled by its severity multiplier
(Critical 5.0, High 3.0, Medium 1.5, Low 0.5); the overall score weights the
categories:

| Category | Weight | Checks |
|----------|--------|--------|
| Resource & schema design | 25% | A01-A12 |
| Versioning & compatibility | 20% | A20-A28 |
| Errors & status semantics | 15% | A13-A19 |
| Pagination, filtering & consistency | 15% | A29-A36 |
| Security & auth | 15% | A37-A43 |
| DX & docs | 10% | A44-A48 |

| Grade | Score | Meaning |
|-------|-------|---------|
| A | 90-100 | Excellent — minor polish only |
| B | 75-89 | Good — some improvement opportunities |
| C | 60-74 | Needs improvement |
| D | 40-59 | Poor — significant problems (also the cap when any hard gate fails) |
| F | <40 | Redesign before consumers integrate |

Hard gates (never-ship, regardless of score): **A20** breaking change without
a version bump + migration note, **A29** unbounded list endpoint without
pagination, **A37** unauthenticated mutating endpoint.

## Contract-style notes

The checklist covers all three styles; these are the style-specific traps to
hold in mind while applying it.

- **REST:** verbs live in the method, not the path; idempotency is a design
  property (retried POSTs need an `Idempotency-Key`); status codes are part of
  the contract, not an implementation detail; pick cursor vs offset pagination
  per data volatility, not per habit (A02, A14, A30, A34).
- **GraphQL:** nullability is your error-isolation mechanism — `!` is a
  promise, not a default; every list field should be a connection before it
  ships; the schema must not structurally require N+1 resolution; deprecate
  with `@deprecated(reason:)` instead of versioning the whole schema
  (A09, A10, A31, A24, A43).
- **Events:** the schema registry and its compatibility mode *are* the
  versioning strategy; ordering and delivery guarantees must be written down,
  not assumed; consumers are idempotent by design (dedup on event id); PII in
  an event payload propagates to every consumer and every replay — minimize it
  at the source (A26, A27, A35, A41).

For the full check definitions, severities, weights, and scoring math, read
`references/api-review-checklist.md`.

## Pitfalls

- **Designing from the database schema outward:** the contract mirrors tables
  and join structure → consumers couple to storage, and every schema migration
  becomes a breaking API change → start from consumer use-cases (Design step
  1) and let the contract be a projection, never an export (A01).
- **Versioning by accident:** no strategy is chosen, so the first breaking
  change invents one under pressure → mixed schemes, undocumented breakage,
  consumers pinned to behavior you didn't know was contractual → decide the
  versioning and evolution policy before v1 ships (Design step 5, A21).
- **Error responses that leak internals:** stack traces, SQL fragments, or
  hostnames flow through the default error handler into responses → attackers
  get a system map and clients parse prose → define one error envelope with
  stable codes at the contract level and test that unhandled errors render
  through it (A13, A15).
- **"We'll paginate later":** a list endpoint ships unbounded because the
  table is small today → the table grows, the response times out, and adding
  pagination is now a breaking change → pagination is a hard gate (A29);
  every collection paginates from day one, even with a generous max page size.

## Next steps

- `test-strategy` — turn the contract into contract tests (provider/
  consumer) so the checklist's compatibility guarantees are enforced by CI,
  not by review.
- `../adr` — record contested API decisions (versioning scheme, pagination
  style, error envelope, registry choice) as ADRs so the rationale survives
  the people who made it.
