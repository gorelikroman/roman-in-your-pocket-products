# Product layer — Reboost

> Loaded on top of the universal rules whenever work concerns Reboost (Roman in your Pocket `products/README.md`).
> Only the product owner edits this file; builds and reviews propose changes.
>
> **Names:** Reboost · reboost · Reboost UI Kit · beluga-ds · reboost-ui · reboost-checkout ·
> helfy-platform-storybook — every name people use for this product in requests.
>
> Product owner: Roman · Design system owner: Roman · Last updated: 2026-11-27 ·
> Decisions log: `design-decisions.md` (this folder, a snapshot).

## 0. Source of truth — read this first

This layer is a **portable summary**. The canonical source is the Reboost design handbook in
the `gorelikroman/beluga-ds` repository (`docs/design-handbook/`, captured from the live Figma
2026-09-07; typography decided 2026-09-15; spacing 2026-09-28; My Account 2026-09-27 … 10-05).
This summary was taken from beluga-ds commit `849f214f` on 2026-11-27 (handbook last changed
2026-10-05). `source.json` in this folder records the commit; `scripts/sync_reboost.py` in the
products repository compares it with beluga-ds and refreshes the layer.

- **When the beluga-ds repository is available** (the working directory, or a clone): read
  the handbook files named below and trust them over this summary. If they disagree, the
  handbook wins; point out the drift so this layer gets refreshed.
- **When it is not** (the desktop app, claude.ai, another repository): work from this file and
  `design-decisions.md`; say "Product: Reboost (summary layer, beluga-ds@849f214f)".
- **Refreshing this layer:** `python3 scripts/sync_reboost.py --beluga <path>` (products
  repository) replaces `design-decisions.md` with the new `09-decisions.md`, records the commit,
  bumps the version and lists the handbook chapters that changed; then update the prose of this
  file for those chapters.
- **Inside beluga-ds, chapter 20 binds the critic** (`20-design-critic-binding.md`, 2026-10-05):
  the project log is `09-decisions.md` — never create a `design-decisions.md` there and never run
  the bootstrap of the review method; the yardstick order is `05` §8 → `05` §4b + `09` → `15` →
  `13` → `16` → `05` §9 → the lenses; a just-built mockup gets the **light mode** (lenses 01 · 04 ·
  05 + 02 and the spacing check, a findings table in chat, blocking stops the handover), a review
  the **full mode** (`reviews/<date>-<slug>/`, the decision board is the project's `review-board`
  skill). Chapter 20 calls the critic by its former name `design-critic` and checks
  `~/.claude/skills/design-critic/SKILL.md`; the critic is now Roman in your Pocket (plugin
  `roman-in-your-pocket`) — read that name as this skill.

Which handbook files each mode reads (all under `docs/design-handbook/`):

| Mode | Read | Why |
|---|---|---|
| build | `15-pattern-library.md` (+ `15-patterns.json`) → `13-typography-roles-and-patterns.md` → `16-spacing.md` → `02-tokens.md` → `04-components.md` → `05-design-rules.md` | shell → blocks → atoms, type roles, gaps, tokens, components, laws |
| review | `20-design-critic-binding.md` → `05-design-rules.md` §8 (hard rules), §4b (archetypes) → `09-decisions.md` → `15` → `13` → `16` → `05` §9 (critic checklist) | the binding, then the product's yardstick in its order, and its open questions |
| My Account (any mode) | `17-my-account-desktop.md` → `18-my-account-pm-board.md` → `19-my-account-blockers.md` | desktop anatomy and porting rules, accepted PM variants, blocker notifications |
| spec | `05-design-rules.md` §4b → `15-pattern-library.md` → `docs/error-states.md` | archetype anatomy, patterns, the error-state contract |
| test | `05-design-rules.md` §8 → `docs/error-states.md` → `docs/upload-component-spec.md` → `10-fix-backlog.md` | blocking rules, state contracts, known defects |

