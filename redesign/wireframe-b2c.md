# KFZ Digital B2C Homepage — Wireframe & Content

**URL**: kfzdigital.de (main domain)
**Primary user**: End customer who needs to register/deregister a car *now*
**Primary goal**: Get user from "I need to register" → committed to a path (online or partner point) in under 60 seconds
**Working language**: English (German localisation is a later step)

---

## Page Architecture (Top to Bottom)

```
1.  Top bar (utility nav)
2.  Header / Main nav
3.  HERO — Plate input + 3 pathways
4.  Trust strip (certifications)
5.  How it works (3 steps)
6.  City search / find a partner point
7.  Comparison table (KFZ Digital vs. Registration Office)
8.  Pricing transparency
9.  Why KFZ Digital (4 value props)
10. Customer reviews / ratings
11. FAQ (top 6, link to full)
12. Secondary: Custom plate reservation teaser
13. B2B link band (subtle, footer-adjacent)
14. Footer
```

---

## 1. Top Bar (utility nav)

```
[Phone icon] +49 (0) 421 491 825 11   |   Mon–Fri 9am–6pm   |   support@kennzeichen.de        [EN ▾]   [For Partners →]
```

**Notes**:
- "For Partners →" links to partners.kennzeichen.de
- Phone is clickable (`tel:`) — older demographic trust signal
- Language switcher (EN default for working draft; DE will be the live default)

---

## 2. Header / Main Nav

```
[Logo]    Registration  |  Deregistration  |  Transfer  |  Custom Plate  |  Locations  |  Help        [Register now →]
```

**Notes**:
- Sticky on scroll
- Primary CTA button right-aligned, accent colour
- "Locations" opens city directory (key SEO hub)

---

## 3. HERO — Plate Input + 3 Pathways

### Layout
Two-column desktop / stacked mobile. Left: headline + plate input. Right: illustration or short looping video showing the digital process.

### Content

**Eyebrow**: `Official i-Kfz Partner · KBA-certified`

**H1**: **Register your car in 15 minutes — fully digital.**

**Subhead**: No waiting times. No office visits. Fully legally compliant under German vehicle registration law.

**Plate input** (prominent, large):
```
┌─────────────────────────────────────────────┐
│  [🇩🇪 D]  [HB] [_____]  [Continue →]        │
└─────────────────────────────────────────────┘
```
- Auto-detects user's city via geolocation/IP and pre-fills city code
- Validates format in real-time
- "Continue →" routes to next step based on input

**Below input — 3 pathways as horizontal cards:**

| 🏃 Fastest path | 🏢 Local service | 📋 Traditional path |
|---|---|---|
| **Register online** | **Local partner point** | **Registration office appointment** |
| 15 min, fully digital | In-person help in your city | When online isn't possible |
| from €99.90 | from €49.90 | Official fees only |
| [Start online →] | [Find a partner →] | [Check requirements →] |

**Trust micro-line below cards**:
`✓ Money-back guarantee · ✓ GDPR-compliant · ✓ Over 50,000 successful registrations`

---

## 4. Trust Strip (Certifications)

Single horizontal band with grayscale logos:

```
i-Kfz Partner  |  KBA  |  ISO 27001  |  ISO 9001  |  GDPR  |  TÜV-verified
```

- Each logo on hover: tooltip explaining what the certification means
- Below: small line — `Recognised by the Federal Motor Transport Authority · Secure data transfer via the official i-Kfz interface`

---

## 5. How It Works (3 Steps)

**Section H2**: **How it works**
**Subhead**: From application to plate — in 3 steps.

Three-step visualisation (numbered, horizontal connector line):

### Step 1 — Enter your details
**Icon**: Form / document
**Text**: Upload your vehicle title, insurance confirmation (eVB), and ID. We verify automatically.
**Time badge**: ~5 min

### Step 2 — Verify online
**Icon**: ID + smartphone
**Text**: Quick verification via German ID card (eID) or video identification. No office visit needed.
**Time badge**: ~5 min

### Step 3 — Receive your registration
**Icon**: License plate
**Text**: Provisional registration arrives by email instantly. Plates and stickers are delivered or collected locally.
**Time badge**: ~5 min

**CTA below**: `[Start with Step 1 →]`

---

## 6. City Search / Find a Partner Point

**Section H2**: **Find a partner point near you**
**Subhead**: 120+ locations across Germany. Personal help in 15 minutes.

**Search input**:
```
┌─────────────────────────────────────────────────┐
│  📍 Enter postal code or city   [Search →]      │
└─────────────────────────────────────────────────┘
```

**Below search — Popular cities grid** (8 tiles):

```
Bremen   |  Hamburg   |  Berlin     |  Cologne
Munich   |  Frankfurt |  Düsseldorf |  Stuttgart
```

Each tile links to `/locations/[city]` — the SEO city pages.

**Map preview** (optional): Small static map showing partner pin density across Germany.

**Below grid**: small text — `No partner nearby? [Register online →]`

---

## 7. Comparison Table — KFZ Digital vs. Registration Office

**Section H2**: **Why KFZ Digital instead of the registration office?**

| | KFZ Digital | Registration Office |
|---|---|---|
| Duration | 15 minutes | 2–4 hours + travel |
| Appointment needed | No | Yes, often weeks of waiting |
| Opening hours | 24/7 available | Mon–Fri, limited |
| In-person attendance | No | Yes |
| Cost | from €99.90 | Official fees + your time |
| Provisional registration | Instant via email | At the counter |

(Green checkmarks for KFZ Digital advantages, neutral for Registration Office)

