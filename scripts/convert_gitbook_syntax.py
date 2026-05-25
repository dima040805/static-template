#!/usr/bin/env python3
"""Convert GitBook-specific syntax to Diplodoc YFM."""

from __future__ import annotations

import re
import sys
from pathlib import Path

HINT_TO_NOTE = {
    'info': 'info',
    'success': 'tip',
    'warning': 'warning',
    'danger': 'alert',
}

CONTENT_REF_LINKS: dict[str, tuple[str, str]] = {
    'mini-kurs': ('Мини-курс', 'Мини-курс/Регистрация_и_личный_кабинет.md'),
    'recepty': ('Рецепты', 'Рецепты/Игра_в_комментариях.md'),
    'sobytiya-scenariya/soobshenie-ot-polzovatelya': (
        'Сообщение от пользователя',
        'Сообщение_от_пользователя.md',
    ),
    'sobytiya-scenariya/net-podkhodyashego-scenariya': (
        'Нет подходящего сценария',
        'Нет_подходящего_сценария.md',
    ),
    'sobytiya-scenariya/pervoe-soobshenie-i-start': (
        'Первое сообщение и старт',
        'Первое_сообщение_и_старт.md',
    ),
    'sobytiya-scenariya/sobytiya-vkontakte': (
        'События ВКонтакте',
        'События_ВКонтакте.md',
    ),
    'sobytiya-scenariya/webhook': ('Webhook', 'Webhook.md'),
    'usloviya/uslovie': ('Условие', 'Условие.md'),
    'usloviya/uslovie-s-variantami': ('Условие с вариантами', 'Условие_с_вариантами.md'),
    'usloviya/proverka-podpiski': ('Проверка подписки', 'Проверка_подписки.md'),
}

HINT_PATTERN = re.compile(
    r'\{%\s*hint\s+style="(?P<style>info|success|warning|danger)"\s*%\}'
    r'(?P<body>.*?)'
    r'\{%\s*endhint\s*%\}',
    re.DOTALL,
)
CONTENT_REF_PATTERN = re.compile(
    r'\{%\s*content-ref\s+url="(?P<url>[^"]+)"\s*%\}\s*'
    r'\[[^\]]*\]\([^)]*\)\s*'
    r'\{%\s*endcontent-ref\s*%\}',
    re.DOTALL,
)
EMBED_PATTERN = re.compile(r'\{%\s*embed\s+url="(?P<url>[^"]+)"\s*%\}')
CODE_PATTERN = re.compile(
    r'\{%\s*code[^%]*%\}\s*(?P<body>.*?)\s*\{%\s*endcode\s*%\}',
    re.DOTALL,
)
TABS_PATTERN = re.compile(
    r'\{%\s*tabs\s*%\}(?P<body>.*?)\{%\s*endtabs\s*%\}',
    re.DOTALL,
)
TAB_PATTERN = re.compile(
    r'\{%\s*tab\s+title="(?P<title>[^"]+)"\s*%\}(?P<content>.*?)\{%\s*endtab\s*%\}',
    re.DOTALL,
)
GITBOOK_SLUG_LINKS = {
    'osnovy/kak-vybiraetsya-scenarii': '../Основы/Как_выбирается_сценарий.md',
}

ESCAPED_BRACE_PATTERN = re.compile(r'\\{\{\s*(?P<body>.*?)\\}\}')


def convert_escaped_braces(text: str) -> tuple[str, int]:
    count = 0

    def replacer(match: re.Match[str]) -> str:
        nonlocal count
        count += 1
        body = match.group('body').strip()
        return f'`{{{{ {body} }}}}`' if body else '`{{}}`'

    return ESCAPED_BRACE_PATTERN.sub(replacer, text), count


NOTE_BLOCK = re.compile(
    r'\{%\s*note\s+(?P<type>info|tip|warning|alert)(?:\s+"[^"]*")?\s*%\}\s*'
    r'(?P<body>.*?)'
    r'\{%\s*endnote\s*%\}',
    re.DOTALL,
)


def normalize_notes(text: str) -> tuple[str, int]:
    count = 0

    def replacer(match: re.Match[str]) -> str:
        nonlocal count
        count += 1
        body = match.group('body').strip('\n')
        return f"{{% note {match.group('type')} %}}\n\n{body}\n\n{{% endnote %}}"

    return NOTE_BLOCK.sub(replacer, text), count


def convert_hints(text: str) -> tuple[str, int]:
    count = 0

    def replacer(match: re.Match[str]) -> str:
        nonlocal count
        count += 1
        style = HINT_TO_NOTE[match.group('style')]
        body = match.group('body').strip('\n')
        return f'{{% note {style} %}}\n\n{body}\n\n{{% endnote %}}'

    return HINT_PATTERN.sub(replacer, text), count


