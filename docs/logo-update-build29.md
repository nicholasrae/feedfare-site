# Build 29 logo update

Updated FeedFare’s website identity to the approved blue footprint and progress
arc from the native app’s Liquid Glass icon, on September 28, 2026.

The source is the native project’s Apple-rendered
`design/app-icon/previews/liquid-glass-default.png`, copied to `app-icon.png`.
Updated assets cover every page’s header/footer, 64/128/256-pixel WebP variants,
PNG/ICO favicons, the 180-pixel Apple touch icon, and the 1200×630 social card.
Legacy root icon URLs remain available with the new artwork. The header has a
higher-resolution source for Retina screens. Icon and social-card references
include `v=build29` to refresh cached assets.

Validation:
- Five-page static checks passed: image metadata, local links, anchors, CSP,
  structured data, and resource budget.
- JavaScript syntax and Git whitespace checks passed.
- Browser previews at 1440×900 and 390×844 show the new header icon without
  horizontal overflow; the footer image loads after scrolling into view.
- The regenerated social card was visually inspected.

This update changes branding only. App preview labels, pricing copy, support,
privacy text, and terms remain unchanged.