---

## 8. Pricing Transparency

**Section H2**: **Transparent pricing — no hidden costs**

Three pricing cards (horizontal):

### Online registration
**€99.90**
- Fully digital
- Provisional registration instantly
- All official fees included
- DHL delivery of plates & stickers

`[Register online →]`

### Local partner
**from €49.90**
- In-person help
- Plates stamped on the spot
- Handles complex cases too
- Same-day appointments available

`[Find a partner →]`

### Custom plate
**€19.90**
- Reservation valid for 90 days
- Available nationwide
- Combinable with registration

`[Reserve your plate →]`

**Below cards — micro-trust**:
`✓ Money-back guarantee if online registration fails despite correct data`

---

## 9. Why KFZ Digital (4 Value Props)

**Section H2**: **Why 50,000+ customers trust us**

2×2 grid:

| 🚀 Fast | 🔒 Secure |
|---|---|
| **15 minutes vs. half a day** | **Official i-Kfz interface** |
| No waiting, no travel, no bureaucracy. | Direct connection to the Federal Motor Transport Authority. ISO-certified. |

| 💶 Transparent | 🤝 Personal |
|---|---|
| **Fixed price, no surprises** | **120+ partners across Germany** |
| What you see is what you pay. Money-back guarantee on technical failures. | If you need help, a partner is nearby. |

---

## 10. Customer Reviews / Ratings

**Section H2**: **What our customers say**

**Rating badge prominent**: `★★★★★ 4.8 / 5 · 1,247 reviews` (Trustpilot/Google equivalent)

Three testimonial cards with: photo, name, city, plate region, star rating, quote.

Example:
> "Done in 12 minutes. I never thought dealing with German bureaucracy could be this easy."
> **Markus K., Bremen (HB)** · ★★★★★

`[Read all reviews →]`

---

## 11. FAQ (Top 6)

**Section H2**: **Frequently asked questions**

Accordion (closed by default):

1. **What do I need for online registration?**
2. **How does the identity verification work?**
3. **When will I receive my plates?**
4. **What does registration really cost?**
5. **What happens if online registration doesn't work?**
6. **Is digital registration legally valid?**

`[See all FAQs →]` — links to full FAQ page

---

## 12. Secondary: Custom Plate Reservation Teaser

**Section H2**: **Got a custom plate in mind?**
**Subhead**: Reserve now — 90 days valid, available nationwide.

Inline form:
```
[HB] [_____ ] [_____]   [Check availability →]
```

Live-availability check ("Available!" / "Already taken") — high engagement element.

---

## 13. B2B Link Band (Subtle)

Thin band before footer, accent background:

```
┌────────────────────────────────────────────────────────────────────┐
│  Car dealership, registration service, or want to integrate        │
│  KFZ Digital into your platform?                                   │
│  [Become a partner →]                                              │
└────────────────────────────────────────────────────────────────────┘
```

Links to `partners.kennzeichen.de`.

---

## 14. Footer

**4 columns:**

**Column 1 — Services**
- Online registration
- Deregistration
- Ownership transfer
- Address change
- Custom plate

**Column 2 — Locations**
- All cities
- Bremen
- Hamburg
- Berlin
- Munich
- [+ regional alphabetical sitemap link]

**Column 3 — Help**
- FAQ
- Document checklist
- Contact
- Check status
- WhatsApp support

**Column 4 — Company**
- About us
- For partners ↗ (external)
- Careers
- Press
- Blog / Guides

**Bottom row:**
`KFZ Digital GmbH · In den Freuen 96, 28719 Bremen · HRB 36819 HB · VAT ID DE343815625`
`Imprint · Privacy · Terms · Cookies`
`Payment methods: [PayPal] [Klarna] [Visa] [Mastercard] [SEPA]`

---

## Mobile-Specific Considerations

- Hero: Stack plate input above pathway cards, swipe between cards
- City grid: Horizontal scroll instead of 4-wide grid
- Pricing cards: Stacked, full-width
- Comparison table: Convert to side-by-side icon comparison (not table)
- Sticky bottom CTA bar on mobile: "Register now" always visible

---

## Conversion Levers Recap (what makes this homepage convert)

1. **Plate input in hero** — captures intent in 1 click (kennzeichenmax pattern)
2. **3 pathways visible immediately** — no analysis paralysis
3. **Pricing shown openly** — kills #1 hesitation (kfzdigital.de's weakness)
4. **Money-back guarantee** — risk reversal (kfzportal24 pattern)
5. **i-Kfz / KBA badges** prominent — legal trust signal
6. **Real reviews + count** — social proof at scale
7. **Comparison table** — makes "why not just go to the office" feel obviously inferior
8. **B2B link present but de-prioritised** — doesn't dilute B2C focus

---

## Open Questions for Denis

1. Confirm pricing: €99.90 / €49.90 / €19.90 — competitive but undercuts Kennzeichenking. OK?
2. How many partner points do we actually have today? (Affects "120+" claim)
3. Are we processing volume yet? (Affects "50,000 customers" — may need to scale claim down)
4. Real customer testimonials available, or do we need to gather?
5. Confirm B2B subdomain: `partners.kennzeichen.de` vs `business.kfzdigital.de` vs other?

---

## Next Steps

1. ⬜ Denis validates pricing + claim numbers
2. ⬜ Source 3 real testimonials with permission
3. ⬜ Wireframe → Figma high-fidelity mockup
4. ⬜ Build city page template (separate doc)
5. ⬜ Build partners.kennzeichen.de structure (separate doc)
