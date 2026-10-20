---
name: cleanui
description: "Distinctive, professional UI without generic AI patterns: pick a bold aesthetic direction, then enforce typography, layout, and platform rules. Use when building or styling web pages, landing pages, dashboards, or components - React, React Native, SwiftUI, Compose, HTML/CSS. Do NOT use for palette/font/style lookups (use ui-design-system-search)."
version: 1.0.0
---

# CleanUI — AI UI Design Enforcement Skill

Use this as the general interface design workflow. For a marketing page led by art direction, `design-taste-frontend` is an alternative. Choose one primary aesthetic workflow; load a specific style preset only when it matches the brief. User requirements, the existing design system, and accessibility take precedence over stylistic bans below.

For substantial visual work, read [visual refinement](references/visual-refinement.md)
for direction exploration, human taste feedback, rendered critique, bounded
iteration, subtraction, media selection, and verification. Reuse that process
rather than adding another review loop. For a small fix, inspect the changed state.

Treat aesthetic examples and limits below as diagnostics, not universal quotas.
Choose typography, section order, components, and effects for the actual content.
Truthful data, accessible interaction, and working behavior remain requirements.

> **STOP. Before you write ANY UI code, read this file.**
>
> You are an AI code generator with deeply ingrained UI habits that produce recognizable "AI-looking" output. This skill exists to override those habits and produce professional, human-designed interfaces.
>
> **Your process for every UI task:**
> 1. Pick a deliberate aesthetic direction (section below) — before any code
> 2. Think about what you would NORMALLY generate
> 3. Check each element against the HARD NO list below
> 4. Replace every violation with the specified alternative
> 5. Only then write the code

> Need to *look up* a palette, font pairing, style, or chart type by keyword? Use the `ui-design-system-search` skill — this skill is for designing and writing the UI itself.

---

## AESTHETIC DIRECTION (BEFORE YOU CODE)

Generic output is a choice you make by not choosing. Before coding, understand the context and commit to a BOLD aesthetic direction:

- **Purpose**: What problem does this interface solve? Who uses it?
- **Tone**: Pick an extreme: brutally minimal, maximalist chaos, retro-futuristic, organic/natural, luxury/refined, playful/toy-like, editorial/magazine, brutalist/raw, art deco/geometric, soft/pastel, industrial/utilitarian, etc. There are so many flavors to choose from. Use these for inspiration but design one that is true to the aesthetic direction.
- **Constraints**: Technical requirements (framework, performance, accessibility).
- **Differentiation**: What makes this UNFORGETTABLE? What's the one thing someone will remember?

**CRITICAL**: Choose a clear conceptual direction and execute it with precision. Bold maximalism and refined minimalism both work — the key is intentionality, not intensity.

Then implement working code that is production-grade and functional, visually striking and memorable, cohesive with a clear aesthetic point-of-view, and meticulously refined in every detail.

### Executing the Direction

- **Typography**: Choose fonts that are beautiful, unique, and interesting. Avoid defaulting to generic web fonts (Inter, Roboto, Arial); opt for distinctive, characterful choices that elevate the aesthetic. Pair a distinctive display font with a refined body font. (On native mobile, platform system fonts still apply — see MOBILE RULES.)
- **Color & Theme**: Commit to a cohesive aesthetic. Use CSS variables for consistency. Dominant colors with sharp accents outperform timid, evenly-distributed palettes.
- **Motion**: Use animations for effects and micro-interactions. Prioritize CSS-only solutions for HTML; use the Motion library for React when available. Focus on high-impact moments: one well-orchestrated page load with staggered reveals (animation-delay) creates more delight than scattered micro-interactions. Use scroll-triggering and hover states that surprise.
- **Spatial Composition**: Unexpected layouts. Asymmetry. Overlap. Diagonal flow. Grid-breaking elements. Generous negative space OR controlled density.
- **Backgrounds & Visual Details**: Create atmosphere and depth rather than defaulting to solid colors. Add contextual effects and textures that match the overall aesthetic: gradient meshes, noise textures, geometric patterns, layered transparencies, dramatic shadows, decorative borders, custom cursors, grain overlays.

