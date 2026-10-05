# FeedFare website

The static website at https://feedfare.app, published from `main` at the root of `nicholasrae/feedfare-site` using GitHub Pages. Keep `CNAME`, `.nojekyll`, and the Google verification file intact.

## Edit and preview

Edit page content in `scripts/build_site.py`, presentation in `assets/site.css`, and the optional walking example in `assets/site.js`.

```sh
python3 scripts/build_site.py
python3 scripts/verify_site.py
node --check assets/site.js
python3 -m http.server 4173 --bind 127.0.0.1
```

The generated HTML is committed so deployment has no package manager or build-service dependency. Content, navigation, and native FAQ disclosures work without JavaScript; the calculator has a static fallback. Header/footer links use the canonical public site, including in copies of the legal pages.

## Images and visual identity

The site uses FeedFare build 29's approved blue footprint Liquid Glass icon, light native surfaces, blue controls, system typography, and restrained translucency. Three real native simulator screenshots use example data and are explicitly labeled as simulator screens. They show native FeedFare 2026.9.28. Source captures are `dashboard-light.png`, `activity-light.png`, and `stats-light.png` from the native app's `docs/native-verification` folder. Do not replace them with customer Health data.

WebP variants are 480 and 800 pixels wide. Dimensions and byte sizes are recorded in `docs/image-budget.json`. The three highest-resolution images total 150,800 bytes; all homepage markup, CSS, JavaScript, displayed icon, and those images total about 191 KB before HTTP compression. Browser source selection, favicons, caching, and headers can affect actual transfer. Historical `screen*.png/jpg` assets remain at their previous URLs for compatibility but are not loaded by the new pages.

`app-icon.png` is the approved 1024-pixel render exported from the native app’s Icon Composer source. Optimized WebP sizes, browser favicons, and the opaque 180-pixel Apple touch icon are derived from that artwork. Logo and social-image URLs use `v=build29` so cached older artwork is refreshed.

`python3 scripts/build_share_image.py` regenerates the 1200×630 social card using Pillow and the macOS Avenir Next font. The generated card is checked in; neither Pillow nor macOS is required to deploy the site.

## One policy, three existing URL locations

The public App Store and existing app builds already link to separate policy locations. Preserve those paths and sync their content when policies change:

```sh
python3 scripts/build_site.py
python3 scripts/sync_legal.py /path/to/feedfare-legal /path/to/nickrae-site
```

The script copies the privacy policy, terms, and five dedicated assets. It only touches the existing policy files and `feedfare/assets/` within the personal website. It never commits or publishes. Review, commit, and push each repository independently.

- Canonical: `https://feedfare.app/privacy-policy.html` and `/terms.html`
- App Store legacy policy: `https://nicholasrae.github.io/feedfare-legal/privacy-policy.html`
- In-app links: `https://nickrae.net/feedfare/privacy.html` and `/feedfare/terms.html`

## Acquisition measurement

App Store Connect generated the provider token `1329661` for this account. This is a public campaign attribution token, not an API credential. CTAs use `site_navigation`, `site_hero`, and `site_download`. Inspect them under Analytics → Acquisition → Campaigns. Apple requires at least five individual Apple Accounts to install through a campaign before reporting it. No analytics script, cookie, customer identifier, Health data, or Screen Time data is added to the website.

## Native paid-download release

The rollout copy describes native FeedFare 2026.9.28, requiring iOS/iPadOS 17 or later, with a US $4.99 one-time price configured in App Store Connect and regional pricing shown by Apple. The website tells visitors to check the current storefront version and price while distribution propagates. Existing owners receive full native access when they install the update on supported devices. Do not imply that every device has already upgraded or that older installed versions no longer use legacy purchase services.

The October 5 rollout copy is backed by App Store Connect Ready for Distribution and the verified US $4.99 current price. Keep the rollout qualifiers until the public native version and price have been verified; do not replace them with universal immediate-availability claims early. The yearly, monthly, and weekly legacy subscription products were verified as Developer Removed from Sale on October 5, 2026, so the site explains that previous plans have been retired and no longer renew. This is separate from installing an app update. Preserve historical purchase/privacy explanations for older installed versions and keep future billing changes tied to verified App Store Connect product state.

When content changes, update homepage, FAQ, support, policy bodies, metadata, social-card label, and sitemap together. Sync policy mirrors using the scoped script above. Keep example data and simulator provenance clear; only replace screenshots with verified app screens.

See `docs/website-update-2026-09-28.md` for the original audit closure and validation limits.
