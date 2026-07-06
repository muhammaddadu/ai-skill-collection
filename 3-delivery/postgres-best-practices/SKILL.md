---
name: postgres-best-practices
description: "Priority-ranked Postgres best practices: query performance and indexing, connection management and pooling, schema design, Row-Level Security, locking and concurrency. Use when writing or reviewing SQL or Postgres schema, fixing slow queries, or planning migrations. Do NOT use for API contract design (`api-design`) or managed-DB provisioning."
type: component
domain: 3-delivery
license: MIT
---

# Postgres Best Practices

## Purpose
Priority-ranked Postgres performance and correctness rules (vendored from Supabase's
`supabase-postgres-best-practices`, ~90% generic Postgres) that guide writing and
reviewing SQL, schema design, and diagnosing slow queries. Each rule ships as a
reference file with an incorrect vs. correct SQL example and the why behind it.

## Outputs
**Artifact:** reviewed/optimized SQL, schema DDL, or migration — with the rule(s) applied cited by name
**Format:** SQL / DDL changes in the target repo, or review comments
**Location:** the target repo's migrations/queries under review
**Audience:** developers and reviewing agents working on a Postgres database

## When to apply

Reference these rules when:
- Writing SQL queries or designing/migrating schemas
- Adding indexes or optimizing a slow query
- Reviewing database-touching diffs
- Configuring connection pooling or debugging connection exhaustion
- Working with Row-Level Security (RLS)

## Rule categories by priority

Work top-down: higher categories have more impact. Read only the rule files you need.

| Priority | Category (impact) | Rule files |
|----------|-------------------|------------|
| 1 | Query performance (CRITICAL) — missing indexes, wrong index types, inefficient plans | `references/query-missing-indexes.md`, `references/query-index-types.md`, `references/query-composite-indexes.md`, `references/query-partial-indexes.md`, `references/query-covering-indexes.md` |
| 2 | Connection management (CRITICAL) — pooling, limits, serverless | `references/conn-pooling.md`, `references/conn-limits.md`, `references/conn-prepared-statements.md`, `references/conn-idle-timeout.md` |
| 3 | Security & RLS (CRITICAL) — policies, privileges | `references/security-rls-basics.md`, `references/security-rls-performance.md`, `references/security-privileges.md` |
| 4 | Schema design (HIGH) — types, keys, constraints, partitioning | `references/schema-data-types.md`, `references/schema-primary-keys.md`, `references/schema-foreign-key-indexes.md`, `references/schema-constraints.md`, `references/schema-lowercase-identifiers.md`, `references/schema-partitioning.md` |
| 5 | Concurrency & locking (MEDIUM-HIGH) — deadlocks, contention | `references/lock-short-transactions.md`, `references/lock-deadlock-prevention.md`, `references/lock-skip-locked.md`, `references/lock-advisory.md` |
| 6 | Data access patterns (MEDIUM) — N+1, batching, pagination | `references/data-n-plus-one.md`, `references/data-batch-inserts.md`, `references/data-pagination.md`, `references/data-upsert.md` |
| 7 | Monitoring & diagnostics (LOW-MEDIUM) — EXPLAIN, pg_stat_statements, vacuum | `references/monitor-explain-analyze.md`, `references/monitor-pg-stat-statements.md`, `references/monitor-vacuum-analyze.md` |
| 8 | Advanced features (LOW) — FTS, JSONB | `references/advanced-full-text-search.md`, `references/advanced-jsonb-indexing.md` |

Each rule file contains:
- Brief explanation of why it matters
- Incorrect SQL example with explanation
- Correct SQL example with explanation
- Optional EXPLAIN output or metrics
- Notes tagged **(Supabase-specific)** where a snippet relies on Supabase's
  `auth.uid()` helper or built-in roles (`anon`, `authenticated`, `service_role`) —
  substitute your own session/user mechanism (e.g. `current_setting()`) elsewhere

## Pitfalls
- **Applying low-priority rules first:** advanced features tuned while a missing index
  dominates → fix category 1–3 issues before anything below them.
- **Copying RLS snippets verbatim outside Supabase:** `auth.uid()` does not exist in
  vanilla Postgres → use the generic `current_setting()` pattern shown in
  `references/security-rls-basics.md`.

## Next steps
- Prove query changes with `references/monitor-explain-analyze.md` before/after
- For contract-level API shape questions, use `api-design`

## References

- https://www.postgresql.org/docs/current/
- https://wiki.postgresql.org/wiki/Performance_Optimization
