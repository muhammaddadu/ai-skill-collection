<!--
TEMPLATE — one epic file (docs/product/epics/E{n}-{slug}.md). Checkbox criteria are the
contract: tick only when a test or shipped artifact proves it. Status line records reality.
-->

# E{{N}} — {{Title}}

> **This doc owns:** the acceptance state of the {{title}} epic. **Index:** [epics](index.md). **Code layout:** [app architecture](../../architecture/app-architecture.md).

**Status:** {{Planned | In progress | ✅ Done (YYYY-MM-DD)}} · **Depends on:** {{E0, … | —}} · **PRD:** {{§refs}}

## Goal

{{One paragraph: the shippable slice this epic delivers and why it comes here in the order.}}

## Deliverables

- {{Concrete thing shipped.}}
- {{…}}

## Acceptance criteria

### Functional

- [ ] {{What the feature must do, mapped to a PRD section. Provable by a test or artifact.}}
- [ ] {{…}}
- [ ] {{Lint / typecheck / unit tests / build all pass.}}

### E2E validation

- [ ] {{The end-to-end behaviour a test must prove, run through the test-auth path (not the real login round-trip).}}

## Notes

{{Decisions, history, supersessions. If scope changed mid-epic, record it here rather than rewriting the criteria.}}
