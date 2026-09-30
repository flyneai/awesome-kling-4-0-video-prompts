#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update shared brand and affiliate sections from data/locales.json."""
import json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
    changed=[]
    for locale,row in json.loads((ROOT/'data/locales.json').read_text()).items():
        p=ROOT/('README.md' if locale=='en' else f'README.{locale}.md')
        s=p.read_text()
        block='<!-- brand-footer:start -->\n<a id="flyne"></a>\n\n## '+row[0]+'\n\n'+row[1]+'\n\n['+row[8]+'](docs/FLYNE.md)\n\n## '+row[2]+'\n\n'+row[3]+'\n\n## '+row[4]+'\n\n'+row[5]+'\n<!-- brand-footer:end -->\n'
        intro='<!-- brand-intro:start -->\n['+row[0]+'](https://flyne.ai/model/kling-4-0/) · ['+row[6]+'](docs/X-VIDEOS.md) · ['+row[7]+'](prompts/inherited-flash-exercises.md)\n\n'+row[1]+'\n<!-- brand-intro:end -->'
        s=re.sub(r'<!-- brand-intro:start -->[\s\S]*?<!-- brand-intro:end -->',lambda m:intro,s)
        out=re.sub(r'<!-- brand-footer:start -->[\s\S]*?<!-- brand-footer:end -->\n?',lambda m:block,s) if '<!-- brand-footer:start -->' in s else s.rstrip()+'\n\n'+block
        if out!=p.read_text():
            changed.append(p.name)
            if '--check' not in sys.argv:p.write_text(out)
    if '--check' in sys.argv and changed:raise SystemExit('Out of date: '+', '.join(changed))
    print(f'Brand sections: {len(changed)} changed')
if __name__=='__main__':main()
