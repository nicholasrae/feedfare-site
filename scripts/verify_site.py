#!/usr/bin/env python3
"""Check static publishing regressions without browser automation or dependencies."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import base64, hashlib, json

ROOT = Path(__file__).resolve().parent.parent
class Document(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path, self.tags, self.ids = path, [], set()
        self.feed(path.read_text())
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append((tag, attrs))
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, (self.path.name, 'duplicate id', attrs['id'])
            self.ids.add(attrs['id'])
        assert not any(k.startswith('on') for k in attrs), (self.path.name, 'inline event')

pages = {name: Document(ROOT/name) for name in
         ('index.html', 'privacy-policy.html', 'terms.html', 'support.html', '404.html')}
for name, page in pages.items():
    assert sum(tag == 'h1' for tag, _ in page.tags) == 1, (name, 'h1')
    assert sum(tag == 'main' for tag, _ in page.tags) == 1, (name, 'main')
    assert any(tag == 'a' and a.get('href') == '#main' for tag, a in page.tags), (name, 'skip link')
    assert any(tag == 'link' and a.get('rel') == 'canonical' for tag, a in page.tags), (name, 'canonical')
    for tag, attrs in page.tags:
        if tag == 'img':
            assert all(k in attrs for k in ('alt', 'width', 'height')), (name, 'image sizing/alt')
        urls = [attrs[k] for k in ('href', 'src') if k in attrs]
        urls += [item.strip().split()[0] for item in attrs.get('srcset','').split(',') if item.strip()]
        for url in urls:
            parts = urlsplit(url)
            if parts.scheme in ('mailto','tel') or (parts.netloc and parts.netloc != 'feedfare.app'):
                continue
            target_name = unquote(parts.path).lstrip('/') or (name if not parts.netloc else 'index.html')
            target = ROOT / target_name
            assert target.is_file(), (name, 'missing target', url)
            if parts.fragment and target.suffix == '.html':
                assert parts.fragment in pages[target_name].ids, (name, 'missing anchor', url)
    print('PASS', name, 'landmarks, image metadata, local links, and anchors')

home = (ROOT/'index.html').read_text()
structured = home.split('<script type="application/ld+json">')[1].split('</script>')[0]
assert json.loads(structured)['@type'] == 'SoftwareApplication'
digest = base64.b64encode(hashlib.sha256(structured.encode()).digest()).decode()
assert 'sha256-'+digest in home
assert len([1 for tag, _ in pages['index.html'].tags if tag=='summary']) == 7
resources = {'index.html', 'assets/site.css', 'assets/site.js', 'assets/app-icon-64.webp'}
resources.update('assets/'+name+'-native-800.webp' for name in ('dashboard','activity','stats'))
size = sum((ROOT/p).stat().st_size for p in resources)
assert size < 250_000, ('homepage budget', size)
print('PASS structured data, CSP hash, FAQ controls, homepage max-resolution resource budget:', size, 'bytes')

def luminance(color):
    parts = [int(color[i:i+2],16)/255 for i in (0,2,4)]
    return sum(weight * (v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4)
               for weight,v in zip((.2126,.7152,.0722),parts))
def contrast(a,b):
    x,y = sorted((luminance(a),luminance(b)))
    return (y+.05)/(x+.05)
for foreground, backgrounds in {
    '586576':['f5f6f9','ffffff','eaf0f8','fafbfd'],
    '0865d5':['f5f6f9','ffffff','eaf0f8'],
    '465467':['f5f6f9'], '46566d':['ffffff'],
    'c6d0dd':['18212e'], 'bcdaff':['18212e'],
    'ffffff':['0865d5'], '064caa':['ffffff','e9f2ff']
}.items():
    for background in backgrounds:
        ratio = contrast(foreground, background)
        assert ratio >= 4.5, ('text contrast',foreground,background,ratio)
        print('PASS text contrast', '#'+foreground, 'on', '#'+background, f'{ratio:.2f}:1')
assert contrast('687b95','f5f7fb') >= 3
print('PASS select boundary contrast')
