# Validation record — Flyne adaptation, 2026-09-30

[Home](../README.md) · [Source history](UPSTREAM.md)

- All 52 catalog prompt bodies match the upstream SHA-256 manifest; all four inherited exercise code blocks also match the immediate source.
- All 15 language homepages retain their source content and use the new Flyne cover, provider URL and localized affiliate sections. This preserves the source's language coverage; it does not claim every English recipe is translated into 15 languages.
- Two additional X records and two original Flyne practice prompts are included. Both new posts lack a complete published generation prompt. The music-video post discloses sponsorship and does not identify its result specifically as Flash.
- `scripts/check_content.py` validates local paths/anchors, source prompt hashes, practice counts, case uniqueness, required metadata, media hosts and brand sections.
- `scripts/build_brand_sections.py --check` and `scripts/build_gallery.py --check` verify generated content is up to date. GitHub Actions runs these checks on push and pull requests.
- The original 12 video URLs returned HTTP 200 using HEAD; all 12 thumbnail requests returned HTTP 200 using GET on 2026-09-30. [Machine-readable results](../data/media-check-20260930.json). This confirms access, not full playback or visual quality. One case is an article without media and another contains two clips.
- The Flyne model page currently describes 4.0 as upcoming and selects Kling 3.0 Turbo. No paid generation, uptime test or independent reproduction was performed.

The prior 2026-09-29 source checks remain attached to inherited case records. They were performed by the source project, not repeated under a new date by Flyne. Our media-access checks are stored separately.

## X expansion — 2026-09-30

- Six additional cases bring the gallery to 18; four new original exercises bring Flyne practice prompts to six.
- Pan’s Kling reply includes a full prompt; its parent video is labeled Seedance and was not imported as a Kling clip. Ozan’s screenshot is labeled partial, not a full prompt.
- New media accessibility results: [six videos and six posters](../data/media-check-expansion-20260930.json). All six video HEAD requests returned HTTP 200. All six poster requests returned HTTP 403 with both HEAD and GET in this environment; preview availability is unresolved. Original post links remain available. HTTP checks do not verify playback or model quality.
