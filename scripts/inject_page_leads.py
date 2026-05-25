#!/usr/bin/env python3
"""Insert visible page descriptions from frontmatter as GitBook-style leads."""

from __future__ import annotations

import re
import sys
from pathlib import Path

FRONTMATTER = re.compile(r'^---\s*\n(?P<meta>.*?)\n---\s*\n', re.DOTALL)
DESCRIPTION = re.compile(r'^description:\s*(?P<value>.+?)\s*$', re.MULTILINE)
H1 = re.compile(r'^#\s+.+\s*$', re.MULTILINE)
NOTE_BLOCK = re.compile(
    r'\{%\s*note\s+(?:info|tip|warning|alert)(?:\s+"[^"]*")?\s*%\}\s*'
    r'.*?\{%\s*endnote\s*%\}',
    re.DOTALL,
)
LEAD_HTML = re.compile(r'\n<p class="yfm-lead">(?P<text>.*?)</p>\s*', re.DOTALL)


def parse_description(meta: str) -> str | None:
    match = DESCRIPTION.search(meta)
    if not match:
        return None
    value = match.group('value').strip()
    if value.startswith('>-'):
        return None
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        value = value[1:-1]
    value = value.strip()
    return value or None


def has_lead(body: str, description: str) -> bool:
    if 'class="yfm-lead"' in body or "class='yfm-lead'" in body:
        return True
    return description in body


def lead_html(description: str) -> str:
    return f'\n\n<p class="yfm-lead">{description}</p>\n\n'


def extract_lead_blocks(body: str) -> tuple[str, list[str]]:
    leads: list[str] = []

    def replacer(match: re.Match[str]) -> str:
        leads.append(match.group('text').strip())
        return '\n'

    cleaned = LEAD_HTML.sub(replacer, body)
    cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)
    return cleaned, leads


def first_note_after_h1(body: str, h1_end: int) -> re.Match[str] | None:
    after_h1 = body[h1_end:].lstrip('\n')
    if not after_h1.startswith('{% note'):
        return None
    return NOTE_BLOCK.match(after_h1)


def inject_lead(text: str) -> tuple[str, bool]:
    frontmatter = FRONTMATTER.match(text)
    prefix = text[: frontmatter.end()] if frontmatter else ''
    body = text[frontmatter.end():] if frontmatter else text
    description = parse_description(frontmatter.group('meta')) if frontmatter else None

    body, existing_leads = extract_lead_blocks(body)
    lead_text = existing_leads[0] if existing_leads else description
    if not lead_text:
        return text, False

    h1 = H1.search(body)
    if not h1:
        if existing_leads:
            return prefix + body, True
        return text, False

    if has_lead(body, lead_text) and not existing_leads:
        return text, False

    note_match = first_note_after_h1(body, h1.end())
    if note_match:
        note_end = h1.end() + len(body[h1.end():].lstrip('\n')) - len(
            body[h1.end():].lstrip('\n')
        ) + note_match.end()
        # recalc note_end simpler:
        after_h1_raw = body[h1.end():]
        leading = len(after_h1_raw) - len(after_h1_raw.lstrip('\n'))
        note_end = h1.end() + leading + note_match.end()
        new_body = body[:note_end] + lead_html(lead_text) + body[note_end:].lstrip('\n')
        return prefix + new_body, True

    if has_lead(body, lead_text):
        return prefix + body, bool(existing_leads)

    new_body = body[: h1.end()] + lead_html(lead_text) + body[h1.end():].lstrip('\n')
    return prefix + new_body, True


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else 'ru')
    changed = 0
    for md_file in sorted(root.rglob('*.md')):
        original = md_file.read_text(encoding='utf-8')
        updated, did_change = inject_lead(original)
        if did_change and updated != original:
            md_file.write_text(updated, encoding='utf-8')
            changed += 1
            print(md_file.relative_to(root))
    print(f'\nUpdated {changed} files')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
