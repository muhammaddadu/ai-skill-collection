# Panel props

Every panel has `title`, `caption` and `prop`. Optional on any panel: `accent: true` (purple title, use for
the human checkpoint and the readout), `accent2: true` (blue title, use for the loop's end), `dots: true`
(halftone background; at most two panels).

| prop | Draws | Fields |
|---|---|---|
| `laptop` | A laptop with a data grid and source labels either side | `left`, `right`: up to three short lines each, e.g. `'orders\nprices\nstock'` |
| `split` | People with a magnifier on the left, a robot detector on the right, a dashed divider | `people` (1–3), `peopleLabel`, `peopleNote` (e.g. "human in the loop"), `botLabel`, `sfx` (e.g. "BEEP!") |
| `card` | A form card with up to three field labels and ruled lines | `fields` (max 3), `accentField` (the one drawn in purple, e.g. "Why") |
| `approve` | One or two people, a ticked card, a stamp and a speech bubble | `labels` (max 2), `bubble`, `sfx` (stamp text, e.g. "APPROVED") |
| `stores` | Three hatched test sites and three outlined control sites | `testLabel`, `controlLabel`, `sfx` (e.g. "WHOOSH!") |
| `phone` | A person with a speech bubble and a phone showing a message and a "why" box | `personLabel`, `bubble`, `app`, `body` (two short lines), `why` |
| `chart` | Test vs control lines with a "live" marker, and up to three ticks | `checks` (max 3) |
| `rule` | A rule card, an arrow to a site, and a robot saying something | `rule` (two lines), `botSays` |
| `none` | Nothing; the caption carries the panel | — |

## Story-level options

| Key | What it does |
|---|---|
| `loop: { from, to, label }` | A curved arrow from panel `from` back to panel `to` (0-based), e.g. a detection feeding back to spotting |
| `tags: [{ panel, text, at, quiet }]` | `at`: `top` (above the panel), `bottom-left`, `bottom-right`. `quiet: true` draws a grey pencil note instead of a sticker |
| `notes: { heading, items }` | Up to five yellow sticky notes under the strip, two short lines each |
| `description` | The accessible label for the whole picture: one sentence per panel, in order |

## Adding a prop
Add a function to `PROPS` in the template: `name: function (x, y, p) { ... }`. Draw inside
`x..x+300`, `y+44..y+208`; the title box sits above and the caption box below. Use the helpers
(`rect`, `line`, `circ`, `ell`, `poly`, `curve`, `lpath`, `text`, `arrow`, `person`, `robot`, `house`,
`bubble`, `sfx`) so the shape is recorded for the Excalidraw export too. A raw `document.createElementNS`
draws on the page but does not export.
