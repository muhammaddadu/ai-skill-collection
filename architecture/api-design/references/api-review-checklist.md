# API Review Checklist

<!-- Scoring conventions mirror the ads skill's references/scoring-system.md (v1.5) -->
<!-- ID convention: A01, A02, … sequential across categories -->

48 ID'd checks across 6 weighted categories. Each check is one testable
statement plus the failure it prevents. Evaluate every applicable check as
PASS, WARNING, or FAIL; mark checks that don't apply to the contract style
(REST / GraphQL / event) as N/A and exclude them from the possible total.

## Category Weights

| Category | Weight | Rationale |
|----------|--------|-----------|
| Resource & schema design | 25% | The shape of the contract is the hardest thing to change after consumers exist |
| Versioning & compatibility | 20% | Breaking a consumer silently is the worst API failure mode |
| Errors & status semantics | 15% | Every client codes against the error model; inconsistency multiplies across consumers |
| Pagination, filtering & consistency | 15% | Unbounded lists and non-idempotent writes are the top production incidents |
| Security & auth | 15% | AuthZ gaps and PII leaks are unshippable regardless of elegance |
| DX & docs | 10% | Adoption and correct usage depend on it, but it can be fixed after ship |

## Scoring Algorithm

```
Score = Σ(C_pass × W_sev × W_cat) / Σ(C_total × W_sev × W_cat) × 100
```

- `C_pass`: PASS = 1, WARNING = 0.5, FAIL = 0; N/A excluded from the possible total
- `W_sev`: severity multiplier of the check
- `W_cat`: category weight

| Severity | Multiplier | Criteria |
|----------|-----------|----------|
| Critical | 5.0 | Ships a security hole, data-corruption path, or consumer breakage. Fix before ship. |
| High | 3.0 | Significant consumer pain or future lock-in. Fix within the current iteration. |
| Medium | 1.5 | Friction or inconsistency. Fix within 30 days. |
| Low | 0.5 | Polish. Nice to have. |

| Grade | Score | Label |
|-------|-------|-------|
| A | 90-100 | Excellent — minor polish only |
| B | 75-89 | Good — some improvement opportunities |
| C | 60-74 | Needs improvement — notable issues |
| D | 40-59 | Poor — significant problems |
| F | <40 | Critical — redesign before consumers integrate |

**Hard gates:** A20, A29, A37 are never-ship rules. Any failed gate means the
contract must not ship (or the change must not merge) regardless of the
numeric score — cap the grade at D and lead the report with the gate failure.

**Quick Wins:** `severity ∈ {Critical, High} AND estimated fix < 15 minutes`,
sorted by `(severity × estimated impact)` descending.

---

## Resource & schema design (25%)

| ID | Check | Severity | Failure it prevents |
|----|-------|----------|---------------------|
| A01 | Contract is derived from named consumers and use-cases, not from the database schema — every endpoint/type/event traces to a consumer need | High | Leaking internal storage shape that can never change without breaking clients |
| A02 | REST: resources are nouns; actions are HTTP verbs or explicit sub-resources (`POST /orders/{id}/cancellation`), not RPC verbs in paths | Medium | An unguessable, verb-soup surface that grows without structure |
| A03 | One naming convention across the whole contract: one casing, one pluralization rule, the same term for the same concept everywhere | Medium | Consumers writing per-endpoint mapping code and guessing field names |
| A04 | Types are precise: money as integer minor units or decimal string (never float); timestamps ISO-8601 UTC; no stringly-typed booleans/numbers | High | Rounding errors and timezone corruption baked into every client |
| A05 | IDs are opaque strings at the boundary, not raw auto-increment integers | Medium | Resource enumeration attacks and permanent coupling to storage |
| A06 | Every enum documents client behavior for unknown future values (tolerate-and-ignore or explicit `UNKNOWN`) | High | Client crashes the day a new enum value ships |
| A07 | No god-objects: a response is one resource plus explicit, opt-in expansion — not a kitchen-sink join of everything reachable | Medium | Payload bloat and hidden coupling that makes every field load-bearing |
| A08 | Required vs optional is explicit per field in the machine-readable schema (OpenAPI `required`, GraphQL non-null, registry schema) | High | Every consumer null-checking everything, or crashing on the field that wasn't |
| A09 | GraphQL: nullability is deliberate — non-null (`!`) only where the server can always guarantee a value; nullable where partial failure must be isolated | High | One failing resolver nulling out an entire query response |
| A10 | GraphQL: schema exposes domain types, not table rows; nested list fields are batchable (dataloader-ready) so the schema doesn't mandate N+1 | High | A schema whose only honest implementation is one query per list item |
| A11 | Events: each event is a past-tense fact (`order.placed`) with a self-contained payload, a stable event `id`, and `occurred_at` | High | Consumers calling back to the producer to make sense of every event |
| A12 | Events: an event catalog exists — one list of event names, owners, and payload schemas; no ad-hoc topics | Medium | Nobody knowing what events exist, who owns them, or what they contain |

