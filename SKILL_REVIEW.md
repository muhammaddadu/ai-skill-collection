# Skills collection review — 2026-09-05

## Scope and evidence

Reviewed the inventory and discovery descriptions of all 140 repository skills,
scanned their entrypoints for repeated content and oversized bodies, and ran
repository-wide manifest, path, name, description, and YAML checks. Semantic
review focused on overlapping workflows and the instructions changed below.
No byte-identical entrypoints were found.

This is a collection and instruction review, not an execution test of every
domain workflow. External provider capabilities, platform benchmarks, and
vendored technical guidance were not comprehensively revalidated online.

## Improvements

| Area | Change |
|---|---|
| Shared facilitation | 25 consumers now load the canonical protocol rather than copying its rules; redundant interaction paragraphs removed |
| Discovery | Clarified direct synthesis versus workshops for positioning, journeys, and story maps |
| Web design | `image-to-code` reuses `imagegen-frontend-web` for art direction and owns extraction, implementation, and visual verification |
| Design presets | Clarified general UI versus specific material/motion styles; removed simulated Python execution claims and added reduced-motion handling |
| Brandkit | Moved optional logo methods, visual modes, and prompt template into routed references; entrypoint reduced from 802 to 496 lines |
| Image providers | `gpt-image` targets requested CLI/API execution or gallery consultation; ordinary Codex image work routes to built-in `imagegen` |
| Networking | Scoped the Expo client skill to React Native/Expo rather than every network operation |
| Full output | Scoped completeness guidance to explicit unabridged requests and allowed complete workspace artifacts |
| Ads | One audit owner and one scoring reference; added missing platform coverage, unverified-evidence handling, and explicit aggregate normalization |
| Authoring | Replaced obsolete commands and conflicting metadata guidance in the PM design reference |

All 140 invocation names and both manifest memberships are retained. Total
entrypoint lines decreased from 43,201 to 41,535. Some content moved into
references; the reduction is not a claim that all those lines were deleted.

## Deliberate boundaries

- Mobile image concepts retain platform, safe-area, navigation, and flow guidance.
- Accessibility/code audits retain a separate purpose from aesthetic design.
- Research collection and executive narrative synthesis remain distinct stages.
- Workflow and workshop skills keep their domain-specific questions and outputs.
- Legacy `design-taste-frontend-v1` remains available for explicit compatibility.
- Plugin-managed and separately installed skills were not rewritten by this repository pass.

## Validation and remaining limitations

- Repository lint passes for all 140 skills and both manifests.
- All 140 YAML frontmatters parse, and names match directories.
- Both installations resolve all 140 manifest entries to the intended repository directories.
- No broken top-level symlinks were found in the Codex, Claude, or agents skill roots.
- Rewritten schema-compatible skills pass the bundled Codex validator.
- The strict Codex validator rejects legacy top-level metadata in 114 skills;
  the other 26 pass. These existing fields include both descriptive metadata
  and runtime-facing fields such as invocation hints. They were retained to
  avoid silently changing cross-runtime behavior. Discovery/link checks do not
  prove every runtime interprets every legacy field identically.
- Several long vendor entrypoints remain. Further extraction should be guided
  by actual invocation behavior and preserve upstream provenance.

## Review scenarios

Checked instruction routing for a ready-to-write positioning statement versus
a guided workshop, a website-image request versus a working website request,
an Expo request versus server networking, and default Codex images versus an
explicit CLI request. These are instruction walkthroughs, not independent
end-to-end generation tests.
