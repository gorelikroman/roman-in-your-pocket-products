# design-critic products

Private companion to [design-critic-core](https://github.com/gorelikroman/design-critic-core):
everything that belongs to our own products and must not travel with the shareable critic.

| Path | What |
|---|---|
| `plugins/design-critic-reboost/` | **Reboost product pack**: the Reboost layer for design-critic (`product.md`, `design-decisions.md`) as a plugin |
| `visual-testing/` | Testplane pilot on the Reboost Storybook: screenshot regression and live layout checks, first results |
| `presentation/` | Team decks, the “Critic in Action” demo page and the short scroll, with standalone HTML |
| `HANDOFF.md` | Where the work stands, for the next agent |

## Install

The critic itself, for everyone (shareable with any team):

```bash
claude plugin marketplace add gorelikroman/design-critic-core
claude plugin install design-critic@design-critic-core
```

A product pack, only for those who work on that product (needs read access to this repository):

```bash
claude plugin marketplace add gorelikroman/design-critic-products
claude plugin install design-critic-reboost@design-critic-products
```

Then name the product in a request: “review the payment form in Reboost”. Without the pack the
critic answers with universal rules only and says so in its first line.

For a whole repository's team, put both marketplaces and plugins in that repository's
`.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "design-critic-core": { "source": { "source": "github", "repo": "gorelikroman/design-critic-core" } },
    "design-critic-products": { "source": { "source": "github", "repo": "gorelikroman/design-critic-products" } }
  },
  "enabledPlugins": {
    "design-critic@design-critic-core": true,
    "design-critic-reboost@design-critic-products": true
  }
}
```

## Adding a product

1. Copy `plugins/design-critic-reboost/` to `plugins/design-critic-<slug>/`.
2. Replace `skills/product-layer/product.md` and `design-decisions.md` with the new product's
   layer (blank ones: design-critic-core `products/_template/`; how to fill them:
   design-critic-core `products/README.md`).
3. Update the names in `skills/product-layer/SKILL.md` and the plugin's `plugin.json`.
4. Add the plugin to `.claude-plugin/marketplace.json`.

Next in line: DoktorABC and the mobile app.

## Updating a pack

Commit the change, bump `version` in the pack's `plugin.json`; teammates run
`claude plugin update design-critic-reboost@design-critic-products`.
