---
name: skill-authoring-workflow
description: "Turn raw PM content into a compliant, publish-ready skill, or design a new skill through guided Q&A that shapes its type, scope, and structure. Enforces THIS repo's conventions and validation gates (generic scaffolding is skill-creator's job). Use when creating or updating a repo skill — even from just an idea or notes."
intent: >-
  Create or update PM skills without chaos. This workflow turns rough notes, workshop content, or half-baked prompt dumps into compliant `skills/<skill-name>/SKILL.md` assets that actually pass validation and belong in this repo. When the user starts from a raw idea rather than finished content, it also runs a guided 5-question design conversation (see references/pm-skill-design.md, absorbed from the retired pm-skill-creator skill) to settle skill type, scope, naming, and structure before drafting.
type: workflow
best_for:
  - "Creating a new repo skill from notes or source material"
  - "Designing a new skill from a raw idea through guided conversation"
  - "Updating an existing skill while keeping standards intact"
  - "Running the full authoring and validation workflow before commit"
scenarios:
  - "Help me turn these workshop notes into a new PM skill"
  - "Help me create a new skill — I know the topic but not the structure"
  - "I need to update an existing skill without breaking the repo standards"
  - "What workflow should I use to author a new skill in this repo?"
---

## Purpose

Create or update PM skills without chaos. This workflow turns rough notes, workshop content, or half-baked prompt dumps into compliant `skills/<skill-name>/SKILL.md` assets that actually pass validation and belong in this repo.

Use it when you want to ship a new skill without "looks good to me" roulette.

**Where this skill fits:** an external plugin already provides a generic `skill-creator` for scaffolding skills from scratch. This skill's niche is **this repo's standards** — the PM skill anatomy, metadata limits, catalog integration, and validation gates. For generic skill scaffolding, the skill-creator plugin skill applies; use this skill to meet this repo's conventions and validation gates.

## Outputs
**Artifact:** A compliant, publish-ready skill directory (SKILL.md plus references/) that passes this repo's validation gates
**Format:** markdown skill files
**Location:** the skills repo, under the chosen domain directory
**Audience:** this repo's skill portfolio (Claude Code + Codex consume it via symlinks)

## Prerequisites
- Raw source material (notes, prompts, workshop content) or at least an idea to shape
- `find-skills` — check the ecosystem first so you don't author a duplicate

## Key Concepts

### Dogfood First

Use repo-native tools and standards before inventing a custom process:
- `scripts/find-a-skill.sh`
- `scripts/add-a-skill.sh`
- `scripts/build-a-skill.sh`
- `scripts/test-a-skill.sh`
- `scripts/check-skill-metadata.py`

### Pick the Right Creation Path

- **Guided wizard (`build-a-skill.sh`)**: Best when you have an idea but not final prose.
- **Content-first generator (`add-a-skill.sh`)**: Best when you already have source content.
- **Manual edit + validate**: Best for tightening an existing skill.

### Definition of Done (No Exceptions)

A skill is done only when:
1. Frontmatter is valid (`name`, `description`, `intent`, `type`)
2. Section order is compliant
3. Metadata limits are respected (`name` <= 64 chars, `description` <= 200 chars)
4. Description says both what the skill does and when to use it
5. Intent carries the fuller repo-facing summary without replacing the trigger-oriented description
6. Cross-references resolve
7. README catalog counts and tables are updated (if adding/removing skills)

### Facilitation Source of Truth

When running this workflow as a guided conversation, use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the interaction protocol.

It defines:
- session heads-up + entry mode (Guided, Context dump, Best guess)
- one-question turns with plain-language prompts
- progress labels (for example, Context Qx/8 and Scoring Qx/5)
- interruption handling and pause/resume behavior
- numbered recommendations at decision points
- quick-select numbered response options for regular questions (include `Other (specify)` when useful)

This file defines the workflow sequence and domain-specific outputs. If there is a conflict, follow this file's workflow logic.

## Application

### Phase 0: Design Through Guided Conversation (When Starting from an Idea)

