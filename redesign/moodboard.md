# UI Inspiration Moodboard — KFZ Digital Redesign

## Context

We have locked the brand direction in `projects/KFZ Digital/redesign/LOGO_BRIEF.md`:
- **Archetype**: Magician × Sage (frictionless + authoritative)
- **Voice**: calm, confident, precise — *quietly German*
- **Owned word**: precision
- **Aesthetic family**: Linear / Vercel / Braun / Porsche Design — not Wise/Revolut/Monzo
- **Palette**: warm off-white `#F6F5F2`, ink `#0E1116`, single signal blue `#1E5BFF` (EU-plate-derived)
- **Typography**: PP Neue Montreal / Söhne / Geist — never Inter/Roboto
- **🌞 Mode: light-default, always.** Dark mode is a possible v2 enhancement, not a launch requirement. All inspiration sources below are filtered for their light-mode treatments. Where a reference is famously dark (e.g. Linear), study only their light sections or extract specific patterns rather than aesthetic.

This document curates UI inspiration sources Denis (and any designer we brief) can study before the Figma round begins. Each reference is tagged with *what to steal* and *what to ignore* — generic "look at these cool sites" lists fail because they don't separate the signal from the noise.

---

## Light-Mode Constraint (read first)

KFZ Digital is a regulated consumer service for a mass German audience including older car owners and dealership staff. Light mode is mandatory for launch because:

1. **Trust requirement** — government-adjacent services in Germany skew light (gov.uk, doctolib, check24). Dark default reads "startup", not "official partner".
2. **Daylight readability** — partners use this at the counter under harsh fluorescent lighting; dark mode washes out.
3. **Print fidelity** — receipts, registration confirmations, and PDF exports must look right; light mode is the source of truth.
4. **Accessibility** — older users (50+, a significant share of car-registration users) have a documented preference for light-on-dark text.

**The constraint**: surfaces are warm off-white `#F6F5F2`, text is ink `#0E1116`, signal blue `#1E5BFF` is used sparingly for accents and the plate motif. No dark hero sections. No black backgrounds anywhere on launch.

---

## Tier 1: Aesthetic North Stars (overall feel)

The 4–5 sites whose *overall vibe* should feel native to KFZ Digital.

### 1. linear.app *(study light-mode sections only)*
- **Steal**: Calm confidence; macro-whitespace; tabular figures for stats; the way version-marker eyebrows precede H1s; their pricing page (which is light)
- **Ignore**: The dark hero — we need warm-off-white as the default surface; the fully geometric "L" mark

### 2. vercel.com *(mixed light/dark — study light sections)*
- **Steal**: Off-white surfaces in their docs and pricing; Geist typography; minimal mark; the way "Powered by" lockups work for sub-brands (useful for partner co-branding)
- **Ignore**: Their dark homepage hero; black-and-white extremism — we need our signal blue to carry emotional weight

### 3. attio.com *(light default ✅)*
- **Steal**: Editorial split layouts; the comparison-vs-incumbent (vs Salesforce) page pattern — direct template for our "vs Registration Office" section; soft ambient shadows on light surfaces
- **Ignore**: CRM-specific language; their density of feature callouts

### 4. mercury.com *(light default ✅, replaces arc.net)*
- **Steal**: Quietly authoritative light-mode banking aesthetic; trust signals on warm-cream surfaces; pricing transparency; how they handle compliance without looking bureaucratic — *closest aesthetic analog we have*
- **Ignore**: US banking language; the gradient hero (subtler than ours should be)

### 5. things.app (Cultured Code) *(light default ✅, replaces raycast.com)*
- **Steal**: The quiet authority of the wordmark; Stuttgart engineering feel; how a single product can hold attention without animation; the typographic rhythm
- **Ignore**: To-do-app context; the desktop-software framing

### 6. notion.so *(light default ✅, bonus reference)*
- **Steal**: Mass-consumer light-mode-first SaaS done with restraint; how they handle a wide audience without dumbing down
- **Ignore**: Cute illustrations; the maximalist landing page below the fold

---

## Tier 2: Layout & Component Patterns (specific UI mechanics)

When a designer asks "how do I build *this* section", here are sources for each piece.

### Hero with input-as-conversion
- **stripe.com/payments** — input field placement
- **doctolib.de** — search-as-hero pattern (most directly transferable: same "find a local professional → book" flow we need)
- **opentable.com** — date/location combined input

### Three-pathway "pick your lane" cards
- **stripe.com/pricing** — three-column comparison done with restraint
- **github.com/pricing** — works at scale, accessible
- **kit.com** (formerly ConvertKit) — pathway cards with clear differentiation

### Step-by-step process visualisations
- **stripe.com/atlas** — the way they show "incorporate → bank → tax" as numbered cinematic moments
- **revolut.com/business/start** — multi-step animation, but study mechanics not aesthetic
- **wise.com/help/articles** — step illustrations with restraint

### Trust strip / certification rows
- **vercel.com/customers** — quiet logo row treatment
- **1password.com/security** — compliance badges shown with explanation (steal this for our i-Kfz / KBA / ISO badges)
- **cloudflare.com/trust-hub** — certifications page reference

### Comparison-vs-incumbent table
- **attio.com/vs/salesforce** — direct template for "KFZ Digital vs Registration Office"
- **linear.app/vs/jira** — visual style of the comparison row
- **superhuman.com** (homepage section) — time-saved framing

### Pricing transparency cards
- **basecamp.com/pricing** — radical clarity, single price
- **proton.me/pricing** — three tiers with honest differentiation
- **mercury.com/pricing** — clean cards, no upsell pressure

