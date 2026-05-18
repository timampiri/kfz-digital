# KFZ Digital Design System

Canonical reference for all three pages (b2c.html, b2b.html, partner.html). All tokens are defined in CSS custom properties at the root of each page; this document is the source of truth for their values and usage.

---

## Color Tokens

| Token | Value | Usage |
|-------|-------|-------|
| `--ink` | `#111110` | Primary text, headings, dark elements |
| `--ink-2` | `#2a2a28` | Secondary text, slightly lighter than --ink |
| `--muted` | `#6e6b66` | Tertiary text, disabled states, metadata |
| `--muted-2` | `#9a9690` | Lighter muted text, placeholders |
| `--line` | `#e6e3dd` | Borders, dividers, hairlines |
| `--paper` | `#f6f3ee` | Light background, hover states |
| `--paper-2` | `#efeae2` | Slightly darker paper, secondary backgrounds |
| `--white` | `#ffffff` | Pure white, card backgrounds, overlays |
| `--accent` | `#e85a3c` | Primary action color (coral), highlights |
| `--accent-2` | `#f3a25e` | Secondary accent (amber), warm highlights |
| `--accent-deep` | `#9d2d20` | Dark accent, hover states on coral |
| `--good` | `#3d9a6c` | Success, positive outcomes (teal) |
| `--warn` | `#d8a93a` | Warnings, caution states (gold) |
| `--bad` | `#d8553a` | Errors, destructive actions (red) |

---

## Spacing & Shape Tokens

| Token | Value | Usage |
|-------|-------|-------|
| `--r-lg` | `20px` | Large border radius (cards, large buttons) |
| `--r-md` | `12px` | Medium border radius (inputs, smaller components) |
| `--r-sm` | `8px` | Small border radius (subtle elements) |
| `--max` | `1240px` | Max content width (wraps) |

---

## Typography

### Font Families
- **Geist** (primary): All body copy, buttons, labels, UI text
  - Weights: 300, 400, 500, 600, 700
  - System fallbacks: `ui-sans-serif, system-ui, -apple-system, Helvetica, Arial, sans-serif`
- **Geist Mono** (eyebrows, labels, code): Uppercase labels, eyebrows, small labels
  - Weights: 400, 500
  - System fallbacks: `ui-monospace, Menlo, monospace`
- **Instrument Serif** (accents): Serif headings, accent typography
  - Weights: 400, 400 italic
  - System fallbacks: `Georgia, serif`

### Heading Scale
```css
h1 { font-size: clamp(40px, 5.4vw, 72px); line-height: 1.02; letter-spacing: -0.035em; }
h2 { font-size: clamp(28px, 3.4vw, 46px); line-height: 1.05; letter-spacing: -0.028em; }
h3 { font-size: 20px; line-height: 1.25; }
```

### Global Typography Rules
- Body line-height: 1.45
- Headings: `letter-spacing: -0.02em` (tightened)
- `text-wrap: balance` on headings
- `text-wrap: pretty` on body text
- Font feature settings: `ss01, cv11` (Geist stylistic sets)
- Antialiasing: `-webkit-font-smoothing: antialiased`

### .eyebrow utility class
- Font: Geist Mono, 11px, uppercase
- Letter-spacing: 0.14em
- Padding: 6px 10px
- Border: 1px solid var(--line)
- Border-radius: 999px (pill)
- Background: #fff
- Display: inline-block

---

## Utility Classes

| Class | Purpose |
|-------|---------|
| `.mono` | Apply Geist Mono font |
| `.serif` | Apply Instrument Serif font |
| `.eyebrow` | Small uppercase label with border pill |
| `.wrap` | Max-width container (var(--max)), centered, 28px padding |

---

## Components

Every reusable component used across the three landing pages, grouped by scope. Each entry shows a minimal copy-pasteable HTML snippet and the key classes that drive it.

### Shared across all three pages

#### Floating Nav

Dark glass pill bar fixed near the top. Used on every page.

