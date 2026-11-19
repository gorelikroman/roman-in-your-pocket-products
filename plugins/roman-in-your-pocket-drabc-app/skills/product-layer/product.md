# Product layer — Dr.ABC Application

> Loaded on top of the universal rules whenever work concerns the Dr.ABC mobile app
> (Roman in your Pocket `products/README.md`). A row here without a source or a reference screen does not exist.
> Only the product owner edits this file; builds and reviews propose changes.
>
> **Names:** Dr.ABC Application · Dr.ABC app · DoktorABC app · DoktorABC mobile · doktorabc-mobile ·
> dr-abc-ui · "мобильное приложение Dr.ABC" · Figma file "Dr.ABC Application" — every name people
> use for this product in requests. The DoktorABC **website** and **Reboost** are different products.
>
> Product owner: Roman · Design system owner: Roman · Last updated: 2026-11-15 ·
> Decisions log: `design-decisions.md` (this folder)
>
> **This layer is the handbook** — there is no separate one. Rules describe the decided target
> state; where the Figma file is behind, §10 lists it, and a screen that contradicts a rule is drift,
> not evidence. Values come from the Figma variables and styles of file `3GnJD8QN587Y912O3F15Cx`; the
> numbers quoted here are a snapshot (base vertical, light theme) and the variable wins on conflict.
> Without Figma access, start the answer with "Product: Dr.ABC Application (summary layer, 2026-11-15)".
>
> Reading order — **build:** §5 → §4 → §2 → §9 → §6 · **review:** §6 → §5 → `design-decisions.md` →
> §10 · **spec:** §5 → §3 → `design-decisions.md` §8 · **test:** §6 → §3 (formats) → §10.

## 1. The product

- **What it is and for whom:** a German-language telemedicine and online-pharmacy app for adults in
  Germany. A patient picks a treatment, answers a medical questionnaire, a doctor approves a
  prescription, the pharmacy ships (DHL, or Uber courier with live tracking). Treatment plans
  (subscriptions) repeat the order.
- **Verticals** (the `category` variable collection, 9 modes): Dr.ABC (base) · ED · Weight loss ·
  Testosterone · Hair loss · Contraception · Diabetes · Asthma · Cannabis. Code slugs: `base, ed,
  weight-loss, testosterone, hair-loss, contraception, diabetes, asthma, cannabis`.
- **Platforms:** iOS first (React Native / Expo; Android follows from the same code). One frame per
  screen, **375 wide**. Units pt = dp. Light theme only; dark mode is not designed. No tab bar (§5).
- **Primary tasks:** find a treatment · answer the questionnaire · choose a pack and a plan and pay ·
  follow an order (status, courier) · manage plans and notifications.
- **Users' typical state:**

| Surface | Verb | State |
|---|---|---|
| Home, Search, Category | find | browsing, often a first visit; leaves easily |
| Product, plan choice (funnel) | choose, buy | buying with doubt; compares packs and prices |
| Questionnaire | answer | committed but tired; each screen should take seconds; medical anxiety |
| Checkout (address, payment) | buy | peak anxiety about money |
| Thank you, Order detail, Uber tracking | glance, wait | wants status and the next step, nothing else |
| Plans, Notifications | manage | calm, routine; anxious around money and health |

- **Locales and house formats:** UI copy is German, formal **Sie**. Dates „15. Okt. 2026“, typed
  dates with the mask DD.MM.YYYY, prices „458,20 €“ (comma, space, € after), "from" price
  „ab 29,99 €“, 24-hour times, rating „4,81“. An English preview exists only as the `copy` variable
  mode `en`. No RTL.

## 2. Design system sources

The truth lives in the Figma file; the skill reads it and never invents values.

| Source | Link / path | Notes |
|---|---|---|
| Component library (design) | Figma file "Dr.ABC Application", key `3GnJD8QN587Y912O3F15Cx` — kit pages 🎨 Foundations `3066:2191` · 🧩 UI KIT `3073:2191` · 🧬 Molecules `3097:2191` · 🏗 Organisms `3097:2192` · Templates `3097:2193` | the only source of components; kit ids in `design-decisions.md` §3 |
| Design tokens | Figma variables: `primitives` · `category` (9 modes) · `semantic` (mode `light`) · `dimensions` · `copy` (STRING, modes `de` default / `en`) | `legacy · …` collections are not used |
| Token export for code | `briefs/app-design-system/dev-handoff/` (TS, CSS, DTCG JSON); reference page https://claude.ai/artifact/UbEhvgCias67ZyGQEgkinL | exported 2026-11-03 |
| Component code | RN kit `dr-abc-ui` (Expo 54); the app `doktorabc-mobile` | the app's i18n keys are the source of copy keys; code not synced after 2026-11-03 |
| Component docs / Storybook | `dr-abc-ui` Storybook 9 (runs locally, no hosted URL) | |
| Icon set | `Icon/*` components on 🧩 UI KIT; outline, monochrome | icon tiles (`IconTile`) only where the kit component has them (`NavMenu`, `NotificationCard`); list rows use a bare icon |
| Working section | page `Ready for Dev \| Phase 3` (`0:1`) → section „Ready for review“ `3168:4410` | edit and build here; `copy` mode `en` |
| Jira-linked section | same page → section `4292:24466` (READY TO DEV) | Jira tickets link to its frames: **never delete or recreate a frame**; updated only by replacing frame contents from the working section; `copy` mode `de` |
| Not a source | pages `legacy · UI KIT`, `In process`; remote libraries; frames named „· OLD (hidden)“; owner reference frames `3167:*` (never modified, clone them) | components from there are replaced by kit ones, see §4 |

