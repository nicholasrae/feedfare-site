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

WebP variants are 480 and 800 pixels wide. Dimensions and byte sizes are recorded in `docs/image-budget.json`. The three highest-resolution images total 150,800 bytes. The October 11 homepage markup, CSS, JavaScript, displayed icons, those images, and the new demo poster total 229,389 bytes before HTTP compression. Browser source selection, favicons, caching, and headers can affect actual transfer. Historical `screen*.png/jpg` assets remain at their previous URLs for compatibility but are not loaded by the new pages.

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

App Store Connect generated the provider token `1329661` for this account. This is a public campaign attribution token, not an API credential. CTAs use `site_navigation`, `site_hero`, `site_download`, `site_press`, and `site_press_footer`. All website download links target the approved “Walking before scrolling” custom product page (`ppid=fc80f820-a690-452a-95d4-76c93fce92d7`), while retaining the existing country-neutral App Store paths and campaign attribution. Inspect them under Analytics → Acquisition → Campaigns. Apple requires at least five individual Apple Accounts to install through a campaign before reporting it. No analytics script, cookie, customer identifier, Health data, or Screen Time data is added to the website.

## Native paid-download release

The website describes released native FeedFare 2026.9.28, requiring iOS/iPadOS 17 or later, with a US $4.99 one-time download price and regional pricing shown by Apple. The public US storefront was rechecked on October 9, 2026 for the version and price. Visitors should check their device compatibility and regional availability on Apple’s listing. Existing owners receive full native access when they install the update on supported devices. Do not imply that every device has already upgraded or that older installed versions no longer use legacy purchase services.

The October 9 availability copy is backed by the public US App Store listing for native version 2026.9.28 and its $4.99 price. Prepared build 30 features are not advertised as released. Dated policy bodies and historical screenshots remain unchanged because this update only refreshes availability wording. The yearly, monthly, and weekly legacy subscription products were verified as Developer Removed from Sale on October 5, 2026, so the site explains that previous plans have been retired and no longer renew. This is separate from installing an app update. Preserve historical purchase/privacy explanations for older installed versions and keep future billing changes tied to verified App Store Connect product state.

When content changes, update homepage, FAQ, support, policy bodies, metadata, social-card label, and sitemap together. Sync policy mirrors using the scoped script above. Keep example data and simulator provenance clear; only replace screenshots with verified app screens.

See `docs/website-update-2026-09-28.md` for the original audit closure and validation limits.

## October 11 purchase explanation and demo

The homepage presents the one-time offer, compatibility, regional pricing and a 56-second walkthrough together. The walkthrough is hosted locally in `assets/feedfare-demo-56s.mp4` (905,505 bytes); its source is assigned only after a visitor presses play. It has native playback controls, inline playback, an optional local English WebVTT track and a YouTube fallback. There is no iframe, autoplay, third-party player, new analytics, cookie, storage or backend. English captions are burned into the video; the optional native track is not enabled by default, avoiding duplicate text. The poster is loaded lazily. JavaScript-disabled visitors can open the captioned MP4 directly.

The video comes from the approved October 11 simulator package. It models steps and app protection in a temporary demonstration build based on the public feature baseline. The visible disclaimer and captions explain that it does not show a physical walk, Apple Health updates, an external app unlocking or iOS Screen Time enforcement. Do not reframe it as real-device evidence. The five-minute wait is shortened in the edit.

The purchase explanation links to the existing permission and protection guidance, including the current 50-app selection limit and lack of website blocking. The Family Sharing FAQ describes Apple's eligible purchase-sharing benefit; it does not imply shared progress or remote parental enforcement. The public US listing was rechecked October 11, 2026 for US $4.99, version 2026.9.28, iOS/iPadOS 17+ and Family Sharing. Terms wording now reflects the already released native app; its effective date and substantive contract terms are unchanged. See `docs/growth-foundation-2026-10-11.md` for provenance and validation boundaries.