**NEVER** use generic AI-generated aesthetics: overused font families, cliched color schemes (particularly purple gradients on white backgrounds), predictable layouts and component patterns, cookie-cutter design that lacks context-specific character. Interpret creatively and make unexpected choices that feel genuinely designed for the context. No two designs should be the same — vary between light and dark themes, different fonts, different aesthetics. NEVER converge on common choices (Space Grotesk, for example) across generations.

**IMPORTANT**: Match implementation complexity to the aesthetic vision. Maximalist designs need elaborate code with extensive animations and effects. Minimalist or refined designs need restraint, precision, and careful attention to spacing, typography, and subtle details. Elegance comes from executing the vision well.

Once the direction is chosen, verify execution against the brief and the shared review protocol. The examples below help diagnose defaults; a justified aesthetic choice is not a failure merely because it differs. (This section is adapted from the frontend-design skill, Apache 2.0 — see [references/frontend-design-LICENSE.txt](references/frontend-design-LICENSE.txt).)

---

## COMMON DEFAULTS TO QUESTION

Use these prompts to find accidental defaults. Retain a choice when it serves the
brief or established design system; do not replace one template with another.

### Typography
- Choose weights that establish hierarchy and remain legible in the selected face.
- Heavy display type may fit an expressive direction; avoid making every element bold.

### Logo / Trust Bars
- **BANNED:** Company names as identical plain text in identical bordered pills/boxes
- **USE INSTEAD:** Make each logo visually distinct — pair icons with names, vary weight/italic/tracking per logo, or use SVG logos
- **SELF-CHECK:** Do all logos look identical? Fix it.

### Uppercase / Letter Spacing
- **BANNED:** `tracking-[0.18em]`, `tracking-[0.2em]`, `tracking-[0.24em]` or any custom wide letter-spacing
- **BANNED:** More than 2 uppercase tracked labels on the entire page
- **USE INSTEAD:** Sentence case. If uppercase needed, `tracking-wider` (0.05em) max.

### Eyebrow Badges
- **BANNED:** Decorative pill/badge above headlines that restates what the headline says (e.g., "AI writing system for content teams")
- **USE INSTEAD:** Remove entirely, or use factual info: "Now in beta", "Trusted by 2,400 teams", "Free plan available"

### Hero Headlines
- Inspect wrapping, hierarchy, and reading effort at the actual viewport sizes.
- Shorten or resize copy when it obscures the message; expressive multi-line
  headlines and longer explanatory text may be appropriate for the content.

### Decorative Copy
- **BANNED:** Ornamental labels like "Live pulse", "Night shift", "Operational clarity without the clutter"
- **USE INSTEAD:** Real data (status, counts, dates) or remove entirely. Every label must serve a function.

### Shadows
- **BANNED:** `shadow-xl`, `shadow-2xl`, blur above 8px on cards
- **USE INSTEAD:** `shadow-sm` or `shadow-none` with subtle border.

### Border Radius
- **BANNED:** Random mixing of `rounded-md`, `rounded-xl`, `rounded-2xl`, `rounded-3xl`, `rounded-[24px]`, `rounded-[32px]`
- **USE INSTEAD:** Pick 2-3 values. Cards: 8-12px. Buttons: 6-8px (or `rounded-full` for pills). Inputs: 6-8px. Be consistent.

### Icons
- **BANNED:** Unicode characters as icons (`↑`, `↓`, `◌`, `⌂`, `◫`)
- **USE INSTEAD:** lucide-react (web), @expo/vector-icons (React Native), SF Symbols (iOS), Material Icons (Android)

### File Structure
- **BANNED:** Entire app in a single file
- **USE INSTEAD:** Separate: screens/pages, components, constants/theme, data, navigation