Token roles the skill should know by name (values stay in the source):

| Role | Token name | Use for |
|---|---|---|
| primary action | `interactive/primary` (+ `-pressed`), label `text/on-brand` | the screen's main button |
| other actions | `interactive/secondary` · `neutral` · `ghost` · `warning` (each + `-pressed`) | secondary buttons; `warning` = „Jetzt bezahlen“ |
| danger | `interactive/danger`; `fill/error`, `text/error`, `icon/error` | destructive actions, errors |
| brand | `fill/brand`, `icon/brand` (fills, icons) · `text/brand` = `text/link` = `border/brand` (text, links, outlines) · `text/brand-on-subtle` (text on tints) | brand surfaces, progress, links |
| surface / canvas | `fill/page` (screen) · `fill/surface` (card) · `fill/surface-sunken` = `fill/muted` (well, inactive chip) · `fill/overlay` (scrim) | backgrounds |
| text primary / secondary | `text/primary` · `text/secondary` · `text/tertiary` · `text/disabled` | text |
| borders | `border/subtle` · `default` · `strong` · `control` · `focus`; widths `border-width/hairline` · `default` · `selected` · `strong` | outlines, dividers, inputs |
| spacing ladder | `space/0…64`; `layout/screen-padding` · `layout/section-gap` · `layout/card-padding` | every gap and padding |
| radius ladder | `radius/surface/*` · `radius/control/*` · `radius/content/*` · `radius/full` | every corner |
| type ladder | text styles `Heading/*` · `Subtitle/*` · `Body/*` · `UI/*` · `Caption/*` | every text |
| motion durations and easing | none yet (§7) | — |

The values below are a snapshot of the base vertical, light theme. Layering: `primitives` (raw palette, never used in components) → `category` (per vertical) →
`semantic` (the **only** colours a screen or component binds). Only brand-related semantic tokens
change between verticals; neutrals and status colours are the same everywhere.

### Colour roles

Hex = base vertical.

| Role | Token | Value / note |
|---|---|---|
| Primary button | `interactive/primary`, `-pressed`; label `text/on-brand` | #38A165 / #2D8151 (button green, not the logo lime); white label accepted (owner) although below 4.5:1 in several verticals — base 3.25, Weight loss and the warning button 2.80 (§8) |
| Brand surface, progress, brand icon | `fill/brand`, `icon/brand` | #7ABA47 lime — fills and icons only, **never text** |
| Brand tint | `fill/brand-subtle`, `interactive/selected` | #F2F8ED |
| Brand text, links, outline borders | `text/brand`, `text/link`, `border/brand` | #2D8151 on white. On grey or tinted surfaces use `text/brand-on-subtle` #395626 |
| Text | `text/primary` · `secondary` · `tertiary` · `disabled` | #08080A · #4B525C · #646C78 · #A6B0BF |
| Surfaces | `fill/page` · `fill/surface` · `fill/surface-sunken` = `fill/muted` · `fill/overlay` | #F5F6F8 screen · #FFFFFF card · #EBEEF2 well, inactive chip · scrim |
| Borders | `border/subtle` · `default` · `strong` · `control` · `focus` | #EBEEF2 · #DEE3EA · #C8CFD9 · #8C94A3 · #5A8836 |
| Status | `fill/{success\|warning\|error\|info}` + `-subtle`; `text/…`; `icon/…` | success text on a tint = `text/success-on-subtle` |
| Other actions | `interactive/secondary` (tint) · `neutral` (grey) · `ghost` · `danger` · `warning` (orange „Jetzt bezahlen“) | each has `-pressed` |
| On brand / photo headers | `interactive/glass`, `border/glass` | glass icon buttons |
| Footer | navy, raw #1F2129 | the footer is an exception (§8) |
| Brand header | `category/gradient/base` + radial glow `gradient/glow-from → glow-to` at 70 % | recolours per vertical |

Mobile has no hover: states are default / pressed / disabled / selected / loading.

### Type

Poppins (400 / 500 / 600) = headings, subtitles, UI (buttons, inputs, labels, links).
Roboto (400 / 500) = body and captions. Nothing else: no Inter, no Roboto Bold / SemiBold, no
Poppins Light. Size scale: **11 · 12 · 13 · 14 · 16 · 18 · 20 · 22 · 24 · 30 · 36** — no other
size exists. Line height and letter spacing are set in % inside the styles.

