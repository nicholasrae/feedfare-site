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

The site uses FeedFare's existing icon, light native surfaces, blue controls, system typography, and restrained translucency. Three real native simulator screenshots use example data and are explicitly labeled as TestFlight previews. Source captures are `dashboard-light.png`, `activity-light.png`, and `stats-light.png` from the native app's `docs/native-verification` folder. Do not replace them with customer Health data.

WebP variants are 480 and 800 pixels wide. Dimensions and byte sizes are recorded in `docs/image-budget.json`. The three highest-resolution images total 150,800 bytes; all homepage markup, CSS, JavaScript, displayed icon, and those images total about 185 KB before HTTP compression. Browser source selection, favicons, caching, and headers can affect actual transfer. Historical `screen*.png/jpg` assets remain at their previous URLs for compatibility but are not loaded by the new pages.

`python3 scripts/build_share_image.py` regenerates the 1200×630 social card using Pillow and the macOS Avenir Next font. The generated card is checked in; neither Pillow nor macOS is required to deploy the site.

## One policy, three existing URL locations

The public App Store and existing app builds already link to separate policy locations. Preserve those paths and sync their content when policies change:

```sh
python3 scripts/build_site.py
python3 scripts/sync_legal.py /path/to/feedfare-legal /path/to/nickrae-site
```

The script copies the privacy policy, terms, and four dedicated assets. It only touches the existing policy files and `feedfare/assets/` within the personal website. It never commits or publishes. Review, commit, and push each repository independently.

- Canonical: `https://feedfare.app/privacy-policy.html` and `/terms.html`
- App Store legacy policy: `https://nicholasrae.github.io/feedfare-legal/privacy-policy.html`
- In-app links: `https://nickrae.net/feedfare/privacy.html` and `/feedfare/terms.html`

## Acquisition measurement

App Store Connect generated the provider token `1329661` for this account. This is a public campaign attribution token, not an API credential. CTAs use `site_navigation`, `site_hero`, and `site_download`. Inspect them under Analytics → Acquisition → Campaigns. Apple requires at least five individual Apple Accounts to install through a campaign before reporting it. No analytics script, cookie, customer identifier, Health data, or Screen Time data is added to the website.

## Native paid-download launch

The September 28 website is truthful about the current public offer: free download with optional in-app purchases. The native full-app paid-download version is in TestFlight, so screenshots and native-only behavior are labeled as previews. When the native app actually launches:

1. Verify the public binary, minimum OS, regional price, and App Store privacy declarations.
2. Update homepage, FAQ, terms, support, metadata, and screenshot captions together.
3. Publish clear instructions for prior subscribers after the subscription transition is decided. Removing a purchase SDK or updating this site does not cancel renewals.
4. Replace preview screenshots only with verified release screens; keep example data labeled.

See `docs/website-update-2026-09-28.md` for the audit closure and validation limits.
