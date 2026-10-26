---
name: product-layer
description: Reboost product layer for design-critic (design system, components, patterns, voice, hard rules, decisions log). Names - Reboost, Reboost UI Kit, beluga-ds, reboost-ui, reboost-checkout, helfy-platform-storybook. Load only when a design-critic request names Reboost or works in the beluga-ds repository.
---

# Reboost — product layer for design-critic

Data, not a procedure. design-critic reads the two files in this folder as the Reboost layer
(design-critic `SKILL.md` · Product layers):

- `product.md` — design system sources, components, patterns, voice, hard rules
- `design-decisions.md` — the decisions log (a snapshot of the handbook's log)

The canonical source is the design handbook in `gorelikroman/beluga-ds`
(`docs/design-handbook/`); on conflict the handbook wins.
