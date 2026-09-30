#!/usr/bin/env python3
"""Build bilingual source notes, remote-media gallery and homepage previews."""
import html,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
    cases=json.loads((ROOT/'data/x-cases.json').read_text())
    count=len(cases); added=sum(c['is_new'] for c in cases)
    intro=f'{count} creator cases: {count-added} inherited from the source collection and {added} added by Flyne AI. Each record gives its own check date and method. New records were checked on 2026-09-30 through the FxTwitter public mirror; selected prompt replies were also read on public X pages. Each record identifies its method. Model names are creator claims. Prompt links distinguish published text from partial screenshots. No independent video generation or full playback-quality audit was performed.'
    zh=f'共 {count} 个创作者案例：{count-added} 个继承自源库，{added} 个由 Flyne AI 新增。新记录于 2026-09-30 通过 FxTwitter 公开镜像读取，其中部分提示词回复也在 X 公开页面核对；各条注明具体方法。各条保留核验日期与方法，模型名称为作者自述。提示词链接区分完整文本与局部截图；没有独立生成复测或完整播放质量评估。'
    md=['# Kling 4.0 / Flash: X videos and prompt lessons','[Home](../README.md) · [中文](../README.zh-CN.md) · [4 inherited exercises](../prompts/inherited-flash-exercises.md) · [2 Flyne exercises](../prompts/flyne-practice.md) · [4 new exercises](../prompts/x-inspired-practice.md) · [HTML gallery](gallery.html)',intro,zh,
        'Media check (2026-09-30): the six latest video URLs returned HTTP 200; their thumbnail requests returned HTTP 403 in this environment. If previews do not load, follow the original X links. / 本轮六条视频直链可访问，缩略图请求返回 403；预览无法显示时请打开 X 原帖。',
        'External videos and thumbnails belong to their authors and are not covered by MIT. Click a preview for the original post, or use the video link. HTML playback requires opening the downloaded gallery in a browser; GitHub displays its source. Upload duration and dimensions are not verified generation settings. / 外部视频与缩略图保留原作者权利，不属于 MIT 授权内容。预览图链接原帖，另附视频直链。上传时长与尺寸不能当作生成参数。']
    cards=[]
    for c in cases:
        evidence=f'{c["checked"]} · {c["verification"]} · '+('Flyne addition / 本次新增' if c['is_new'] else 'Inherited record / 继承记录')
        md += [f'## {c["title"]} / {c["title_zh"]}',f'**Creator:** [{c["creator"]} (@{c["handle"]})]({c["url"]})\n\n**Evidence:** {evidence}\n\n**Model claim:** {c["model_claim"]}',c['lesson']+'\n\n'+c['lesson_zh']]
        media=[];links=[]
        for n,v in enumerate(c['videos'],1):
            md += [f'[![{c["title"]}]({v["poster"]})]({c["url"]})',f'[Watch video / 观看视频]({v["url"]}) · {v["duration"]}s · {v["width"]}×{v["height"]} (upload metadata)']
            media.append(f'<video controls preload="none" playsinline poster="{html.escape(v["poster"])}"><source src="{html.escape(v["url"])}" type="video/mp4"></video><p><a href="{html.escape(v["url"])}">Open video / 观看视频</a></p>')
        if c['prompt_url']:
            if c['prompt_status']=='partial-screenshot-at-source':
                md.append('**Partial prompt screenshot only / 仅有局部提示词截图。**')
            label='Partial prompt screenshot / 局部提示词截图' if c['prompt_status']=='partial-screenshot-at-source' else 'Creator prompt / 作者提示词'
            md.append(f'[{label}]({c["prompt_url"]})');links.append(f'<a href="{c["prompt_url"]}">{label}</a>')
        else:md.append('**Full prompt not published in this record / 此记录没有公开完整提示词。**')
        if c['exercise']:
            label='Flyne original practice / Flyne 原创练习' if c['is_new'] else 'Inherited practice / 继承练习'
            md.append(f'[{label}]({c["exercise"]}) — not render-tested / 未实测')
            public='https://github.com/flyneai/awesome-kling-4-0-video-prompts/blob/main/'+c['exercise'].removeprefix('../')
            links.append(f'<a href="{public}">{label}</a>')
        cards.append(f'<article><h2>{html.escape(c["title"])}</h2><p>{html.escape(c["title_zh"])}</p><p><a href="{c["url"]}">@{c["handle"]} · X</a></p><p>{html.escape(c["model_claim"])}</p>'+''.join(media)+f'<p>{html.escape(c["lesson"])}</p><p>{html.escape(c["lesson_zh"])}</p><p>{html.escape(evidence)}</p><p>'+ ' · '.join(links)+'</p></article>')
    outputs={ROOT/'docs/X-VIDEOS.md':'\n\n'.join(md)+'\n'}
    outputs[ROOT/'docs/gallery.html']='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Flyne AI — Kling video examples</title><style>body{margin:0;background:#101927;color:#e8eef8;font:16px/1.6 system-ui}header,main,footer{max-width:1100px;margin:auto;padding:24px}a{color:#85dcff}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,420px),1fr));gap:24px}article{padding:20px;background:#1c2a3d;border-radius:12px}video{width:100%;max-height:380px}h1{font-size:36px}h2{font-size:22px}</style><header><p>FLYNE AI · COMMUNITY EXAMPLES</p><h1>Kling 4.0 / Flash: videos & prompt lessons</h1><p>'''+html.escape(intro)+'</p><p>'+html.escape(zh)+'''</p><a href="https://flyne.ai/model/kling-4-0/">Flyne AI</a></header><main>'''+''.join(cards)+'''</main><footer>External creator media, not Flyne generation results. Outside the repository MIT license. If playback fails, use the original X post.</footer></html>\n'''
    for lang,name in [('en','README.md')]:
        p=ROOT/name;s=p.read_text()
        block='<!-- video-showcase:start -->\n## '+('Watch a test, then try a prompt' if lang=='en' else '先看案例，再复制提示词')+'\n\n'
        block+=(f'{count} source-linked cases. Explore the newest examples below, follow published prompt text or labeled screenshots, then try the separate original exercises.' if lang=='en' else f'{count} 个带来源的案例。下面展示本轮新增内容，可查看作者公开的提示词或注明不完整的截图，再尝试另写的原创练习。')+'\n\n'
        block+='<table><tr>\n'
        for i,c in enumerate(cases[-6:]):
            if i and i%2==0:block+='</tr></table>\n\n<table><tr>\n'
            v=c['videos'][0];title=c['title'] if lang=='en' else c['title_zh']
            source=f'<a href="{c["prompt_url"]}">Creator prompt</a>' if c['prompt_url'] else 'Full prompt unavailable'
            if c['prompt_status']=='partial-screenshot-at-source':source=source.replace('Creator prompt','Partial prompt screenshot')
            block+=f'<td width="450" valign="top"><a href="{c["url"]}"><img src="{v["poster"]}" width="450" alt="{html.escape(title)}"></a><br><strong>{html.escape(title)}</strong><br><a href="{c["url"]}">@{c["handle"]} · X</a><br>{source}<br><a href="{c["exercise"].removeprefix("../")}">Separate practice</a></td>\n'
        block+='</tr></table>\n\n[All cases](docs/X-VIDEOS.md) · [4 inherited exercises](prompts/inherited-flash-exercises.md) · [2 Flyne exercises](prompts/flyne-practice.md) · [4 new exercises](prompts/x-inspired-practice.md)\n<!-- video-showcase:end -->'
        outputs[p]=re.sub(r'<!-- video-showcase:start -->[\s\S]*?<!-- video-showcase:end -->',lambda m:block,s)
    changed=[]
    for p,out in outputs.items():
        if not p.exists() or p.read_text()!=out:
            changed.append(str(p.relative_to(ROOT)))
            if '--check' not in sys.argv:p.write_text(out)
    if '--check' in sys.argv and changed:raise SystemExit('Out of date: '+', '.join(changed))
    print(f'Gallery: {count} cases, {len(changed)} files changed')
if __name__=='__main__':main()
