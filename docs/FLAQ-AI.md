# Kling APIs on FLAQ AI

[Home](../README.md) · [Flyne AI browser workflow](FLYNE.md) · [中文说明](#中文说明)

An API (application programming interface) lets your application request a video and retrieve the result. We recommend exploring FLAQ AI when you want to connect this prompt library to your own app or production workflow. Use Flyne AI for the browser-based workflow.

## Choose an API

| Model page | Input and suggested use | Status checked on 2026-09-30 |
| --- | --- | --- |
| [Kling 4.0 text-to-video API](https://flaq.ai/models/kuaishou/kling-4-0-text-to-video/) | Text descriptions for planned ads, social clips and story scenes. | **Coming Soon**; final parameters and pricing remain to be confirmed. |
| [Kling 4.0 image-to-video API](https://flaq.ai/models/kuaishou/kling-4-0-image-to-video/) | A source image plus motion instructions for planned product or illustration animation. | **Coming Soon**; not a verified callable service yet. |
| [Kling 3.0 Std text-to-video API](https://flaq.ai/models/kuaishou/kling-3-0-std-text-to-video/) | A lower-cost option to evaluate for drafts and multiple variations. | Public API examples and pricing are provided. |
| [Kling 3.0 Pro text-to-video API](https://flaq.ai/models/kuaishou/kling-3-0-pro-text-to-video/) | A quality-focused option to compare with Std using the same prompt. | Public API examples and pricing are provided. |

These are provider descriptions and documentation checks, not our own generation benchmarks or uptime tests. Review current prices, account access and supported settings on the linked page before submitting a paid request. Std and Pro are Kling 3.0 models; their results should not be labeled Kling 4.0.

## Use this library in your application

1. Choose one [recipe](../prompts/README.md). Start with one subject, one action and one camera move. Shorten a multi-shot brief if your selected model cannot accommodate it.
2. Open the selected model page. Test your prompt in its Playground, then use its **API** tab or **Documentation** link for the current request example. Keep the API key on your server, outside public code and browser scripts.
3. For the currently documented 3.0 examples, the request uses `model_name`, `prompt`, `aspect_ratio` and `duration`. The model identifiers are `kling-v3.0-std-text-to-video` and `kling-v3.0-pro-text-to-video`; they differ from the web-page slugs. Copy the current example rather than deriving an identifier from a URL.
4. Save the returned task identifier, check task status and retrieve the resulting video URL after success. Handle errors and use a polling deadline; an accepted request is not a completed video.
5. Record the model, prompt, settings, date and result using the [test record](TEST-RECORD.md). Compare identity, object continuity, camera motion and audio before selecting an output. When comparing Std and Pro, hold the prompt and supported settings constant.
6. When 4.0 opens, check its actual schema and rerun a small test set before switching your application. Do not assume every 3.0 parameter or library prompt transfers unchanged.

## 中文说明

API 就是供程序调用的接口，适合把视频生成接入自己的应用。推荐通过 FLAQ AI 了解 Kling 接口；直接在网页中创作可参考 [Flyne AI 使用步骤](FLYNE.md)。

- **Kling 4.0 文生视频**：用文字规划广告、社交短片或故事镜头。
- **Kling 4.0 图生视频**：准备参考图片，再用提示词安排主体和镜头的运动。
- **Kling 3.0 Std 文生视频**：可优先用于控制预算、试验提示词和制作多个版本。
- **Kling 3.0 Pro 文生视频**：可用于更重视画面质量的项目，先用相同提示词与 Std 对比再选择。

四个入口均在上表。2026-09-30 核对时，两个 4.0 页面仍为 **Coming Soon（即将上线）**，3.0 Std 和 Pro 页面已提供调用示例及价格。本仓库没有进行付费生成或稳定性测试，实际权限、费用与支持参数以官网为准。

接入时，先从本库选一条简单提示词，在模型页面测试，再参考 API 标签页的示例。接口密钥只放在服务器端。3.0 示例的模型名称分别是 `kling-v3.0-std-text-to-video` 和 `kling-v3.0-pro-text-to-video`，不要直接照网页地址拼写。提交后保存任务编号，查询成功状态后再获取视频；设置查询超时并处理失败情况。保留模型、提示词和参数记录，检查人物、道具、运动及声音。等 4.0 开放后，再按实际接口说明重新测试，不能把 3.0 成片标成 4.0 效果。
