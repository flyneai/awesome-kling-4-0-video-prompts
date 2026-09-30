#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Check local links/anchors, inherited recipes, provenance and gallery contracts."""
import hashlib,json,re,sys
from pathlib import Path
from urllib.parse import unquote,urlsplit
ROOT=Path(__file__).resolve().parents[1]
errors=[]
def require(ok,msg):
    if not ok:errors.append(msg)
def anchors(text):
    out=set(re.findall(r'<a\s+id="([^"]+)"',text));seen={}
    for title in re.findall(r'^#{1,6} (.+)$',text,re.M):
        title=re.sub(r'\[([^]]+)\]\([^)]*\)',r'\1',title)
        slug=re.sub(r'[^\w\- ]','',title.lower()).replace(' ','-')
        n=seen.get(slug,0);seen[slug]=n+1
        out.add(slug+(f'-{n}' if n else ''))
    return out
files=list(ROOT.rglob('*.md')); count=0
for p in files:
    s=p.read_text()
    body=re.sub(r'(`{3,}|~{3,})[^\n]*\n[\s\S]*?\1','',s)
    urls=re.findall(r'\]\(([^\s)]+)(?:\s+"[^\"]*")?\)',body)+re.findall(r'(?:href|src)="([^"]+)"',body)
    for raw in urls:
        u=urlsplit(raw)
        if u.scheme or u.netloc:continue
        target=(p.parent/unquote(u.path)).resolve() if u.path else p
        require(target.exists(),f'{p.relative_to(ROOT)}: missing {raw}')
        if target.exists() and target.suffix=='.md' and u.fragment:
            require(unquote(u.fragment) in anchors(target.read_text()),f'{p.relative_to(ROOT)}: missing anchor {raw}')
        count+=1
manifest=json.loads((ROOT/'data/upstream-prompts.json').read_text())
total=0
for name,hashes in manifest['files'].items():
    blocks=re.findall(r'```text\n([\s\S]*?)```',(ROOT/name).read_text())
    require([hashlib.sha256(x.encode()).hexdigest() for x in blocks]==hashes,name+': inherited prompt altered')
    total+=len(blocks)
require(total==52,f'Expected 52 inherited recipes, got {total}')
new=re.findall(r'```text\n([\s\S]*?)```',(ROOT/'prompts/inherited-flash-exercises.md').read_text())
require(len(new)==4,'Expected 4 inherited exercises')
flyne=re.findall(r'```text\n([\s\S]*?)```',(ROOT/'prompts/flyne-practice.md').read_text())
require(len(flyne)==2,'Expected 2 Flyne practice prompts')
for name in ROOT.glob('README*.md'):
    s=name.read_text()
    for x in ['https://flyne.ai/model/kling-4-0/','https://flyne.ai/affiliate-program/','Kling 3.0 Turbo','https://flaq.ai/models/kuaishou/kling-4-0-text-to-video/','https://flaq.ai/models/kuaishou/kling-4-0-image-to-video/','Coming Soon','assets/images/flyne-kling-cover.png']:
        require(x in s,f'{name.name}: missing {x}')
    require(s.rstrip().endswith('<!-- brand-footer:end -->'),name.name+': brand footer misplaced')
    require('https://github.com/flaqai/awesome-kling-4-0' not in s,name.name+': obsolete adaptation introduction')
    require(s.count('<!-- brand-intro:start -->')==1,name.name+': duplicate brand intro')
cases=json.loads((ROOT/'data/x-cases.json').read_text())
require(len(cases)==len({c['id'] for c in cases})==12,'Duplicate or missing cases')
require(sum(c['is_new'] for c in cases)==2,'Expected 2 added X cases')
for c in cases:
    require(c['checked'] and c['verification'] and c['rights'],c['id']+': missing provenance')
    if c['is_new']:require(c['exercise'] and c['videos'] and c['model_claim'],c['id']+': incomplete new case')
    for v in c['videos']:
        require(urlsplit(v['url']).hostname=='video.twimg.com',c['id']+': unexpected video source')
        require(urlsplit(v['poster']).hostname=='pbs.twimg.com',c['id']+': unexpected thumbnail source')
license=(ROOT/'LICENSE').read_text();require('2026 Flaq AI' in license and '2026 aivideoweb' in license,'Copyright notices missing')
if errors:print('\n'.join(errors));sys.exit(1)
print(f'OK: {len(files)} Markdown files, {count} local links, {total} inherited + {len(new)} inherited exercises + {len(flyne)} Flyne exercises, {len(cases)} X cases')
