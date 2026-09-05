# Extracting a design from section images

Use this after inspecting the actual reference images and before implementation.
Record the section, source image, visual priority, and unresolved details.

| Area | What to extract | Implementation consequence |
|---|---|---|
| Copy | Readable headings, support text, navigation, CTA labels | Preserve approved wording; flag illegible or generated claims |
| Typography | Serif/sans character, display/body contrast, relative size, weight, tracking, line height and wrapping | Choose an available named face and a responsive type scale; do not claim exact font identification from appearance |
| Spacing | Outer gutters, section gaps, card padding, text-to-CTA and image-to-text distances | Create repeatable spacing tokens and preserve the visual cadence |
| Layout | Alignment, columns, section order, focal point, density and negative space | Translate into responsive grid/flex rules and an intentional mobile reading order |
| Components | Button hierarchy, shape, padding, outlines, inputs, cards, dividers, shadows and radius relationships | Build consistent component variants and define missing states |
| Colour | Background, surfaces, text hierarchy, accents, borders, image tint and gradients | Preserve palette roles and verify contrast in the implementation |
| Media | Aspect ratios, framing, crop position, overlays and repeating treatments | Use stable frames and correctly fitted assets rather than arbitrary image sizes |
| Identity | Repeated motifs, icon treatment, typography behavior and brand tone | Keep all sections recognisable as the same site |

## Ambiguity and detail images

First preserve the visible layout, spacing, and component family. If a material
detail is still unclear, use a fresh section or detail generation that keeps the
same palette, type character, buttons, radii, and image treatment. Inspect it
before accepting it. Avoid repeated generations that do not resolve a concrete
question; document the remaining assumption or ask for the missing input.

Do not extract a tiny pricing block from a full-page collage and treat it as a
precise specification. A crop can enlarge existing pixels, but cannot recover
illegible copy or missing geometry. Prefer readable section references.

Text recognition is not fact verification. Confirm prices, metrics, customer
names, testimonials, and product claims against supplied content before using
them in production. Use accurate logo artwork rather than generated lettering.

## Fidelity decisions

For each material deviation record the reference, observed relationship,
implemented choice, and reason. Appropriate reasons include mobile layout,
accessibility, available licensed fonts, or a confirmed user change. Avoid
replacing distinctive visual decisions merely because a stock component is
easier to use.

Compare rendered output, not just class names. Whitespace, type hierarchy,
button proportions, and image crops must survive together for the result to
feel like the reference.
