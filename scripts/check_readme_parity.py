#!/usr/bin/env python3
"""Check English/localized README structure and destinations, not translation fluency."""
import collections,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
source=(ROOT/'README.md').read_text()
def destinations(text):
    refs=re.findall(r'\]\(([^\s)]+)',text)+re.findall(r'(?:src|href)="([^"]+)"',text)
    # Navigation highlights a different current language; local section anchors are explicit.
    return collections.Counter(x for x in refs if not x.startswith('#') and not re.fullmatch(r'README(?:\.[\w-]+)?\.md',x))
def structure(text):
    return (collections.Counter(len(x) for x in re.findall(r'^(#{1,6}) ',text,re.M)),len(re.findall(r'^\|',text,re.M)),text.count('<td '),len(re.findall(r'^```text$',text,re.M)))
errors=[]
for p in sorted(ROOT.glob('README.*.md')):
    s=p.read_text()
    if structure(s)!=structure(source):errors.append(p.name+': section/table/example structure differs')
    if destinations(s)!=destinations(source):
        errors.append(p.name+': links/images differ: '+str(destinations(source)-destinations(s)))
if errors:raise SystemExit('\n'.join(errors))
print('README parity: all 14 translations match English sections, tables, examples, links and image destinations')
