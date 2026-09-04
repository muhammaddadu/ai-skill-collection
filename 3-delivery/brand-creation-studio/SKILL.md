---
name: brand-creation-studio
description: Create or rebrand an identity through research, strategy, visual exploration, iteration, stress testing, and handover. Use for a full brand journey; use `brandkit` for one presentation board.
metadata:
  intent: Build a strategically grounded, distinctive identity while preserving the visible research, experimentation, critique, rejected routes, refinement, real-world application, and handover evidence that explain how the final system was reached.
  type: workflow
  domain: delivery
---

# Brand Creation Studio

## Purpose

Use this skill to create a new brand, rebrand an organisation, refresh an identity, explore visual directions, or produce a brand-identity presentation that shows the full creative journey.

Behave like a senior brand strategist, creative director, and identity designer. Create an identity that is strategically right, visually distinctive, formally resolved, and usable in the real world. The process is evidence of how the answer was reached; it is not the product.

Do not use this full workflow when the user only wants a single brand-board image; use `brandkit` for that narrower task.

## Outputs

**Artifact:** A research-backed brand strategy, identity system, visual exploration record, contextual applications, presentation deck, and handover package

**Format:** Markdown working documents, accurate vector/raster identity assets, generated visual studies and mockups, and a deck/PDF where appropriate

**Location:** `brand-work/<brand-slug>/` by default, or the user's chosen project location

**Audience:** Brand owners, decision-makers, designers, implementers, and production partners

## Core principles

- Before beginning, read [`references/failure-modes.md`](references/failure-modes.md).
- A complete-looking deck around an average identity is a failed run. Never let a polished deck, mockup, or rationale rescue weak design.
- Use existing conversation and project context before asking questions. Ask only when an unknown genuinely blocks useful progress.
- When information is incomplete, create a provisional brief and label assumptions.
- Proceed end to end without seeking approval at every phase. If the user wants involvement, useful review points are strategy/category diagnosis, first divergent visual round, refined shortlist, and final route before production.
- Do not ask the user to choose among weak routes. If nothing passes a quality gate, say so and loop back.
- Use current public research when competitors, culture, category, naming, domains, market, or trends materially affect the work.
- Describe trademark, company-name, and domain checks as preliminary screening, never legal clearance.
- When image-generation tools are available, use them throughout exploration, critique, and contextual testing—not only for final mockups.
- In Codex, use `imagegen` built-in mode for raster moodboards, sketch sheets, imagery, and mockups. Move selected project assets into the project workspace; use its CLI fallback only when the user explicitly chooses it.
- Never rely on generated image text for final wordmarks or typographic specifications. Render final lettering with accurate type/vector/design tools.
- Avoid close replication of living designers, studios, brands, or recognisable copyrighted campaigns. Competitor references support analysis and differentiation, not cloning.
- Do not hide weak identity design behind beautiful mockups.

## Workspace

Create a structure suited to the requested scope, normally:

```text
brand-work/<brand-slug>/
  00-brief/
  01-research/
  02-strategy/
  03-territories/
  04-visual-lab/
    raw/
    wordmarks/
    marks/
    typography/
    colour/
    systems/
  05-shortlist/
  06-refinement/
  07-final-identity/
  08-flat-comps/
  09-mockups/
  10-brand-story/
  11-handover/
```

Maintain `decision-log.md`, `cliche-red-list.md`, `quality-gates.md`, and `asset-manifest.md`. The decision log records material changes, evidence, alternatives, critique, and next moves; it is not marketing copy.

## Workflow

### 1. Understand the brand

Build or infer a concise brief covering:

- organisation, product, service, purpose, and business model
- current brand state and equity, when applicable
- audiences and buying or decision context
- geography, category, price/market position, and growth ambition
- brand problem, desired business outcome, and emotional goal
- functional, practical, regulatory, and sector constraints
- competitors plus desired and undesired references

Distil it into this design challenge:

> We need to create a brand that feels **[desired qualities]** for **[audience]**, while avoiding **[category clichés or undesired traits]**, so that **[business outcome]** becomes more likely.

Also capture one sentence each for the brand, what the audience needs to feel or believe, and the desired future-state perception. Do not preselect colours, typefaces, or logo metaphors in the brief.

### 2. Research and diagnose

Audit a useful sample of direct competitors and adjacent brands. When the market supports it, prefer 8–15 direct competitors and 3–8 adjacent references.

For each, examine logo structure, typography, colour, imagery, layout, motion/digital behaviour, voice, category clichés, distinctive choices, and dated or generic patterns. Do not imitate a competitor.

For a rebrand, also identify what should be retained, what has equity, what feels dated or inconsistent, and what fails at small scale or in digital contexts.

Create a category saturation map showing what is overused, underused, and genuinely open. Produce `cliche-red-list.md` and a synthesis with:

- category conventions
- whitespace and opportunities
- equity worth preserving
- risks to avoid
- five to eight actionable design implications

Research must change design decisions; avoid decorative competitor boards without conclusions.

### 3. Define usable strategy

Create:

- one clear positioning statement
- a brand promise
- 4–6 characteristics, each tied to behaviour and design
- 2–3 productive personality tensions, such as “premium, not aloof”
- voice guidance: sound, anti-voice, rhythm, formality, vocabulary, and headline examples
- 4–6 strategic design principles

Create three intentionally sharp design provocations that turn the strategic tension into a question the visual lab can test. A provocation should challenge a category assumption rather than restate a brand value.

Avoid personality lists that could describe any brand.

### 4. Build distinct creative territories

Create 3–5 genuinely different territories before selecting a route. Each includes:

- a central idea and the strategic tension it resolves
- an anti-category move and recognition mechanism
- typography, composition, imagery, and colour-behaviour hypotheses
- potential mark behaviours rather than a premature finished logo
- verbal expression and explicit failure conditions

Territory test: if the logo were hidden, every territory should still feel recognisably different. Minor colour variations are not distinct territories.

Do not select a winner from territory prose. A territory earns advancement only after visual evidence exists.

### 5. Experiment before polishing

Read and apply [`references/visual-lab-protocol.md`](references/visual-lab-protocol.md). This is the most important phase. Use multiple independent visual rounds and inspect every actual output before choosing the next move; never critique the prompt instead of the rendered image.

Explore at least four conceptual families. When scope allows, aim for 40–80 raw ideas across wordmarks, typographic interruptions, monograms, negative space, abstract or geometric devices, transformed metaphors, no-symbol systems, responsive marks, and image-led routes.

Explore accurate real-type specimens across case, stacking, width, classification, tracking, weight contrast, and custom letter modifications. Generated lettering is never final typography. Redraw promising marks accurately in vector or another deterministic method.

Test colour as a system across light/dark modes, tonal ranges, accessible text/background combinations, imagery, print-like contexts, and digital UI.

Develop motifs that live beyond the logo: frames, lines, crops, patterns, grids, negative space, icons, textures, motion principles, and image treatments.

### 6. Critique and iterate

After every meaningful visual round, inspect the work and apply [`references/creative-review-rubric.md`](references/creative-review-rubric.md). Record what works, what fails, strategic fit, distinctiveness, practicality, and the exact next move.

Create at least two visible critique-and-iteration cycles between first sketches and final identity unless the user explicitly requests a smaller exploration. Do not praise everything. Kill weak ideas and explain why.

### 7. Select and develop the route

Before shortlisting, create a flat mini-system probe for every serious contender: exact logo/wordmark, type hierarchy, colour behaviour, recognisable layout and graphic devices, imagery direction, one digital application, and one print or environmental application.

Read and apply [`references/quality-gates.md`](references/quality-gates.md). Shortlist no more than 2–3 routes on visible strategic, formal, and system evidence—not taste or rationale alone. If none passes, return to visual exploration. Develop:

- master wordmark and stacked/horizontal lockups
- symbol or mark where appropriate
- monochrome, colour, and small-size versions
- favicon or app icon
- clear-space and minimum-size logic
- typography hierarchy
- supporting visual language

Create at least two refinement iterations for the leading route, documenting specific changes to geometry, spacing, typography, colour, composition, and system logic. State the central design idea in one sentence, then connect it directly to strategy.

### 8. Build the identity system

Define:

- logo family and mark/icon
- clear space and minimum sizes
- colour palette with HEX/RGB and CMYK where relevant
- accessible contrast guidance
- primary/secondary typography and type hierarchy
- layout and grid principles
- photography or illustration style
- iconography, graphic devices, patterns, and motion principles
- tone of voice

Add sound cues, data-visualisation principles, UI tokens, co-branding, sub-brand architecture, campaign systems, or environmental graphics only when relevant.

The system needs at least three recognition assets beyond the logo, such as distinctive type behaviour, colour behaviour, a framing/crop system, a graphic device, imagery treatment, motion, or signature composition.

### 9. Stress-test in context

Design accurate flat comps before environmental mockups. Choose applications that match the actual business, including:

- one tiny digital context
- one core product or conversion context
- one large environmental context
- one formal or corporate context
- one expressive or marketing context
- one black-and-white or one-colour context

Use image generation for environmental mockups, photography direction, signage, campaigns, branded spaces, and contextual tests. Overlay accurate logo artwork and typography where possible instead of asking an image model to redraw them.

A mockup must answer a design question. Composite accurate artwork where possible; do not let an image model invent the final logo or wordmark. If the identity only succeeds on a luxury mockup, it is not finished.

### 10. Review the complete system

Run the red-team review in [`references/failure-modes.md`](references/failure-modes.md), then apply the final-route and production gates in [`references/quality-gates.md`](references/quality-gates.md).

Ask:

> If every logo were removed, would the remaining typography, colour, imagery, and composition still feel like this brand?

If not, strengthen the wider system. Do not proceed to presentation because the schedule or folder structure says to.

### 11. Tell the creation story

Read [`references/brand-deck-structure.md`](references/brand-deck-structure.md) before building the deck.

Curate the presentation only after the identity is good. Make it editorial and art-directed: generous whitespace, confident typography, full-bleed moments, varied pacing, and restrained UI-like decoration. Show visual evidence, ideas that died, breakthrough, and refinement; include rejected routes only when they clarify the story.

### 12. Package the handover

Unless the user requests a smaller scope, deliver:

- `brand-strategy.md`, `research-summary.md`, and `decision-log.md`
- accurate logo family in appropriate vector/raster formats
- colour, typography, imagery, and visual-system specifications
- moodboards, sketch sheets, concept sheets, and iteration comparisons
- realistic mockups and relevant digital/campaign concepts
- presentation deck and PDF where appropriate
- concise brand-guideline document
- asset manifest, source-file list, font/licensing notes, and implementation notes

## Creative-director behaviour

Be decisive and connect critique to the brief. It is useful to say that a route is strategically strong but generic, memorable but fragile at small sizes, visually premium while the core identity does too little, or simply should be killed.

When a concept fails, record why and change direction rather than endlessly polishing it.

## Completion criteria

Do not call the brand finished until:

- research produced a specific cliché red list and actionable implications
- at least three materially distinct territories were visually explored
- divergent generated rounds were inspected between iterations
- exact typography studies use named, licensable typefaces
- promising marks were redrawn accurately
- two or three serious routes became flat mini-systems before selection
- the leading route has at least two visible refinement iterations
- the final route passes the quality gates, including no-logo, monochrome, small-size, accessibility, and production tests
- at least three recognition assets exist beyond the logo
- flat comps prove the system before mockups
- the final red-team review has no unresolved generic default
- the deck was curated after the identity and final assets are organised for handover

If the user explicitly requests a smaller scope, state which completion criteria remain outside that scope instead of pretending the full identity is finished.