### City/location finder pages (SEO template)
- **doctolib.de/zahnarzt/berlin** — the gold standard for German location-based landing pages
- **uber.com/global/en/cities/berlin** — local content patterns
- **airbnb.com/berlin** — local SEO + booking conversion combined

### Customer testimonial blocks
- **linear.app** (homepage scrolling testimonials) — restraint
- **height.app/customers** — single testimonial as full section
- **mercury.com/customers** — case study card design

### FAQ accordion done well
- **stripe.com/pricing** (FAQ at bottom)
- **vercel.com/pricing** — visually quiet, fast to scan

### Footer architecture
- **vercel.com** — 4-column with quiet hierarchy
- **stripe.com** — exhaustive but never overwhelming
- **linear.app** — minimal but complete

---

## Tier 3: German / Local Sector References (vocabulary + cultural fit)

Sources that prove the aesthetic translates to a German consumer audience and avoids feeling like a Silicon Valley import.

### Direct domain analogs (booking/registration in Germany)
- **doctolib.de** — the most directly analogous service we have access to: search for local provider, book appointment, partly digital partly in-person. **Study deeply.**
- **check24.de** — Germany's largest comparison site; sets the bar for "trustworthy German consumer service" — note their certification badges
- **verivox.de** — utility comparison; trust signal density

### German design-led sites (aesthetic alignment)
- **teenageengineering.com** — Swedish but reads German-engineering; restraint as branding
- **braun.de** — the source-of-truth for "less but better" — even if their site is dated, the product photography and typography rhythm is the template
- **leica-camera.com** — premium German precision; how to make a heritage brand feel modern without losing weight
- **manufactum.de** — German "good quality" trust signals; editorial product layouts
- **mykeepa.com** — German SaaS done with personality

### German fintech / regulatory-heavy services
- **n26.com** — *study but do not copy aesthetics* — proves a modern brand can win in regulated German space. Note their compliance-page transparency.
- **trade-republic.com** — minimal trust-building; mobile-first
- **finanzfluss.de** — content-led trust; good editorial system

---

## Tier 4: Sector-Adjacent Inspiration

Outside our market but solving structurally similar problems (book a local pro → complete a regulated process).

### Local-pro booking
- **getyourguide.com** — local-product discovery with strong city pages
- **treatwell.de** — beauty bookings in Germany; same "find local + book" flow

### Government/regulated service done premium
- **gov.uk** — accessibility and clarity gold standard
- **estonia.ee/e-residency** — digital-first government service marketed beautifully
- **id.me** — identity verification (analogous to our eID flow), trust messaging

### Insurance and risk-reversal patterns (for our money-back guarantee)
- **lemonade.com** — risk reversal as hero messaging
- **friday-insurance.com** (German) — minimal, modern, regulated

---

## Anti-References (do not steal from)

If a designer cites any of these as inspiration, push back:

| Site | Why not |
|---|---|
| **kennzeichenking.de** | Medieval kitsch — direct competitor we explicitly want to look different from |
| **wise.com** | Specifically banned in the logo brief; over-cited and over-imitated |
| **revolut.com** | Banned; circular monogram + neon aesthetic is the exact "fintech cliché" we reject |
| **monzo.com** | Same; consumer-fintech default skin |
| **uber.com** (homepage) | All-caps wordmark + thick geometric sans — explicitly listed as anti-pattern |
| **Generic Webflow/Framer templates** | "AI-generated SaaS template" feel — death of brand ownership |
| **Tailwind UI default screenshots** | Default-Tailwind aesthetic = looks like every other prototype |
| **Awwwards "agency portfolio" sites with extreme animation** | We are precision, not spectacle |
| **Any dark-default SaaS aesthetic** | Light-mode constraint. If a reference looks great only in dark mode, extract the *pattern* (e.g. Linear's whitespace rhythm) and translate to light surfaces — never copy the dark surfaces themselves. |

---

## How to Use This Moodboard

### For Denis (founder review)
1. Open Tier 1 (5 sites) — within 10 minutes you'll know if the strategic direction resonates
2. If it does → proceed; if it doesn't → we re-discuss positioning before any design work

### For the designer brief packet
1. **Embed full-page screenshots** of Tier 1 + Tier 2 references — not links (designers don't always click)
2. **Annotate each screenshot** with the "what to steal / what to ignore" tags from this doc
3. **Include the anti-references** with red-X annotations on competitor screenshots
4. Pair this doc with `LOGO_BRIEF.md` and `HOMEPAGE_WIREFRAME.md`

### For ongoing reference checks
- When reviewing a draft (Manus, Claude app, Figma, etc.) ask: *which Tier 1 site does this remind me of?*
  - If the answer is "none of them" → the draft is off-brief
  - If the answer is "an anti-reference" → reject
  - If the answer is one of our north stars → refine

### File locations
- This moodboard: `/Users/apple/.claude/plans/what-websites-we-can-inherited-duckling.md` (will be moved into the project)
- **Recommended permanent home**: `projects/KFZ Digital/redesign/UI_INSPIRATION.md`

---

## Verification

This is a research/curation document, not code — verification means:

1. **Denis review**: Open Tier 1 in browser tabs; confirm 3+ of 5 feel aligned with his vision
2. **Designer alignment**: Brief the designer with this doc + LOGO_BRIEF.md; first concepts back should visibly reference 2–3 Tier 1 sources
3. **Anti-reference check**: First-round concepts should *not* resemble any anti-reference (especially default-Tailwind / fintech monogram aesthetics)
4. **Drift monitoring**: As new drafts arrive (Manus, Claude app, etc.), tag each against this list — if drafts repeatedly land outside the moodboard, reinforce briefing
