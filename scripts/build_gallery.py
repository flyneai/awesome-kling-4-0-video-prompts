#!/usr/bin/env python3
"""Build bilingual source notes, remote-media gallery and homepage previews."""
import html,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
    cases=json.loads((ROOT/'data/x-cases.json').read_text())
    count=len(cases); added=sum(c['is_new'] for c in cases)
    intro=f'{count} creator cases: {count-added} inherited from the source collection and {added} added by Flyne AI. Each record gives its own check date and method. New cases were checked through the FxTwitter public mirror on 2026-09-30, not through a signed-in X session. Model names are creator claims. Full prompts are linked only when published. No independent video generation or full playback-quality audit was performed.'
    zh=f'共 {count} 个创作者案例：{count-added} 个继承自源库，{added} 个由 Flyne AI 新增。新案例于 2026-09-30 通过 FxTwitter 公开镜像读取，未在登录后的 X 页面核验。各条保留核验日期与方法，模型名称为作者自述。完整提示词仅在作者公开时提供链接；没有独立生成复测或完整播放质量评估。'
    md=['# Kling 4.0 / Flash: X videos and prompt lessons','[Home](../README.md) · [中文](../README.zh-CN.md) · [4 inherited exercises](../prompts/inherited-flash-exercises.md) · [2 Flyne exercises](../prompts/flyne-practice.md) · [HTML gallery](gallery.html)',intro,zh,'External videos and thumbnails belong to their authors and are not covered by MIT. Click a preview for the original post, or use the video link. HTML playback requires opening the downloaded gallery in a browser; GitHub displays its source. Upload duration and dimensions are not verified generation settings. / 外部视频与缩略图保留原作者权利，不属于 MIT 授权内容。预览图链接原帖，另附视频直链。上传时长与尺寸不能当作生成参数。']
    cards=[]
    for c in cases:
        evidence=f'{c["checked"]} · {c["verification"]} · '+('Flyne addition / 本次新增' if c['is_new'] else 'Inherited record / 继承记录')
        md += [f'## {c["title"]} / {c["title_zh"]}',f'**Creator:** [{c["creator"]} (@{c["handle"]})]({c["url"]})\n\n**Evidence:** {evidence}\n\n**Model claim:** {c["model_claim"]}',c['lesson']+'\n\n'+c['lesson_zh']]
        media=[];links=[]
        for n,v in enumerate(c['videos'],1):
            md += [f'[![{c["title"]}]({v["poster"]})]({c["url"]})',f'[Watch video / 观看视频]({v["url"]}) · {v["duration"]}s · {v["width"]}×{v["height"]} (upload metadata)']
            media.append(f'<video controls preload="none" playsinline poster="{html.escape(v["poster"])}"><source src="{html.escape(v["url"])}" type="video/mp4"></video><p><a href="{html.escape(v["url"])}">Open video / 观看视频</a></p>')
        if c['prompt_url']:
            md.append(f'[Creator prompt / 作者提示词]({c["prompt_url"]})');links.append(f'<a href="{c["prompt_url"]}">Creator prompt / 作者提示词</a>')
        else:md.append('**Full prompt not published in this record / 此记录没有公开完整提示词。**')
        if c['exercise']:
            label='Flyne original practice / Flyne 原创练习' if c['is_new'] else 'Inherited practice / 继承练习'
            md.append(f'[{label}]({c["exercise"]}) — not render-tested / 未实测')
            public='https://github.com/flyneai/awesome-kling-4-0-video-prompts/blob/main/'+c['exercise'].removeprefix('../')
            links.append(f'<a href="{public}">{label}</a>')
        cards.append(f'<article><h2>{html.escape(c["title"])}</h2><p>{html.escape(c["title_zh"])}</p><p><a href="{c["url"]}">@{c["handle"]} · X</a></p><p>{html.escape(c["model_claim"])}</p>'+''.join(media)+f'<p>{html.escape(c["lesson"])}</p><p>{html.escape(c["lesson_zh"])}</p><p>{html.escape(evidence)}</p><p>'+ ' · '.join(links)+'</p></article>')
    outputs={ROOT/'docs/X-VIDEOS.md':'\n\n'.join(md)+'\n'}
    outputs[ROOT/'docs/gallery.html']='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Flyne AI — Kling video examples</title><style>body{margin:0;background:#101927;color:#e8eef8;font:16px/1.6 system-ui}header,main,footer{max-width:1100px;margin:auto;padding:24px}a{color:#85dcff}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,420px),1fr));gap:24px}article{padding:20px;background:#1c2a3d;border-radius:12px}video{width:100%;max-height:380px}h1{font-size:36px}h2{font-size:22px}</style><header><p>FLYNE AI · COMMUNITY EXAMPLES</p><h1>Kling 4.0 / Flash: videos & prompt lessons</h1><p>'''+html.escape(intro)+'</p><p>'+html.escape(zh)+'''</p><a href="https://flyne.ai/model/kling-4-0/">Flyne AI</a></header><main>'''+''.join(cards)+'''</main><footer>External creator media, not Flyne generation results. Outside the repository MIT license. If playback fails, use the original X post.</footer></html>\n'''
    for lang,name in [('en','README.md'),('zh','README.zh-CN.md')]:
        p=ROOT/name;s=p.read_text()
        block='<!-- video-showcase:start -->\n## '+('Watch a test, then try a prompt' if lang=='en' else '先看案例，再复制提示词')+'\n\n'
        block+=('12 source-linked videos: 10 inherited cases plus two new dialogue and music-workflow cases. Original prompts are linked where available; separate exercises are untested.' if lang=='en' else '12 个带来源的视频案例：10 个继承案例，加上双人对白与音乐流程两个新案例。原提示词仅在作者公开时提供链接，另写练习均未实测。')+'\n\n'
        block+='<table><tr>\n'
        for i,c in enumerate(cases[6:]):
            if i and i%2==0:block+='</tr></table>\n\n<table><tr>\n'
            v=c['videos'][0];title=c['title'] if lang=='en' else c['title_zh']
            source=f'<a href="{c["prompt_url"]}">Creator prompt / 原提示词</a>' if c['prompt_url'] else 'Full prompt unavailable / 未公开完整提示词'
            block+=f'<td width="450" valign="top"><a href="{c["url"]}"><img src="{v["poster"]}" width="450" alt="{html.escape(title)}"></a><br><strong>{html.escape(title)}</strong><br><a href="{c["url"]}">@{c["handle"]} · X</a><br>{source}<br><a href="{c["exercise"].removeprefix("../")}">Separate practice / 另写练习</a></td>\n'
        block+='</tr></table>\n\n[All 12 cases / 全部案例](docs/X-VIDEOS.md) · [4 inherited exercises / 继承练习](prompts/inherited-flash-exercises.md) · [2 Flyne exercises / 新增练习](prompts/flyne-practice.md)\n<!-- video-showcase:end -->'
        outputs[p]=re.sub(r'<!-- video-showcase:start -->[\s\S]*?<!-- video-showcase:end -->',lambda m:block,s)
    changed=[]
    for p,out in outputs.items():
        if not p.exists() or p.read_text()!=out:
            changed.append(str(p.relative_to(ROOT)))
            if '--check' not in sys.argv:p.write_text(out)
    if '--check' in sys.argv and changed:raise SystemExit('Out of date: '+', '.join(changed))
    print(f'Gallery: {count} cases, {len(changed)} files changed')
if __name__=='__main__':main()