| Style | Font | Size / line | Use for |
|---|---|---|---|
| `Heading/Display` · `H1` · `H2` · `H3` · `H4` · `H5` | Poppins SemiBold | 36 / 30 / 24 / 20 / 18 / 16 | content headings; `H5` = `NavBar` title when steps are shown |
| `Heading/Title 22 · Medium`, `Title 20 · Medium` | Poppins Medium | 22, 20 / 130 % | `Title 20` = `NavBar` title without steps; `Title 22` = order-detail header |
| Display 22 / 24 / 30 *(decided, not yet created — §10)* | Poppins Medium, 110 %, −0.5 px | 22 / 24 / 30 | large marketing headings (Home, Category, How it works), tile and card titles |
| `Subtitle/Subtitle XL·Medium`, `L·Medium`, `L·SemiBold`, `M·Medium`, `M·SemiBold` | Poppins | 18 / 16 / 14, 120–130 % | row and card titles, labels such as „Lieferadresse“, „Gesamt:“ |
| `Body/Body L`, `Body M`, `Body M · Medium`, `Body S`, `Body S · Medium` | Roboto | 18 / 16 / 14, 145–150 % | prose; `Body S` is also the section heading above a card |
| `UI/Button L`, `UI/Button S` | Poppins Medium | 16 / 14 | button labels (inside `Button`) |
| `UI/Input` | Poppins Regular | 16 | field value |
| `UI/Label`, `UI/Label-chips` | Poppins Regular | 13 / 12 | tab labels; chip labels |
| `UI/Link`, `UI/Link L` | Poppins Medium, **underlined** | 14 / 16 | every text link |
| `Caption/Caption`, `Caption M`, `Caption · Strike`, `Overline` | Roboto | 12 / 12 / 12 / 11 | meta, legal, old price; `Overline` is not used for section headings |

### Spacing

Scale `space/0…64`: 0 · 2 · 4 · 6 · 8 · 10 · 12 · 16 · 20 · 24 · 32 · 40 · 48 · 64
(`padding/*`, `gap/*` are aliases). Every gap and padding is bound to a variable.

| What | Value | Token |
|---|---|---|
| Screen side margin | 16 | `layout/screen-padding` |
| Top padding of the content under the header | 24 | `space/24` |
| Gap between sections | 32 | `layout/section-gap` |
| Section heading → its card | 8 | `space/8` |
| Card padding | 16 | `layout/card-padding` |
| Compact row (dense list) | 12 vertical × 16 horizontal | `space/12`, `space/16` |
| Bottom sheet | top 8, sides 16, bottom 34 | — (kit master still has bottom 24, §10) |
| System values, kept as plain numbers | status bar 52 · home indicator 34 · reserve under the content = height of the sticky bar · negative overlap of a white sheet over a coloured header | not tokens |

### Radius

Concentric (iOS 26 style): inner radius = outer radius − inset.

| What | Value | Token |
|---|---|---|
| Card, inset group, menu, toast | 24 | `radius/surface/card` |
| Nested block inside a card; option row in a dense list | 16 | `radius/surface/nested` |
| Bottom sheet (top corners), hero bottom corners | 40 | `radius/surface/sheet` |
| Dialog | 32 | `radius/surface/dialog` |
| Input | 16 | `radius/control/input` |
| Buttons, chips, search, icon buttons, badges | capsule | `radius/control/*`, `radius/full` (code: `capsule(height)`) |
| Checkbox | 6 | `radius/control/checkbox` |
| Thumbnails | ≤ 40 → 8 · 41–80 → 12 · > 80 → 16 | `radius/content/*` |

Do not use `radius/component/*` (deprecated), `radius/surface/nested-16` (its value is 8) or
`radius/control/in-card` (belonged to the cancelled "Button shape B").

### Borders and elevation

| What | Value | Token |
|---|---|---|
| Card outline, divider, input, chip, glass outline | 1 physical pixel, colour `border/default` | `border-width/hairline` (RN `StyleSheet.hairlineWidth`) |
| Outline / secondary button | 1 | `border-width/default` |
| Selected option, selected card | 1.5 | `border-width/selected` |
| Focus, error | 2 | `border-width/strong` |
| Shadow levels | three: **card** 0 / 2 / 12, black 5 % · **bottom bar** 0 / −4 / 16, black 8 % (as on `StickyBottomBar`) · **floating** 0 / 4 / 24, black 25 % (as on `NavMenu`; menus, floating button) | effect styles (values confirmed by the owner 2026-11-15) — not created yet (§10) |

## 3. Voice and terms

- **Voice:** German, formal **Sie**, sentence case („Plan wählen“). No exclamation marks in errors.
  A warning states the consequence and the way out. A button label names the action („Andere
  Behandlungen ansehen“, „Antwort ändern“); an instruction to press a button never sits inside a
  notice.
- **Terms (one term per concept):** „Weiter“ · „Ändern“ · „Benachrichtigen“ · „Jetzt bezahlen“ ·
  „Erneut bestellen“ · „Neue Bestellung“ · „Plan beenden“ · „Zur Kategorie“. Order status words
  follow the app's timeline, six steps: Bestellung erstellt → Bezahlt → Rezept genehmigt → An die
  Apotheke geschickt → Versandt → Zugestellt. One delivery promise everywhere: DHL delivery in
  2–4 days.