```html
<div class="nav-wrap">
  <nav class="nav">
    <a class="brand" href="#"><span class="brand-mark"></span>Kennzeichen<small>for Business</small></a>
    <div class="nav-tabs"><button class="is-active">Tab</button><button>Tab</button></div>
    <div class="nav-right"><a class="btn btn-ghost">Login</a><a class="btn btn-primary">CTA <span class="arr">→</span></a></div>
  </nav>
</div>
```

- `.nav-wrap` is the positioning shell; `.nav` is the dark pill
- `.brand-mark` is the logo glyph; `<small>` after brand text for sub-label
- `.nav-tabs` holds clickable/tab buttons; `is-active` marks the current tab
- `.nav-right` aligns CTAs to the far right; can include language toggle

#### Section wrappers

```html
<section><div class="wrap">...</div></section>
<section class="section-paper"><div class="wrap">...</div></section>
<div class="section-head"><span class="eyebrow">— Label</span><h2>Heading</h2><p>Lead text.</p></div>
```

- Plain `<section>` uses white background; `.section-paper` paints `--paper` warm off-white
- `.wrap` enforces `--max` width and 28px gutters
- `.section-head` is the standard intro block (eyebrow + heading + lead paragraph)

#### Buttons

Base `.btn`: 11px 16px padding, 999px (pill) radius, 14px/500 type, `inline-flex` with 8px gap, 0.15s transitions on transform/background/color/border. `.arr` icons translate +2px on hover.

```html
<a class="btn btn-primary">Become a partner <span class="arr">→</span></a>
<a class="btn btn-coral">Apply now <span class="arr">→</span></a>
<a class="btn btn-ghost">Download info sheet</a>
<a class="btn btn-light">Secondary action</a>
```

| Variant | Background | Text | Hover |
|---------|------------|------|-------|
| `.btn-primary` | `var(--ink)` | `#fff` | `#000` |
| `.btn-coral` | `var(--accent)` | `#fff` | `#d54a2d` |
| `.btn-ghost` | transparent + 1px border | `var(--ink)` | `var(--paper)` |
| `.btn-light` | `#fff` + 1px border | `var(--ink)` | `var(--paper)` |

#### Eyebrow Label

```html
<span class="eyebrow">— Section label</span>
```

- Geist Mono, 11px uppercase, 0.14em tracking, pill border (`var(--line)`), white background
- The leading `— ` em-dash is convention, not enforced by CSS

#### FAQ Accordion

```html
<div class="faq-list">
  <details class="qa" open>
    <summary>Question text<span class="pl">+</span></summary>
    <div class="ans">Answer paragraph.</div>
  </details>
</div>
<div class="faq-support">
  <div class="stack-av"><span class="av">JM</span><span class="av b">RP</span><span class="av c">SL</span></div>
  <div class="text"><b>Have more questions?</b><span>Talk to our partner team</span></div>
  <a class="btn btn-coral">Contact <span class="arr">→</span></a>
</div>
```

- `details.qa` is a native disclosure; `<summary>` carries the question, `.pl` is the +/− indicator
- `.faq-support` is the optional support block (avatars + contact CTA) shown alongside the list
- `.stack-av` arranges overlapping avatar circles; variants `.av.b`, `.av.c` cycle accent shades

#### Steps List

```html
<ol class="steps-list">
  <li>
    <span class="n">01</span>
    <div><div class="h">Step heading</div><div class="d">Step description.</div></div>
  </li>
</ol>
```

- `.n` is the large numeric marker; `.h` is the bold step heading; `.d` is the description
- Use for any numbered process (onboarding, "how it works", partner application)

#### Compare Cards

```html
<div class="compare-grid">
  <div class="compare-card featured">
    <span class="tag coral">Recommended for most</span>
    <h3>Option name</h3>
    <p>Short pitch.</p>
    <ul class="compare-list"><li>Bullet</li><li>Bullet</li></ul>
  </div>
  <div class="compare-card"><span class="tag">High volume</span><h3>Alternative</h3>...</div>
</div>
```

