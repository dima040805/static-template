#!/usr/bin/env python3
"""Fix GitBook markdown artifacts: leads, headings, escapes."""

from __future__ import annotations

import re
import sys
from pathlib import Path

LEAD_TO_HEADING = re.compile(r'(</p>)\n(#{1,6}\s)', re.MULTILINE)
HEADING_ESCAPE = re.compile(r'^(?P<hashes>#{1,6}\s+)(?P<title>.+)$', re.MULTILINE)


def fix_lead_spacing(text: str) -> tuple[str, int]:
    new_text, count = LEAD_TO_HEADING.subn(r'\1\n\n\2', text)
    return new_text, count


def fix_heading_escapes(text: str) -> tuple[str, int]:
    count = 0

    def replacer(match: re.Match[str]) -> str:
        nonlocal count
        title = match.group('title')
        if '\\_' not in title and '\\*' not in title:
            return match.group(0)
        count += 1
        cleaned = title.replace('\\_', '_').replace('\\*', '*')
        return f'{match.group("hashes")}{cleaned}'

    return HEADING_ESCAPE.sub(replacer, text), count


def fix_text(text: str) -> tuple[str, dict[str, int]]:
    stats: dict[str, int] = {}
    text, stats['lead_spacing'] = fix_lead_spacing(text)
    text, stats['heading_escapes'] = fix_heading_escapes(text)
    return text, stats


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else 'ru')
    totals: dict[str, int] = {}
    changed_files = 0

    for md_file in sorted(root.rglob('*.md')):
        original = md_file.read_text(encoding='utf-8')
        updated, stats = fix_text(original)
        if updated == original:
            continue
        md_file.write_text(updated, encoding='utf-8')
        changed_files += 1
        parts = ', '.join(f'{k}={v}' for k, v in stats.items() if v)
        print(f'{md_file.relative_to(root)}: {parts}')
        for key, value in stats.items():
            totals[key] = totals.get(key, 0) + value

    print(f'\nUpdated {changed_files} files')
    for key, value in sorted(totals.items()):
        print(f'  {key}: {value}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
