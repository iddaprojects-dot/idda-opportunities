"""Validate data.json before every commit: python3 tools/validate.py"""
import json, sys, re, datetime
d = json.load(open('data.json'))
err = []
ORG_REQ = ['id','c','type','title','funder','emoji','amount','who','req','how','tip','url']
Y_REQ = ['id','cat','title','by','emoji','get','who','url','el']
TYPES = {'eu','intl','regional','national','embassy','bilateral','foundation'}
CATS = {'scholar','lead','startup','travel','train'}
ST = {'upcoming','later','watch','rolling'}
def chk_date(s, where):
    if not s: return
    try: datetime.datetime.fromisoformat(s.replace('Z','+00:00'))
    except Exception: err.append(f'{where}: bad date {s!r}')
for key, req in (('org', ORG_REQ), ('youth', Y_REQ)):
    ids = set()
    for it in d.get(key, []):
        w = f"{key}:{it.get('id')}"
        for k in req:
            if k not in it: err.append(f'{w}: missing {k}')
        if it.get('id') in ids: err.append(f'{w}: duplicate id')
        ids.add(it.get('id'))
        chk_date(it.get('deadline'), w); chk_date(it.get('opens'), w)
        if not it.get('deadline') and it.get('st') not in ST: err.append(f'{w}: no deadline needs st in {ST}')
        if key == 'org' and it.get('type') not in TYPES: err.append(f'{w}: bad type')
        if key == 'youth' and it.get('cat') not in CATS: err.append(f'{w}: bad cat')
        if not str(it.get('url','')).startswith('https://'): err.append(f'{w}: url must be https')
if len(d.get('org', [])) < 10 or len(d.get('youth', [])) < 10: err.append('too few items: refusing (page would look empty)')
if err:
    print('\n'.join(err)); sys.exit(1)
print(f"OK: {len(d['org'])} org, {len(d['youth'])} youth, checked {d.get('checked')}")