- `.featured` lifts the recommended card visually
- `.tag` is the small label pill; `.tag.coral` adds emphasis
- `.compare-list` is a bullet list scoped to compare cards

#### Footer

```html
<footer>
  <div class="foot">
    <div><a class="brand">...</a><p class="blurb">One-line description.</p></div>
    <div><h4>Column heading</h4><ul><li><a href="#">Link</a></li></ul></div>
    <div><h4>...</h4><ul>...</ul></div>
    <div><h4>...</h4><ul>...</ul></div>
  </div>
  <div class="foot-bottom"><span>© 2026 KFZ Digital GmbH · …</span><span><a>Impressum</a><a>Datenschutz</a></span></div>
</footer>
```

- `.foot` is a 4-column grid (brand blurb + 3 link columns)
- `.foot-bottom` is the legal/copyright strip beneath

---

### B2C-specific (b2c.html)

#### Search Box

```html
<div class="search-box">
  <input type="text" placeholder="Enter city or postal code">
  <button class="btn btn-coral">Find options <span class="arr">→</span></button>
</div>
```

- Input + coral CTA in a single rounded shell; lives in the B2C hero

#### City Chips

```html
<div class="city-chips">
  <button onclick="selectCity('Bremen', '28')">Bremen (28)</button>
  <button onclick="selectCity('Hamburg', '20')">Hamburg (20)</button>
</div>
```

- Quick-select buttons rendered as pill chips, sitting under the search box

#### Search Result Card

```html
<div class="search-result found">
  <div class="search-result-content">
    <div class="search-result-text"><h3>Partner name</h3><p>Address · distance</p></div>
  </div>
  <div class="search-result-cta"><button class="btn btn-coral">View details</button></div>
</div>
<div class="search-result notfound">...</div>
```

- Two states: `.found` (partner returned) and `.notfound` (fall back to online)
- `.search-result-cta` aligns one or two CTAs to the right

#### Doc Cards

```html
<div class="docs-grid">
  <div class="doc-card">
    <div class="ico">📋</div>
    <div class="nm">Document name</div>
    <div class="d">One-line description.</div>
  </div>
</div>
```

- Used for the "What you'll need" checklist; `.ico` is the icon slot (emoji or inline SVG)

#### B2B Promo Band

```html
<div class="b2b-band">
  <h3>Are you a registration service or dealership?</h3>
  <p>KFZ Digital for Business — list your location, process registrations.</p>
  <a href="b2b.html" class="btn" style="background:#fff;color:var(--ink)">Learn more <span class="arr">→</span></a>
</div>
```

- Coral radial-gradient panel that funnels B2C visitors over to the B2B page

#### Form Modal

```html
<div class="modal-backdrop" id="formModalBackdrop">
  <div class="modal" id="formModal">
    <button class="modal-close">×</button>
    <h2>Modal heading</h2>
    <div class="progress-dots" id="progressDots"></div>
    <form><div class="form-group"><label>Field</label><input></div></form>
  </div>
</div>
```

- `.modal-backdrop` is the scrim; `.modal` is the dialogue panel
- `.progress-dots` renders the multi-step indicator; `.form-group` wraps each label+input

#### FAQ Topic Tabs

```html
<div class="faq-topic-tabs">
  <button class="faq-topic-btn is-active">Getting started</button>
  <button class="faq-topic-btn">Online process</button>
</div>
<div class="faq-list" data-faq-topic="general">...</div>
```

- Tab strip placed above the FAQ list; `data-faq-topic` switches which list is visible

#### Split Layout

```html
<div class="split">
  <div class="split-img">
    <div class="split-pills"><span class="pill"><span class="ico"></span>Pill text</span></div>
  </div>
  <div><span class="eyebrow">— Label</span><h2>Heading</h2><p class="lead">Lead.</p>...</div>
</div>
```

- 2-column band: visual on one side, content on the other
- `.split-img` accepts a CSS gradient background; `.split-pills` overlays floating pill captions

