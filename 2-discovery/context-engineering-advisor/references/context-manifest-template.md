# Context Manifest — Template

Give this template to the user in Step 4 (boundary ownership) or Step 9
(action plan) when they need to formalize their context boundary. Adapt the
example entries to their product.

```markdown
# Context Manifest: [Product/Feature Name]

## Always Persisted (Core Context)
- Product constraints (technical, regulatory)
- User preferences (role, permissions, preferences)
- Operational glossary (20 key terms)

## Retrieved On-Demand (Episodic Context)
- Historical PRDs (retrieve via semantic search)
- User interview transcripts (retrieve relevant quotes)
- Competitive analysis (retrieve when explicitly needed)

## Excluded (Out of Scope)
- Meeting notes older than 30 days (no longer relevant)
- Full codebase (use code search instead)
- Marketing materials (not decision-relevant)

## Boundary Owner: [Name]
## Last Reviewed: [Date]
## Next Review: [Date + 90 days]
```

Usage notes:
- **Always Persisted** should pass the 80% test: referenced in 80%+ of interactions.
- **Retrieved On-Demand** covers the <20% items; the gray zone (20-80%) depends on retrieval latency vs. context window cost.
- **Excluded** entries should each state *why* (falsification test failed — no concrete failure if omitted).
- Review quarterly; the boundary owner runs the audit.