### Fabricated Data
- **BANNED:** Sparklines, trend lines, bars, gauges or figures made from hard-coded or randomly generated values, in any product that displays real data
- **USE INSTEAD:** Chart only what a query returns. If the honest series isn't available or is too expensive to compute, show a different *measured* fact (a count, a share, a "top X holds N%") or nothing at all.
- **WHY:** In an analytics, finance, health or ops product, a decorative chart is a false claim about the data. The design-system tile that has a sparkline slot does not entitle you to invent a series to fill it.
- **SELF-CHECK:** For every visual encoding on the screen, name the field it came from. Can't? Delete it.

---

## LAYOUT RULES

### Match Layout to Content Type

| Content Type | Layout | Don't Use |
|---|---|---|
| Images/visual (food, travel, products) | Horizontal carousels, image grids, hero images | Text-only vertical lists |
| Data/numbers (finance, fitness, analytics) | Stat cards, progress bars, metric grids | Hero image cards |
| Feed (social, news, posts) | Full-width stacking cards, infinite scroll | Sectioned layout with drag handles |
| Items to browse (e-commerce, tasks, email) | Vertical list with search/filters | Hero sections |
| Multimedia (streaming, music, podcasts) | Horizontal scroll shelves (Netflix-style) | Vertical lists |
| Chat/messages | Contact list + chat detail | Hero cards or stat grids |
| Maps/location | Map view + bottom sheet overlay | Standard list layout |

### Component-Relative Layout
- A component that renders in more than one container width (full page, side panel, modal, print) must respond to **its own** width, not the viewport. Use container queries (`@container` + `@md:`/`@lg:` in Tailwind v4, `container-type: inline-size` in CSS).
- Symptom you are missing this: a card looks right on the page and breaks inside a drawer or split view, and the "fix" is a pile of viewport breakpoints that contradict each other.

### Anti-Templating Rules
- **NEVER use the same layout skeleton for every app.** Read the prompt, identify the content type, pick the right layout.
- **NEVER use ALL of these together:** hero card + grid buttons + drag handle + segmented control + vertical list. That's a template.
- If the app is image-heavy, show **actual images** — thumbnails, photos — not just icons in rounded squares.
- Use **horizontal scrolls** (`FlatList horizontal`, CSS `overflow-x-auto`) for categories, featured items, content shelves. AI generators underuse these.

---

## DESIGN TASTE

### One Expressive Element
- When a brand owns a signature gradient, texture or illustration style, use it **once per view**: one headline word, one card edge, one primary action. Repeating it on every surface turns a brand asset into wallpaper and destroys hierarchy.
- Never use a brand gradient as a fill for data (bars, lines, map regions). Data colour comes from a dedicated chart palette, so series stay distinguishable and never collide with chrome.

### Color Restraint
- Monochrome or near-monochrome palettes often look better than colorful ones.
- Color should appear mainly in actions (buttons, links), status (badges), and highlights (selected states). Not on everything.
- Dark elements (cards, sections) are justified ONLY when they represent a real-world object (credit card, media player, code block) or create deliberate visual rhythm. Not just "for variety."

### List Items
- **NEVER use letter initials as the only identifier.** Use category-specific icons (utensils for restaurant, bus for transport, repeat for subscription) in rounded squares.
- Always include **metadata**: date/time, category, status. "Restaurant" feels fake. "Restaurant · May 5 · 14:28" feels real.

### Filters
- Any list with 5+ items should have a filter or segmented control.
- Segmented control: pill-track style with solid fill on selected segment.

### Action Buttons
- Borderless style often looks cleaner: icon in muted-background square + label below. No card wrapper, no shadow, no border needed.

---

## MOBILE RULES

See [Mobile Patterns Reference](references/mobile-patterns.md) for full iOS color palettes, Android Material 3 tokens, component guidelines, and code examples.

### All Platforms
- Use **real navigation libraries**, not custom View-based nav bars. React Native: `@react-navigation/bottom-tabs`. iOS: `TabView`. Android: Material `NavigationBar`.
- **NEVER build floating pill-shaped bottom nav bars.** No `position: absolute`, no `borderRadius: 28`, no dark floating pill.
- Use **Platform.select()** or **Platform.OS** for conditional styling in React Native.
- Define design tokens (colors, spacing, radii, typography) in a constants file.
- Handle 3 states per screen: loading (skeletons), content, empty.