- **Words never used:** „du“ forms; Title Case labels („Plan Wählen“); English strings in the `de`
  mode („Change“ instead of „Ändern“); unified or "corrected" fee amounts.
- **Copy mechanics:** copy is not typed into layers. Every UI string is a variable of the `copy`
  collection (name = the app's i18n key with `/`), and the text layer is named by its source: `t:key`
  existing app key · `t+:key` new key proposed in design (German draft, needs the copywriter) ·
  `cms:key` text from the backend (questionnaire, product copy — cannot be changed in design) ·
  `data:…` dynamic data. To change a text, change the variable in both modes.
- **German is longer than English:** check every new screen in `copy` mode `de` for wrapping and
  clipping before calling it done.
- **Fees and amounts are data.** Treatment fee, service fee and shipping differ per category and come
  from the backend; never unify them in a mockup.
- Layer, frame and section names, annotations, board texts: **English.** Only in-app copy is German.

## 4. Components — when to use which

Always check the kit first and reuse; a new component, variant, token or style needs the owner's yes
before it is created. Reference = the kit component (ids on the kit pages) or a screen in the
working section `3168:4410`.

| Need | Use | Not | Reference |
|---|---|---|---|
| Primary action (screen CTA) | `StickyBottomBar` (button · button+link · price+button · cart+button · two-buttons · floating-cta) on **every** screen with a main action, funnel included | a CTA inside the last card; a loose bar | `3109:2378`; Plan detail `3168:11875` |
| Any text action | `Button` — Style primary · secondary · neutral · ghost · danger · outline · link · link-neutral · warning; Size L (56) / S (40); State default / pressed / disabled / loading; **capsule** | `Shape=rounded`, `CardAction` (cancelled shape B); remote `MainButton` / `Button`; a styled frame | `3074:23952` |
| Icon action, header buttons | `IconButton` L 52 / S 40 (primary · neutral · ghost · `glass-light` on a light page · `glass-dark` on brand, gradient or photo) | remote `icon_btn`, `camera` | `3076:2249` |
| Header with "back" | `NavBar` (343 × 52): leading button 52, centre slot 215 wide for the title, trailing button 52, optional steps (§5) | `AppHeader · flow-center` (duplicate), a hand-built top bar | `4198:8171`; Mix 1 `4120:13980` |
| Special headers | `AppHeader` Layout `home` · `search` · `order-detail` · `hero` | building them by hand | `3108:2579` |
| Funnel progress | `Progress/Steps` in the header: segment 17, current 53, height 2, gap 8 | "N of M" text | `3081:2236` |
| Section heading | `SectionHeader`: small grey text **above** the card (`Body S`, sentence case, `text/secondary`, inset 16, 8 to the card), optional count or link on the right | a heading inside the card; UPPERCASE overline; a loose H5 | `3101:2233` (decided look = instance override, §10); Plan detail `3168:11875` |
| Single / multiple choice | `SelectionRow` — questionnaire: Style `card`, r24, Control `none` for single choice (selection = tint + 1.5 border), `checkbox` for multiple; dense lists (packs, plans): compact rows r16, 12 × 16, price in the trailing slot | `Radio` groups in the questionnaire; hand-built option rows | `3089:2687`; ED 01 `3298:12564`; Mix 1 packs `4120:13980` |
| Dosage, filters | `FilterChip` (selected = filled brand, white label) | `SegmentedControl` for dosage | `3080:2266`; V22 `3167:47167` |
| Text input | `TextField` with a floating label; `TextArea`; `Dropdown`, `Combobox`, `DatePicker`, `SearchField` are built on it | a static label above; remote `input`; a placeholder as the label | `3082:2292` |
| Error on a field | the field's error look (outline `border-width/strong` 2, message under the field); consent: inline error under the checkbox, button stays enabled | a disabled button that explains nothing; a toast | ED 14 `4220:17138`, 14b `3301:12194` |
| Label + value, totals | `KeyValueRow` (default · total · discount) | `Row/Price`, `Row/Bullet` from "In process" | `3101:2247` |
| Product line in a summary | `OrderLineItem` | legacy `Image and Info Container` | `3103:2346` |
| Product | `ProductCard` Layout card · row · tile · result; price via `PriceBlock` (prefix „ab“, old price struck) | legacy `ProductCard` | `3112:3079`, `PriceBlock` `3102:2275` |
| FAQ, expandable text | `AccordionItem` rows with dividers, grouped in **one** card | one card per question; remote `NEW FAQ` | `3104:2282`; Plan detail support `3168:11875` |
| Notice inside content | `Callout` — brand (green) for reassuring notes, info / success / warning / error by meaning; Style `summary` for the warm summary banner | a grey plate, an outlined pill, a toast as a notice | `3090:2716`; Order 03d `3242:8840` |
| Small note under a button | plain `Caption` text | a Callout | text style `Caption/Caption` |
| Status of an item | `Badge` (neutral · brand · success · warning · error · info) | colour alone; a chip | `3080:2241` |
| Order timeline | `OrderTimeline` (decided, Uber-tracking look; not built yet — until then copy the timeline from Uber R1) | `TimelineStep` from "In process" | Uber R1 `4398:27562` |
| Bottom sheet | `BottomSheet` (Header title+close / title+reset; Footer button / button+link / none); **no grabber** — close by X or swipe-down | a loose frame with its own paddings | `3110:2846`; Mix 1b `4203:14786` |
| Confirmation of a destructive action | sheet pattern „Plan beenden“ (consequences → alternatives → safe primary → destructive as red text); a short confirmation = `Dialog` (one · two · destructive) | a red primary button for a reversible action | „Plan beenden“ `3340:10464`; `Dialog` `3110:2930` |
| Transient feedback | `Snackbar` (dark; neutral · success · error · warning), above the sticky-bar zone | a toast for a blocking error | `3105:2326` |
| Empty state, error, offline, loading, success | `EmptyState` (Tone empty · error · offline · success · loading); `Skeleton` while loading | "No data" text | `3111:2773`, `3210:2490`; Plan error `3222:8811` |
| Navigation | burger in the header → `NavMenu` popover over a blurred screen | `TabBar` (deprecated, not used) | `3164:26652`; Home menu `4221:18735` |
| Notification | `NotificationCard` (unread · read · action · resolved · …); the unread dot takes the colour of the notification type | grouping by topic, section headers | `3111:2851`; card states `3168:8526` |
| List row, settings | `ListItem`, `ListGroup` | hand-built rows | `3090:2772`, `3109:2576` |
| Cannabis effects | `EffectIcon` (11 effects), `EffectTile` | redrawn bubbles | `3257:10085`, `3257:10086` |

Tolerated non-kit pieces (do not replace, do not copy into new screens): the footer „Footer v2 —
Navy“ with its remote `accordions` and `Legal / PCi`; remote `usp-item` on Category; `Row` (product
line) in Order detail and Uber; the rating widget „4,81 · Sehr gut“ (stays bold as an external trust mark; sizes on the scale).

## 5. Patterns

Assembly: **one shell per screen → sections → kit components.** Reference node ids are in the
working section `3168:4410`.

### Shell rules shared by every screen
- **Use when:** always
- **Structure:** page background `fill/page`; content in white cards (`fill/surface`, r24, hairline outline and the card shadow) · side margin 16, content starts 24 under the header, sections 32 apart · a section = small grey heading above (8) + its card · the main action lives in `StickyBottomBar` · header by type (next pattern)
- **Reference:** Plan detail `3168:11875`
- **Decisions log rows:** SHP-4 · SPC-3 · SPC-4 · SPC-6 · TYP-5 · CMP-3 · PAT-12

### Header by screen type
- **Use when:** choosing the top of any screen
- **Structure:**

| Screen type | Header | Title |
|---|---|---|
| Any screen with "back" — funnel, questionnaire, product, category, plans, notifications, sheets as screens | `NavBar`: back left, optional button right, centred title, optional steps | with steps → `Heading/H5` 16 SemiBold; without steps → `Title 20 · Medium` (long titles such as „Benachrichtigungen“ fit the 215 px slot); title may be absent (questionnaire, product) |
| Home | `AppHeader · home` on the brand surface with glow: logo, glass burger | — |
| Search | `AppHeader · search` on brand: glass back, search field | — |
| Order detail, Uber tracking | `AppHeader · order-detail`: back, order number **bold**, date, copy-ID button, progress | `Title 22 · Medium` around the bold number |

- **Reference:** Mix 1 `4120:13980` (NavBar with steps), Cannabis V23c `3735:14291` (NavBar without steps), Home `4041:11533`, CALENDAR 03 `3309:11534`
- **Decisions log rows:** HDR-1 · HDR-2 · HDR-3 · HDR-4 · HDR-5 · CMP-17 · TYP-6

### Questionnaire step
- **Use when:** one medical question per screen inside a treatment funnel
- **Structure:** `NavBar` (back, steps, no title) → question → helper → `SelectionRow` cards r24 (single: no radio; multiple: checkbox) or `TextArea` / `DatePicker` → sticky „Weiter“. Follow-up and rejection screens keep the shell; a rejection offers a primary way out + a link back. Consent: the button stays enabled, a tap without the checkbox shows the inline error. Leaving mid-flow: „…“ in the header's trailing slot opens a small menu; leaving asks for confirmation in a `Dialog` (menu `5019:37187`, dialog `5023:37549`)
- **Reference:** ED 01 `3298:12564`, ED 12b `3301:12100`, ED S 01 `3298:13316`, ED 14 / 14b `3300:12249` / `3301:12194`
- **Decisions log rows:** CMP-5 · PAT-5 · PAT-6 · HDR-9 · CPY-5

### Funnel: product → plan → checkout
- **Use when:** buying a treatment after the questionnaire
- **Structure:** `NavBar` (back, title, steps, menu) → cards: product with pack rows (compact `SelectionRow` r16) and dosage chips → plan options → address form (`TextField`) and payment → totals (`KeyValueRow`) → reassuring note (`Callout` brand) → sticky CTA
- **Reference:** Mix 1 `4120:13980`, Mix 2 `4120:14150`, Mix 3 `4120:39534`
- **Decisions log rows:** CMP-3 · CMP-4 · CMP-6 · CMP-7 · CMP-8 · CMP-10 · CMP-12 · CPY-3

### Product page
- **Use when:** describing one treatment before the funnel
- **Structure:** `NavBar` without title → hero (bottom corners 40) → tabs (`UI/Label`) → sections → similar treatments (`ProductCard` row, „ab“ before the price, no chevron) → sticky bar
- **Reference:** V22 `3167:47167` (owner frame), Cannabis V23c `3735:14291`
- **Decisions log rows:** CMP-15 · CMP-7 · CMP-3 · PAT-11

### Category page
- **Use when:** presenting one vertical and its treatments
- **Structure:** `NavBar` with title → hero → Display headings → `usp-item` rows (kept) → `ProductCard`s → FAQ (`AccordionItem` in one card) → footer
- **Reference:** Category ED `4075:14790`
- **Decisions log rows:** TYP-3 · TYP-4 · PAT-8 · CMP-9 · PAT-7

### Home
- **Use when:** the app's start screen
- **Structure:** brand header → category tiles (Display 22 titles, Caption subtitles) → How it works (`HowItWorks`) → treatments → FAQ → floating „Neue Bestellung“ → navy footer. **Being redesigned by the owner** (draft `4995:72760`: a green zone that grows with an active order; layout and notice options not chosen) — do not derive new rules from Home until he picks
- **Reference:** Home `4041:11533`
- **Decisions log rows:** TYP-3 · TYP-4 · HDR-7 · PAT-7 · CMP-22 · CMP-19 · open question 10

### Search
- **Use when:** finding a treatment by name or symptom
- **Structure:** brand search header → `SearchFilterBar` → `ProductCard · result`, one card per result → end-of-results / loading-more
- **Reference:** `3334:29379`, `4216:16765`, `4216:16889`
- **Decisions log rows:** CMP-21

### Account list / detail
- **Use when:** plans, settings and other account screens
- **Structure:** `NavBar` with centred title → sections (heading above card) → `ListItem` / `KeyValueRow` cards → quiet secondary actions at the bottom („Plan beenden“ as grey text)
- **Reference:** Plan detail `3168:11875`; Home with an active plan `3168:11516`
- **Decisions log rows:** HDR-2 · TYP-5 · CMP-10 · PAT-12

### Notifications
- **Use when:** the list of messages about orders, plans and payments
- **Structure:** `NavBar` → filter chips → `NotificationCard`s, unread first, no group headers; action-required = `Button S primary`, other actions = `Button S outline`
- **Reference:** N01 `3168:8264`, card states `3168:8526`
- **Decisions log rows:** PAT-1 · CMP-18

### Order detail
- **Use when:** one order's status, delivery and payment
- **Structure:** order header with the 6-step order progress (one segment per backend status, every order state) → status card with the timeline → delivery → payment (`KeyValueRow`, totals) → further information (`AccordionItem`) → support
- **Reference:** CALENDAR 03 `3309:11534`, 03d payment due `3242:8840`, 03e cancelled `3242:9115`
- **Decisions log rows:** PAT-3 · PAT-4 · HDR-4 · HDR-6 · TYP-6 · CMP-10 · CMP-11 · COL-7 · STA-6

### Live courier tracking
- **Use when:** an Uber delivery is on its way
- **Structure:** order header → map / status card → courier timeline → same sections as Order detail
- **Reference:** Uber R1 `4398:27562`, R0–R7
- **Decisions log rows:** CMP-11 · HDR-4

### Thank you
- **Use when:** right after a successful order
- **Structure:** brand gradient screen → what happens next → outline actions (calendar)
- **Reference:** CALENDAR 01 `3313:11406`
- **Decisions log rows:** PAT-10

### Bottom sheet
- **Use when:** a short task or a choice on top of the current screen
- **Structure:** `BottomSheet`: title + close (X in a grey circle), content padding 16, bottom 34, no grabber; full-height lists scroll inside; a second sheet may stack on top (Sort & filter)
- **Reference:** Mix 1b `4203:14786`, address sheet `4222:17204`, About plans `4214:16237`
- **Decisions log rows:** CMP-13 · open question 5

### Destructive confirmation
- **Use when:** an action with consequences the user may regret (end a plan, cancel)
- **Structure:** sheet: consequences → alternatives → **safe** primary → destructive as red text
- **Reference:** „Plan beenden“ `3340:10464`
- **Decisions log rows:** PAT-2

### Menu
- **Use when:** moving between the app's areas
- **Structure:** burger → `NavMenu` popover over a blurred screen: Bestellungen / Abos, Benachrichtigungen (+ count), Warenkorb, Einstellungen, Abmelden
- **Reference:** Home menu `4221:18735`, Mix 1 menu `4221:18490`, V22 menu `4221:18227`
- **Decisions log rows:** HDR-7

### States every flow draws
- **Use when:** any list, detail or action that loads, fails or can be empty
- **Structure:** loading (`Skeleton`), error (`EmptyState · error`, retry = primary), empty, offline, success toast (`Snackbar` above the sticky bar), action loading / failed on the card that owns the action. A blocking error is an inline `Callout` above the button, not a toast
- **Reference:** Plan loading / error `3222:8766` / `3222:8811`; skip delivery confirm → loading → toast → error `4223:17887…18121`; Notifications 02–08 `3168:8309…8479`; Order 03b / 03c `3242:8753` / `3242:8794`
- **Decisions log rows:** STA-1 · STA-2 · STA-3 · STA-4 · STA-5 · CMP-20

## 6. Hard rules

The product's non-negotiables, confirmed rule by rule by the owner on 2026-11-15 (sources in
`design-decisions.md` · Hard rules). A violation is `debt` with no `context` exception (review
method §4.5), except the tolerated pieces listed in `design-decisions.md`.