---

### B2B-specific (b2b.html)

#### Feature Cards Grid

```html
<div class="feature-grid">
  <div class="fcard chart-card">
    <div class="head"><span class="ttl">Card title</span><span class="seg"><b>1M</b><span>3M</span></span></div>
    <div class="figure">142 / month<b>+24 new partners</b></div>
    <svg class="chart" viewBox="0 0 600 140">...</svg>
    <div class="meta"><div class="h">Caption heading</div><div class="d">Caption description.</div></div>
  </div>
  <div class="fcard dark">...</div>
</div>
```

- `.fcard` is the base card; modifiers: `.chart-card`, `.auto-card`, `.donut-card`, `.user-card`, `.dark`
- `.head` is the card top bar; `.figure` is the big stat; `.meta` is the bottom caption block

#### Logo Strip

```html
<div class="logos">
  <div class="lbl">Trusted by partner points across Germany</div>
  <div class="logos-row">
    <span class="lg"><svg>...</svg>Bremen Zentrum</span>
    <span class="lg"><svg>...</svg>Nordwest Auto</span>
  </div>
</div>
```

- `.lbl` is the small caption above the row; each `.lg` pairs an inline SVG glyph with a name

#### Testimonial

```html
<div class="testi">
  <div class="stat"><div class="big">+62%</div><div class="lbl">more registrations<br>after joining</div></div>
  <div class="photo"><span class="caption">Bremen-Mitte · 2024</span></div>
  <div class="quote">
    <div><span class="eyebrow">— Testimonial</span><blockquote>"Quote text."</blockquote></div>
    <div class="who"><b>Name</b><br><span>Role, company</span></div>
  </div>
</div>
```

- 3-column grid: numeric stat · photo placeholder · pull quote with attribution

#### Pricing Cards

```html
<div class="pricing">
  <div class="price-card">
    <div class="tier">Tier name</div>
    <div class="blurb">One-line pitch.</div>
    <div><div class="price">€5</div><div class="seat">per registration processed</div></div>
    <a href="#" class="btn">Apply <span class="arr">→</span></a>
  </div>
  <div class="price-features">
    <span class="eyebrow">What's included</span>
    <ul><li><span class="ic"></span><div><b>Feature</b><span>Detail.</span></div></li></ul>
  </div>
</div>
```

- `.price-card` is the price summary; `.price-features` is the inclusions list paired alongside

#### Code Block

```html
<pre class="code-card"><span class="cc">// Comment</span>
{
  <span class="ck">"key"</span>: <span class="cv">"keyword-value"</span>,
  <span class="ck">"string"</span>: <span class="cs">"literal-string"</span>
}</pre>
```

- Syntax tokens: `.ck` key, `.cv` keyword/identifier, `.cs` string literal, `.cc` comment
- Used in the Platforms & API tab to show sample requests/responses

#### CTA Bar

```html
<div class="cta-bar">
  <div><div class="t">Ready to become a partner point?</div><div class="s">Application takes 5 minutes.</div></div>
  <div><a class="btn btn-ghost">Download info sheet</a><a class="btn btn-coral">Apply now <span class="arr">→</span></a></div>
</div>
```

- Inline conversion bar at the end of a section: copy on the left, button group on the right

#### Big CTA

```html
<div class="bigcta">
  <div class="bigcta-grid">
    <div><div class="bigcta-eyebrow">— All audiences</div><h2>Heading.</h2><p>Body.</p><a class="btn btn-primary">CTA <span class="arr">→</span></a></div>
    <div class="bigcta-mock">
      <div class="tabbar"><div class="dots"><i></i><i></i><i></i></div><span>kennzeichen.de</span></div>
      <div class="kpis"><div class="kpi"><div class="l">Label</div><div class="v">Value</div></div></div>
    </div>
  </div>
</div>
```

- Closing section that pairs a large pitch with a stylised browser-window mock + KPIs

#### Dashboard Mock

