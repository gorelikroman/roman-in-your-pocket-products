# Roman in your Pocket products

Companion to [roman-in-your-pocket](https://github.com/gorelikroman/roman-in-your-pocket):
everything that belongs to our own products and must not travel with the shareable critic.

| Path | What |
|---|---|
| `plugins/roman-in-your-pocket-reboost/` | **Reboost product pack**: the Reboost layer for Roman in your Pocket (`product.md`, `design-decisions.md`) as a plugin |
| `plugins/roman-in-your-pocket-drabc-app/` | **Dr.ABC Application pack**: the layer of the DoktorABC mobile app (Figma file `3GnJD8QN587Y912O3F15Cx`) — handbook, hard rules and the owner's decisions log |
| `visual-testing/` | Testplane pilot on the Reboost Storybook: screenshot regression and live layout checks, first results |
| `presentation/` | Team decks, the “Critic in Action” demo page and the short scroll, with standalone HTML |
| `HANDOFF.md` | Where the work stands, for the next agent |

## Install

The critic itself, for everyone (shareable with any team):

```bash
claude plugin marketplace add gorelikroman/roman-in-your-pocket
claude plugin install roman-in-your-pocket@roman-in-your-pocket
```

A product pack, only for those who work on that product (needs read access to this repository):

```bash
claude plugin marketplace add gorelikroman/roman-in-your-pocket-products
claude plugin install roman-in-your-pocket-reboost@roman-in-your-pocket-products
claude plugin install roman-in-your-pocket-drabc-app@roman-in-your-pocket-products
```

Then name the product in a request: “review the payment form in Reboost”, “design the pause-plan screen for the Dr.ABC app”. Without the pack the
critic answers with universal rules only and says so in its first line.

For a whole repository's team, put both marketplaces and plugins in that repository's
`.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "roman-in-your-pocket": { "source": { "source": "github", "repo": "gorelikroman/roman-in-your-pocket" } },
    "roman-in-your-pocket-products": { "source": { "source": "github", "repo": "gorelikroman/roman-in-your-pocket-products" } }
  },
  "enabledPlugins": {
    "roman-in-your-pocket@roman-in-your-pocket": true,
    "roman-in-your-pocket-reboost@roman-in-your-pocket-products": true,
    "roman-in-your-pocket-drabc-app@roman-in-your-pocket-products": true
  }
}
```

## Adding a product

1. Copy `plugins/roman-in-your-pocket-reboost/` to `plugins/roman-in-your-pocket-<slug>/`.
2. Replace `skills/product-layer/product.md` and `design-decisions.md` with the new product's
   layer (blank ones: roman-in-your-pocket `products/_template/`; how to fill them:
   roman-in-your-pocket `products/README.md`).
3. Update the names in `skills/product-layer/SKILL.md` and the plugin's `plugin.json`.
4. Add the plugin to `.claude-plugin/marketplace.json`.

Next in line: the DoktorABC website.

## Updating a pack

Commit the change, bump `version` in the pack's `plugin.json`; teammates run
`claude plugin update roman-in-your-pocket-reboost@roman-in-your-pocket-products`.

**Reboost follows beluga-ds.** The Reboost pack summarises the design handbook in
`gorelikroman/beluga-ds`; `source.json` in the pack records the commit it was taken from.
After the handbook changes:

```bash
python3 scripts/sync_reboost.py --beluga ../beluga-ds --check   # what changed; exit 1 when behind
python3 scripts/sync_reboost.py --beluga ../beluga-ds           # refresh the log, the commit, the version
```

The script replaces `design-decisions.md` with the new `09-decisions.md` and lists the chapters
whose changes `product.md` must absorb; update that prose (or ask the critic to), commit and
push. The Dr.ABC app pack has no outside source: it is the handbook itself.
