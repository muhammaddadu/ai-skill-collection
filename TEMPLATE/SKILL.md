---
name: <domain>-<object>            # must equal the directory name, kebab-case
description: "<Verb> the <artifact> … Use when <specific trigger phrases>. Do NOT use for <adjacent case handled by another skill>."  # <=350 chars target, 500 hard cap
type: component | interactive | workflow | advisor
domain: product | growth | design | architecture | engineering | quality | operations | career | utilities | meta
tested_date: YYYY-MM-DD            # required if content pins a tool/SDK/platform version
# requires: "<tool> >= x, < y"     # version constraints for moving targets
---

# <Skill title>

## Purpose
One paragraph: the outcome this skill produces and for whom.

## Outputs
**Artifact:** <name of the deliverable>
**Format:** <markdown | json | diagram | …>
**Location:** <where it is saved, e.g. docs/adr/NNN-<slug>.md in the target repo>
**Audience:** <who consumes it>

## Prerequisites
- <upstream skill or artifact this consumes, e.g. "an approved problem-statement">

## Workflow
Step-by-step instructions. Interactive skills delegate pacing to
`../workshop-facilitation` (meta domain). Keep the body ≤~500 lines; route
detail to references/ with explicit pointers:
- For <subtopic>, read `references/<file>.md`

## Pitfalls
- **<Name>:** symptom → consequence → fix

## Next steps
- <downstream skill that consumes this output>