## Public press kit

`press.html` is generated by `scripts/build_site.py` from current public product facts and existing approved assets. It provides the 1024-pixel icon, three native simulator screens labeled as example data, public video links with their proof boundaries, and Nick's already public contact. The 56-second video is a modeled simulator demonstration; the 24-second Settings video is an actual interface preview with example progress and step connections/protection off. A separate development-news section now describes the planned iPhone Duo update; it does not advertise those features as publicly released or claim unrecorded device outcomes. It adds no scripts, image files, media files, forms or backend. Footer links are shared with the policy mirrors, so re-run the scoped legal sync when publishing it.

## October 22 iPhone Duo development update

The homepage includes a dedicated `#iphone-duo` section and a discoverable hero link. The existing compatibility FAQ, support guide and press kit distinguish the planned compact/open layouts and expanded Stats from the current App Store release. No Duo screenshot or demo is published: visual folding, pending-session continuity and actual system Split View remain unverified in the build 36 QA record. Existing simulator imagery and video retain their original labels. No badge, Apple endorsement or simultaneous outer/inner-screen behavior is claimed.

Source evidence: `/Users/nick/Documents/rork-feedfare/release-evidence/duo-build36-validation-2026-10-22/QA-report.md`. Website verification and publication evidence: `/Users/nick/Documents/rork-feedfare/release-evidence/website-duo-2026-10-22/`. Legal bodies, dates, pricing, campaign links and existing media are unchanged.

The October 22 update also removes dated current-version labels from availability, compatibility, support and press copy. Apple remains the source for the latest public version. Historical screenshot, policy and release-verification references are retained.

## October 23 iPhone Duo App Store launch

The homepage, compatibility FAQ, support guide and press kit now describe version 2026.10.22 as live on the App Store. On October 23 at 21:32 UTC, the exact App Version item was Approved, App Store Connect showed build 37 Ready for Distribution, and the public U.S. listing displayed version 2026.10.22 with the $4.99 offer and no availability error. Public version/build correlation is verified; physical installation and worldwide availability were not tested. Visitors should check Apple’s listing for device compatibility and regional availability.

Compact/expanded layouts, selected-day Stats, Calm and session-confirmation continuity are backed by the build 37 release notes and simulator checks. Physical iPhone Duo testing remains pending. Historical screenshots and the existing simulator demo keep their original provenance; no new video is published. Download links keep the Walking before scrolling custom-page ID and existing campaign attribution. Legal bodies, pricing and existing assets remain unchanged.

Release proof: `/Users/nick/Documents/FeedFare-Releases/2026.10.22-37/PublicAppReviewMonitoring/evidence/20261023T213143Z-observation.json`. Website publication evidence: `/Users/nick/Documents/rork-feedfare/release-evidence/website-duo-live-2026-10-23/`. The separate local Duo video preparation in the original website checkout remains untouched.

## October 29: next setup and session update submitted

The homepage's separate `#next-update` preview, support guide and press kit now describe the submitted 2026.10.27 update while preserving the live 2026.10.22 Duo announcement. Build 39 was submitted to public App Review on October 29; the new features are not advertised as live. The preview covers unfinished setup, Health/optional Motion guidance, blocked-screen help, preferred-session review, default-off one-minute warnings and Lock Screen Live Activities, and the seven-day recap. The support guide explains elapsed access windows and unused whole-minute refunds.

Public submission ID: `bbc8122d-280a-47f2-867b-b81e2256d4c0`. Source release evidence is `/Users/nick/Documents/FeedFare-Releases/2026.10.27-39/`; website publication evidence is `/Users/nick/Documents/rork-feedfare/release-evidence/website-build39-2026-10-29/`. Physical-device outcomes remain unverified. All download destinations/campaign parameters, existing media/provenance, pricing and legal bodies are preserved. This site change does not alter ads or app source. The older dirty checkout and its deferred Duo video work remain untouched.
