# KFZ Digital — B2C Landing Page Research Findings

> **Purpose:** Reference document for Claude Code when building the production B2C consumer landing page for kfzdigital.de. Contains verified facts, competitor analysis, UX decisions, and content requirements.

---

## 1. Product Overview

KFZ Digital is a German vehicle registration platform that:
- Connects end consumers to **certified partner registration points** (physical offices)
- Offers **fully online i-Kfz registration** as a fallback when no local partner is available
- Targets **German car owners** who need to register, re-register, transfer ownership, or deregister a vehicle

**Primary B2C goal:** User finds a local partner point or starts online registration within 60 seconds of arriving on the page.

---

## 2. Two Registration Options — Verified Facts

### Option A: Local Partner Service

| Attribute | Detail |
|---|---|
| Service fee | ~€150–200 (partner service fee, excludes authority fees) |
| Authority fees | ~€26–35 (Zulassungsbehörde, billed separately) |
| Turnaround | ~15 minutes on-site |
| eID required | No |
| Vehicle age limit | None — handles pre-2015 vehicles |
| Complex cases | Yes (imported cars, lien, ownership disputes) |
| Physical visit | Required |
| Source | Verified against real operator pricing: DKK24, Zulassung24.berlin, Blue Service Team |

### Option B: Fully Online (i-Kfz)

| Attribute | Detail |
|---|---|
| Registration fee (Neuzulassung) | **€16.30** online vs **€30.60** at the counter |
| Deregistration fee (Abmeldung) | **€2.70** online vs **€16.80** at the counter |
| Authority fees | ~€26–35 (same as in-person) |
| eID required | **Yes** — German Personalausweis with activated online function (or electronic Aufenthaltstitel) |
| Vehicle age limit | Must have security codes in Zulassungsbescheinigung — generally only vehicles registered **after 01.01.2015** |
| Turnaround | **1–3 business days** |
| Physical visit | None |
| App required | AusweisApp2 (iOS/Android) for eID verification |
| Source | Kraftfahrt-Bundesamt (KBA) official fee schedule; Federal Ministry of Transport |

**Key differentiator summary:**
- Local partner: faster on-site, handles complex/old cases, no eID needed, more expensive
- Online: cheapest option (roughly half the counter fee), no office visit, requires German eID and post-2015 vehicle

---

## 3. Hero Section Requirements

### Search behaviour
- **Primary CTA** is a PLZ/city search field — not a button
- On search:
  - **Partner found** → show partner name, address, distance, opening hours, "Get directions" CTA. **Do not show the online option.**
  - **No partner found** → show online registration fallback (Mobegu / Concept MAX) + "Request a partner in [city]" email capture
- Search should fire on input (debounced) and on Enter / button click

### Quick city chips (below search bar)
Display these cities as one-click shortcuts:
- Bremen (PLZ prefix: 28)
- Hamburg (PLZ prefix: 20/21/22)
- Berlin (PLZ prefix: 10/12/13)
- Munich (PLZ prefix: 80/81)
- Frankfurt (PLZ prefix: 60/63)
- Cologne (PLZ prefix: 50/51)

Cities with active partners show green dot; others show "Online only".

### Trust badges (in hero, below search)
Display these four as a horizontal strip:
1. KBA certified · i-Kfz connected
2. DSGVO compliant
3. eID secure
4. All German Zulassungsbezirke

---

## 4. Page Sections (in order)

### 4.1 Hero
- Headline: "Register your car digitally — in 15 minutes"
- Subline: "Find a local registration partner near you, or complete your registration fully online."
- PLZ/city search as primary CTA
- Quick city chips
- Trust badge strip

### 4.2 Trust strip (full-width, below hero)
Five items: KBA certified, DSGVO compliant, eID secure payment, All German Zulassungsbezirke, Official government portal connected

### 4.3 Compare options (two cards)

**Card 1 — Local partner service** (featured/recommended)
- Icon: map pin
- Badge: "Recommended for most"
- Price: ~€150–200 service fee + official fees (~€26–35)
- Features:
  - ✓ Done in ~15 minutes on-site
  - ✓ Handles complex cases (used cars, lien, imported)
  - ✓ No German eID required
  - ✓ Expert guidance through paperwork
  - ✓ Plates can be sorted on the same visit
  - – Requires a physical visit