1. Only components from the kit pages of this file. Nothing from `legacy · UI KIT`, "In process" or
   remote libraries in a new screen. No new component, variant, token or style without the owner.
2. No bare hex: every fill, stroke and text colour is a `semantic` variable; never a primitive,
   never a `legacy · …` variable.
3. Every gap and padding is a `space/*` / `layout/*` variable. Off-scale values do not exist; the
   only plain numbers are the system values in §2.
4. Every text layer has a text style from §2. Fonts are Poppins and Roboto only; sizes only from
   the scale.
5. Radii only from `radius/*`: card 24, nested 16, sheet 40, dialog 32, input 16, controls capsule.
6. Buttons are capsules everywhere. The screen's main action sits in `StickyBottomBar`.
7. Every card has the hairline outline and the card shadow; a selected option has a 1.5 outline.
8. A section heading is small grey text above its card — never inside the card, never uppercase.
9. Every link is underlined (`UI/Link`, `UI/Link L`).
10. Screen margin 16, content top 24, section gap 32, card padding 16 (compact row 12 × 16).
11. Every screen with "back" uses `NavBar`; Home, Search and Order detail use their `AppHeader`
    layout. No tab bar.
12. Vertical colour only through the `category` mode, never by recolouring layers.
13. UI copy is German (Sie), bound to `copy` variables; layer and frame names are English.
14. Restyling an owner screen changes components, tokens, text styles and spacing only — never the
    composition or the content. Matching an owner frame means copying his exact values.

