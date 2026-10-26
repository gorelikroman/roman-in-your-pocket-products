# Handoff — where the work stands and where to start

For the next agent. State as of 2026-10-26. The owner writes in Russian: answer in Russian,
briefly. Rule names, IDs and severity stay English.

## Three repositories

| Repository | Visibility | What |
|---|---|---|
| `gorelikroman/design-critic-core` | shareable | **The critic.** Product-neutral: no product or company is named anywhere, history included. Plugin `design-critic@design-critic-core`. English only (`scripts/check_skill.py` enforces it). |
| `gorelikroman/design-critic-products` | private (this one) | **Our products.** Product packs (`plugins/design-critic-<slug>/`), the Testplane pilot, presentations, this note. |
| `gorelikroman/design-critic` | private, legacy | The repository the core was split from. Its history holds the Reboost layer. Superseded by the two above; keep it read-only. |

`gorelikroman/beluga-ds` (the Reboost design system) is read-only for agents.

## Read first

1. design-critic-core `README.md` and `SKILL.md` — modes, language, product lookup, precedence.
2. design-critic-core `products/README.md` — layers and how a pack is built.
3. design-critic-core `notes/owner-decisions-2026-09-26.md` — the owner's decisions.
4. `plugins/design-critic-reboost/skills/product-layer/product.md` — the only product so far.
5. `visual-testing/README.md` — the Testplane pilot and its results.

## Settled rules

- **The core never names a product or a company.** Anything about Reboost, DoktorABC, the
  mobile app or our company goes to this repository.
- The core lookup order: installed packs (`design-critic-<slug>:product-layer`), then the
  core's `products/*/`, then the working repository's `.design-critic/`. A product is never
  guessed: with no name and no repository layer, universal rules only.
- Reply in the language of the request; IDs, severity and state names stay English.
- Before pushing to the core: `python3 scripts/check_skill.py`.

## Open work

1. **DoktorABC pack** and **mobile app pack** — full study of each product: design system
   from Figma and tokens, key screens, decisions log; the mobile app adds iOS and Android
   rules (lenses 12, 14). Waiting on the owner for Figma libraries, tokens and 5–10 reference
   screens per product. DoktorABC is medical: overshoot and bouncy easing are blocking there.
2. **Browser extension** for QA and reviews: run design-critic-core `scripts/live-checks.js`
   on the open page, highlight findings, compare with the Figma frame, file a bug from
   `templates/bug-report.md`. The checks already ran on all 349 Reboost stories
   (`visual-testing/`).
3. **Testplane in beluga-ds CI**: move `visual-testing/` config and references into beluga-ds
   so both passes run on its pull requests (owner's change; read-only for agents).
4. **Demo page cuts**, proposed and not answered (`presentation/demo/critic-in-action.html`):
   drop “A button that doesn’t respond” and “A toast that eases in”; fix the ⌘K card with real
   keyboard input; default the Reduce Motion checkbox to on; merge the seven text-only QA cards
   into one checklist.
5. **A catalog citation to check** in the core: `lenses/09-motion-and-interaction.md` ·
   Motion gaps cites `N-08`, which is about layout shift, not appear and disappear transitions.

## What the owner values

- Plain words over terms; one idea per block; something visible or clickable.
- Depth shown with real numbers, real rule IDs and real script output; never invented rules.
- Material for every role: designer, developer, product manager, QA.
