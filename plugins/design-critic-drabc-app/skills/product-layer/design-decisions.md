# Design decisions log — Dr.ABC Application

> The project's own yardstick, accrued from reviews and decision boards. The `design-critic` skill
> carries the universal rules (lenses 01–14 and the catalog); everything specific to this product —
> archetypes, named components, colour and type roles, tolerated exceptions — lives here.
> A row without a reference screen does not exist. Lifecycle: `method/review-method.md` §5.
>
> Created: 2026-10-08 · Rewritten: 2026-11-11 from the owner's answers on four decision boards ·
> Updated: 2026-11-15 with the round-3 board (hard rules + open questions) ·
> Project owner: Roman · Figma: `3GnJD8QN587Y912O3F15Cx` ·
> Last review: `reviews/2026-11-10-consistency-audit/` (124 screens of the READY TO DEV section)
>
> Node ids are in the working section „Ready for review“ `3168:4410` unless a kit page or the
> Jira-linked section `4292:24466` is named. Counts in "Violations" are from the census of
> 2026-11-10 and describe Figma on 2026-11-11.

## Status legend

| Status | Meaning |
|---|---|
| `candidate` | seen in one cluster; the project owner has not objected |
| `confirmed` | seen on **3+ screens across 2+ clusters**, the project owner has not objected — or decided by the owner directly, written `confirmed (owner, <date> · <board item>)` |
| `decision-needed` | the product does it two ways, or counter-evidence appeared; listed under Open questions; the project owner decides |

Status is editorial (is this row a rule of the project). It is not an audit result: a
`confirmed` row is checked on every screen and gets `pass` / `partial` / `fail` there.

## Promotion rule

- `candidate` → `confirmed`: 3+ screens across 2+ clusters, or an owner answer on a decision board.
  Never from one screen, however convincing.
- Counter-evidence downgrades: a contradiction in a later cluster moves a row to
  `decision-needed` with the score (how many screens each way).
- Only the project owner promotes rows into hard rules or the handbook, and only the project
  owner edits this file. Reviewers propose changes in `decisions-delta.md` inside their
  review folder.
- A reference screen that contradicts a confirmed rule is a violation, not evidence.
- A confirmed row outranks a universal `warning` or `note` (a deviation from the universal
  becomes `context`, citing the row). It never outranks a universal `blocking`.
- A later owner answer replaces an earlier one; the old row moves to "Superseded decisions".

## Owner confirmations

- 2026-10-07 — kit plan: brand, one Button, capsule, floating label, % line height, everything bound.
- 2026-10-08 — boards round 1 and 2, final review board: 30+ answers: navigation, radius system, notifications, order detail, formats, fees.
- 2026-10-26 / 28 — chat: target look = ChatGPT iOS + iOS 26; glass header buttons; Button L = 56; two card radii.
- 2026-11-01 — critic audit board (d0–d7, findings): text-safe brand colours, links = brand colour, copy and screen fixes.
- 2026-11-10 — consistency board, round 1 (36 items): typography, spacing, radius, colour, components, hygiene.
- 2026-11-11 — consistency board, round 2 (13 of 14 items): headers, section gap, display sizes, card outline + shadow, kit changes.
- 2026-11-15 — rules board, round 3 (26 items): hard-rule list reviewed rule by rule (14 kept, 2 moved to warnings); open questions Q1–Q7, Q9, Q12 answered; Q8 kept open.
- 2026-11-17 — chat: motion register (between restrained and playful, micro-animations with character), `Switch`, `SegmentedControl`, `Tabs` motion, press feedback, popover enter / exit (MOT-1 … MOT-7).

---

## 1. Brand and colour