Product warnings (listed; a human accepts or rejects): German text that wraps or clips; a flow
without loading / error / empty states; a toast used for a blocking error; more than one filled
button on a screen; a hand-built block that has a kit twin; an English string in `de` mode;
brand lime (`fill/brand`, `icon/brand`) used as a text colour — brand text uses `text/brand`, on a
tint `text/brand-on-subtle`; a frame of the Jira-linked section `4292:24466` deleted or recreated
(Jira tickets link to its frame ids — replace contents instead, §9).

## 7. Motion register

- **Register (owner, 2026-11-17):** between restrained and playful. Calm, short moves, plus
  micro-animations with character: a **light overshoot (about 5 %)** on small things the finger has
  just touched — a released button, the `Switch` thumb, the `SegmentedControl` thumb, a radio dot or a
  tick popping in. **Never** an overshoot on sheets, dialogs, menus, errors or destructive actions:
  those settle without bounce. The motion should read as made on purpose, not as a default.
- **One motion set** — source `drabc-app-ds` `src/utils/motion.ts`; no other curve or duration:

  | Token | Value | Use |
  |---|---|---|
  | `ease.out` | cubic-bezier(0.23, 1, 0.32, 1) | entrances, small state changes |
  | `ease.inOut` | cubic-bezier(0.77, 0, 0.175, 1) | something that stays on screen and moves: soft start, sharp acceleration, soft landing |
  | `ease.accelerate` | cubic-bezier(0.3, 0, 1, 1) | exits |
  | `ease.drawer` | cubic-bezier(0.32, 0.72, 0, 1) | sheets settling |
  | `duration.press` / `quick` / `standard` / `slow` | 120 / 180 / 240 / 300 ms | press · toggles, indicators, popovers · toasts, dialogs · sheets |
  | `spring.lively` | stiffness 300, damping 24 (≈ 5 % overshoot) | the character: touched small things |
  | `spring.settle` | stiffness 300, damping 35, no overshoot | sheets, anything that must not bounce |
  | `pressScale` | 0.97 (buttons, chips) · 0.92 (icon button, checkbox, radio) | press feedback, springs back on release |

  The numbers are a proposal that follows the owner's description; he has not judged them on a device yet.
