#!/usr/bin/env python3
"""Copy the canonical policies to their existing App Store and in-app URLs.

Usage: python3 scripts/sync_legal.py /path/to/feedfare-legal /path/to/nickrae-site
No Git operations or publishing are performed.
"""
from pathlib import Path
import argparse
import shutil

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('legal_repo', type=Path)
parser.add_argument('personal_repo', type=Path)
args = parser.parse_args()
root = Path(__file__).resolve().parent.parent
targets = [(args.legal_repo, 'privacy-policy.html'),
           (args.personal_repo / 'feedfare', 'privacy.html')]
for target, privacy_name in targets:
    if not (target / privacy_name).is_file() or not (target / 'terms.html').is_file():
        raise SystemExit(f'Expected existing FeedFare policies in {target}')
for target, privacy_name in targets:
    for source, destination in [('privacy-policy.html', privacy_name), ('terms.html', 'terms.html')]:
        shutil.copyfile(root / source, target / destination)
    assets = target / 'assets'
    assets.mkdir(exist_ok=True)
    for name in ['site.css', 'app-icon-64.webp', 'app-icon-128.webp', 'favicon.png', 'apple-touch-icon.png']:
        shutil.copyfile(root / 'assets' / name, assets / name)
    print(f'Synced policies and five scoped assets to {target}')