If the user has a raw idea, framework, or unstructured notes — rather than finished source content — run the guided design session first: **read [`references/pm-skill-design.md`](references/pm-skill-design.md)**. It defines a 5-question adaptive conversation (raw material → skill type → naming/scope → key content → pitfalls) plus the PM skill anatomy and metadata constraints, and ends with a complete SKILL.md draft. Then continue at Phase 1 to check for duplicates and at Phase 4 to validate the draft.

If the user already knows what to build, skip straight to Phase 1.

### Phase 1: Preflight (Avoid Duplicate Work)

1. Search for overlapping skills:

```bash
./scripts/find-a-skill.sh --keyword "<topic>"
```

2. Decide type:
- **Component**: one artifact/template
- **Interactive**: 3-5 adaptive questions + numbered options
- **Workflow**: multi-phase orchestration

### Phase 2: Generate Draft

If you have source material:

```bash
./scripts/add-a-skill.sh research/your-framework.md
```

If you want guided prompts:

```bash
./scripts/build-a-skill.sh
```

### Phase 3: Tighten the Skill

Manually review for:
- Clear "when to use" guidance
- One concrete example
- One explicit anti-pattern
- No filler or vague consultant-speak

### Phase 4: Validate Hard

Run strict checks before thinking about commit:

```bash
./scripts/test-a-skill.sh --skill <skill-name> --smoke
python3 scripts/check-skill-metadata.py skills/<skill-name>/SKILL.md
python3 scripts/check-skill-triggers.py skills/<skill-name>/SKILL.md --show-cases
```

### Phase 5: Integrate with Repo Docs

If this is a new skill:
1. Add it to the correct README category table
2. Update skill totals and category counts
3. Verify link paths resolve

### Phase 6: Optional Packaging

If targeting Claude custom skill upload:

```bash
./scripts/zip-a-skill.sh --skill <skill-name>
# or zip one category:
./scripts/zip-a-skill.sh --type component --output dist/skill-zips
# or use a curated starter preset:
./scripts/zip-a-skill.sh --preset core-pm --output dist/skill-zips
```

## Examples

### Example: Turn Workshop Notes into a Skill

Input: `research/pricing-workshop-notes.md`  
Goal: new interactive advisor

```bash
./scripts/add-a-skill.sh research/pricing-workshop-notes.md
./scripts/test-a-skill.sh --skill <new-skill-name> --smoke
python3 scripts/check-skill-metadata.py skills/<new-skill-name>/SKILL.md
```

Expected result:
- New skill folder exists
- Skill passes structural and metadata checks
- README catalog entry added/updated

### Anti-Pattern Example

"We wrote a cool skill, skipped validation, forgot README counts, and shipped anyway."

Result:
- Broken references
- Inconsistent catalog numbers
- Confusion for contributors and users

## Common Pitfalls

- Shipping vibes, not standards.
- Choosing `workflow` when the task is really a component template.
- Bloated descriptions that exceed upload limits.
- Descriptions that say what the skill is but not when Claude should trigger it.
- Descriptions that silently hit the 200-char limit and get cut off mid-thought.
- Letting `intent` become a substitute for a weak trigger description.
- Forgetting to update README counts after adding a skill.
- Treating generated output as final without review.

## Next steps
- `workshop-facilitation` — delegate pacing to it if the new skill is interactive

## References

- [`references/pm-skill-design.md`](references/pm-skill-design.md) — Guided 5-question PM skill-design conversation + PM skill anatomy (absorbed from the retired `pm-skill-creator` skill)
- [`workshop-facilitation`](../workshop-facilitation/SKILL.md) — Interaction protocol for the guided phases
- `README.md`
- `AGENTS.md`
- `CLAUDE.md`
- `docs/Building PM Skills.md`
- `docs/Add-a-Skill Utility Guide.md`
- Anthropic's [Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf)
- `scripts/add-a-skill.sh`
- `scripts/build-a-skill.sh`
- `scripts/find-a-skill.sh`
- `scripts/test-a-skill.sh`
- `scripts/check-skill-metadata.py`
- `scripts/check-skill-triggers.py`
- `scripts/zip-a-skill.sh`
