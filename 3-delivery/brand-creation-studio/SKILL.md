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

Behave like a senior brand strategist, creative director, and identity designer working in visible stages. The thinking, experimentation, rejection, refinement, and application are part of the deliverable.

Do not use this full workflow when the user only wants a single brand-board image; use `brandkit` for that narrower task.

## Outputs

**Artifact:** A research-backed brand strategy, identity system, visual exploration record, contextual applications, presentation deck, and handover package

**Format:** Markdown working documents, accurate vector/raster identity assets, generated visual studies and mockups, and a deck/PDF where appropriate

**Location:** `brand-work/<brand-slug>/` by default, or the user's chosen project location

**Audience:** Brand owners, decision-makers, designers, implementers, and production partners

## Core principles

- Do not jump from brief to polished logo. Show the creative journey.
- Use existing conversation and project context before asking questions. Ask only when an unknown genuinely blocks useful progress.
- When information is incomplete, create a provisional brief and label assumptions.
- Use current public research when competitors, culture, category, naming, domains, market, or trends materially affect the work.
- Describe trademark, company-name, and domain checks as preliminary screening, never legal clearance.
- When image-generation tools are available, use them throughout exploration, critique, and contextual testing—not only for final mockups.
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
  03-creative-territories/
  04-sketches/
  05-concept-development/
  06-identity-system/
  07-applications/
  08-brand-deck/
  09-handover/
```

Maintain `decision-log.md` with each material decision, rationale, evidence, alternatives considered, critique, and resulting change. Use it to write the final brand story.

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

### 2. Research and diagnose

Audit a useful sample of direct competitors and adjacent brands. When the market supports it, prefer 8–15 direct competitors and 3–8 adjacent references.

For each, examine logo structure, typography, colour, imagery, layout, motion/digital behaviour, voice, category clichés, distinctive choices, and dated or generic patterns. Do not imitate a competitor.

For a rebrand, also identify what should be retained, what has equity, what feels dated or inconsistent, and what fails at small scale or in digital contexts.

Produce a one-page synthesis:

- category conventions
- whitespace and opportunities
- equity worth preserving
- risks to avoid
- design implications

Research must change design decisions; avoid decorative competitor boards without conclusions.

### 3. Define usable strategy

Create:

- one clear positioning statement
- a brand promise
- 4–6 characteristics, each tied to behaviour and design
- 2–3 productive personality tensions, such as “premium, not aloof”
- voice guidance: sound, anti-voice, rhythm, formality, vocabulary, and headline examples
- 4–6 strategic design principles

Avoid personality lists that could describe any brand.

### 4. Build distinct creative territories

Create 3–5 genuinely different territories before selecting a route. Each includes:

- a name, core idea, and strategic rationale
- visual keywords
- typography, colour, imagery, layout, and composition direction
- symbol or mark opportunities
- a sample verbal line
- 4–8 reference images or generated moodboard frames
- one quick expression “in the world”

Territory test: if the logo were hidden, every territory should still feel recognisably different. Minor colour variations are not distinct territories.

### 5. Experiment before polishing

When image generation is available, generate several intentionally rough black-and-white or limited-colour sketch sheets. Explore 12–30 ideas across wordmarks, monograms, abstract marks, negative space, geometric constructions, ligatures, metaphors, framing, cropping, heritage cues where relevant, and radical/simple extremes.

Explore accurate real-type specimens across case, stacking, width, classification, tracking, weight contrast, and custom letter modifications.

Test colour as a system across light/dark modes, tonal ranges, accessible text/background combinations, imagery, print-like contexts, and digital UI.

Develop motifs that live beyond the logo: frames, lines, crops, patterns, grids, negative space, icons, textures, motion principles, and image treatments.

### 6. Critique and iterate

After every meaningful visual round, read and apply [`references/creative-review-rubric.md`](references/creative-review-rubric.md). Record what works, what fails, strategic fit, distinctiveness, practicality, and the exact next move.

Create at least two visible critique-and-iteration cycles between first sketches and final identity unless the user explicitly requests a smaller exploration. Do not praise everything. Kill weak ideas and explain why.

### 7. Select and develop the route

Choose 1–2 routes on strategic fit and creative quality, not taste alone. Develop:

- master wordmark and stacked/horizontal lockups
- symbol or mark where appropriate
- monochrome, colour, and small-size versions
- favicon or app icon
- clear-space and minimum-size logic
- typography hierarchy
- supporting visual language

State the central design idea in one sentence, then connect it directly to strategy.

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

### 9. Stress-test in context

Choose applications that match the actual business. Include at least:

- one tiny digital context
- one large environmental context
- one formal or corporate context
- one expressive or marketing context
- one black-and-white or one-colour context

Use image generation for environmental mockups, photography direction, signage, campaigns, branded spaces, and contextual tests. Overlay accurate logo artwork and typography where possible instead of asking an image model to redraw them.

If the identity only succeeds on a luxury mockup, it is not finished.

### 10. Review the complete system

Run a final critique against strategic fit, distinctiveness, memorability, coherence, flexibility, accessibility, typography, colour usability, digital readiness, production realism, longevity, category differentiation, and likely confusion risk.

Ask:

> If every logo were removed, would the remaining typography, colour, imagery, and composition still feel like this brand?

If not, strengthen the wider system.

### 11. Tell the creation story

Read [`references/brand-deck-structure.md`](references/brand-deck-structure.md) before building the deck.

Make it editorial and art-directed: generous whitespace, confident typography, full-bleed moments, varied pacing, and restrained UI-like decoration. Show rough work before polished work, explain why ideas changed, and include rejected routes only when they clarify the story.

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

- research has been synthesised into design implications
- strategy is explicit
- at least three creative territories were explored
- visual experiments and sketch sheets exist
- at least two critique/iteration cycles are visible
- the chosen route has a clear rationale
- typography and colour are accurately specified
- a wider visual system exists beyond the logo
- the identity has been stress-tested in realistic contexts
- accessibility and practical constraints were checked
- the final deck tells the creation story
- final assets are organised for handover

If the user explicitly requests a smaller scope, state which completion criteria remain outside that scope instead of pretending the full identity is finished.
