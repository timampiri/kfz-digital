# Transcript Library — KFZ Digital

Raw call recordings with Denis Novakov (founder), transcribed and translated to English. Use these as design input: extract requirements, decisions, and feedback.

**Rule:** Always use English `.md` files only. Ignore `.vtt`, `.txt`, and Russian `.md` files.

---

## How to Use Transcripts

Transcripts are timestamped conversation logs, not structured docs. When pulling requirements:
- Search for keywords (e.g. "registration", "dealership", "button") — don't read top to bottom
- Treat timestamps as navigation markers, not content
- Cross-reference against `research/` docs — insights from these calls are already distilled there

**Never use transcripts as a build reference** — use `redesign/DESIGN.md` and `research/` instead. Transcripts are raw material only.

---

## Files

### `8.05/Denis 8.05 - English.md`
**Date:** 8 May 2026 | **Topic:** Platform roadmap & architecture  
Denis outlines the product vision: integrating with government systems, building a car dealership platform, migrating from Gulyan/Concept MAX to their own React microservices infrastructure, and adding an AI registration assistant.

Key themes: React migration, microservices, government API integration, registration flow redesign, white-label for dealerships.

---

### `15.05/KFZ DIGITAL V1 review - 15.05 - English.md`
**Date:** 15 May 2026 | **Topic:** V1 design review session  
Walkthrough of the V1 landing page design in Figma. Denis reviews pages, navigates between frames, and gives live feedback on layout and structure.

Key themes: Figma navigation feedback, page structure review, V1 landing page critique.

---

## Adding New Transcripts

When a new audio is processed via `kennzeichen-transcribe-translate` skill:
1. Files land in `transcript/{DD.MM}/` (e.g. `transcript/22.05/`)
2. Add an entry to this file under **Files** — date, topic, and 2-line summary
3. Update `research/` docs if the call contains new decisions or requirements