## Errors & status semantics (15%)

| ID | Check | Severity | Failure it prevents |
|----|-------|----------|---------------------|
| A13 | One machine-readable error envelope across the API (e.g. RFC 9457 Problem Details): stable `code`, human `message`, correlation id | High | Per-endpoint error parsing duplicated in every client |
| A14 | REST: status codes are semantically correct — 400/401/403/404/409/422/429 distinguished; no 200-with-error-body | High | Clients unable to branch on outcome without parsing prose |
| A15 | No error response leaks internals: no stack traces, SQL, file paths, hostnames, or dependency names in any error payload | Critical | Handing attackers a map of the system |
| A16 | Validation errors enumerate all field-level failures in one response, not first-failure-only | Medium | Submit-fix-submit loops that burn users and support |
| A17 | Error `code` values are a documented, stable enum clients can program against; messages may change, codes may not | High | Clients string-matching on messages that break on reword |
| A18 | GraphQL: errors use the `errors` array with `extensions.code`; partial-data-plus-errors semantics are documented | Medium | Clients treating any error as total failure and discarding good data |
| A19 | Retryability is explicit: 429/503 carry `Retry-After`; docs state which error codes are safe to retry | Medium | Retry storms against a struggling backend, or clients giving up on transient errors |

## Versioning & compatibility (20%)

| ID | Check | Severity | Failure it prevents |
|----|-------|----------|---------------------|
| A20 | **GATE:** no breaking change ships without a version bump AND a written migration note | Critical | Silently breaking every existing consumer |
| A21 | Versioning strategy is chosen and documented before v1 ships (URL `/v1/`, header, or additive-only evolution) — not improvised per change | High | Versioning by accident: three inconsistent schemes in one API |
| A22 | "Breaking change" is defined in the contract docs: removed/renamed field, type change, tightened validation, semantic change, new required request field | High | Breakage shipped as a "patch" because nobody agreed what breaking means |
| A23 | Additive evolution rules are stated: new response fields must be ignorable by old clients; new request fields optional with safe defaults | High | Old clients failing on fields they were never told to expect |
| A24 | Deprecations are marked in-schema (OpenAPI `deprecated: true`, GraphQL `@deprecated(reason:)`) with a replacement and a sunset date | High | Zombie fields nobody dares remove because nobody was told to leave |
| A25 | Deprecated element usage is measurable (metrics/logs per field or endpoint), so sunset decisions are data-driven | Medium | Removing a "dead" field that a top consumer still calls daily |
| A26 | Events: schemas live in a registry (or versioned schema repo) with an enforced compatibility mode (backward/forward/full) | Critical | Producers silently publishing payloads consumers can no longer parse |
| A27 | Events: every payload carries its schema version (or registry id); consumers resolve the version explicitly | High | Consumers guessing the shape of what they just dequeued |
| A28 | Contract diff runs in CI (openapi-diff, graphql-inspector, registry compat check) so breaking changes are caught mechanically | High | Compatibility depending on reviewer vigilance instead of a gate |

