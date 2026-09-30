#!/usr/bin/env python3
"""Render localized READMEs from English structure and reviewed translation maps.

No network calls. Update translations whenever --check reports changed source text.
Run after build_brand_sections.py and build_gallery.py.
"""
import hashlib, html, json, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
LOCALES=json.loads((ROOT/'data/locales.json').read_text())
# Preserve syntax, destinations and inline technical identifiers, translating labels.
TOKEN=re.compile(r'(!?\[)([^\]\n]*)(\]\([^\n]*?\))|(<[^>]+>)|(`[^`]+`)|(\*\*|\*|\|)')
def fragments(line):
    pos=0
    for m in TOKEN.finditer(line):
        if m.start()>pos:yield False,line[pos:m.start()]
        if m.group(1):
            yield True,m.group(1);yield False,m.group(2);yield True,m.group(3)
        else:yield True,m.group(0)
        pos=m.end()
    if pos<len(line):yield False,line[pos:]
def source_parts(source):
    # Existing localized brand data remains authoritative for shared sections.
    source=re.sub(r'<!-- brand-(intro|footer):start -->[\s\S]*?<!-- brand-\1:end -->',lambda m:'@@BRAND_'+m.group(1).upper()+'@@',source)
    return source.splitlines(keepends=True)
def is_literal(line):
    t=line.strip()
    return not t or t.startswith(('@@BRAND_','<!--','```','~~~','[![','|---','> [!')) or '**English**' in line

def units(source):
    out=[]
    for line in source_parts(source):
        if is_literal(line):continue
        line=re.sub(r'^(#{1,6} |[-+] |\d+\. |> )','',line)
        for literal,s in fragments(line):
            s=s.strip()
            if not literal and re.search(r'[A-Za-z]',s) and s not in out:out.append(s)
    return out

def brand(kind,row):
    if kind=='INTRO':body='['+row[0]+'](https://flyne.ai/model/kling-4-0/) · ['+row[6]+'](docs/X-VIDEOS.md) · ['+row[7]+'](prompts/inherited-flash-exercises.md)\n\n'+row[1]
    else:body='<a id="flyne"></a>\n\n## '+row[0]+'\n\n'+row[1]+'\n\n['+row[8]+'](docs/FLYNE.md)\n\n## '+row[2]+'\n\n'+row[3]+'\n\n## '+row[4]+'\n\n'+row[5]
    return '<!-- brand-'+kind.lower()+':start -->\n'+body+'\n<!-- brand-'+kind.lower()+':end -->\n'

def render(source,locale,translations):
    out=[]
    for line in source_parts(source):
        marker=re.fullmatch(r'@@BRAND_(INTRO|FOOTER)@@\n?',line)
        if marker:out.append(brand(marker[1],LOCALES[locale]));continue
        if '**English**' in line:
            line=line.replace('**English**','[English](README.md)')
            line=re.sub(r'\[([^]]+)\]\(README\.'+re.escape(locale)+r'\.md\)',r'**\1**',line)
            out.append(line);continue
        if is_literal(line):out.append(line);continue
        header=re.match(r'^(#{1,6}) (.+)',line)
        if header:
            slug=re.sub(r'[^\w\- ]','',header[2].lower()).replace(' ','-')
            out.append('<a id="'+slug+'"></a>\n')
        prefix=re.match(r'^(#{1,6} |[-+] |\d+\. |> )',line)
        pre=prefix[0] if prefix else ''
        body=line[len(pre):];segments=[]
        for literal,s in fragments(body):
            if literal:
                # Translate image alt labels without changing image paths or layout.
                s=re.sub(r'alt="([^"]*)"',lambda m:'alt="'+html.escape(translations.get(html.unescape(m[1]),html.unescape(m[1])),quote=True)+'"',s)
                segments.append(s)
            else:
                key=s.strip();value=translations.get(key,key)
                segments.append(s[:len(s)-len(s.lstrip())]+value+s[len(s.rstrip()):] if key else s)
        out.append(pre+''.join(segments))
    return ''.join(out)

def main():
    source=(ROOT/'README.md').read_text();required=units(source);changed=[]
    for locale in LOCALES:
        if locale=='en':continue
        p=ROOT/'data/readme-translations'/f'{locale}.json'
        data=json.loads(p.read_text());mapping=data['translations']
        missing=[s for s in required if s not in mapping or not mapping[s].strip()]
        if missing:raise SystemExit(f'{locale}: {len(missing)} untranslated source segments: {missing[:3]}')
        for text in required:
            for ratio in re.findall(r'\b\d+:\d+\b',text):
                if ratio not in mapping[text]:raise SystemExit(locale+': ratio/time marker changed: '+text)
        if data['source_sha256']!=hashlib.sha256(source.encode()).hexdigest():raise SystemExit(locale+': English source changed; review and refresh translations')
        dest=ROOT/f'README.{locale}.md';result=render(source,locale,mapping)
        if dest.read_text()!=result:
            changed.append(dest.name)
            if '--check' not in sys.argv:dest.write_text(result)
    if '--check' in sys.argv and changed:raise SystemExit('Out of date: '+', '.join(changed))
    print(f'README translations: {len(LOCALES)-1} languages, {len(required)} source segments, {len(changed)} changed')
if __name__=='__main__':main()