```html
<div class="stage-mock">
  <div class="stage-mock-head"><div class="dots"><i></i><i></i><i></i></div><span class="url">partner.kennzeichen.de</span><span class="badge">● Live</span></div>
  <div class="stage-mock-title">Today's registrations<span class="mut">12 active</span></div>
  <div class="stage-mock-row"><span class="av">MS</span><div><div class="nm">Customer name</div><div class="pl">HB · KD · 4471</div></div><span class="pill g">Approved</span></div>
</div>
```

- Browser-chrome wrapper (`.stage-mock-head`) + table-like rows of fake registrations
- `.pill` status variants: `.g` green/approved, `.w` warn/pending, default = neutral

---

### Partner-specific (partner.html)

#### Topbar

```html
<div class="topbar">
  <div class="topbar-left">
    <div class="topbar-item"><svg>...</svg><a href="tel:...">0421 ...</a></div>
    <div class="topbar-item"><svg>...</svg><a href="mailto:...">info@…</a></div>
    <div class="topbar-item"><svg>...</svg><span>Mon–Fri 07:00–17:00</span></div>
  </div>
  <div class="right">KFZ Digital certified partner · Bremen</div>
</div>
```

- Thin contact strip pinned above the nav; phone / email / hours / partner badge

#### Partner Hero Grid

```html
<header class="hero">
  <div class="hero-grid">
    <div>
      <!-- hero pills, h1, sub, CTAs, hero-stats -->
    </div>
    <aside class="info-card">...</aside>
  </div>
</header>
```

- 2-column hero: left-aligned text content + sticky `.info-card` sidebar on the right

#### Hero Pills

```html
<div class="hero-pills">
  <span class="hero-pill"><svg>...</svg>Bremen · Falkenweg 16</span>
  <span class="hero-pill status"><span class="dot"></span><span class="status-text">Open now</span></span>
  <span class="hero-pill partner"><svg>...</svg>KFZ Digital partner</span>
</div>
```

- Variants: default location pill, `.status` with animated `.dot`, `.partner` branded chip

#### Hero Stats Row

```html
<div class="hero-stats">
  <div class="stat"><div class="stat-lbl">Turnaround</div><div class="stat-val">~24h</div></div>
  <div class="stat"><div class="stat-lbl">No appointment</div><div class="stat-val">Walk-in</div></div>
</div>
```

- 4-column bordered grid of metric label + value pairs

#### Info Card

```html
<aside class="info-card">
  <div class="info-card-head"><h3>Office information</h3><p>Walk in Mon–Fri</p></div>
  <div class="info-rows">
    <div class="info-row"><span class="info-row-icon"><svg>...</svg></span>
      <div><div class="info-row-lbl">Address</div><div class="info-row-val">Falkenweg 16<br>28865 Lilienthal</div></div>
    </div>
  </div>
  <div class="map-box"><svg>...</svg><span>MAP — FALKENWEG 16</span></div>
  <div class="info-card-cta"><a class="btn btn-coral">Book <span class="arr">→</span></a></div>
</aside>
```

- Sticky sidebar with dark gradient header, info-row list, map placeholder, CTA cluster

#### Booking Form

```html
<div class="booking-grid">
  <div><span class="eyebrow">— Get started</span><h2>Book in 60s.</h2><p class="lead">…</p><div class="meta-list">...</div></div>
  <div class="booking-card">
    <div class="booking-card-head"><h3>Book an appointment</h3><p>We'll confirm by phone.</p></div>
    <div class="booking-form"><div class="form-group"><label>Full name</label><input></div>...<button class="btn btn-coral">Send request</button></div>
    <div class="form-success"><div class="tick">✓</div><div class="h">Request received</div><div class="d">…</div></div>
  </div>
</div>
```

- 2-column: pitch on the left, form card on the right; `.form-success` overlays on submit

#### Services Grid