- CTA: "Find a local partner →" → triggers partner search / opens partner modal

**Card 2 — Fully online**
- Icon: monitor/laptop
- Badge: "Cheapest option"
- Price: €16.30 official fee (new registration) vs €30.60 counter
- Features:
  - ✓ Cheapest option — roughly half the counter fee
  - ✓ No office visits, 24/7 availability
  - ✓ Confirmation sent immediately on approval
  - – Requires German eID (Personalausweis) with online function
  - – Vehicle must have been registered after 01.01.2015
  - – Processing takes 1–3 business days
- CTA: "Start online registration →" → opens registration form

### 4.4 How it works (side-by-side, two columns)

**Column 1 — Local partner (4 steps)**
1. Find a partner near you (search by city/PLZ)
2. Prepare your documents (ZB I & II, ID, eVB, TÜV)
3. Visit the partner office (~15 minutes, no appointment)
4. Drive away (digital confirmation, plates sorted on-site)

**Column 2 — Fully online (4 steps)**
1. Check eligibility (eID card, vehicle post-2015, security codes in ZB)
2. Fill in your details (vehicle data, eVB, address, IBAN for Kfz-Steuer)
3. Verify with eID (AusweisApp2, NFC chip, legally binding)
4. Receive confirmation (1–3 business days, email)

### 4.5 Documents checklist (two columns)

**Always required:**
- Zulassungsbescheinigung Teil I (vehicle registration — kept in car)
- Zulassungsbescheinigung Teil II (title document / Fahrzeugbrief)
- eVB number (7-digit electronic insurance confirmation from insurer)
- Valid ID — Personalausweis or passport with registered German address
- HU/TÜV certificate (current Hauptuntersuchung, not expired)
- IBAN (European bank account, for Kfz-Steuer SEPA direct debit)

**Additional where applicable:**
- COC document (new vehicles — Certificate of Conformity from manufacturer)
- Power of attorney / Vollmacht (if registering on behalf of another person)
- Old plates (deregistration — both front and rear required)
- Handelsregisterauszug (company registrations — commercial register extract)
- Import documents (foreign-registered vehicles — customs clearance + COC)
- Plate reservation PIN (if Wunschkennzeichen reserved online)

### 4.6 FAQ (accordion)
Content reused from existing kfzdigital.de:

1. Can I register my car online if I only have a passport?
   → No. Requires Personalausweis or electronic Aufenthaltstitel with eID function. Passport holders must use a local partner.

2. How long does online registration actually take?
   → 1–3 business days after submission. Not all Zulassungsstellen have fully implemented the digital portal. Local partner: ~15 minutes on-site.

3. Why is online registration cheaper than going in person?
   → German government sets lower fees for i-Kfz to encourage digital uptake. Neuzulassung: €16.30 online vs €30.60 counter. Abmeldung: €2.70 online vs €16.80.

4. My car was registered before 2015 — can I still register online?
   → Probably not via self-service. Pre-2015 vehicles lack security codes needed for i-Kfz. A local partner can still handle it via direct KBA access.

5. What is an eVB number and how do I get one?
   → 7-digit code from your car insurer confirming coverage. Required before any registration. Get it from your insurer — issued within minutes of taking out a policy.

6. Is it safe to send original documents to an online service?
   → Reputable services are official KBA digitisation project members. If uncomfortable sending originals by post, use a local partner instead.

7. What is an eVB number and how do I get one?
   → Electronische Versicherungsbestätigung — 7-digit code from insurer. Required before starting. All German insurers issue these as standard.

8. Can I register online from anywhere in Germany?
   → Yes, if your Zulassungsstelle supports i-Kfz (most do now). Check your district. Local partners cover all districts regardless.

### 4.7 Footer
- Back to kfzdigital.de link
- Legal Impressum: Kfz Digital GmbH · Denis Novakov · In den Freuen 96 · 28719 Bremen · Tel: 042149182511 · Info@kfzdigital.de · USt-IdNr.: DE343815625 · HRB 36819HB
- Links: Impressum · Datenschutz · AGB · Contact
- B2B link: "Are you a dealership or Zulassungsdienst? → KFZ Digital for Business" linking to b2b.kfzdigital.de

