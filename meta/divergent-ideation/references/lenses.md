# Choose lenses by what they change

Select a small contrasting set. Each should uncover a different mechanism or
assumption; five personas making the same suggestion do not create breadth.

| Lens | Prompt to reshape the search |
|---|---|
| Remove an assumption | Which assumed component or step could disappear? What would replace its function? |
| Inversion | What would reliably defeat the goal? Reverse those causes into possible approaches. |
| Severe resource limit | What preserves the essential outcome with almost no time, budget, or infrastructure? |
| Relax one resource limit | If one bottleneck vanished, what becomes possible? Which part can be made practical now? |
| Physical constraints | How do latency, locality, memory, energy, or capacity change the mechanism? |
| Logistics | Could batching, routing, buffering, inventory, or returns management solve the bottleneck? |
| Operations under failure | What approach is understandable and recoverable when a dependency fails? |
| Provability | What would make the outcome inspectable, attributable, and reversible? |
| Incentives | Who bears the cost and who benefits? Could a different incentive remove the problem? |
| Distant mechanism | Borrow a mechanism from biology or games; explain its causal mapping and where the analogy breaks. |

For architecture, try assumption removal, logistics, and failure recovery. For a
brand, try category inversion, severe resource limits, and a distant mechanism;
turn the resulting concepts into the brand workflow's visual probes. For campaign
concepts, vary customer tension, proof mechanism, and framing before varying wording.
These are starting sets, not mandatory recipes.

An extreme lens may relax a preference, but cannot silently remove an actual
requirement. "No database" can inspire a design alternative; it cannot erase a
specified retention obligation. A biological analogy is a hypothesis generator,
not evidence that a distributed system will behave like an immune system.

## Compact example

Brief: a reporting job makes the user wait; avoid duplicate exports and preserve
the existing access checks.

- Baseline: improve the current synchronous path.
- Assumption removal: let a queued job return a receipt immediately.
- Logistics: batch repeated requests for the same authorized report snapshot.
- Failure recovery: provide resumable status and explicit cancellation.

Cluster by execution and reuse mechanism. A blind retry can look convenient but
duplicate exports; call that out and inspect idempotency before recommending it.
Develop the best contenders with evidence about job duration, permissions, and
recovery behavior. Do not invent timeouts or claim the proposed queue already exists.
