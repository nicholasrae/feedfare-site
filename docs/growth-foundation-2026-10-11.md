# FeedFare website purchase explanation — October 11, 2026

This is the first website work package from the FeedFare growth plan. The local homepage now gives visitors the mechanism, full-app purchase, demonstration and setup requirements in one place. It does not establish conversion improvement; paid units and proceeds still need separate measurement.

## What changed

- The hero explains choosing apps, earning minutes by walking and using one app for a timed session. It shows US $4.99 once, the full app, no subscription and no FeedFare account beside the App Store action.
- A 56-second landscape demo is hosted on the site. Its MP4 and caption track are assigned after the visitor presses play. Native playback controls and a direct YouTube fallback remain available; JavaScript-disabled visitors have a direct MP4 link.
- A visible disclosure explains that steps and protection are simulated in a temporary demonstration build and that the five-minute wait is shortened. The recording does not show a real walk, Apple Health updates, an external app unlocking or iOS Screen Time enforcement.
- The purchase explanation links to existing permissions, step-delay and protection guidance. It states the current 50-app selection limit and that website blocking is not included.
- The FAQ explains eligible Apple Family Sharing as purchase sharing, with separate setup and progress on each device. It does not offer a shared balance or remote parental controls.
- One stale terms sentence now describes the native app as available. No substantive contract terms changed; October 5 remains the effective date, with the copy update dated October 11.
- Canonical navigation links, the stylesheet cache version and sitemap dates were updated. Privacy and support policy bodies and legacy subscription guidance are retained.

## Sources and asset provenance

The parent agent verified the [public US App Store listing](https://apps.apple.com/us/app/feedfare-earn-screen-time/id6758923557) on October 11: US $4.99, native version 2026.9.28, iPhone/iPad with iOS/iPadOS 17+, and Family Sharing. Regional prices and eligibility are left to Apple. [Apple Family Sharing](https://support.apple.com/en-us/108380) is linked in the FAQ.

Permission behavior and limits come from the existing released-version [support guide](https://feedfare.app/support.html). The App Store attribution provider token is the existing documented `1329661`; no new or guessed tokens were added.

The source video is `/Users/nick/Documents/FeedFare-Marketing/2026-10-11/simulator-demo/feedfare-sim-demo-walkthrough-2026-10-11.mp4`, also published at [the public YouTube video](https://www.youtube.com/watch?v=EQfLgETl0m0). The site MP4 is byte-identical to that source, 56 seconds, 1920 × 1080, H.264, 905,505 bytes. Its SHA-256 is `5952c85e17df860f2618b109de7e221fd8a67c050aa4b9284cd8417718509423`.

The poster is a 1200 × 675 WebP derived from that video's supplied poster. The local WebVTT track is converted from its English SRT; captions are also already burned into the video. Byte sizes and hashes are recorded in `docs/growth-foundation-2026-10-11.json`.

## Validation and deployment boundary

These checks passed locally:

```sh
python3 scripts/build_site.py
python3 scripts/verify_site.py
node --check assets/site.js
```

The existing verifier covers landmarks, image sizing and alternatives, local assets, navigation anchors, structured data, the CSP hash, FAQ controls and text-contrast pairs. It also checks the local video source, preload policy, captions and simulator disclosures. The homepage's maximum-resolution static resource bundle, including all three app screens and the demo poster, totals 229,389 bytes before compression; this is a bounded file-size calculation, not a browser transfer measurement. The 905,505-byte MP4 is separate and loaded on demand.

Preview with `python3 -m http.server 4173 --bind 127.0.0.1` from this repository. Root owns browser verification of responsive layout, keyboard controls, actual media loading/playback, and any commit or publication. This preparation did not deploy, commit, modify app source, add analytics or alter account settings. The pre-existing untracked `design/` folder was left intact. If publishing changes to shared legal page assets, sync the existing legal mirrors with `scripts/sync_legal.py` and review each repository independently.

Root browser checks passed October 11: desktop 1280px and mobile 390px layouts have no horizontal overflow; images render after lazy loading; Enter activates the video; playback reaches readyState 4 with a 56-second duration and no media error; the Family Sharing answer expands; no browser errors were observed. Before activation the video has no source. English captions are burned in, with an optional native track disabled by default to avoid duplicate subtitles. Screenshots and production publication evidence are retained in the FeedFare repository under `release-evidence/growth-sprint-2026-10-12/`.