### iOS
- Quiet, soft, premium. Restrained color. System fonts (SF Pro). Semantic colors (`.label`, `.secondaryLabel`, `.systemBackground`). Translucent nav/tab bars. `listStyle(.insetGrouped)`. SF Symbols for icons. Hairline separators. Corner radius: 10-12. No heavy shadows — use background contrast.

### Android (Material 3)
- Structured, bold, expressive. Material components from `material3`. Tonal surfaces (`tonalElevation`) instead of drop shadows. `Scaffold` with `TopAppBar` + `NavigationBar`. `ListItem` composable for list rows. `HorizontalDivider()` between items. Corner radius: 12dp for cards. Generate color scheme from seed color.

### React Native / Expo
- Platform-conditional colors, shadows, and spacing via `Platform.select()`.
- iOS uses `shadowColor`/`shadowOpacity`/`shadowRadius`. Android uses `elevation`.
- Different background colors per platform: iOS `#F2F2F7`, Android `#F9F9FF`.
- Different primary colors: iOS `#007AFF`, Android uses Material seed color.

---

## WEB RULES

### Creative Freedom + Structure
You have freedom on: color palette, font choice, border radius values, brand personality, background treatments.

Section structure, headline wrapping, and component patterns follow the content
and task. Responsive behavior and accessibility must be verified.

### Navigation
- Choose navigation placement and persistence for the information architecture.
- Show the primary action clearly; verify usable small-screen navigation.
- Blur, stickiness, and a hamburger are options, not required styling.

### Landing Page Structure
Build a narrative around the audience's actual decision: what it is, why it
matters, credible evidence, and the relevant action. Include pricing, testimonials,
feature grids, or a process explanation only when the product and supplied content
justify them. Select section count, order, and composition accordingly. Never
invent customer endorsements or add an empty section to complete a template.

### Hero
- Establish the main promise and primary action with a clear reading order.
- Choose type-led, image-led, interactive, or split composition for the brief.
- Add secondary actions and proof only when they improve the user's decision.

### Feature Cards
- Icon container: at least 48px with tinted background. Not tiny.
- Card padding: generous (p-6 to p-8).
- Each card should feel full — icon + title + description.

### Pricing
- Featured tier: inverted (dark bg, light text) or thicker border + "Most popular" badge.
- Full-width CTA in each card.

### Sign-In
- Prioritize a clear form, supported authentication methods, recovery, and feedback.
- Include a brand panel or social login only when justified by the product.

### Dashboard
- Organize around the user's recurring tasks and actual available data.
- Choose navigation and density for those tasks; do not add greetings, stat cards,
  upgrade prompts, or activity feeds merely to fill a dashboard skeleton.

### Dark Mode
- Background: very dark gray, not pure black.
- Text: off-white, not pure white.
- Borders: dark gray. Reduce color saturation.

---

## PRE-OUTPUT CHECKLIST

Before returning code, verify:

Apply the aesthetic prompts below only where relevant to the chosen direction.
Complete the evidence and subtraction checks in the shared visual-refinement
reference; a stylistic count is not a substitute for inspecting the result.

**Typography:**
- [ ] Type weights create a deliberate, readable hierarchy

**Visual:**
- [ ] No `tracking-[0.18em]` or wider
- [ ] Max 2 uppercase labels on the entire page
- [ ] Logo bar items look visually distinct from each other
- [ ] No shadow-xl or shadow-2xl on cards
- [ ] Consistent border radius (2-3 values max)

**Hero:**
- [ ] Headline wrapping and scale support the chosen hierarchy at tested sizes
- [ ] Eyebrow badge (if present) adds new info, doesn't restate headline
- [ ] Subtitle is 1-2 sentences, not a paragraph

**Structure:**
- [ ] Multiple files (screens, components, constants, navigation)
- [ ] Real icon library (not Unicode)
- [ ] Platform-specific styling (React Native)
- [ ] Loading/empty states exist

**Layout:**
- [ ] Layout matches content type (not the same template every time)
- [ ] List items have category icons + metadata
- [ ] Lists with 5+ items have filters