| # | Decision | Why | Reference | Violations | Status |
|---|---|---|---|---|---|
| COL-1 | Brand = lime **#7ABA47** (`fill/brand`, `icon/brand`); it is a fill and icon colour, never text | owner's brand; lime text measures 2.35:1 | Foundations `3066:2191`; `semantic` collection | — | confirmed (owner, 2026-10-07; narrowed 2026-11-01 · d2) |
| COL-2 | Primary button = **button green #38A165** (`interactive/primary`), pressed #2D8151, white label | lime is too light for a white label; owner picked the darker green | `Button` `3074:23952` | — | confirmed (owner, 2026-10-29; contrast in every vertical accepted 2026-11-15 · Q07) |
| COL-3 | Brand text, links and outline borders use the text-safe step: `text/brand` = `text/link` = `border/brand` (#2D8151 base). On grey or tinted surfaces → `text/brand-on-subtle` (#395626). Success text follows the same pair | readable green on white and on tints | audit 2026-11-01, d2 / d3 | 4 texts use `fill/brand` as text colour (status-bar time, „18 Min.“) | confirmed (owner, 2026-11-01 · d2, d3) |
| COL-4 | Links take the vertical's brand colour (the separate link green #269C6E is retired for text) | "links use the brand colour, so they differ per category" | same | — | confirmed (owner, 2026-11-01 · d3) |
| COL-5 | One kit for nine verticals: components bind `semantic` tokens that alias the `category` mode; nothing is recoloured by hand | one change propagates | `category` collection, 9 modes | — | confirmed (owner, 2026-10-07) |
| COL-6 | Vertical colours stay even where they resemble a status colour (Testosterone red, Weight loss orange); status meaning is carried by icon + text | owner keeps the brand palette | board 2026-10-08 · V1 | — | confirmed (owner) |
| COL-7 | „Jetzt bezahlen“ is an orange button (`Button` Style `warning`), label SemiBold | payment due must stand out from the brand action | Order 03d `3242:8840` | contrast 2.80:1, accepted (tolerated exceptions) | confirmed (owner, 2026-10-08 · F1; 2026-11-01 · f02; 2026-11-15 · Q07) |
| COL-8 | Colours of loose layers are `semantic` variables; legacy collections and raw hex are rebound; page background is `fill/page` on every screen | one palette | applied 2026-11-10 (796 paints) | residue: 91 paints, mostly in Home `4041:12277`; raw #1F2129 footer | confirmed (owner, 2026-11-10 · C2) |
| COL-9 | `text/tertiary` is dark enough to pass on white and on `fill/page` (#646C78) | hints must stay readable on the grey page | `semantic` | — | confirmed (owner, 2026-10-08 · Q8) |
| COL-10 | Brand header surface = base colour + large blurred radial glow at 70 %, bound to `category/gradient/*` | owner's reference `3167:47003`; recolours per vertical | `AppHeader` Surface `brand` | — | confirmed (owner, 2026-10-08) |
| COL-11 | Light theme only | scope | `semantic` has one mode | — | confirmed (owner, 2026-10-07) |
| COL-12 | Grey text keeps the nearest-colour mapping of 2026-11-10: former "secondary" text → `text/tertiary`, former "tertiary" (meta) → `text/disabled` | the look stays as the owner drew it | Notifications 01 `3168:8264` (meta line) | — | confirmed (owner, 2026-11-15 · round 3 · Q03) |
| COL-13 | White label on the primary button is accepted in every vertical, below 4.5:1 included: base and Cannabis 3.25, Weight loss 2.80, Contraception 4.15, Asthma 3.53; and on the orange „Jetzt bezahlen“ 2.80 | brand decision | `Button` `3074:23952`; token export 2026-11-03 | — | confirmed (owner, 2026-11-15 · round 3 · Q07) |

## 2. Typography

| # | Decision | Why | Reference | Violations | Status |
|---|---|---|---|---|---|
| TYP-1 | Two families: Poppins (headings, UI) and Roboto (body, captions). Inter is replaced; weights stay within 400 / 500 / 600 (Poppins) and 400 / 500 (Roboto) | one voice | text styles on Foundations | Inter ×19, Roboto Bold / SemiBold ×55 (45 of them the rating widget — tolerated, Q02), Poppins Light ×2 | confirmed (owner, 2026-11-10 · T5) |
| TYP-2 | Size scale 11 · 12 · 13 · 14 · 16 · 18 · 20 · 22 · 24 · 30 · 36; every other size moves to the nearest step (tie → larger) | scaled blocks left fractional sizes | applied to 41 texts 2026-11-10 | 62 texts still off the scale (display headings, rating widget, V22 pack rows) | confirmed (owner, 2026-11-10 · T6) |
| TYP-3 | Large marketing headings = **Display**: Poppins Medium, line height 110 %, tracking −0.5 px, sizes **22 / 24 / 30** — strictly on the scale, 26 becomes 24 | "make them all like Home, Category and How it works" | Home `4041:11533`, Category `4075:14790`, `HowItWorks` `4200:4493` | 26 px ×13, fractional 25.86 / 27.42 ×6; styles not created | confirmed (owner, 2026-11-10 · T7; 2026-11-11 · T7) |
| TYP-4 | Tile and card titles of 22 px (Home tiles, Category cards, Category article) = Display 22 | three fonts for one role | Home tiles, Category `4075:14790` | Inter Bold ×12, Roboto SemiBold ×6, Poppins Light ×2 | confirmed (owner, 2026-11-11 · T5b) |
| TYP-5 | Section heading = small grey text **above** the card, everywhere (`SectionHeader`, `Body S`, sentence case, `text/secondary`) | grouped-list look of the ChatGPT / iOS 26 reference; one pattern instead of three | Plan detail `3168:11875` | kit master still shows UPPERCASE overline 11 / SemiBold 18 (the decided look is an instance override); headings inside cards on Order 03d / 03e ×15; loose H5 ×37 (Order, Uber); UPPERCASE overline ×51 (Search, V22, Category); gap to the card 12 instead of 8 in places | confirmed (owner, 2026-11-10 · T1) |
| TYP-6 | Screen title in the order-detail header = `Title 22 · Medium`; the order number stays bold | the number is data, not a heading | CALENDAR 03 `3309:11534` | H3 20 SemiBold ×11 | confirmed (owner, 2026-11-10 · T2) |
| TYP-7 | Links are always underlined (`UI/Link` 14, `UI/Link L` 16) | a link must be recognisable without colour | Plan detail „Ändern“ | ≈ 24 inside instances, 36 in Search `ProductCard`s | confirmed (owner, 2026-11-10 · T3) |
| TYP-8 | Every text has a text style. Exact twins are bound; the rest maps to the nearest style of the same family: Roboto Regular 12 → `Caption`; Roboto Regular 14 → `Body S`; Medium 12 with tracking → `Caption M`; Poppins Regular 13 (tabs) → `UI/Label`; Poppins Medium 15 link → `UI/Link L`; Poppins SemiBold 15 → `H5`; Poppins Medium 14 → `Subtitle M·Medium`; Poppins Medium 16 → `Subtitle L·Medium`; Roboto Medium 10 → `Caption M`; Poppins Regular 14 link → `UI/Link` | no loose type | board 2026-11-11 · T4 table | ≈ 455 loose texts without a style | confirmed (owner, 2026-11-10 · T4; 2026-11-11 · T4) |
| TYP-9 | Line height and letter spacing are set in % inside text styles | scale with size | all text styles | — | confirmed (owner, 2026-10-07) |
| TYP-10 | Crossed-out old price uses a strike style (`Caption · Strike`) | one way to show an old price | `PriceBlock` `3102:2275`; Home plan cards | `Body S · Strike` deleted 2026-11-10 (unused) | confirmed (owner, 2026-10-08 · F4; 2026-11-01 · f46) |
| TYP-11 | Unused styles are deleted only at zero uses in the whole file; `UI/Label` and `UI/Button L` stay | `UI/Label` fits the V22 tabs | — | — | confirmed (owner, 2026-11-10 · T8) |

## 3. Components

Kit ids — 🧩 UI KIT: Button `3074:23952` · IconButton `3076:2249` · Checkbox `3077:2227` · Radio
`3077:2238` · Switch `3077:2251` · Badge `3080:2241` · FilterChip `3080:2266` · Progress/Steps
`3081:2236` · TextField `3082:2292` · Dropdown `3084:2367` · Combobox `3084:2482` · DatePicker
`3085:2699` · TextArea `3088:2613` · SearchField `3088:2642` · SegmentedControl `3089:2612` ·
SelectionRow `3089:2687` · Callout `3090:2716` · ListItem `3090:2772` · Tabs `3100:2784`.
🧬 Molecules: SectionHeader `3101:2233` · KeyValueRow `3101:2247` · PriceBlock `3102:2275` ·
OrderLineItem `3103:2346` · AccordionItem `3104:2282` · TrustBar `3104:2311` · Snackbar `3105:2326` ·
OrderProgress `3105:2366` · CategoryTile `3106:2450` · Skeleton `3210:2490` · EffectIcon `3257:10085` ·
EffectTile `3257:10086` · HowItWorksStep `4200:2571`.
🏗 Organisms: AppHeader `3108:2579` · NavBar `4198:8171` · StickyBottomBar `3109:2378` · ListGroup
`3109:2576` · BottomSheet `3110:2846` · Dialog `3110:2930` · EmptyState `3111:2773` · NotificationCard
`3111:2851` · ProductCard `3112:3079` · OrderCard `3113:3157` · OrderSummaryCard `3113:3389` ·
ActivePlanCard `3114:3421` · StepList `3115:3335` · SearchFilterBar `3116:3349` · PromoBanner
`3116:3451` · LegalFooter `3117:3450` · NavMenu `3164:26652` · ActiveOrderCard `3241:3879` ·
HowItWorks `4200:4493`. Deprecated: TabBar `3117:3568`, CardAction `3365:2467`.

| # | Decision | Why | Reference | Violations | Status |
|---|---|---|---|---|---|
| CMP-1 | One `Button` for every text action, link styles included (9 styles × L 56 / S 40 × 4 states) | one source for every action | `3074:23952` | remote `MainButton` ×2, remote `Button` ×2 | confirmed (owner, 2026-10-07; L = 56 on 2026-10-28) |
| CMP-2 | Buttons are **capsules everywhere**. The October "shape B" (radius 12 for a full-width button at the bottom of a card) is cancelled | one shape | sticky bars | 18 in-card buttons with radius 12; `Shape=rounded` and `CardAction` still in the kit | confirmed (owner, 2026-11-10 · R2) |
| CMP-3 | The screen's main action sits in `StickyBottomBar` on every screen, funnel included. Buttons inside product cards on Category are not the screen CTA and stay | the action is always reachable | Plan detail `3168:11875`, questionnaire | Mix 1 / 2 / 3 CTA inside the card; V22 loose `order-bar` | confirmed (owner, 2026-11-10 · S7) |
| CMP-4 | Option rows: **r24** for standalone questions, **r16** for dense lists (packs, plans) with padding 12 × 16 and the price on the right | a dense list needs smaller rows | questionnaire ED 01 `3298:12564`; Mix 1 packs `4120:13980` | Mix 2 plans and V22 packs r24; compact `SelectionRow` variant not built | confirmed (owner, 2026-11-10 · R1; kit change 2026-11-11 · X3) |
| CMP-5 | Questionnaire single choice shows **no radio**: selection = brand tint + outline (`SelectionRow` Control `none`); multiple choice shows a checkbox | pace: a tap is the answer | ED 01 `3298:12564`, ED 11 `3298:13146` | — | confirmed (owner, 2026-10-08 · E3) |
| CMP-6 | Selected outline = **1.5** (`border-width/selected`) everywhere | 1 and 2 px were both in use | Mix 1 selected pack `4120:14027` | kit `SelectionRow` master still 2; V22 selected rows 1 | confirmed (owner, 2026-11-10 · C4) |
| CMP-7 | Dosage is chosen with **chips** (`FilterChip`) everywhere | one control for one job | V22 `3167:47167` | Mix 1 segmented switch | confirmed (owner, 2026-11-10 · K8) |
| CMP-8 | Inputs = kit `TextField` with a floating label; Dropdown, Combobox, DatePicker build on it | owner request | `3082:2292` | Mix 3 address form: 9 remote `input` | confirmed (owner, 2026-10-07; 2026-11-10 · K7) |
| CMP-9 | FAQ = `AccordionItem` rows with dividers inside **one** card | one accordion look | Plan detail support `3168:11875` | remote `NEW FAQ` ×77 and three flat looks (Home, V22, Mix 3, Category) | confirmed (owner, 2026-10-08 · E5; 2026-11-10 · K2) |
| CMP-10 | Label–value lines = `KeyValueRow` | kit twin exists | Plan detail | `Row/Price` + `Row/Bullet` ×88 (Order 03 / 04 / 05, Uber) | confirmed (owner, 2026-11-10 · K3) |
| CMP-11 | Order timeline becomes a kit component `OrderTimeline` with the Uber-tracking look; Order detail aligns to it | the Uber version is the newest and clearest | Uber R1 `4398:27562` | `TimelineStep` from "In process" ×66; component not built | confirmed (owner, 2026-11-10 · K4) |
| CMP-12 | Reassuring notes (grey plate in Mix 3, green note in Order 03d / 03e, outlined pill in V22) all become the green `Callout` Tone `brand`. A plain caption under a button stays a caption | "the first three can look like the second" | Order 03d `3242:8840` | Mix 3 grey plate, V22 outlined pill | confirmed (owner, 2026-11-10 · K9) |
| CMP-13 | Bottom sheets are the kit `BottomSheet` with one padding set (top 8, content 16, bottom 34); every state the screens use must exist in the component before the swap; sheet content is not redrawn | "all states must work" | Mix 1b `4203:14786`, address sheet `4222:17204` | 17 loose sheets with four padding sets; missing kit states: full-height list, filter row, empty result, stacked sheet | confirmed (owner, 2026-11-10 · S6; 2026-11-11 · X3) |
| CMP-24 | Bottom sheets have **no grabber**: close by the X in a grey circle or by swipe-down, as the kit `BottomSheet` is built | one way to close, as decided on 2026-10-08 | `BottomSheet` `3110:2846` | the hand-built sheets show a grabber (17) | confirmed (owner, 2026-11-15 · round 3 · Q05) |
| CMP-14 | Exact kit twins replace non-kit pieces without asking: `icon_btn` → `IconButton`, remote buttons → `Button`, legacy status chips → `Badge`, Mix 3 checkbox → `Checkbox` | kit first | — | icon_btn ×31, badges ×4, checkbox ×1 | confirmed (owner, 2026-11-10 · K6; 2026-11-11 · X3) |
| CMP-15 | „Ähnliche Behandlungen“ on the product page = kit `ProductCard` row: „ab“ stays before the price, no chevron | kit twin exists in Mix 1 | Mix 1 `4120:13980` | legacy `ProductCard` ×8 on V22 | confirmed (owner, 2026-11-11 · K6b) |
| CMP-16 | Product line of an order: legacy `Image and Info Container` → `OrderLineItem`; `Row` in Order detail and Uber stays | owner keeps his Order detail rows | Plan detail `3168:11875` | legacy ×2 (Category) | confirmed (owner, 2026-11-11 · K6c) |
| CMP-17 | Header icon buttons are glass components: `IconButton` `glass-light` on a light page, `glass-dark` on brand, gradient or photo; back button is a 52 circle | iOS 26 look; same button on every screen | Mix 1 `4120:13980`, Home `4041:11533` | — | confirmed (owner, 2026-10-08 · Q7; 2026-10-28) |
| CMP-18 | Notification card: unread = brand outline + dot, icon tile tinted by type, title 16 Medium; action-required → `Button S primary`, other actions → `Button S outline`; cancelled tile neutral | the owner's original looked better; CTAs must be visible | N10 card states `3168:8526` | — | confirmed (owner, 2026-10-08) |
| CMP-25 | The unread dot on `NotificationCard` takes the colour of the notification type (green for a shipped order, orange for a failed payment…), as drawn now | owner keeps the current look | Notifications 01 `3168:8264` | — | confirmed (owner, 2026-11-15 · round 3 · Q12) |
| CMP-19 | Active order card puts the **status** first: small product row, 6-segment progress (done = dark brand, current = bright brand), caption „Jetzt“ + large status, timestamp and next step | the user comes for the status | `ActiveOrderCard` `3241:3879`; owner reference `3167:48304` | — | confirmed (owner, 2026-10-08) |
| CMP-20 | Snackbar is dark | contrast with the light page | `Snackbar` `3105:2326` | — | confirmed (owner, 2026-10-08 · E6) |
| CMP-21 | Search: round filter icon button + a second row of sort dropdowns; search field has a brand submit button; one card per result | owner's search redesign `3167:46813` | `SearchFilterBar` `3116:3349`; `3334:29379` | — | confirmed (owner, 2026-10-08 · F3; 2026-11-01 · d6) |
| CMP-22 | How-it-works cards are neutral with a hairline outline | they lacked contrast with the page | `HowItWorksStep` `4200:2571` | — | confirmed (owner, 2026-11-01 · f12) |
| CMP-23 | Out-of-stock product: muted card + `Badge` + „Benachrichtigen“ | — | D7 `4223:18222`, D8 `4223:18530` | — | confirmed (owner, 2026-10-08 · E4) |

## 4. Spacing

| # | Decision | Why | Reference | Violations | Status |
|---|---|---|---|---|---|
| SPC-1 | Every gap and padding is bound to a `space/*` / `layout/*` variable; values equal to a token are bound, off-scale values are rounded per the owner-approved list (14 → 12 vertical / 16 horizontal, 3 → 4, 23 → 24, 27.42 → 24, 2.02 → 2, 7.3 → 8, 11 → 12, 21 → 20, 25 → 24) | one scale | 1,750 values bound 2026-11-10 | 516 unbound values left (off-scale or system) | confirmed (owner, 2026-11-10 · S5; 2026-11-11 · S5) |
| SPC-2 | System values stay plain numbers and are part of the rules: status bar 52, home indicator 34, reserve for the sticky bar, negative overlaps of a sheet over a header | they are not design choices | Mix 1 header `4120:13980` | — | confirmed (owner, 2026-11-11 · S5) |
| SPC-3 | Content top padding under the header = **24** on every screen | one start line | questionnaire ED 01 | applied 2026-11-10 to 64 frames + Order / Uber | confirmed (owner, 2026-11-10 · S2) |
| SPC-4 | Screen side margin = **16** everywhere; the footer keeps 30 | one margin | — | applied 2026-11-10 | confirmed (owner, 2026-11-10 · S4) |
| SPC-5 | Card padding **16**; compact row **12 × 16** | 14 × 16 and 8/16/16/12 were noise | Plan detail cards | V22 pack rows 14 × 16 (go with CMP-4) | confirmed (owner, 2026-11-10 · S3) |
| SPC-6 | Gap between sections = **32** everywhere (`layout/section-gap`); heading → card = 8 | the token and Plan detail already say 32 | Plan detail `3168:11875` | Order 03 / 04 / 05 + Uber 20; Order 03d / 03e, V23, Mix 3 24; V22 48 | confirmed (owner, 2026-11-11 · S1) |
| SPC-7 | Key–value lines inside a card are spaced by 8, never cramped | ChatGPT reference metrics | Plan detail | — | candidate |

## 5. Shape, borders, elevation

| # | Decision | Why | Reference | Violations | Status |
|---|---|---|---|---|---|
| SHP-1 | Concentric radius system (iOS 26): card / inset group / menu / toast 24, nested 16, sheet 40 (top corners), dialog 32, input 16, checkbox 6, controls capsule; thumbnails 8 / 12 / 16 by size; inner radius = outer − inset | owner's inspiration: macOS / iOS 26 | radius board `3342:2191`; `dimensions` collection | — | confirmed (owner, 2026-10-08 · F7) |
| SHP-2 | Only two card radii: 24 and 16 | fewer shapes | — | — | confirmed (owner, 2026-10-28) |
| SHP-3 | Raw and scaled radii go to tokens: pills → `radius/full`, 28 / 20 → 24, 8.1 → 8, 5.7 → 6, 14 → 16; hero bottom corners 28 → 40 | one scale | applied 2026-11-10 (326 nodes) | 37 unbound (mixed corners, Home `4041:12277`) | confirmed (owner, 2026-11-10 · R3) |
| SHP-4 | **Every card has a hairline outline and the card shadow** (0 / 2 / 12, black 5 %) | owner chose both, on all cards | Order 03 `3309:11534` (shadow), `HowItWorksStep` (outline) | ≈ 200 flat cards; ≈ 40 with a 1 px outline; the 33 shadowed cards (Order, Uber) have a 1 px outline instead of the hairline | confirmed (owner, 2026-11-10 · C1; 2026-11-11 · X1) |
| SHP-5 | Three shadow levels as effect styles: card · bottom bar · floating | ≈ 30 raw shadow signatures were in use | — | styles not created | confirmed (owner, 2026-11-10 · C3); values 2026-11-15 · Q09: card 0 / 2 / 12 5 % · bottom bar 0 / −4 / 16 8 % (`StickyBottomBar`) · floating 0 / 4 / 24 25 % (`NavMenu`); card outline `border/default` |
| SHP-6 | Hairline = 1 physical pixel (`border-width/hairline`) for dividers, card, input, chip and glass outlines | iOS-native thin lines | hairline review 2026-10-29 | — | confirmed (owner, 2026-10-29) |
| SHP-7 | Every fill, stroke, padding, gap and radius in a kit component is bound to a variable | one change propagates | kit audit 2026-10-08 | — | confirmed (owner, 2026-10-07) |

## 6. Headers and navigation

| # | Decision | Why | Reference | Violations | Status |
|---|---|---|---|---|---|
| HDR-1 | The reference header is the kit `NavBar`: a button on each side, title in the middle, progress steps under it; title or steps may be absent | "this is the reference: two buttons at the sides, title in the middle, and the progress bar" | Mix 1 `4120:13980` | Mix top bar is a wrapper around `NavBar` (fine) | confirmed (owner, 2026-11-10 · K1) |
| HDR-2 | It is used on **every screen with "back"**, account screens included; special headers only on Home, Search and Order detail | one header | questionnaire, Category, V22, V23 already use it (54 screens) | Plans and Notifications: large left title via `AppHeader` (34 screens) | confirmed (owner, 2026-11-11 · K1) |
| HDR-3 | `NavBar` title: with steps `Heading/H5` 16 SemiBold, without steps `Title 20 · Medium` | smaller when a progress bar is shown; 20 lets long titles („Benachrichtigungen“) fit the 215 px slot | Mix 2 `4120:14150` (16), Cannabis V23c `3735:14291` (22 → 20) | `NavBar` master title has no style; Cannabis V23 and Category titles differ | confirmed (owner, 2026-11-15 · round 3 · Q01) |
| HDR-4 | Order detail and Uber use `AppHeader · order-detail` (number bold, date, copy-ID button, progress) | kit twin exists | `AppHeader` `3108:2579` | 11 hand-built headers | confirmed (owner, 2026-10-08; 2026-11-11 · K1) |
| HDR-5 | Funnel step progress: segment 17, current 53, height 2, gap 8, centred — only in the funnel header | "I meant the progress bar in the header when you start the funnel" | `Progress/Steps` `3081:2236` | — | confirmed (owner, 2026-10-08 · d4) |
| HDR-6 | Order-status progress = equal segments following the app's six timeline steps | real backend statuses | `OrderProgress` `3105:2366` | 4-step bars on Order 03d `3242:8840` and the copied-number toast `4216:16412` | confirmed (owner, 2026-10-08 · d3, d4; **6 steps everywhere** 2026-11-15 · Q06) |
| HDR-7 | **No tab bar.** Navigation = burger in the header → `NavMenu` popover over a blurred screen; Home has a floating „Neue Bestellung“ pill | owner's reference section `3158:20812` | Home menu `4221:18735` | — | confirmed (owner, 2026-10-08 · E1) |
| HDR-9 | Leaving the questionnaire mid-flow: „…“ overflow in the `NavBar` trailing slot → small menu in the `NavMenu` style → leave-confirmation `Dialog` („Fragebogen verlassen?“). No tab bar and no bottom exit button in funnels | the sticky CTA owns the bottom; exit lives in the header | menu `5019:37187`, dialog `5023:37549` (board `5018:37061`) | not rolled out to the steps; the menu is a mock, not a kit component | confirmed (owner, 2026-11-11 · variant C) |
| HDR-8 | `AppHeader · flow-center` duplicates `NavBar` and is removed once no screen uses it | one component per job | — | still in the kit | confirmed (owner, 2026-11-11 · X3) |

## 7. Screens and flows

| # | Decision | Why | Reference | Violations | Status |
|---|---|---|---|---|---|
| PAT-1 | Notifications: no topic grouping and no section headers; unread first, read below; denser list (gap 8); summary banner warm (`Callout` Style `summary`), no icon | owner compared with his original | N01 `3168:8264` | — | confirmed (owner, 2026-10-08) |
| PAT-2 | Destructive confirmation = sheet with consequences and alternatives, a **safe** primary and the destructive action as red text | owner approved variant B on sight | „Plan beenden“ `3340:10464` | — | confirmed (owner, 2026-10-08) |
| PAT-3 | Order detail = kit version: status timeline first, then delivery, payment, further information, support; the cost note „Alle Kosten inkl. …“ is small, without icon; copy button next to the order number | owner picked variant B | CALENDAR 03 `3309:11534`, 03d `3242:8840` | section headings inside cards (superseded by TYP-5) | confirmed (owner, 2026-10-08 · d2; heading placement changed 2026-11-10) |
| PAT-4 | Cancelled order offers „Details“ + „Erneut bestellen“; items come before totals | — | `OrderCard` `3113:3157`, 03e `3242:9115` | — | confirmed (owner, 2026-10-08 · F9, F10) |
| PAT-5 | Questionnaire rejection keeps the shell and offers a primary way out („Andere Behandlungen ansehen“) + a link back („Antwort ändern“) | no dead end | ED S 01 `3298:13316` | — | confirmed (owner, 2026-11-01 · f23) |
| PAT-6 | Consent: „Weiter“ stays enabled; a tap without the checkbox shows the inline error state | a disabled button explains nothing | ED 14 `4220:17138`, 14b `3301:12194` | — | confirmed (owner, 2026-11-01 · d5) |
| PAT-7 | The footer „Footer v2 — Navy“ stays a frame with remote internals; only its background and spacing are bound. It is an exception to the type and component rules | owner keeps the website footer | Home `4041:11533` | — | confirmed (owner, 2026-11-10 · K10; 2026-11-11 · K6d) |
| PAT-8 | Remote `usp-item` rows on Category stay as they are | owner's choice | Category `4075:14790` | title „Original-Medikamente aus Deutschland“ clips | confirmed (owner, 2026-11-11 · K6a) |
| PAT-9 | System-UI screens (lock screen, Dynamic Island, push, share sheet, system calendar) are marked `System reference · ` and excluded from the rules | they follow the OS | `4412:29058`, `4416:29065`, `4219:16477`, `3313:11466` | — | confirmed (owner, 2026-11-10 · H4) |
| PAT-10 | Thank-you screen: brand gradient background bound to tokens; outline buttons | contrast fix | CALENDAR 01 `3313:11406` | — | confirmed (owner, 2026-11-01 · f37, f38) |
| PAT-11 | Restyle keeps the owner's composition: swap components, tokens, text styles, spacing; never redraw or simplify. Matching an owner frame = copying his exact values | an agent once over-redrew How-it-works and Thank-you | owner frames `3167:*` | — | confirmed (owner, 2026-10-08) |
| PAT-12 | Target look: ChatGPT iOS + iOS 26 — two backgrounds (white, light grey), white inset groups, monochrome outline icons without tiles in rows, flat primary button, quiet destructive actions, accent only for the primary button, links, toggles, selection, status | owner's reference | Plan detail `3168:11875` | where it differs from a later answer (links underlined, card outline + shadow), the later answer wins | confirmed (owner, 2026-10-26) |

## 8. States and feedback

| # | Decision | Why | Reference | Violations | Status |
|---|---|---|---|---|---|
| STA-1 | Every list or detail screen draws loading (`Skeleton`), error, empty and offline (`EmptyState`) | no blank screens | Plan loading / error `3222:8766` / `3222:8811`; N02–N08 `3168:8309…8479`; Order 03b / 03c | — | candidate (4 clusters) |
| STA-2 | Retry is always the primary button | one retry style | Plan error `3222:8811`, Order 03c `3242:8794` | — | confirmed (owner, 2026-11-01 · f42) |
| STA-3 | A blocking error is an inline `Callout` above the button, not a toast | the toast disappears before it is read | skip-delivery error `4223:18121` | — | confirmed (owner, 2026-11-01 · f45) |
| STA-4 | Snackbars sit above the sticky-bar zone | they covered the CTA | address saved `4222:17552`, copied `4216:16412` | — | confirmed (owner, 2026-11-01 · f41) |
| STA-5 | An action with a wait shows confirm → loading → result (toast or inline error) | — | skip delivery `4223:17887…18121` | — | candidate |
| STA-6 | Future timeline steps show no time | a time that has not happened misleads | CALENDAR 03 `3309:11534` | — | confirmed (owner, 2026-11-01 · f39) |

## 9. Copy, localisation, formats

| # | Decision | Why | Reference | Violations | Status |
|---|---|---|---|---|---|
| CPY-1 | German, formal Sie, sentence case | — | copy edits 2026-11-01 | — | confirmed (owner, 2026-11-01 · f06, f07) |
| CPY-2 | Dates: typed with the mask DD.MM.YYYY; every displayed date reads „15. Okt. 2026“. Prices „458,20 €“, 24-hour times | de-DE | `DatePicker` `3085:2699` | — | confirmed (owner, 2026-10-08 · D1, E8; 2026-11-01 · f08) |
| CPY-3 | Fees are different things with per-category amounts and come from the backend — never unified in design | they are data | Order summary | — | confirmed (owner, 2026-10-08 · Q6; 2026-11-01 · d1) |
| CPY-4 | UI strings live in the `copy` variable collection (modes `de` / `en`); text layers are named `t:` / `t+:` / `cms:` / `data:` + key | one source for both languages; German overflow is caught by switching the mode | convention of 2026-10-08; N01 `3168:8264` | new `t+` keys carry draft German (Q11) | confirmed (owner, 2026-10-08) |
| CPY-5 | Questionnaire and product copy come from the backend and are not edited in design | — | ED screens | — | confirmed (owner, 2026-10-08) |
| CPY-6 | Delivery promise: DHL delivery in 2–4 days, the same everywhere | "that is the true one" | — | — | confirmed (owner, 2026-11-01 · f09) |
| CPY-7 | Layer, frame, section names and annotations are English; generic names (`Frame 123`) are renamed by role | handoff to developers | renamed 785 layers 2026-11-10 | — | confirmed (owner, 2026-10-08; 2026-11-10 · H1) |

## 10. Figma process

| # | Decision | Why | Reference | Violations | Status |
|---|---|---|---|---|---|
| FIG-1 | Jira-linked frames (section `4292:24466`) are never deleted or recreated; they are updated by replacing frame contents from the working section `3168:4410` | Jira links point at frame ids | — | — | confirmed (owner) |
| FIG-2 | Replaced frames are hidden („· OLD (hidden)“), not deleted or archived | owner wants them at hand | 41 hidden frames | — | confirmed (owner, 2026-11-10 · H2) |
| FIG-3 | Owner reference frames `3167:*` are not modified; clone them | they are the originals | — | V22 `3167:47167` was edited with the owner's OK (2026-11-01 · d7) | confirmed (owner) |
| FIG-4 | Reuse kit components first; a new component needs the owner's yes | — | — | — | confirmed (owner) |
| FIG-5 | Each divergence is decided by the owner on a decision board (options with real crops, a recommendation, a comment field); nothing is normalised by guesswork | "show me cases" | boards of 2026-10-08, 11-01, 11-10, 11-11 | — | confirmed (owner) |
| FIG-6 | One agent writes to the Figma file at a time | parallel writes corrupt each other | — | — | confirmed (owner) |
| FIG-8 | Home: the working frame `4041:12277` is right; the duplicate „10 € sichern“ block in its Jira copy `4292:29906` goes at the next sync | the copy repeats the header promo | `4041:12277` | Jira copy `4292:29906` | confirmed (owner, 2026-11-15 · round 3 · Q04) |
| FIG-7 | All layout bugs found are fixed (overlaps, clipped headings, untranslated strings) | — | Home `4041:11533` (fixed 2026-11-10) | Plan „Change“, Category FAQ overlap (German render) | confirmed (owner, 2026-11-10 · H3) |

---

## 11. Motion

| # | Decision | Why | Reference | Violations | Status |
|---|---|---|---|---|---|
| MOT-1 | Register between restrained and playful: calm, short moves plus micro-animations with a light overshoot (about 5 %) on small things the finger has just touched; never on sheets, dialogs, menus, errors or destructive actions | "something between restrained animation and bounce; micro-animations that show character, that this is not slop" | `drabc-app-ds` `src/utils/motion.ts` | — | confirmed (owner, 2026-11-17 · chat) |
| MOT-2 | One motion set: curves `ease.out` / `ease.inOut` / `ease.accelerate` / `ease.drawer`, durations 120 / 180 / 240 / 300 ms, springs `lively` (≈ 5 % overshoot) and `settle` (none), press scale 0.97 / 0.92 | 4 curve pairs and 9 durations were in use | `src/utils/motion.ts` | — | candidate (values proposed 2026-11-17; not judged on a device) |
| MOT-3 | `Switch` moves with a soft start, a sharp acceleration and a soft landing | owner request | `Switch` `3077:2251` | — | confirmed (owner, 2026-11-17 · chat) |
| MOT-4 | `SegmentedControl`: the selected thumb slides between segments and can be dragged | owner request | `SegmentedControl` `3089:2612` | — | confirmed (owner, 2026-11-17 · chat) |
| MOT-5 | `Tabs` (and the deprecated `TabBar`) animate the change of the selected tab | owner request | `Tabs` `3100:2784` | — | confirmed (owner, 2026-11-17 · chat) |
| MOT-6 | Every pressable gives feedback while the finger is down: colour plus a small scale that springs back; checkbox, radio and switch included | nothing changed under the finger on three controls | — | — | confirmed (owner, 2026-11-17 · chat: "do what you propose") |
| MOT-7 | Dropdown lists and the calendar fade in and drop into place, leave faster; no bounce | they appeared and vanished in one frame | `Dropdown` `3084:2367`, `DatePicker` `3085:2699` | — | confirmed (owner, 2026-11-17 · chat: "do what you propose") |
| MOT-8 | A change from the keyboard is a cut; nothing animates on first paint; reduced motion = instant change with the state still visible | design-critic lens 09 | — | — | candidate |

## Open questions for the project owner

Numbers are never reused. Answered questions stay listed with their answer.

1. ~~Header title sizes~~ — answered 2026-11-15: with steps 16 SemiBold, without steps
   `Title 20 · Medium` (HDR-3).
2. ~~Rating widget and copyright~~ — answered 2026-11-15: stays bold as an external trust mark, sizes
   rounded to the scale; tolerated exception.
3. ~~Grey text ladder~~ — answered 2026-11-15: keep the nearest-colour mapping (COL-12).
4. ~~Home frame `4041:12277` vs its Jira twin~~ — answered 2026-11-15: the working frame is right
   (FIG-8).
5. ~~Bottom sheet handle~~ — answered 2026-11-15: no grabber (CMP-24).
6. ~~Order progress, 6 or 4 steps~~ — answered 2026-11-15: 6 everywhere (HDR-6).
7. ~~Primary-button contrast~~ — answered 2026-11-15: accepted as a brand decision (COL-13).
8. ~~Motion register and tokens~~ — answered 2026-11-17: between restrained and playful, light
   overshoot on touched small things (MOT-1); the values in MOT-2 are still a proposal.
9. ~~Shadow values and card outline colour~~ — answered 2026-11-15: the kit values are the rule
   (SHP-5).
10. **Home** is being redesigned: ten above-the-fold variants (section `4973:30698`), the owner's
    draft with a dynamic green zone (`4995:72760`), notice options B / C / E (section `5030:37524`)
    and the category-deck prototype — none chosen. The new drafts are 402 wide; every READY TO DEV
    screen is 375. Decided in its own thread.
11. **Copywriter:** final German for the `t+` keys.
12. ~~Unread dot colour~~ — answered 2026-11-15: colour by notification type (CMP-25).

## Tolerated exceptions

| Where | Deviates from | Why it is allowed | Since |
|---|---|---|---|
| White label on `interactive/primary` #38A165 (base, Cannabis) | lens 03 · Contrast floors (3.25:1) | owner's decision | 2026-11-01 |
| White text on lime #7ABA47 fills; lime `icon/brand`, `icon/success` on white (decorative, next to text) | lens 03 · Contrast floors (2.35:1) | owner's brand decision | 2026-10-07 |
| Footer „Footer v2 — Navy“: remote components, unstyled texts, side padding 30, raw navy | hard rules 1–4 | owner keeps the website footer as is | 2026-11-10 |
| Remote `usp-item` on Category, clipped title included | hard rule 1 | owner: keep as is | 2026-11-11 |
| `Row` (product line) in Order detail and Uber | hard rule 1 | owner keeps his rows | 2026-11-11 |
| Rating widget and copyright (Roboto Bold / SemiBold; sizes rounded to the scale) | hard rule 4 | external trust mark (owner, Q02) | 2026-11-15 |
| White label on the primary button in Weight loss 2.80, Contraception 4.15, Asthma 3.53 and on the orange „Jetzt bezahlen“ 2.80 | lens 03 · Contrast floors | owner's brand decision (COL-13) | 2026-11-15 |
| Meta text at `text/disabled` (2.19:1 on white) from the nearest-colour mapping | lens 03 · Contrast floors | owner keeps the look (COL-12) | 2026-11-15 |
| System-UI reference screens (SF Pro, OS layouts) | all product rules | they document the OS | 2026-11-10 |
| Questionnaire content, incl. the QS01 dead end | copy rules | content comes from the database | 2026-10-08 |
| Thank-you: white on lime; „start“ screen not rebuilt; motivation line at 40 % white | lens 03 | owner: keep as is | 2026-10-08 |
| System spacing values (52, 34, sticky reserve, negative overlap) | hard rule 3 | not design choices | 2026-11-11 |

## Hard rules (owner-promoted, blocking)

Reviewers treat these as blocking severity: always debt, no context exception (except the
tolerated exceptions above). Full wording: `product.md` §6 — the critic enforces that list; keep
both in step. Compiled on 2026-11-11 from the owner's "everywhere / always" answers; reviewed by
the owner rule by rule on 2026-11-15: 14 kept, 2 moved to product warnings (listed below the
rules in `product.md` §6).

1. Only kit components; nothing new without the owner (FIG-4, CMP-14).
2. No bare hex — only `semantic` variables (COL-5, COL-8).
3. Every gap and padding bound to `space/*` / `layout/*`; plain numbers only for system values (SPC-1, SPC-2).
4. Every text has a text style; Poppins and Roboto only; sizes only from the scale (TYP-1, TYP-2, TYP-8).
5. Radii only from `radius/*` (SHP-1, SHP-2, SHP-3).
6. Buttons are capsules; the main action sits in `StickyBottomBar` (CMP-2, CMP-3).
7. Every card has the hairline outline and the card shadow; selected outline 1.5 (SHP-4, CMP-6).
8. Section heading = small grey text above the card (TYP-5).
9. Every link is underlined (TYP-7).
10. Margin 16, content top 24, section gap 32, card padding 16 (SPC-3, SPC-4, SPC-5, SPC-6).
11. `NavBar` on every screen with "back"; `AppHeader` only on Home, Search, Order detail; no tab bar (HDR-1, HDR-2, HDR-4, HDR-7).
12. Vertical colour only through the `category` mode (COL-5).
13. UI copy German (Sie), bound to `copy` variables; layer names English (CPY-1, CPY-4, CPY-7).
14. A restyle keeps the owner's composition and copies his exact values (PAT-11).

Moved to warnings on 2026-11-15 (the critic reports them, a human decides): brand lime used as a
text colour (COL-1, COL-3); a frame of the Jira-linked section deleted or recreated (FIG-1).

---

## Superseded decisions (history — do not apply)

| Was | Replaced by | When |
|---|---|---|
| "Button shape B": radius 12 for a full-width button at the bottom of a card (`CardAction`, `radius/control/in-card`) | capsule everywhere (CMP-2) | 2026-11-10 |
| Section headings inside the cards on Order detail (owner tweak of 2026-10-09) | heading above the card everywhere (TYP-5) | 2026-11-10 |
| Two section-header styles by role: overline for groups, H4 for content sections | one style (TYP-5) | 2026-11-10 |
| Links without underline (ChatGPT reference) | always underlined (TYP-7) | 2026-11-10 |
| Content cards without border and shadow (ChatGPT reference) | hairline + card shadow on every card (SHP-4) | 2026-11-11 |
| Brand text and links in lime #7ABA47 / link green #269C6E | text-safe brand step (COL-3, COL-4) | 2026-11-01 |
| Selected outline 2 px | 1.5 (CMP-6) | 2026-11-10 |
| Large left title on account screens | centred `NavBar` title (HDR-2) | 2026-11-11 |
| Header title always H3 20 SemiBold (F5 of 2026-10-08) | TYP-6, HDR-3 | 2026-11-10 |
| Button L = 52 | L = 56 (CMP-1) | 2026-10-28 |
| Display heading 26 px | Display 22 / 24 / 30 (TYP-3) | 2026-11-11 |
