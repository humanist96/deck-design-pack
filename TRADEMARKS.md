# Trademarks and Design Attribution

## Summary

This pack contains **no third-party trademarks, logos, wordmarks, fonts, or photographs**. Every SVG, specification, and helper script in this repository is original work by the copyright holder and is released under the [MIT License](LICENSE).

## What the templates are

Each template is an original slide design system. Where a template's specification says it draws on a design *idiom* — "dark product UI", "monochrome developer platform", "cinematic product keynote" — it refers to broadly practised, non-proprietary design conventions: near-black surface stepping, hairline borders, polarity inversion between light and dark sections, single-accent restraint, full-bleed photographic composition, angular geometry.

These conventions are not owned by any company. The templates implement them from scratch in SVG, with their own palettes, type ramps, page rosters, spacing systems, and layout contracts.

## Company names in specifications

Some `design_spec.md` files name a company as a **reference point for the design idiom** ("Linear 계열", "Vercel 계열에서 착안"). This is descriptive, comparative reference — it identifies the visual family a reader may already recognise. It is not a claim of origin, endorsement, affiliation, sponsorship, or approval by any named company.

Template identifiers and display names are deliberately original (`midnight-panel`, `polarity`, `gradient-mesh`, `warm-doc`, `open-road`, `signal-green`) so that no third-party mark appears in a product name, file path, or index entry.

All trademarks referenced remain the property of their respective owners.

## Colour values

Hex colour values, spacing scales, and corner-radius values are factual measurements, not creative expression, and are not subject to copyright. Where a specification records such a value it is stated as a fact about a publicly visible design, and the surrounding prose is written independently.

## Fonts

**No font files are bundled.** Typography across the pack is locked to **Pretendard** (SIL Open Font License), which the consuming workspace supplies. Where a reference design uses a proprietary or separately-licensed typeface (for example Söhne, Geist, Universal Sans, or an in-house corporate face), that typeface is **not used and not shipped** — the templates reproduce its character through weight span, letter-spacing, and size ramp only.

Because PPTX does not embed fonts, decks exported from these templates require Pretendard to be installed on any machine that opens them.

## Images and logos

**No photographs, icons, or logo assets are bundled.**

- Brand marks are text slots (`{{BRAND_MARK}}`) that the deck author fills with their own organisation name.
- The `open-road` template marks photographic regions with an `ltUpDiag` pattern placeholder. The author supplies their own licensed imagery.

## Reporting

If you believe any part of this repository infringes a trademark or other right, please open an issue describing the specific file and concern.