## Pagination, filtering & consistency (15%)

| ID | Check | Severity | Failure it prevents |
|----|-------|----------|---------------------|
| A29 | **GATE:** no unbounded list — every collection endpoint / list field paginates with an enforced, documented max page size | Critical | The 2-million-row response that takes the service down |
| A30 | Pagination style is chosen deliberately: cursor-based for large or mutating sets; offset only for small, stable, jump-to-page data — with the choice documented | High | Skipped and duplicated rows under concurrent writes |
| A31 | GraphQL: list fields use the connection pattern (`edges`/`pageInfo`, `first`/`after`); no raw unbounded `[Type!]!` on hot paths | High | Unpaginatable fields that require a breaking change to fix later |
| A32 | Page responses expose an opaque `next` cursor or link (and has-more/total where cheap); clients never construct page URLs by hand | Medium | Clients hard-coding URL math that breaks when pagination changes |
| A33 | Filter and sort parameters are an explicit validated whitelist, not a pass-through to the query engine | High | Accidental full-table scans and filter injection via crafted params |
| A34 | Writes are idempotent under retry: PUT/DELETE naturally; POST create accepts an `Idempotency-Key` (or a natural dedup key) | Critical | Duplicate orders and double charges on network retry |
| A35 | Events: ordering guarantees are explicit (per-key ordering via partition key, or explicitly none) and consumers dedup on event `id` | Critical | Double-processing and out-of-order state corruption |
| A36 | Mutable resources support concurrency control: `ETag`/`If-Match` or a version field on update | Medium | Lost updates when two clients edit the same resource |

## Security & auth (15%)

| ID | Check | Severity | Failure it prevents |
|----|-------|----------|---------------------|
| A37 | **GATE:** no unauthenticated mutating endpoint — and no "temporarily open" write path | Critical | Anonymous writes to production data |
| A38 | Authorization is specified per endpoint/field with object-level checks — possessing an id is not permission (no BOLA/IDOR) | Critical | Any logged-in user reading any other user's data by iterating ids |
| A39 | Rate limits and quotas are part of the contract (limits, headers, 429 behavior), at minimum for unauthenticated and write paths | High | One consumer's loop becoming everyone's outage |
| A40 | Sensitive fields are classified in the schema; PII never appears in URLs, query strings, or fields destined for logs | Critical | PII in access logs, browser history, and referrer headers |
| A41 | Events: payloads are audited for PII — minimized, tokenized, or encrypted; retention and replay implications documented (GDPR erasure vs immutable log) | Critical | Unerasable personal data replicated into every downstream consumer |
| A42 | Inputs are constrained at the contract: max lengths, patterns, ranges, max array sizes, max body size | High | DoS via pathological or oversized input the schema happily accepted |
| A43 | GraphQL: query depth/complexity limits are stated and production introspection policy is explicit | High | A single crafted deep query exhausting the backend |

## DX & docs (10%)

| ID | Check | Severity | Failure it prevents |
|----|-------|----------|---------------------|
| A44 | A machine-readable contract (OpenAPI / GraphQL SDL / AsyncAPI) is the source of truth — linted and diffed in CI; prose docs link to or generate from it | High | Docs and implementation drifting until neither is trusted |
| A45 | Every endpoint/type/event has a description plus at least one realistic request/response example — no `foo`/`bar` placeholders | Medium | Consumers reverse-engineering semantics from staging traffic |
| A46 | An auth + first-call walkthrough exists: a new consumer reaches a successful call without talking to the team | Medium | Every integration starting with a meeting |
| A47 | A conventions note (casing, timestamps, pagination, error envelope) is published once and referenced by every new endpoint | Low | Each new endpoint reinventing conventions slightly differently |
| A48 | A changelog exists per version: what changed, deprecations, migration notes, sunset dates | Medium | Consumers discovering changes when their integration breaks |