- **Interactions decided:** `SegmentedControl` — the selected thumb slides and can be dragged (follows
  the finger, lands where the momentum points); `Switch` — soft start, sharp acceleration, soft landing,
  the thumb stretches under the finger; `Tabs` — the underline slides to the selected tab, the pill
  fill crossfades; dropdown lists and the calendar fade in and drop 6 px into place, leave faster.
- **Always:** a change from the keyboard is a cut; nothing animates on first paint; exits are shorter
  than entrances; transform and opacity only; under reduced motion movement becomes an instant change
  and the state stays visible; a haptic tick on a segment change and a switch flip, never as the only
  feedback.
- **Decided earlier:** bottom sheets close by swipe-down as well as by the X; `NavBar` has a
  `Scrolled` state (reference Mix 1 scrolled `4219:17385`); How it works steps expand one at a time
  (`4200:16578…16628`). The Home category deck (pinned-deck scroll) is a prototype awaiting approval.

## 8. Tolerated exceptions (summary)

Full table with reasons: `design-decisions.md`. In short: white label on the primary button and on
lime and the primary buttons of every vertical incl. the orange „Jetzt bezahlen“ (below 4.5:1, owner's brand decision) · the navy footer with its remote parts · remote
`usp-item` · `Row` in Order detail · the rating widget (bold, sizes on the scale) · grey text kept on the nearest-colour mapping (meta text at `text/disabled`) · questionnaire texts from the backend ·
system-UI reference screens (lock screen, Dynamic Island, push, share sheet, system calendar —
frames prefixed `System reference · `; they follow the OS, not this system) · hidden „· OLD“ frames
(kept, never copied).

## 9. Working in Figma

1. Build or edit only in the working section `3168:4410`. Never in `4292:24466`.
2. Start from the nearest existing screen of the same shell (§5) and from kit components.
3. Set the frame's `category` mode to the vertical and check `copy` mode `de`.
4. Bind everything: colours → `semantic`, spacing → `space` / `layout`, radius → `radius`, text →
   styles, copy → `copy` variables (name the layer `t:` / `t+:` / `cms:` / `data:`).
5. A bound text that shows a stale string usually has a static override on the owning instance's
   TEXT property (Button `Label`, header `Overline`): bind the property itself.
6. After binding a paint to a variable through the plugin API (`setBoundVariableForPaint`),
   restore the paint's opacity — the call resets it to 100 %.
7. Replaced frames are hidden and renamed „· OLD (hidden)“, not deleted.
8. One agent writes to the file at a time.
9. A finished change reaches the Jira-linked section by replacing the contents of the matching
   frame (ids survive), then a wrap check in `de` mode. Kit masters are shared by both sections:
   a visible change to a master appears in the Jira-linked frames immediately.
10. Layer names: English, by role (Stack, Row, Card, Content, Section, Actions…); no `Frame 123`.

## 10. Known drift and open questions

The critic reports these as known debt or `decision-needed`, not as new findings on every screen.

**Decided, not yet in Figma** (state on 2026-11-15; the mechanical pass of 2026-11-10 bound tokens,
colours, radii and names on loose layers of the working section only):

- Kit: Display 22 / 24 / 30 text styles and the three effect styles do not exist; the `SectionHeader`
  master still shows an UPPERCASE overline 11 and a Poppins SemiBold 18 title — the decided look
  (`Body S` 14, sentence case, `text/secondary`, inset 16) exists only as overrides on the screens,
  and the gap to the card is 12 in places; `BottomSheet` bottom padding is 24; `Button` still has `Shape=rounded` and
  `CardAction` exists; `SelectionRow` has no compact r16 variant and its selected outline is 2;
  `BottomSheet` lacks full-height list, filter row, empty result and stacked-sheet states;
  `OrderTimeline` is not built; `AppHeader · flow-center` still exists; `NavBar` title and texts in
  `NavMenu`, `HowItWorks`, `ActivePlanCard` have no style (decided: `H5` with steps, `Title 20 · Medium`
  without); `ProductCard` link lost its underline; the effect styles card / bottom bar / floating are
  not created.
- Screens: about 200 cards are flat (no outline, no shadow); Order detail 03d / 03e keep section
  headings inside cards; Plans and Notifications still use the large left title (`AppHeader`);
  Order detail 03 / 04 / 05 and Uber build their header by hand; 17 bottom sheets are loose frames;
  Mix 1–3 and V22 keep the CTA or order bar outside `StickyBottomBar`; Mix 3 address fields are
  remote `input`; Mix 1 dosage is a segmented switch; FAQs on Home / V22 / Mix 3 / Category are not
  `AccordionItem`; section gaps of 20 / 24 / 48 remain; headings of 26 px remain; ≈ 455 loose
  texts have no style; ≈ 60 links inside instances are not underlined; 18 in-card buttons have
  radius 12; the hand-built bottom sheets show a grabber (decided: none); Order 03d and the
  copied-number toast screen show a 4-step order progress (decided: 6); the rating widget has
  fractional sizes 10–14 (decided: round to the scale, keep bold).
- The questionnaire exit („…“ menu + leave dialog, decided 2026-11-11) is drawn on one board only;
  the menu is a mock, not a kit component, and the steps do not have it yet.
- The Jira-linked section `4292:24466` has none of the 2026-11-10 changes yet. Its Home copy
  `4292:29906` has a duplicate „10 € sichern“ block under the rating; the working frame `4041:12277`
  is right, the block goes at the next sync.
- Layout bugs visible only in German: Plan row link shows „Change“ instead of „Ändern“ (static
  instance property), Category FAQ question overlaps the answer.
- Code (`dr-abc-ui`) is not synced with any decision after 2026-11-03.

**Open questions for the owner** (numbered in `design-decisions.md`; Q1–Q7, Q9 and Q12 were
answered on 2026-11-15, Q8 on 2026-11-17): Home
layout and category deck (Q10, decided in its own thread) · German copy for `t+` keys (Q11,
copywriter).
