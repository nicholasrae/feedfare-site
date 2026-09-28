# Website update — September 28, 2026

The FeedFare site now uses the native app's light surfaces, blue controls, rounded cards, and familiar type. The layout leads with a real dashboard, then explains earning time, shows Activity and Stats, and provides permission and purchase help.

## Audit findings addressed

| Finding | Change |
| --- | --- |
| 1. Incorrect privacy policy | Replaced food-sharing/account content with Health, Motion, Screen Time, local storage, migration, optional sharing/notifications, RevenueCat legacy purchases, hosting, and reset details. Synced the website, App Store-linked repository, and in-app legal URLs. |
| 2. Purchase/feature mismatch | Current public offer and future native paid release are explicitly separated. No premature “pay once” sales promise; existing subscription help is prominent. App Store pricing and release controls are unchanged. |
| 3. 43 MB eager preview | Three responsive WebP native screenshots replace six large posters. Hero prioritized; below-fold images lazy-loaded. Full-resolution versions are accessible via links. |
| 4. Low contrast | Main normal-text combinations pass calculated 4.5:1 contrast. Secondary text is at least 5.18:1 across used light surfaces; blue links at least 4.78:1. Select boundary and focus states improved. |
| 5. Pointer-only FAQ | Seven native details/summary disclosures support Enter/Space and expose collapsed/expanded state. |
| 6. Broken logo/About | Ordinary home links, a real About section, native fragment navigation, and sticky-header offsets. Removed custom scrolling script. |
| 7. Mobile clipping | Flexible grids and uncapped FAQ content; no overflow at the tested 320, 375, 390, 768, and 1280 widths. |
| 8. Uncontrolled animation | No decorative loops, autoplay, scroll reveals, or forced smooth scroll. Reduced-motion/transparency rules and forced-color support added. |
| 9. Excessive length/old artwork | Real product appears in the hero. Mobile page is approximately half its previous height. Main desktop download action is within the first 720-pixel screen. |
| 10. Compatibility/rules | Public iOS 15.1 and native iOS 17 requirements distinguished; adjustable 100→5 example, single-app sessions, and separate 1,000-step streak explained. |
| 11. Unsupported claims/math | Removed savings badges, trial promises, popularity claims, and universal setup/outcome timing claims. |
| 12. Thin support | Added permissions, live-step refresh, delayed Health sync, app selection, session enforcement, local reset, and legacy billing guidance. |
| 13. Semantics/script failure | Main landmark, skip link, headings, native links, visible focus, and content visible without reveal scripts. Calculator fallback is supplied. |
| 14. Metadata | Canonical URLs, accurate descriptions, SoftwareApplication JSON-LD, Smart App Banner, new sharing card, and dated sitemap including Support. Existing Google verification preserved. |
| 15. Measurement | Real App Store Connect provider token used with three placement campaign labels; no website tracking SDK. Reporting requires Apple's volume threshold. |
| 16. Hosting/polish | Shared navigation, self-hosted assets/system fonts, branded 404, restrictive CSP and referrer meta policies. GitHub Pages cannot set arbitrary response headers; no claim that X-Content-Type-Options or Permissions-Policy headers were added. |

## Validation

- Static validator: five pages, local assets/anchors, one H1/main, skip link, image dimensions/alt text, structured data, CSP script hash, screenshot/resource budget, text and select-boundary contrast.
- JavaScript syntax and Git whitespace checks passed.
- Browser: mobile/tablet/desktop layouts; calculator 1,000→50 and 2,000→100; keyboard Enter opens and Space closes FAQ; expanded answer content is not clipped at 320 pixels; section anchor stays below header; privacy navigation and narrow-screen legal page.
- Highest-resolution screenshot total: **150,800 bytes**, versus **42,952,725 bytes** for the previous six PNGs: a **99.65% reduction** in the screenshot payload. Homepage markup, CSS, JS, icon, and three largest screenshots are approximately **185 KB** before compression. This is a resource budget, not measured Core Web Vitals.
- Identical policy bodies and dedicated assets are maintained at all existing locations through the sync script. Canonical links point back to feedfare.app.

## Practical limits and release follow-up

This does not certify formal WCAG conformance. A physical iPhone Safari/VoiceOver session, OS text-size testing, and real reduced-motion preference testing remain device checks. Static fallbacks and media queries were inspected; browser scripting was not globally disabled during the test. PageSpeed quota was exhausted during the audit, so no Lighthouse or field performance score is claimed. Search Console indexing and actual campaign conversions require subsequent traffic and reporting.

The paid-download offer is still a separate App Store release step. The website is accurate for today's public app and clearly labels the native preview. Before that release, verify physical-device protection, the purchase/subscriber transition, and App Store privacy declarations against the submitted native binary.