---

## 5. Partner Registration Office Page

Each partner point gets a dedicated subpage (e.g. `/bremen/blue-service-team`). This is a separate template page — see `kfz_partner_office.html` for the reference prototype.

**Partner page sections:**
1. Top bar (phone, email, opening hours)
2. Sticky nav (Services / How it works / Prices / Documents / Reviews / Location / FAQ)
3. Hero with partner name, open/closed live status, stats row (turnaround, walk-in, rating, years operating)
4. Sticky info card (address, hours, phone, email, map placeholder, book appointment CTA)
5. KFZ Digital certified partner badge
6. Services grid (6 service types with prices)
7. How it works (5 steps)
8. Pricing table (all services, transparent fees, authority fee disclaimer)
9. Documents checklist (always required + additional)
10. Reviews (score summary with bar chart + 4 review cards)
11. Location & opening hours (hours table with today highlighted + map)
12. FAQ (6 questions)
13. Sidebar: appointment booking form + trust certifications + nearby partner locations

**Live JS behaviour:**
- Open/closed status badge calculated from current time vs Mon–Fri 07:00–17:00
- Today's row highlighted in hours table

---

## 6. Online Registration Form (Modal)

5-step flow opened from "Start online registration" CTA:

| Step | Title | Fields |
|---|---|---|
| 1 | Registration type | Radio: Neuzulassung / Umschreibung / Wiederzulassung / Außerbetriebsetzung |
| 2 | Vehicle details | VIN (17 chars), HSN (4 chars), TSN (3 chars), First registration date, Security code |
| 3 | Holder details | First name, Last name, DOB, PLZ, City, Street address, eVB number |
| 4 | Bank details | IBAN, Account holder name + fee summary (€16.30 + €26–35 authority = ~€42–51) |
| 5 | eID verification | AusweisApp2 instructions, summary, SEPA mandate checkbox, submit |
| Success | Confirmation | Reference number (KFZ-YYYY-XXXXX), 1–3 business days notice |

**Progress bar:** 5 dots, filled blue up to current step.

---

## 7. Competitor Research

### KennzeichenMax (kennzeichenmax.de)
- **Focus:** Physical plate shops + online ordering. Plates only, not full registration.
- **Strength:** City-specific pages (e.g. `/kennzeichen/hb` for Bremen). Each city page has shop photos, exact hours, Google Maps. Drives local SEO.
- **Strength:** Same-day dispatch for plates ordered before 14:00.
- **Weakness:** No digital registration — directs users to Zulassungsstelle for the actual registration step.
- **Reuse:** City page structure — each city needs its own page with local partner details.

### KennzeichenKing (kennzeichenking.de)
- **Focus:** National plate ordering + Zulassungsstellen directory.
- **Strength:** Zulassungsstellen pages for every German district — very strong SEO.
- **Strength:** Breadcrumb structure (State → District → City).
- **Weakness:** No digital registration.
- **Reuse:** Zulassungsstellen page structure — list official offices AND our partner points side by side.

### KennzeichenServices.de — White Label
- **Focus:** B2B infrastructure — white-label shops and API for Kfz services.
- **Strength:** Clean two-track B2B offer (full white-label vs API integration).
- **Strength:** Case studies (Klickjäger, netTraders, Bußgeldkatalog.org).
- **Reuse:** Two-track B2B page model and case study format → applied to B2B domain.

### ZULEX (zulex.de)
- **Focus:** B2B i-Kfz software for dealerships, Zulassungsbetriebe, fleets.
- **Strength:** KBA-certified, ISO 27001 + ISO 9001 prominently displayed.
- **Strength:** Three segment pages (Zulasser / Autohäuser / Flotten).
- **Strength:** Customer testimonials with named contacts and company logos.
- **Weakness:** No consumer touchpoint.
- **Reuse:** Segment-specific B2B page structure → applied to B2B domain.

