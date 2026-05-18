# KFZ Digital Platform Redesign — Content Strategy

*Based on Denis & Rina discussion (Denis 8.05)*

---

## Page Structure Overview

### 1. Homepage / Landing Page
**Primary Goal**: Pull end-customers to registration — lead with digital registration as the hero

**Key Message**: "Digital Zulassung in 15 Minuten" (Digital Registration in 15 Minutes)

**Structure**:
- Hero section: Digital registration value prop
- How it works (3-step explanation)
- City/location search (main CTA)
- Why choose us (trust signals)
- Partner locations overview
- FAQ (top questions)
- B2B link (footer/secondary navigation)

**Flow Decision Logic**:
- If user finds a local registration point → direct to that partner
- If no location found → redirect to online registration (Concept MAX, Mobegu)
- No pricing shown on homepage

---

### 2. City-Specific Registration Pages
**Purpose**: Detailed entry points for each city/region

**Content per city page**:
- City name + Zulassungsstelle (registration office) info
- How digital registration works in this specific city
- Partner points list (with addresses, hours, contact)
- Step-by-step registration process
- Documents needed
- Online alternative if no partner available
- CTA to book/register

**Interlinked Structure**: Cities reference each other where relevant

---

### 3. B2B Section (Separate Landing)
**Target Audience**: Car dealerships, registration service points, white-label partners

**Three B2B Tiers**:

#### a) Registration Points (Zulassungsstellen)
- Become a partner point
- Join our franchise model
- Benefits: traffic, revenue share (€5 per registration)
- Requirements & onboarding

#### b) Car Dealerships (Autohändler)
- Streamlined registration for customers
- Batch processing
- Higher fees justify value (€15 per registration vs €5 for service points)
- Dashboard access to manage registrations

#### c) White-Label / API Partners
- Full platform rebranding under partner brand
- SDK integration
- For online stores (Concept MAX, similar platforms)
- API documentation & developer resources

**B2B Page Layout**:
- Hero: "Grow Your Business with KFZ Digital"
- Comparison: 3 partnership tiers
- Features: User management, batch processing, reporting, support
- Case studies/testimonials
- Pricing (if needed — or contact form)
- CTA: "Become a Partner"

---

### 4. Supporting Pages

#### About / Platform Explanation
- What is digital Zulassung?
- How it works technically
- Why use KFZ Digital?
- Company info (Denis Novakov, KFZ Digital GmbH)
- Contact: +49 (0) 42149182511, Bremen

#### FAQ
- Organize by user type: End customers, B2B partners, dealerships
- Keep current FAQ content from kfzdigital.de
- Add KFZ Digital-specific Q&A

#### Number Plates (Secondary)
- Optional: Reserve plates for free (link to KFZ Digital Motiv or similar)
- Mention that dealerships/partners can sell plates with margins
- Don't push this on homepage — keep focus on registration

---

## Content Migration from kfzdigital.de

✅ **Reusable Content**:
- Company registration process explanations
- eID/digital identification details
- GDPR compliance statements
- B2B feature descriptions (permissions, batch processing, workflows)
- FAQ structured content
- Contact info & company details

❌ **What to Remove/Redesign**:
- Feature cards (redesign for new structure)
- B2B portal focus (now separated into three B2B tiers)
- Plates-first messaging (registration is the hero now)
- Generic "schnell, einfach, jederzeit" tagline (make it specific to registration)

---

## New Messaging Framework

**Headline Variations**:
1. "Digital Zulassung in 15 Minuten" (Registration in 15 minutes)
2. "Finden Sie Ihren Zulassungspunkt" (Find your registration point)
3. "Auto registrieren ohne Wartezeiten" (Register your car without wait times)

**Value Props**:
- Fast: Complete registration in 15 minutes at a partner point
- Simple: Step-by-step guidance, no confusing paperwork
- Anywhere: Find a registration point near you, or do it online

**B2B Value Props**:
- Franchisees: Easy revenue stream, pre-vetted platform
- Dealerships: Streamline customer registration, increase throughput
- Online Stores: White-label your own registration platform

---

## Call-to-Action Strategy

**Primary CTAs**:
1. "Find Your Registration Point" (city search)
2. "Register Now" (for online path)
3. "Become a B2B Partner" (partnership tier)

**Secondary CTAs**:
- "Learn More" (how it works)
- "Reserve Number Plates" (link out, secondary)
- "Contact Us" (support, partnership inquiries)

---

## User Flows (Wireframe Reference)

### End Customer Flow:
1. Land on homepage
2. Enter city/postal code
3. See partner locations nearby
4. Choose a partner OR redirect to online
5. Begin registration/book appointment

### B2B Partner Flow:
1. Land on B2B section
2. Choose tier (registration point, dealership, white-label)
3. Review benefits & requirements
4. "Become a Partner" → contact/signup form
5. Onboarding (documentation, API access, etc.)

---

## Content Tone & Language

- **Language**: German (de-DE)
- **Tone**: Professional, trustworthy, B2B-focused
- **No marketing fluff**: Be direct about benefits
- **Legal clarity**: Explain what digital registration actually means
- **Local relevance**: Emphasize regional registration point network

---

## Next Steps

1. ✅ Create logo options (3-5 concepts)
2. ⬜ Design Figma mockups for homepage + city pages
3. ⬜ Finalize B2B section layout
4. ⬜ Extract & organize FAQ by user type
5. ⬜ Write final copy for each section
6. ⬜ HTML/React build (based on Figma approval)
