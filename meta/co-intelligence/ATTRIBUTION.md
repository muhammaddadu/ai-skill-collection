# Attribution

## The framework

The conceptual framework in this skill is **Ethan Mollick, *Co-Intelligence: Living and Working with AI***
(Portfolio / Penguin Random House, April 2024). Specifically his:

- the **jagged frontier** — AI capability as uneven, with an invisible boundary
- the **centaur / cyborg** distinction between working modes
- the **four principles**: always invite AI to the table; be the human in the loop; treat AI like a person
  but tell it what kind of person it is; assume this is the worst AI you will ever use

**This skill does not reproduce the book and is not a substitute for it.** It contains no extended quotation.
What it does is translate the framework into an operational checklist — a decision procedure and a review
gate — which the book does not provide, because it is a work of argument rather than a manual.

Read the book for the argument, the supporting narrative, and the futures discussion, none of which this
skill attempts to cover.

## What is original here

- The **inside/outside the frontier task table**, and the framing that the dangerous zone is "just outside,
  and fluent about it" rather than clearly outside
- The **guardrail paired against each of the four principles** — each principle stated, then the strongest
  published counter-evidence to its naive application
- The **centaur/cyborg selection criteria** based on whether provenance is required
- The **four-check workflow** and the pitfalls table
- The framing that **fluency and correctness are independent variables**, and the measurement supporting it

## The human-accountability questions and the review prompt

The four accountability questions and the reusable review prompt came to this skill via **a practitioner's
own derived working notes on the book, shared 2026-07-28** — not from the book's text. They are a
practitioner's distillation, and are included because they are good, not because they are canonical. They
should not be attributed to Mollick.

## Empirical claims — sources and status

The research cited is **independent of the book** and used to test its principles rather than to support
them. Each is labelled in `SKILL.md` by source type.

| Claim | Source | Status |
|---|---|---|
| 91.2% benchmark vs 21.3% on real enterprise warehouses | Spider 2.0, arXiv 2411.07763 | Preprint, verified |
| Experienced developers 19% slower with AI; 40pp self-report overestimate | METR, July 2025 | Preprint + first-party research org |
| Analysts check procedure not data | CHI 2024 | Peer-reviewed |
| Reasoning traces used to rationalise wrong answers | AVI 2026 | Peer-reviewed |
| 21% → >95% → ~65% context decay | First-party engineering account, 2026 | Vendor-published, method disclosed |
| 53% correct rated 95% acceptable | Preprint, 2025 | Same system, same period |
| Throughput up / stability down | DORA 2025 | Vendor-published research, method disclosed |
| 15% gain concentrated in least-experienced workers | *Quarterly Journal of Economics* 140(2), 2025 | Peer-reviewed, quasi-experimental |

⚠️ **One claim is deliberately marked unverified in the skill.** Mollick's own BCG field experiment
(Dell'Acqua, Mollick et al.) is widely cited with figures around 40% improvement inside the frontier and ~19
percentage points worse outside. Those numbers are **recalled, not checked against the paper**, and the
skill instructs the reader to verify them before quoting. This is deliberate: a skill about not trusting
fluent output should not itself smuggle in an unverified round number.

## Licence

The framework belongs to its author; the operational translation is provided under the same terms as the
rest of this skills collection. Nothing here is a licensed derivative of the book, and no permission from
the publisher was sought or implied.