### DKK24 (dkk24.de) — Local operator, Hamburg
- **Type:** Physical Zulassungsdienst
- **Notable:** 15+ years operating, 100,000+ cases, DIN certified, Top Dienstleister 2020/2023/2025, 1,600+ ProvenExpert reviews, #1 in Hamburg on "Wer kennt den Besten"
- **Processing time (current):** 1–3 business days for registration; same day for Abmeldung
- **Service fee:** Not publicly listed
- **Walk-in:** Yes, Mon–Fri 09:00–17:00, Burgstr. 12, 20535 Hamburg
- **Partner potential:** Strong candidate — established, digitisation-minded, Hamburg coverage

### Zulassung24.berlin — Local operator, Berlin
- **Type:** Physical + online Zulassungsdienst, 16 drop-off shops across Berlin
- **Notable:** Services from €19, complete registration with plates €179, Halterwechsel €99
- **Processing time (current):** ~4 business days
- **Sofortzulassung:** Available at Berlin Steglitz, ~20 minutes
- **Partner potential:** Strong candidate — Berlin coverage, multi-location

### KfzPortal24 (kfzportal24.de)
- **Type:** Online-only platform, B2B marketplace model
- **Notable:** Official KBA digitisation project member, 300+ districts, online registration €99.90 all-in, deregistration €39.90
- **Note:** This is a **direct competitor** for the online registration path. Used as reference for what a polished online service looks like.

---

## 8. Key Business Rules for Development

1. **Never show online options when a local partner exists in the searched city.** The partner point is the primary revenue driver and must be shown exclusively in cities where they operate.

2. **No plate sales or plate registration on the B2C landing.** Plates are out of scope for this page.

3. **No pricing listed for local partner services.** Partner pricing varies. Only online fees (€16.30 etc.) are shown as they are government-set.

4. **B2B is a completely separate domain** (`b2b.kfzdigital.de`). The B2C page links to it only via a slim footer bar — not embedded in the main content.

5. **German as primary language in production** — prototype is in English for handoff clarity. All final copy should be German with English toggle.

6. **City pages are required for SEO** — each partner city needs a dedicated `/[city]` subpage following KennzeichenMax's structure. This is the main organic traffic acquisition strategy.

7. **FAQ schema markup (JSON-LD)** must be added to the FAQ section for Google rich results.

---

## 9. Content Reusable from Current kfzdigital.de

| Content | Reuse | Notes |
|---|---|---|
| FAQ section (20+ Q&As) | Direct reuse | Well-written, German-market appropriate |
| Compliance/security copy (eID, KBA, DSGVO) | Adapt | Surface higher in the page hierarchy |
| Feature block descriptions | Adapt | Currently buried; rewrite for consumer audience |
| Legal entity / Impressum | Direct reuse | Required for German law |
| Contact details (phone, email) | Direct reuse | 042149182511 / Info@kfzdigital.de |

---

## 10. Open Questions (Blocking for Production)

| Question | Blocks |
|---|---|
| Confirmed list of active partner cities | City page launch order, search partner DB |
| Confirmed partner pricing per city | Option card pricing on B2C |
| Is Mobegu still the primary online partner? | Fallback CTA links |
| German copy owner (Denis review vs fresh translation) | All body copy |
| Which certifications confirmed (i-Kfz phase, KBA number, ISO) | Trust section |
| Datenschutz and AGB pages content | Footer legal links (required by German law) |
| Real review data (platform, count, score) | Reviews section on partner pages |

---

## 11. File Reference

| File | Description |
|---|---|
| `kfz_digital_b2c.html` | B2C consumer landing page prototype |
| `kfz_digital_b2b.html` | B2B domain prototype (3 segments) |
| `kfz_partner_office.html` | Partner registration office page template |
| `KFZ_Digital_Project_Brief.docx` | Full project brief with strategy and competitor analysis |

---

*Research conducted May 2026. Sources: KBA official fee schedule, DKK24.de, Zulassung24.berlin, KfzPortal24.de, KennzeichenMax.de, KennzeichenKing.de, KennzeichenServices.de, ZULEX.de, Federal Ministry of Transport (BMVD).*