**The product's own skills.** beluga-ds ships Reboost-specific skills in `.claude/skills/`:
`prd-to-figma` (PRD → brief → UI schema → Figma → critic), `reboost-mockup` (one screen, popup
or edit in Figma), `reboost-review` (the owner's review method against §4b and `09`),
`reboost-setup` (Figma MCP and access check), `figma-add-icon`, `review-board`. Inside that
repository they own the Figma mechanics (`use_figma` and the library); Roman in your Pocket brings
the universal method and the other roles' modes (spec, test, code review). Both judge against
the same handbook. `refero-design` is for tasks with no Reboost pattern, never primary.

## 1. The product

- **What it is:** a US telehealth / online-prescription product. A questionnaire leads to a
  medical review, then treatment and plan choice, checkout and order confirmation; a patient
  account ("My Account") holds subscriptions, orders, settings and billing. Trust signals:
  HIPAA, LegitScript, "Our Pharmacy Partners".
- **Categories** (theme modes, `04 Category` in Figma, `data-theme` in code): weight-loss, ed,
  menopause, testosterone, birth-control, peptides, compounded-glp, hair-loss, anti-aging,
  lab-analysis, metabolic-support, anti-nausea; the brand default mode is `reboost`.
- **Patient variants:** `FTB-A` first time, no GLP-1 before; `FTB-B` switching from another
  provider; `RP` returning patient (refill).
- **Platforms:** responsive web only. Every screen has two frames, mobile 375 and desktop
  (920 / 924 / 1440 in the funnel, 1240 in My Account), placed side by side; desktop content is
  one 520 px column in the funnel and in the account. No native app.
- **Users' state by surface** (from the 85-screen review):

| Surface | Verb | State |
|---|---|---|
| Questionnaire landing | decide | arrived from an ad, three seconds to decide, leaves easily |
| Questionnaire steps | choose | committed but tired; each screen should take seconds |
| Medical review, disqualify | recover | anxious: "am I a good fit?"; FTB-B fears a thrown-off dose |
| Treatment plan | buy | buying with doubt |
| Checkout | buy | peak anxiety |
| Account dashboard, details | glance | calm, routine; anxious around money and health |
| Pause, dose change | decide | mild anxiety |

- **Locale and formats:** US English. Money `$37` (never `37$`), a discount `−$5`, a zero fee
  reads as a word ("Free"), dates "Mar 14" / "Oct 15, 2026", weight in lbs. Money and dates
  reach UI components as pre-formatted strings; components never format them.

## 2. Design system sources

| Source | Where | Notes |
|---|---|---|
| Component library (Figma) | "🇺🇸 UI KIT - reboost", file key `BvhK4O1XjvVipAAS7yZ1h3`, page `🧩 UI Kit` (`167:972`) | 224 components; the `Archive` page is not a source; "UX/UI Redesign" library variables are prohibited |
| Product Figma files | funnel `42dzqhSYu8TNmywyhJJfOR` (page `✅ READY TO DEV`), questionnaires `OscW6YOfVFHkhDVHUYR2Ro`, My Subscription `v39wDgVX92yl64SGbrpQEa`, Settings / My Account `kdVxqJLPU5UaZoiAKIudlF`, **My Account ALL** `cG25dEPqZo1coNEABUAIAk` (page `fo Review PM` `1:4`: mobile + desktop pairs, the PM board, blockers), review collection `vdFkmYUE5h0ndTS9pfc2k8` | map: `docs/design-handbook/01-figma-map.md` |
| Design tokens | `packages/ui/src/styles/globals.css` (+ `typography.css`, `fonts.css`); Figma collections 01 Primitives, 02 Semantic, 03 Sizing, 04 Category | "source of truth = Figma Variables"; snapshot in `02-tokens.md` |
| Component code | `@sml-hub/reboost-ui` (`packages/ui`), `@sml-hub/reboost-checkout` (`packages/checkout`), GitHub Packages | consuming: `CONSUMING.md`; code rules: `AGENTS.md` |
| Component docs | Storybook `apps/storybook` (`pnpm storybook`, port 6006); no deployed URL | groups: Primitives, Molecules, Domain, Commerce, Foundations, Questionnaire, Pilot Screens, Handoff / Checkout |
| Code Connect | `packages/ui/src/figma/*.figma.ts` | checkout package is out of scope |
| DS MCP server | `apps/ds-mcp` (`@sml-hub/ds-mcp`, not deployed): `get_component_inventory`, `get_tokens`, `get_policies`, `get_doctrine`, `search_knowledge`, `validate_design` | local: `DS_MCP_ALLOW_ANON=1 pnpm --filter @sml-hub/ds-mcp start` |
| Icons | `@sml-hub/reboost-ui/icons` (116 icons); thin linear, stroke 1.5–2; 16 in rows, 24 standalone, 64–80 as popup illustration | |

**Token roles by name** (values stay in the source; bind semantic `02` tokens, never `01`
primitives or hex):

| Role | Token names |
|---|---|
| Primary action | `fill/primary` (dark-green pill, white text), `fill/primary-hover`; category keys `key/*` via the mode |
| Destructive | `fill/destructive`, `surface/destructive`, `border/destructive`; `urgent` set for errors |
| Feedback | `text-`, `surface-`, `icon-`, `border-`, `fill-` × `success` · `warning` · `info`, always as a triad of one semantic |
| Canvas and surfaces | `surface/background` (warm cream), `surface/card`, `surface/muted`, `surface/accent`, `surface/brand`, `surface/brand-subtle`, `surface/inverse` |
| Text | `text/main` (dark forest green, not black), `text/secondary`, `text/tertiary`, `text/disabled`, `text/heading`, `text/brand` |
| Borders | `border/main` (warm hairline), `border/input`, `border/selected`, `border/focus` |
| Spacing | `padding-*` and `gap-*` 3xs…5xl = 2 · 4 · 6 · 8 · 12 · 16 · 20 · 24 · 32 · 40 · 48 (gap 6xl 64); ≥ 768 px the large steps grow (the `03 Sizing` Mobile / Desktop mode); off-ladder values (5, 9, 10, 14, 18, 28, 30, 36, 60) do not exist. Which gap goes between two neighbours: §6 · Spacing between neighbours |
| Type | role styles from `13-typography-roles-and-patterns.md` (`Heading/Title`, `Heading/Lead`, `Heading/Heading` 22, `Display/Stat`, `Body/Body`, `Body/Caption`, `Body/Legal`, `UI/Button`, `UI/Option`, `UI/Input`, …); code classes `ds-*` |
| Radii | `radius/*` 3xs…2xl = 2 · 4 · 6 · 8 · 12 · 16 · 20 · 24, `full`; cards r = 16 |
| Elevation | `shadow/xs` focus · `sm` resting cards · `md` popovers · `lg` dialogs and sheets · `xl` toasts |
| Tap target | `tap/min` |

## 3. Visual character (what makes a screen "ours")

- A warm base: cream canvas, near-white cards, warm borders and greys; body text dark green.
- Brand = forest green + sage; gold only for accent captions. No lavender, no 3D art, no photo
  collages.
- Flow screens open with a soft hero gradient (`gradient/hero-fade`), then a centered
  `Heading/Title` and a `Heading/Lead`.
- Cards are thin hairline containers (1 px `border/main`, r = 16, `shadow/sm` or none); the
  hierarchy inside a card is nuance (weight, tone), not colour.
- Host Grotesk carries meaning (headings, names, values, prices, buttons, options); Roboto
  carries prose and utility and is never larger than 14 (except text typed in a field).
  Poppins, Inter and Manrope are prohibited.
- The only "loud" screen allowed is the trust / welcome screen.
- Source: `05-design-rules.md` §4.

## 4. Voice and terms

- Headings are an action or a promise, not a section name ("Almost done — review and
  consent", not "Legal Consent"); the subtitle never repeats the breadcrumb.
- The CTA names the next step or the reward ("Check your eligibility", "Continue to see your
  treatment"); a sensitive change names the procedure ("Send verification link", not "Save").
- Address the user by name in the title when the name is known ("Welcome back, {name}").
- Give, then ask: the result or reassurance comes before any form.
- Consequences are stated in text, not colour: option captions say what happens ("Resumes
  Oct 15, 2026"). Waiting screens name the result ("Matching you with the right treatment").
- Errors: one problem, one next step; no jargon, no blame, no exclamation marks, no codes; the
  verbs are *couldn't*, *try again*, *check*. The customer never sees a status code, a stack
  trace or the word "server". Fixed copy: ErrorPage "Something didn't work as expected" /
  "Your progress is safe." / "Try now"; toast "We couldn't complete that action. Please try
  again."
- Bad news (out of stock) is a calm white card, no red and no icon.
- Caps only for short labels (≤ ~20 characters).
- Canonical strings (with their styles): "Due today:", "Due after doctor approval:", "Order
  summary", "Most popular", "Based on your answers", "Recommended starting path", "Your
  information is never shared and is protected by HIPAA." (`13-typography-roles-and-patterns.md`).
- **No glossary exists yet.** Known term drift, to be decided: doctor / provider / clinician /
  physician; "Log in" vs "Sign in"; "Close" vs "Got it"; "Identity Verification" vs "Upload a
  photo of your ID". Stable: "Select photo" / "Take photo" (in that order), "I agree —
  continue", "Go back" / "Quit questionnaire".

## 5. Components — when to use which

Full catalogue: `04-components.md` (Figma node ids, properties) and `COMPONENT-MAP.md`
(Figma → code). Selection rules: `05-design-rules.md` §5.

| Need | Use | Not |
|---|---|---|
| Primary action | `Button` default (one per screen; full-width pill); `black` for account CTAs | a second filled button; a styled div |
| Secondary action | underlined text link in the funnel; ghost button in the account | a second primary |
| Recovery vs exit | recovery primary, exit outline | exit as primary |
| Questionnaire answer | `OptionButton` / `Forms/ButtonQuestion` (checkbox = multi + Continue; no checkbox = single, auto-advance) | `RadioGroup` (radio only for real settings: payment method, tier) |
| Labelled field | `FormField` + `Input` / `Select` / `Combobox` (floating label, helper under the field) | native `input` / `select`; a placeholder as the label |
| Short known list / search | `Select` / `Combobox` (reuse, never rebuild) | a custom dropdown |
| Status | dot + word → `Badge` (≥ 3 states or "action required") → red card border only for Failed | colour alone; a filled badge for a binary state |
| Inline warning | `Alert` type warning; a critical note inside a card = callout on `surface/muted` | a toast (Sonner) as an inline warning; an Alert inside a card |
| Action failed, user stays | `ErrorToast` (sage badge, never red; one at a time) | a red toast; a page |
| User cannot continue | `ErrorPage` (error / not-found) | a toast |
| Parameterised action, transitional state | `Popup` — a **bottom sheet at every breakpoint**: docked to the bottom edge, top corners 24, bottom 0, slides up; on desktop 520 wide, centred horizontally (owner 2026-09-27/29) | a separate page; a centred modal |
| Blocker notification in My Account (payment failed, verify identity, doctor needs info, refill questions) | `Feedback/NotificationStrip` — **always one** strip, by priority payment → identity → doctor → refill; first item of the content column; the whole strip is tappable, not dismissible; on Home they are ordinary "What's new" cards, no accent (`19` §0) | several strips; an amber bar on Home |
| A control the user cannot change (e.g. order emails) | shown **disabled, not hidden**: `Forms/Switch State=Disabled` + `information-circle` 16 after the label + `Core/Tooltip` with the reason ("Order emails can’t be turned off") | hiding the row |
| Unsaved changes when leaving a form | `Overlays/Popup` sheet "Leave without saving?": primary "Keep editing" + red outline "Leave without saving" (candidate, `17` §5); not after Save, Cancel, no edits or auto-save | a new component; losing the form silently |
| Irreversible confirmation | `AlertDialog` | a Popup with a red primary for a reversible action |
| Side drawer | `Sheet` (left / right only) | Sheet as a bottom panel |
| Empty list | `Empty` (sage line illustration 160–180, heading, one sentence, primary with the action icon) | "No data" |
| Loading | `Spinner` / `Skeleton`; waiting screen = ring around the monogram + the result line | a hand-drawn spinner |
| Upload | `FileUpload` (id / prescription / bodyPhoto / document; empty, uploading, success, error, disabled; errors inline) — also in the My Account ID-verification popup (`Subject=Id`) | a modal mid-questionnaire; a new dropzone |
| Card layout | `CardBase` (padding 16, 12 on top with an eyebrow) | `Core/Card` (20) for composites |
| Checkout, subscription, account blocks | `Commerce/*` (`OrderSummaryCard`, `PlanOptionCard`, `PaymentMethodRow`, `CouponRow`, `KeyValue`, …) | rebuilding them from primitives |
| Edit vs navigate | pencil = edit in place; chevron = navigate | |
| Icon button | `Button size="icon"` in code; `Core/IconButton` in Figma | a Button emulating an icon button |

## 6. Patterns

Assembly: **one shell per screen → blocks → atoms**, each slot with a named type role and kit
component (`15-pattern-library.md`, `15-patterns.json`). Archetype anatomy confirmed on 85
screens: `05-design-rules.md` §4b; reasoning and reference nodes: `design-decisions.md`.

| Shell | Anatomy (short) |
|---|---|
| S1 Account page | hero gradient → floating white pill header → breadcrumb ("‹ Parent" deeper) → `Heading/Title` → `Heading/Lead` (≤ 2 lines) → content; no primary on a dashboard, actions live in the card that owns them. **Desktop** (`17` §2): frame 1240, header pill 969 centred and sticky, header → page 56, left rail `Navigation/AccountRail` 173 (**one level**, depth shown by "‹ Parent", no breadcrumbs), rail ↔ column 56, content column **520**, back link → title 16, title 44 → content 40, blocks 32, the HIPAA `Footer` last in the column on **every** desktop page (gap 40) |
| S2 Funnel step | dark hero gradient → `Navigation/Header` → centered title → `Heading/Subtitle` → content → primary → "Skip" underlined link → trust footer (HIPAA line + badges + Pharmacy Partners); desktop one 520 column |
| S3 Questionnaire step | coupon → header (‹, segmented progress without "N of M", ⋯) → QuestionTag (follow-ups, the only amber spot) → question (22, left) → helper → options → Skip / Sign in → sticky primary; no trust footer on mobile |
| S4 Popup | icon → `Heading/Heading` 22 (no exceptions, never a second Title) → subtitle → buttons; a bottom sheet on every breakpoint, desktop 520 wide, content fills it (472); a popup screen in Figma is a viewport crop (1240 × 1080, mobile 375 × 840) with the sheet docked to the bottom |
| S5 In-page state | Heading 22 centered + caption |
| S6 Full-page error / 404 | `ErrorPage` |

Archetypes (details in §4b): **treatment plan** (recommendation → SpecStrip → benefits →
dosage → alternatives → how it works → FAQ → sticky primary + outline; price is the second
hero) · **checkout** (one step: title → "Due today: $0 / Due after doctor approval: $509"
reassurance → order summary → delivery → billing → coupon (inert → Applied → Error, value
kept) → payment rows with radio → CTA → FAQ → trust footer) · **order confirmation** (the
mandatory next step as the single dark card; "What happens next?" timeline) · **parameterised
action** (Popup: context card on `surface/accent` → one sentence on consequence and
reversibility → options with consequence captions → primary + ghost; reversible = green,
red only for irreversible) · **account forms** (one card, floating labels, locked values as
KeyValue with 🔒 ⓘ, "(Optional)" in the label) · **empty state** · **breakscreen** (a fact
screen; see §9 on its two dominants).

**My Account** (`17`, `18`, `19`): mobile → desktop porting keeps sticky bars and buttons out
of the auto-layout body (pinned to the viewport bottom, column-wide), snackbars float at the
top under the header (480 wide on desktop), chats become a 520 × 760 panel. Section cards
(Shipping, Pharmacy, Medication Instructions, Lab results): gap `gap/lg`, top `padding/md`,
bottom `padding/xl`, header row 44 with the title centred, title `Heading/Subheading` (22 desktop
/ 18 mobile); Payment breakdown keeps a one-line title. FAQ and "Need help?" blocks: vertical
padding 16 on every page. Status and empty screens: the button sits right under the message
(`gap/xl`), not pinned to the bottom. ID verification on My Order: a solid lavender card (V2d)
above the order tracker → two bottom-sheet popups, the second with `Forms/FileUpload`
`Subject=Id`. Lab results: one row (document icon, name, date · PDF · size, download icon
button) on `surface/success`. Notifications: *Order & Plan* shows a locked Email row with a
tooltip; *Medication reminders* has no channel toggles, only a line and "Manage reminders".

### Spacing between neighbours (`16-spacing.md`, rule v1.1, owner 2026-09-27/28)

For `itemSpacing` in auto-layout this chapter wins over `05` §3. Pick the gap by **how the two
neighbours relate**, never by eye or by their size; bind it to `gap/*` (`03 Sizing`), and the
Mobile / Desktop mode gives the number.

| Relation | Meaning | M | D | Token |
|---|---|---|---|---|
| attached | part of one element: label over value, field → helper | 4 | 4 | `gap/2xs` |
| inline | side by side in a row: icon + text, button + button, tabs | 8 | 8 | `gap/sm` |
| group | equal repeats: list rows, cards in a list, a button stack, fields in a row | 12 | 12 | `gap/md` |
| heading | a heading over its content; a question over a field; "Back" → screen title | 16 | 16 | `gap/lg` |
| block | different groups inside a block: a stack of form fields, lead → fields | 24 | 32 | `gap/2xl` |
| section | block → block; content → actions; two sections in one card | 32 | 40 | `gap/3xl` |
| page | header → content; page sections | 48–64 | 56–80 | `gap/5xl` / `gap/6xl` |

Shifts (only these): inline with a badge ≥ 28 → 12, with a thumbnail ≥ 44 → 16; group of items
≥ 250 high → 16; a small heading inside a card on mobile → 12; a single large heading ≥ 22 over
content ≥ 200 → section 32 / 40; price → `Body/Legal` footnote 16 / 24. **Text over text** uses
the visible distance instead (half-leadings subtracted, snapped to 0 / 2 / 4 / 8 / 12 / 16): e.g.
`Heading/Heading` 22 → text = 12, Title / H2 → text = 16, paragraph → paragraph = 4, subheading
16–18 → caption = 4. Zero: table rows, segments, carousel arrows; `auto` to push a CTA down.
Invariants: **inner gap ≤ outer gap**; one container, one relation (split mixed ones); mobile and
desktop use the same variable, never a bigger token "because it is wider"; an icon or button next
to text keeps 12 for long content.

## 7. Hard rules (blocking for Reboost)

From `05-design-rules.md` §8, `AGENTS.md` and the policies; a violation is `debt` with no
`context` exception.

1. Only components from the "🇺🇸 UI KIT - reboost" library (code: `@sml-hub/reboost-ui`,
   `@sml-hub/reboost-checkout`); no new component, token or style without the DS owner.
2. No bare hex / rgb: only `02 Semantic` variables (+ `key/*`); never `01` primitives.
3. Every gap and padding is a `03 Sizing` variable; an off-ladder value does not exist.
4. Every text layer uses a role style from `13-typography-roles-and-patterns.md`; bare text,
   Poppins and Inter are prohibited; text inside buttons, options and tabs keeps its `UI/*`
   style. Code: typography only via `ds-*` classes.
5. Radii only from `radius/*` (code: `rounded-xl` / `rounded-2xl` banned — but see §9).
6. At most one solid-primary button and one Title (H1) per screen — and no other competing
   dominant (owner decision 2026-09-26): anything as loud as the dominant is blocking.
7. Every input and dropdown has a label; a placeholder is not a label.
8. Mobile first; tap targets ≥ `tap/min`; two frames per screen (mobile + desktop), paired names
   `{StepCode} / {platform} / {variant}`.
9. "UX/UI Redesign" variables are prohibited.
10. Category theming only via the `04 Category` mode / `data-theme`, never manual recolouring.
11. Questionnaire answers are always `OptionButton`, never `RadioGroup`.
12. Code: errors via `aria-invalid` / `FormField error=`; checkout components never route,
    fetch or format money and dates (they arrive as strings).

Product warnings (listed, a human accepts or rejects; `05` §8): inner gap ≥ outer gap (the
critic still reports this one as blocking — it is a universal blocking rule, and `20` §4 leaves it
open for the owner); missing
required states (loading / error / empty / success); weak desktop coverage; no alt on an
image; no name on an icon button; line length outside 40–70; a centered element hanging in
nothing; more than 5 text styles on one screen; an element "not from here".

## 8. Motion register

- Register: **restrained** — "every transition explains an interaction; no decorative 'wow'
  motion" (`figma-agent-skills/reboost-doctrine.md`).
- No duration or easing tokens exist yet (code values are hardcoded; Figma has one `Easing`
  variable). Reference values: question transition exit 220 / enter delay 120 / enter 320 ms,
  horizontal for next / back, vertical for a follow-up; ErrorToast in 240 ms
  `cubic-bezier(0.2,0.8,0.2,1)`, out 180 ms; floating label 150 ms ease-out; accordion 200 ms.
- Plan switch (`docs/plan-switch-motion.md`): compositor properties only, never `ease-in` on an
  entrance, never fade dark into white; reduced motion = instant swap + 200 ms copy fade; input
  locked during the transition.

## 9. Known drift and open questions

The critic reports these as `decision-needed` or as known debt, not as new findings on every
screen. Canonical list: `09-decisions.md` (open questions) and `07-staleness-report.md`.

**Conflicts with a universal `blocking` rule** — a product decision cannot override these
(precedence in `SKILL.md`); the critic keeps reporting them until the owner changes the product
rule or the universal one:

- The invalid-submit shake is deliberately not gated by reduced motion (`globals.css`), against
  lens 10 · Non-colour cues and reduced motion.
- The questionnaire breakscreen is described as "the one legitimate case of two dominants",
  against lens 01 · Single dominant (whose only exception is a hero number and its phrase read
  as one sentence).

**Inside the product:**

- Field standard: floating label with a required asterisk (`05` §4) vs "(Optional)" in the label
  and no asterisk (`05` §4b, account forms) vs a bare placeholder (questionnaire) — Q10 / Q24.
- Tap target: the owner decided 44 (Figma changed), code `--tap-min` and `validate_design` still
  use 48.
- Radii: `AGENTS.md` bans `rounded-xl` / `rounded-2xl`, Figma and `globals.css` define them, six
  components use `rounded-xl`.
- Default theme: Figma default is `reboost` green; code `:root` is still weight-loss orange
  (owner decided the code changes).
- Two component kits in one file: questionnaires still use the legacy `Button-question`,
  `Coupon`, `Skip / Sign in` (Q62); two card standards (`Core/Card` vs `CardBase`); two
  uploaders.
- Primitive colours used directly in nine components (button, badge, alert, icon-badge,
  checkbox, option-button, combobox, skeleton, error-page).
- Icons: `AGENTS.md` says lucide-react only, the kit ships its own 116 icons.
- No dark mode, no motion tokens, no breakpoint tokens (only `md` = 768).
- Open product questions (`09-decisions.md`): single-choice control in the account (Q1 / Q8),
  empty-state heading level (Q2), funnel title size and logo (Q11), two primaries on plan
  format (Q13), "Pay – $509" vs "Continue" (Q16), secondary style in popups (Q18), consent with
  no control (Q21), disqualify terminal not drawn (Q22), sheet vs popup (Q28), large-number
  format (Q29), "Close" primary or outline (Q61).
- My Account (`17` §10, `18` §4): which desktop Home (V1–V8 built, V5 / V8 recommended; Q67),
  which widgets (Q68), rail on Home (Q69), HIPAA footer on desktop (Q70, since applied on every
  desktop page), publishing the rail and the unsaved-changes warning to the kit (Q71), the warning
  inside sheets (Q72); ID-verification result states not drawn; Lab results position and click
  behaviour; the identity illustration is not a kit component and lavender has no semantic token
  (the ID card binds the primitive `color/lavender/600`, against hard rule 2 and the "no lavender"
  character of §3 — an owner-accepted exception for this card).
- Spacing (`16` §7): label over value 0 or 4; accordions and step timelines; the stat exception
  binds the primitive `space/24` (against `02-tokens.md`); `05` §3 contradicts invariant 1 and
  awaits an edit. Gap conformance on 2026-09-28: 79 % (kit 57 %, My Account 78 %, funnel 86 %,
  questionnaires 69 %).
- Kit changes of 2026-09-29 (section cards, desktop Popup 520, component descriptions) are made
  but **not published**; `Feedback/NotificationStrip` is in the kit and in code.
- Fix backlog of confirmed debt (copy, maths, style): `10-fix-backlog.md`.
