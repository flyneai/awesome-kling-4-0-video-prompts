# Sources, license and maintenance

[Home](../README.md) · [Contribution guide](../CONTRIBUTING.md)

Flyne AI adapted [the immediate source collection](https://github.com/aivideoweb/awesome-kling-4-0-prompts) at commit [bd8a2562fbc260e54aa03a17c9d02bdc739050dd](https://github.com/aivideoweb/awesome-kling-4-0-prompts/tree/bd8a2562fbc260e54aa03a17c9d02bdc739050dd) on 2026-09-30.

The source itself adapted [flaqai/awesome-kling-4-0](https://github.com/flaqai/awesome-kling-4-0) at commit 85dc22c779a63c4a4fe657d337f014de7da904d7. The 52 main recipes, five scene/hero images and multilingual guide structure originated with Flaq AI. The immediate source added four exercises, ten-case source records, its cover and maintenance tools. All prior copyright notices remain in [LICENSE](../LICENSE). Earlier changelog entries describe work in those source repositories.

Flyne additions: a newly generated brand cover, Flyne service and affiliate links across all 15 language homepages, two new source-linked X examples, two separately authored practice prompts, and adapted generation/validation scripts. The four inherited exercises are not newly authored Flyne prompts. No paid video generation or service uptime test was performed.

The provider page was checked on 2026-09-30: [Flyne Kling 4.0 preview](https://flyne.ai/model/kling-4-0/) describes 4.0 as upcoming and its form selects Kling 3.0 Turbo. The link is a recommended entry for availability and current-model drafts, not proof of stable 4.0 access. Original 2026-09-29 model announcements and inherited verification dates remain historical records.

## Source media

X authors retain rights to posts, thumbnails and footage. External media is linked, not copied into this repository or relicensed under MIT. New records were read through the FxTwitter public mirror on 2026-09-30. Their model labels are creator claims, not independently reproduced results. A sponsored music-video workflow and a Flash dialogue test have different evidence boundaries; each entry states them. Neither new post supplies a full generation prompt, so the separate exercises are explicitly untested original briefs.

## Updating

1. Compare future upstream changes with the pinned source commit. Preserve source attribution and Flyne sections.
2. Edit `data/locales.json`, then run `python3 scripts/build_brand_sections.py` for all language introductions and footers.
3. Add cases to `data/x-cases.json`, including original URL, creator, model claim, prompt availability, date, verification method, media and rights. Set `is_new` only for Flyne additions. Do not promote inherited checks to new verification dates.
4. Keep the 52 catalog recipes, four inherited exercises and two Flyne exercises separately counted. Link a [test record](TEST-RECORD.md) before claiming any practice was render-tested.
5. Run `python3 scripts/build_gallery.py`, both generators with `--check`, `python3 scripts/check_content.py`, and `git diff --check`.
6. Recheck provider controls and terms when updating product claims. Record the actual model used. A Turbo draft is not a 4.0 result.
7. Check external media periodically when maintaining the project. If a URL fails, keep the original source link and flag the failure; do not substitute unrelated footage.