```html
<div class="service-grid">
  <div class="service-card featured">
    <span class="ico"><svg>...</svg></span>
    <div class="row-top"><h3>Neuzulassung</h3><span class="tag coral">Most popular</span></div>
    <p>Service description.</p>
    <div class="price">From €79 + official fees</div>
  </div>
  <div class="service-card">...</div>
</div>
```

- `.featured` adds the highlighted treatment; `.tag.coral` / `.tag.green` flag service status

#### Notice

```html
<div class="notice info"><div class="inner"><svg>...</svg><span>Informational message.</span></div></div>
<div class="notice warn"><div class="inner"><svg>...</svg><span>Heads-up about delays.</span></div></div>
```

- Two flavours: `.info` (neutral) and `.warn` (gold). `.inner` aligns icon + text horizontally

#### Pricing Table

```html
<table class="price-table">
  <thead><tr><th>Service</th><th>Our fee</th></tr></thead>
  <tbody>
    <tr>
      <td><div class="name">Neuzulassung <span class="tag coral">incl. plates</span></div><div class="desc">New registration including plate embossing</div></td>
      <td class="amt coral">€79</td>
    </tr>
  </tbody>
</table>
```

- Standard HTML table with custom typography; `.amt.coral` highlights the headline price

#### Reviews

```html
<div class="review-summary">
  <div><div class="review-score">4.8</div><span class="stars">★★★★★</span><div class="review-score-lbl">350+ reviews</div></div>
  <div class="review-breakdown">
    <div class="review-bar-row"><span class="lbl">5★</span><div class="review-bar-track"><div class="review-bar-fill" style="width:82%"></div></div><span class="pct">82%</span></div>
  </div>
  <div class="review-trust"><span class="trust-pill"><svg>...</svg>Top Dienstleister 2025</span></div>
</div>
<div class="reviews-grid">
  <div class="review-card"><span class="stars">★★★★★</span><blockquote>"Quote."</blockquote><div class="who">Name</div><div class="when">Date · Source</div></div>
</div>
```

- `.review-summary` is the aggregate; `.reviews-grid > .review-card` lists individual reviews

#### Nearby Partners

```html
<div class="nearby-wrap">
  <a class="nearby-card" href="#">
    <div class="nearby-num">1</div>
    <div><div class="nearby-name">KFZ Digital Hamburg</div><div class="nearby-meta">Grindelallee 45, Hamburg</div></div>
    <div class="nearby-dist">74 km</div>
  </a>
</div>
```

- Compact horizontal cards listing other partner locations with rank + distance

---

## Figma Workflow

**Figma file ID:** `FD0JCQoy6e9CJ99HEFbqrd`

The Figma MCP server is connected to Claude Code. That means components designed in Figma can be implemented directly in HTML without copy-pasting specs by hand.

### Designing a new component

1. Build the component in the Figma file linked above.
2. Right-click the frame → **Copy link** to capture the node URL.
3. In Claude, say: _"Implement the [component name] from Figma"_ and paste the URL.
4. Claude reads the design via `get_design_context` and writes the HTML/CSS using the tokens defined in this file — no new hex values, no improvised spacings.

### Fetching a Figma frame

Say: _"Show me the [frame name] from the KFZ Digital Figma file"_ — Claude uses `get_screenshot` to render the frame inline so you can review it without leaving the editor.

### Comparing design vs. implementation

Say: _"Compare the b2c.html hero against the Figma hero frame"_ — Claude reads both, lists the deltas (spacing, copy, colour usage), and proposes fixes.

### Rules

- Components built from Figma must use this file's existing colour, spacing, and typography tokens. Never introduce raw hex values or new spacing scales.
- If a Figma design implies a new token, surface that explicitly in the response and update this file _before_ writing any HTML.
- Use the canonical `:root` block in `b2b.html` as the CSS source when copying tokens into a new page.

---

## Notes

- **Responsive:** Headings use `clamp()` for fluid scaling; mobile viewport respected
- **Dark Mode:** Not included in launch (light-mode only per constraints)
- **Accessibility:** 4.5:1 contrast minimum on all text; never rely on color alone for meaning
- **Performance:** All styles inline in `<style>` blocks; no external CSS files
- **Language:** Designed for both English (current) and German (future localization)

