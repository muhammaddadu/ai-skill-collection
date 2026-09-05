---
name: image-to-code
description: Generate or use website reference images, extract their design system, and implement a matching frontend. Use when the deliverable includes working code; use `imagegen-frontend-web` for reference images only.
---

# Image-to-code website workflow

## Purpose and outputs

Turn section reference images into a working website with faithful layout,
typography, spacing, imagery, and component behavior. Use for marketing pages,
portfolios, editorial sites, and visual redesigns.

Deliver reference images, a concise extraction record, working frontend files,
and evidence of visual verification in the user's project. Keep generated
references in a project-owned asset directory; follow existing conventions.

## Shared art direction

Read `imagegen-frontend-web` for the image-design phase. It is the source for
hero composition, section rhythm, palette, typography, media direction, visual
variation, and image-quality checks. Do not invent a second aesthetic rule set
here or layer conflicting frontend presets over the chosen direction.

Its image-only response instructions govern that phase, not the final output
of this workflow: continue through implementation and verification.

User-supplied designs, copy, branding, and requested scope take precedence.
When a precise reference or design system already exists, use it rather than
forcing an unrelated new design. Technical bug fixes do not require generating
a new visual concept.

## 1. Establish the reference set

- Inspect existing project structure, framework, assets, and design constraints.
- Identify the requested sections and primary user action.
- Generate references first when visual exploration is needed and a generator
  is available. In Codex, use built-in `imagegen` and its current tool guidance.
- Prefer one large horizontal reference per section so text, spacing, buttons,
  and layout proportions remain readable. Keep section order, palette, type
  character, CTA family, radius logic, and image treatment consistent.
- For a scoped hero, produce a hero reference; for an eight-section build,
  cover all eight sections. Do not expand a small request to a full-site pack.
- Inspect the actual rendered outputs before implementation. If generation is
  unavailable, state the limitation and use available references without
  claiming generated evidence.

## 2. Extract the design

Read [design extraction](references/design-extraction.md) before translating
images into code. Record per-section findings and unresolved details, with
references to the actual images.

Extract observable relationships rather than presenting estimated pixels or
font identities as measured facts. Separate visible design from proposed
responsive behavior and interaction states that a still image cannot show.

Resolve material ambiguity before building that part. For an unreadable
section, generate a fresh, clearer section or detail reference consistent with
the chosen design. A crop may help inspection, but does not restore missing
detail or prove that invented text and spacing were in the original.

## 3. Implement faithfully

- Preserve section order, composition, whitespace rhythm, text/image balance,
  type hierarchy, palette roles, component families, and media proportions.
- Use semantic HTML and real text, controls, and components. Do not deliver the
  reference screenshot as the website.
- Reuse the project's stack and design tokens; translate the observed design
  into responsive layout rules rather than fixed desktop coordinates.
- Keep the first viewport readable on a small laptop and on mobile. Adapt
  wrapping, stacking, gutters, and media framing without losing hierarchy.
- Use stable media aspect ratios and appropriate image fitting.
- Implement required navigation, links, forms, and state feedback. A visual
  reference does not specify behavior: use the brief and existing product
  conventions to fill those gaps.
- Provide keyboard access, visible focus, readable contrast, and reduced-motion
  behavior. Motion implied by an image is a cue, not proof of an interaction.
- Use supplied or verified copy. Generated testimonials, prices, customer logos,
  and performance claims are concept placeholders, not publishable facts.
- Preserve deliberate visual choices instead of reverting to generic rows,
  tight spacing, nested cards, or decorative technical labels for convenience.

## 4. Compare the built result

Render the implementation and compare each section with its reference at
representative desktop, small-laptop, and mobile sizes.

Check hierarchy, line wrapping, gutters, section cadence, CTA prominence,
media crops, component proportions, palette, and cross-section consistency.
Check actual font loading, overflow, interaction states, and asset paths.

Fix visible drift in code. If a reference cannot work responsively or
accessibly, make the smallest faithful adjustment and record why. Do not
regenerate the reference merely to make a weak implementation look compliant.

If browser or visual inspection is unavailable, report what remains unverified
instead of claiming fidelity from code inspection alone.

## Completion

All requested sections are implemented, usable, and connected to actual
assets. The extraction record distinguishes observed details from assumptions.
Report material deviations and verification limits, and link the working
result and selected reference images. Complete the code deliverable before
ending the image-to-code workflow.
