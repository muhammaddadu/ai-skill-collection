---
name: comic-sketch-story
description: "Draw a process or vision as a one-page hand-drawn comic strip (HTML, rough.js) with an Excalidraw export. Use when asked to sketch a story, draw a flow as a comic, or turn a pitch into a picture. Do NOT use for a written six-frame narrative (storyboard) or a formal slide deck."
type: component
domain: utilities
tested_date: 2026-10-27
requires: "roughjs 4.6.6 (CDN); Excalidraw clipboard/file format v2"
---

# Comic sketch story

## Purpose
Tell one story in a single picture: a strip of four to eight comic panels, drawn by hand on dotted paper,
that follows one thing (a recommendation, an order, a ticket, a customer) from start to finish. It is for
executives and teams who will not read a document but will look at a picture for thirty seconds. The page
also copies itself into Excalidraw, so the reader can keep editing it there.

## Outputs
**Artifact:** a comic sketch page, plus an optional `.excalidraw` file
**Format:** a single self-contained HTML file (rough.js from jsDelivr, Google Fonts) and Excalidraw JSON
**Location:** the target repo's deliverables folder, e.g. `deliverables/<slug>-sketch.html` and `<slug>.excalidraw`
**Audience:** leaders and teams who need the story at a glance; anyone who will rework it in Excalidraw

## Prerequisites
- The story itself: who does what, in what order, and what changes for whom. If it is not settled, agree
  the beats in prose first (`storyboard` or a short list), then draw.
- Facts that appear on the page come from the user or their sources. A number with no source does not go on it.

## Workflow

1. **Write the beats before drawing.** One line per panel, four to eight panels, in order. Each beat is
   something a named person or system does. Name the actors the way the business does, and ask who they are
   if unsure: who spots, who approves, who carries it out. Mark the human checkpoints.
2. **Copy `assets/template.html`** to the target location and edit only the `STORY` block:
   - `title` (short, upper case in the comic face), `subtitle`, `stamp` (e.g. DRAFT or empty)
   - `panels[]`: `title`, `caption` (two lines, about 34 characters each), `prop`, and the prop's fields
   - optional `loop`, `tags`, `notes`, and `description` (the accessible label)
   For the props and their fields, read `references/props.md`.
3. **Write captions plainly.** Each says what happens and to whom. No slogans, no "not X but Y", no
   clipped fragments like "Each change arrives with why". Run `humanizer` over the captions and notes.
4. **Keep it light.** One caption and at most one bubble or sound effect per panel. Leave out timelines,
   pencilled caveats and open questions unless asked; they belong in the reply or a companion doc.
5. **Look at it once.** Render the page at about 1440px wide and check for: captions running past their
   box, the subtitle colliding with the title, tags overlapping panel titles. Fix, then publish.
6. **Export.** The page's "Copy for Excalidraw" button puts the scene on the clipboard; paste it into a
   blank canvas at excalidraw.com. For a file, run
   `node scripts/export-excalidraw.js <page.html> <out.excalidraw>` and hand over the file.
7. **Publish** as an artifact or share the file. If it is an artifact, say who can open it.

## Pitfalls
- **Busy page:** three-line captions, pencil notes and a timeline on every panel → nobody reads it → one
  plain two-line caption per panel; move the rest to the reply.
- **Bombast:** slogans and contrast lines read as AI → readers discount the whole picture → plain
  statements of who does what, checked with `humanizer`.
- **Wrong actors:** a single named analyst standing in for a whole group → stakeholders object to the
  picture → ask who spots, who approves, who executes, and draw the groups.
- **Product names fighting:** two product names with equal weight confuse the story → tag the lead product
  with a sticker and the supporting one with a quiet pencil note (`tags[].quiet`).
- **Downloads blocked:** artifact viewers block page-started downloads → the export is a clipboard copy
  with a selectable-text fallback, and the `.excalidraw` file comes from the script.
- **Excalidraw text overflow:** Virgil is wider than the page fonts → the engine shrinks exported text
  (0.74 hand, 0.7 comic) and sizes boxes from measured Virgil widths; keep those factors if you edit it.
- **Caption overflow:** more than about 34 characters per line spills past the caption box → shorten the
  words, never the font.

## Next steps
- `humanizer` for the final pass on captions
- `storyboard` when the story needs a written narrative alongside the picture