---

## V1 Components (b2c.html — added 2026-05-16)

New component classes introduced when implementing the Figma V1 design (file `AQZXgQZYUAHJsZiwD0x9Va`, node `1:231`). All live in `landing/design-system.css` after the existing `@media` blocks; all reuse existing tokens (no new hex / spacing values).

| Component | Class(es) | Used in |
|---|---|---|
| Hero secondary line | `.hero-secondary` | b2c hero — "No partner nearby? Register online instead →" under city-chips |
| 4-column compare table | `.compare-wrap`, `.compare-table` (table-based), `.is-primary`, `.row-label`, `.compare-ctas` | b2c compare — Local partner (highlighted) · Fully online · Registration office |
| Rating band | `.rating-band`, `.rating-stars`, `.rating-stars-row`, `.rating-score`, `.rating-meta` | b2c reviews header (4.8/5 + meta line) |
| 3-up reviews grid | `.reviews-grid--3up` (modifier on existing `.reviews-grid`) | b2c — Trustpilot-style customer quotes |
| FAQ contact card | `.faq-contact-card`, `.faq-contact-avatars`, `.faq-avatar`, `.faq-contact-text`, `.faq-contact-title`, `.faq-contact-sub` | b2c FAQ left column — 3 stacked avatars + "Have more questions?" CTA |
| Shared big CTA | `.shared-cta`, `.shared-cta-copy`, `.shared-cta-eyebrow` | b2c bottom — dark gradient panel, "Three audiences. One platform." |
| KPI grid (2×2) | `.kpis`, `.kpi`, `.kpi-value`, `.kpi-label` | b2c shared CTA right column — 120+ / 50,000+ / 16 / <15 min |

**Skipped from Figma deliberately:** Pricing card section (`.pricing-layout`, `.price-primary`, `.price-secondary`) — pricing stays off the b2c landing per Denis's review ("remove the price").

**Backup of pre-V1 versions:** `landing/archive/v1-backup-2026-05-16/`.

---

## V2 Components (city / Zulassungsstelle / directory — added 2026-05-17)

Scaffolded as part of the kfzdigital.de redesign (May 15 V1 review). The site pivots into an SEO-driven traffic-routing hub: PLZ search → city page (with partner cards) OR no-partner fallback (redirect to kennzeichenmax.de). Four new pages added: `city.html`, `cities.html`, `zulassungsstelle.html`, `zulassungsstellen.html`.

### New tokens

| Token | Value | Why |
|---|---|---|
| `--gov` | `#2d4f8d` | Official government office (Zulassungsstelle) accent. Visually distinct from `--accent` (coral = commercial partner) so public/private content reads at a glance. |
| `--warn-deep` | `#8a6c1f` | Darker amber for text contrast on warn-tinted backgrounds (e.g. "no partner yet" badge). |

### Component reference

