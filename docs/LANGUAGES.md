# Language & Localization Directory

[Home](../README.md) · [Prompt catalog](../prompts/README.md) · [Multilingual audio](MULTILINGUAL-AUDIO.md)

This repository provides complete aligned README translations in **15 languages**. Language coverage in the repository is not the same as native speech support in a video model.

> **Verified Kling Video 3.0 native-dialogue languages:** Chinese, English, Japanese, Korean and Spanish. Other languages below are documentation/localization languages. For unsupported spoken dialogue, test the live model first or generate clean visuals and add verified voice-over in post-production.

Kling AI has announced broader language, accent and dialect support for the full 4.0 release planned for October 2026. Kling 4.0 Flash is in limited early access; the table below remains a documented 3.0 baseline, not a claim about every 4.0 mode.

## 15-language directory

| Language | Localized guide | Repository UI | Verified native dialogue baseline |
|---|---|---:|---:|
| English | [README](../README.md) | Full | Yes |
| 简体中文 | [使用指南](../README.zh-CN.md) | Full | 是 |
| 繁體中文 | [使用指南](../README.zh-TW.md) | Full | 是 |
| 日本語 | [ガイド](../README.ja-JP.md) | Full | 対応 |
| 한국어 | [가이드](../README.ko-KR.md) | Full | 지원 |
| Español | [Guía](../README.es-ES.md) | Full | Sí |
| Français | [Guide](../README.fr-FR.md) | Full | Not in verified list |
| Deutsch | [Leitfaden](../README.de-DE.md) | Full | Not in verified list |
| Português (Brasil) | [Guia](../README.pt-BR.md) | Full | Not in verified list |
| Italiano | [Guida](../README.it-IT.md) | Full | Not in verified list |
| العربية | [الدليل](../README.ar.md) | Full | Not in verified list |
| Русский | [Руководство](../README.ru-RU.md) | Full | Not in verified list |
| Bahasa Indonesia | [Panduan](../README.id-ID.md) | Full | Not in verified list |
| ไทย | [คู่มือ](../README.th-TH.md) | Full | Not in verified list |
| Tiếng Việt | [Hướng dẫn](../README.vi-VN.md) | Full | Not in verified list |

## What is localized

| Content | English | Simplified Chinese | Other 13 languages |
|---|---:|---:|---:|
| Full README: positioning, status, examples, catalog, checklists, FAQ and contributing | Full | Full translation | Full translation |
| Six homepage X preview cards and all source links | Full | Full translation | Full translation |
| Bicycle-light starter and universal prompt template on the README | English | Translated | Translated |
| Four illustrated highlights, source links and image destinations | Full | Full translation | Full translation |
| Flyne overview, four FLAQ API recommendations and affiliate section | Full | Full translation | Full translation |
| 52 linked production recipes | Canonical English source | English source linked | English source linked |
| Linked X notes and supplementary exercises | Shared documents | Shared documents | Shared documents |

The English README is the source for all 14 translations. This scope covers the complete homepage, not translations of every linked document or all 52 recipe files. Model-dialogue support remains separate from documentation language.

## Keeping translations aligned

1. Update `README.md`; update shared brand copy in `data/locales.json` and case data in `data/x-cases.json` when needed.
2. Run `python3 scripts/build_brand_sections.py` and `python3 scripts/build_gallery.py` to finish the English source.
3. Review and update every translation map in `data/readme-translations/`. Keys are exact English text segments. Translate new or changed segments and update `source_sha256` only after reviewing the new source. These files include translated image descriptions and both homepage prompt blocks.
4. Run `python3 scripts/build_readme_translations.py` to rebuild the other 14 READMEs. Do not edit their generated bodies directly.
5. Run all three generators with `--check`, then `python3 scripts/check_readme_parity.py`, `python3 scripts/check_content.py`, and `git diff --check`.

The parity check compares heading levels, tables, code-block counts, example cards, links and image destinations. Explicit anchors keep internal links stable after heading translation. The source hash flags subsequent English edits. These checks detect omissions and structural drift; they do not prove translation fluency.

## Shared prompt labels

Use the same block order in any language. Models often handle clear labels better than prose with mixed purposes.

| Meaning | EN | 简中 | 日本語 | 한국어 | ES |
|---|---|---|---|---|---|
| Output | `[OUTPUT]` | `[输出]` | `[出力]` | `[출력]` | `[SALIDA]` |
| Continuity anchors | `[CONTINUITY ANCHORS]` | `[连续性锚点]` | `[連続性アンカー]` | `[연속성 앵커]` | `[ANCLAS DE CONTINUIDAD]` |
| World / location | `[WORLD]` | `[空间与环境]` | `[空間・環境]` | `[공간과 환경]` | `[MUNDO Y ESPACIO]` |
| Timed shots | `[TIMED SHOTS]` | `[逐秒镜头]` | `[時間別ショット]` | `[시간별 샷]` | `[PLANOS POR TIEMPO]` |
| Performance | `[PERFORMANCE]` | `[表演]` | `[演技]` | `[연기]` | `[INTERPRETACIÓN]` |
| Audio | `[AUDIO]` | `[声音]` | `[音声]` | `[오디오]` | `[AUDIO]` |
| Constraints | `[CONSTRAINTS]` | `[约束]` | `[制約]` | `[제약]` | `[RESTRICCIONES]` |

## Localization rules

1. Preserve prompt IDs, character names, timecodes and reference numbering.
2. Translate directing intent, not just individual words.
3. Keep exact spoken dialogue in the intended performance language.
4. Do not turn a documentation language into an unsupported native-audio claim.
5. Keep camera direction and screen direction unambiguous after translation.
6. Localize examples culturally; do not stereotype accents, clothing or behavior.
7. Verify names, numbers, technical terms, packaging and subtitles independently.
8. Add accessible captions in post-production when frame-to-frame text stability matters.
9. When the English README changes a dated model claim or featured external case, update all localized status and case sections in the same pull request; preserve direct source links and the distinction between creator tests and official specifications.

## Template for any language

```text
[OUTPUT / LOCALIZED LABEL]
{duration}; {aspect ratio}; {single take or multi-shot}; {visual finish}.

[CONTINUITY]
{named adult subject, stable face/hair/silhouette/wardrobe};
{product or prop shape, material, color, markings}. Keep unchanged.

[WORLD]
{location, time, weather, practical light, starting positions}.

[TIMED SHOTS]
0–{x}s — {shot size, angle, camera path}. {one primary action}. {physical response}.
{x}–{y}s — {next shot}. {one primary action}. {payoff and final frame}.

[AUDIO]
{speaker} ({language, tone, pace}): “{short exact line}”
{ambience}; {synchronized foley}; {music entry/exit}.

[CONSTRAINTS]
Preserve identity, geometry, direction and lighting. One speaking mouth at a time.
No unrequested text, translation, subtitles, logos, watermarks or extra objects.
```

## Contributing a localization

Before adding a language, translate one complete prompt and compare it with the canonical English version for timing, camera path, identity anchors, audio ownership and constraints. Ask a fluent reviewer to check both naturalness and technical meaning. See [CONTRIBUTING.md](../CONTRIBUTING.md).