def convert_content_refs(text: str) -> tuple[str, int]:
    count = 0

    def replacer(match: re.Match[str]) -> str:
        nonlocal count
        count += 1
        url = match.group('url').strip('/')
        if url not in CONTENT_REF_LINKS:
            raise ValueError(f'Unknown content-ref url: {url}')
        title, href = CONTENT_REF_LINKS[url]
        return f'- [{title}]({href})'

    return CONTENT_REF_PATTERN.sub(replacer, text), count


def convert_embeds(text: str) -> tuple[str, int]:
    count = 0

    def replacer(match: re.Match[str]) -> str:
        nonlocal count
        count += 1
        url = match.group('url')
        if '.mp4' in url.lower():
            return (
                f'\n<video controls width="100%" src="{url}">\n'
                f'  Ваш браузер не поддерживает видео. '
                f'<a href="{url}">Скачать видео</a>\n'
                f'</video>\n'
            )
        return f'\n[Смотреть видео]({url})\n'

    return EMBED_PATTERN.sub(replacer, text), count


def convert_code_blocks(text: str) -> tuple[str, int]:
    count = 0

    def replacer(match: re.Match[str]) -> str:
        nonlocal count
        count += 1
        return match.group('body').strip()

    return CODE_PATTERN.sub(replacer, text), count


def convert_tabs(text: str) -> tuple[str, int]:
    count = 0

    def replacer(match: re.Match[str]) -> str:
        nonlocal count
        count += 1
        body = match.group('body')
        tabs = TAB_PATTERN.findall(body)
        if not tabs:
            return match.group(0)

        parts = ['{% list tabs %}', '']
        for title, content in tabs:
            parts.extend([f'- {title}', '', content.strip(), ''])
        parts.append('{% endlist %}')
        return '\n'.join(parts)

    return TABS_PATTERN.sub(replacer, text), count


def convert_gitbook_links(text: str) -> tuple[str, int]:
    count = 0
    for slug, href in GITBOOK_SLUG_LINKS.items():
        old = f']({slug})'
        new = f']({href})'
        if old in text:
            text = text.replace(old, new)
            count += 1
    return text, count


def convert_text(text: str) -> dict[str, int]:
    stats: dict[str, int] = {}
    text, stats['hints'] = convert_hints(text)
    text, stats['notes'] = normalize_notes(text)
    text, stats['content_refs'] = convert_content_refs(text)
    text, stats['embeds'] = convert_embeds(text)
    text, stats['code_blocks'] = convert_code_blocks(text)
    text, stats['tabs'] = convert_tabs(text)
    text, stats['links'] = convert_gitbook_links(text)
    text, stats['escaped_braces'] = convert_escaped_braces(text)
    return text, stats


def process_file(path: Path) -> dict[str, int]:
    original = path.read_text(encoding='utf-8')
    converted, stats = convert_text(original)
    total = sum(stats.values())
    if total and converted != original:
        path.write_text(converted, encoding='utf-8')
    return stats


def scan_invalid_tags(text: str) -> list[str]:
    valid_prefixes = ('note ', 'endnote', 'list tabs', 'endlist', 'cut ', 'endcut')
    invalid: list[str] = []
    for match in re.finditer(r'\{%\s*([^%]+?)%\}', text):
        tag = match.group(1).strip()
        if tag.startswith(valid_prefixes):
            continue
        invalid.append(tag)
    return invalid


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else 'ru')
    if not root.exists():
        print(f'Path not found: {root}', file=sys.stderr)
        return 1

    totals: dict[str, int] = {}
    changed_files = 0
    for md_file in sorted(root.rglob('*.md')):
        stats = process_file(md_file)
        file_total = sum(stats.values())
        if file_total:
            changed_files += 1
            parts = ', '.join(f'{k}={v}' for k, v in stats.items() if v)
            print(f'{md_file.relative_to(root)}: {parts}')
            for key, value in stats.items():
                totals[key] = totals.get(key, 0) + value

    print(f'\nUpdated {changed_files} files')
    for key, value in sorted(totals.items()):
        print(f'  {key}: {value}')

    remaining: dict[str, list[str]] = {}
    for md_file in sorted(root.rglob('*.md')):
        for tag in scan_invalid_tags(md_file.read_text(encoding='utf-8')):
            remaining.setdefault(tag, []).append(str(md_file.relative_to(root)))

    if remaining:
        print('\nRemaining unsupported tags:')
        for tag, files in sorted(remaining.items()):
            print(f'  {tag}: {", ".join(files)}')
        return 1

    print('\nAll GitBook-specific {% %} blocks converted.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