| Component | Class(es) | Used in |
|---|---|---|
| Breadcrumb | `.breadcrumb`, `.sep`, `.current` | All detail pages above hero |
| Variant divider | `.variant-divider`, `.badge` | `city.html` only — separates Variant A (with partner) from Variant B (no partner). Template-only marker; removed when splitting into per-city files. |
| City hero | `.city-hero`, `.city-meta`, `.region`, `.partner-count` (`.none` variant) | `city.html`, `cities.html`, `zulassungsstellen.html` |
| PLZ re-search bar | `.city-research` | `city.html` hero — compact postal-code input lets users re-search without going home |
| Partner card (mini) | `.partner-list`, `.partner-card-mini`, `.pcm-head`, `.pcm-name`, `.pcm-badge`, `.pcm-meta`, `.pcm-hours`, `.pcm-cta` | `city.html` Variant A — slim 320px+ cards listing local partners (name, address, phone, hours, rating, CTA) |
| No-partner fallback | `.no-partner-fallback`, `.nf-card`, `.nf-icon`, `.nf-ctas`, `.nf-divider`, `.nf-sec` | `city.html` Variant B, `cities.html` bottom — prominent CTA to kennzeichenmax.de when no local partner |
| Zulassungsstelle summary | `.zs-summary`, `.zs-summary-card`, `.zs-icon`, `.zs-body`, `.zs-eyebrow`, `.zs-name`, `.zs-addr`, `.zs-cta` | `city.html` — single-row link to the city's official office detail page |
| Gov badge | `.gov-badge`, `.gov-badge .dot` | `zulassungsstelle.html` hero, `zulassungsstellen.html` hero — marks content as official. Uses `--gov` token. |
| Gov info card | `.gov-info-card`, `.gic-head`, `.gic-name`, `.gic-rows`, `.gic-row` (`.lbl` / `.val`), `.gic-hours`, `.gic-cta` | `zulassungsstelle.html` sticky sidebar — like `.info-card` but no booking form, links to gov.de instead |
| Gov services list | `.gov-services-list` | `zulassungsstelle.html` — services offered grid (deregistration, owner enquiry, short-term plates…) with `--good` checkmarks |
| Zulassungsstelle detail layout | `.zs-detail-grid`, `.zs-side` | `zulassungsstelle.html` — 1fr / 360px columns; sticky right sidebar |
| Faster-partners CTA | `.faster-partners`, `.fp-head`, `.fp-eyebrow`, `.fp-sub` | `zulassungsstelle.html` — "Skip the queue" section bridging users back to partner cards |
| City card | `.city-grid`, `.city-card`, `.cc-head`, `.cc-name`, `.cc-region`, `.cc-foot`, `.cc-count` (`.none` variant), `.cc-arrow` | `cities.html` — directory grid item with partner-count badge or "Online only" |
| Directory search | `.directory-search` | `cities.html`, `zulassungsstellen.html` — pill-shaped filter bar |
| Alpha index | `.alpha-index` | `cities.html` — A–Z jump nav; `.disabled` for letters with no entries |
| Region group | `.region-group`, `.rg-head`, `.rg-name`, `.rg-count`, `.office-list` | `zulassungsstellen.html` — Bundesland heading |
| Office row | `.office-row`, `.or-body`, `.or-name`, `.or-city`, `.or-arrow` | `zulassungsstellen.html` — slim list item linking to office detail |

### Reused existing components

City and Zulassungsstelle pages also use: `.nav-wrap` / `.nav` (shared dark glass nav), `.faq` accordion, `.eyebrow`, `.btn-coral` / `.btn-ghost`, `.section-paper`, `.notice.info` / `.notice.warn` (existing), and the standard `footer` block.

### Existing-page modifications (Phase 2 of redesign)

- **b2c.html** — pricing pill ("€16.30 only") replaced with delivery-speed value prop; FAQ entry on pricing reframed (no concrete prices); modal step removed concrete fee figures; footer "Pricing" link replaced with links to `cities.html` and `zulassungsstellen.html`; nav gains Cities + Offices links; "Find a partner" CTA wired to `cities.html`; search-results refactored to link to `city.html#{slug}` (and use safe DOM methods instead of `innerHTML` for the search-result and fallback cards — fixes a latent XSS vector while removing innerHTML).
- **b2b.html** — Zulassungsdienste hero reframed as "Become a partner — process registrations in 15 minutes"; new 6-row comparison table inserted (KFZ Digital partner / Traditional Zulassungsstelle / Fully online) leading the tab; Dealerships sub-copy updated to emphasise white-label microsite and basic site-building tools.
- **partner.html** — back-link points to `city.html#bremen` (was `b2c.html`); "Nearby partners" link to "Find all partner locations" replaced with link to `cities.html`. Pricing inside the partner's own pricing table and service cards retained — it's the partner's own page where prices are appropriate.

**Backup of pre-V2 versions:** `landing/archive/pre-v2-backup-2026-05-17/`.
