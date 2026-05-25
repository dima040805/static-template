#!/usr/bin/env python3
"""Import missing Markdown pages from GitBook API into static-template/ru/."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.parse
from dataclasses import dataclass
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
DEFAULT_STRUCTURE = ROOT.parent / 'docs_smartbotpro.json'
DEFAULT_RU = ROOT / 'ru'

sys.path.insert(0, str(SCRIPT_DIR))
from convert_gitbook_syntax import convert_text  # noqa: E402

SPACE_ID = 'vTd8XmFMqkqZga7zhLuk'
API_BASE = f'https://api.gitbook.com/v1/spaces/{SPACE_ID}/content'

PATH_OVERRIDES: dict[str, str] = {
    'nachalo-raboty/korotko-o-glavnom': 'Начало_работы/Коротко_о_главном.md',
    'instrumenty/statistika': 'Инструменты/Статистика.md',
    'instrumenty/rassylki': 'Инструменты/Рассылки.md',
    'mini-kurs': 'Мини-курс/Мини-курс.md',
    'recepty': 'Рецепты/Рецепты.md',
    'scenarii/peremennye/peremennaya-vlozhenie': (
        'Сценарии/Переменные/Переменная_“Вложение”.md'
    ),
    'scenarii/peremennye/gde-srabotal-bot-realm': (
        'Сценарии/Переменные/Где_сработал_бот_—_%realm%.md'
    ),
    'scenarii/priem-oplaty/priem-oplaty-cherez-t-bank': (
        'Сценарии/Прием оплаты/Прием_оплаты_через_Т-Банк.md'
    ),
    'scenarii/integracii/google-tablicy': (
        'Сценарии/Интеграции/Google-таблицы/Google-таблицы.md'
    ),
    'scenarii/integracii/http-zaprosy': 'Сценарии/Интеграции/HTTP-запросы.md',
    'scenarii/integracii/bitrix24/sozdanie-ai-bota-s-izmeneniem-statusa-v-bitrix24': (
        'Сценарии/Интеграции/Bitrix24/'
        'Создание_AI-бота_с_изменением_статуса_в_Bitrix24.md'
    ),
    'instrumenty/smartbot-ai/recepty-s-ai-botom/ii-lidogenerator': (
        'Инструменты/Smartbot AI/Рецепты с AI ботом/ИИ-лидогенератор.md'
    ),
    'instrumenty/magaziny-v-telegram/import-tovarov-iz-excel-faila': (
        'Инструменты/Магазины в Telegram/Импорт_товаров_из_Excel-файла.md'
    ),
    'nocode-cloud/n8n/bloki-v-n8n-uzly-nody': (
        'Nocode_Cloud/n8n/Блоки_в_n8n_(узлыноды).md'
    ),
    'dokumenty/podpiska-i-tarify/kak-rabotaet-oplata-ai-botov': (
        'Документы/Подписка и тарифы/Как_работает_оплата_AI-ботов.md'
    ),
    'dokumenty/dogovor-publichnoi-oferty/redakciya-1-ot-15-fevralya-2022-g': (
        'Документы/Договор публичной оферты/Редакция_№1_от_15_февраля_2022_г.md'
    ),
    'dokumenty/dogovor-publichnoi-oferty/redakciya-2-ot-2-noyabrya-2022-g': (
        'Документы/Договор публичной оферты/Редакция_№2_от_2_ноября_2022_г.md'
    ),
    'mini-kurs/shablon-test-s-naborom-ballov': (
        'Мини-курс/Шаблон_«Тест_с_набором_баллов».md'
    ),
}

LINK_PATH_OVERRIDES: dict[str, str] = {
    'Редакция №3 от 13 декабря 2022г': (
        'Документы/Договор публичной оферты/Редакция_№3_от_13_декабря_2022_г.md'
    ),
    'Редакция №4 от 31 января 2023г': (
        'Документы/Договор публичной оферты/Редакция_№4_от_31_января_2023_г.md'
    ),
    'Редакция №5 от 19 января 2024г': (
        'Документы/Договор публичной оферты/Редакция_№5_от_19_января_2024_г.md'
    ),
    'Редакция №6 от 7 августа 2024г': (
        'Документы/Договор публичной оферты/Редакция_№6_от_7_августа_2024_г.md'
    ),
    'Редакция №7 от 17 декабря 2024г': (
        'Документы/Договор публичной оферты/Редакция_№7_от_17_декабря_2024_г.md'
    ),
}


@dataclass(frozen=True, slots=True)
class GitBookPage:
    title: str
    path: str | None
    document_id: str | None
    kind: str
    target_url: str | None = None


def normalize_title(title: str) -> str:
    return re.sub(r'\s+', ' ', title.strip())


def title_to_filename(title: str) -> str:
    cleaned = title.replace('«', '«').replace('»', '»')
    cleaned = re.sub(r'\s+', '_', cleaned.strip())
    return f'{cleaned}.md'


def walk_pages(nodes: list[dict]) -> list[GitBookPage]:
    result: list[GitBookPage] = []
    for node in nodes:
        target_url = None
        if node.get('kind') == 'link':
            target = node.get('target') or {}
            target_url = target.get('url')
        result.append(
            GitBookPage(
                title=node.get('title', ''),
                path=node.get('path'),
                document_id=node.get('documentId'),
                kind=node.get('kind', ''),
                target_url=target_url,
            ),
        )
        result.extend(walk_pages(node.get('pages', [])))
    return result


def resolve_target_path(page: GitBookPage, existing_files: set[str]) -> str | None:
    if page.path and page.path in PATH_OVERRIDES:
        return PATH_OVERRIDES[page.path]

    if page.kind == 'link':
        return LINK_PATH_OVERRIDES.get(page.title)

    if not page.document_id:
        return None

    if page.path == 'smartbot-pro':
        return 'Smartbot_Pro.md'

    filename = title_to_filename(page.title)
    matches = [path for path in existing_files if path.endswith(f'/{filename}') or path == filename]
    if len(matches) == 1:
        return matches[0]
    if len(matches) > 1 and page.path:
        slug_parts = page.path.split('/')[:-1]
        for candidate in matches:
            if all(part.replace('-', ' ') in candidate.lower() or part in candidate.lower()
                   for part in slug_parts[-2:]):
                return candidate
        return matches[0]
    return None


def fetch_markdown(page_path: str, token: str) -> str:
    encoded_path = urllib.parse.quote(page_path, safe='')
    url = f'{API_BASE}/path/{encoded_path}?format=markdown'
    result = subprocess.run(
        [
            'curl',
            '-sS',
            '-H',
            f'Authorization: Bearer {token}',
            url,
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(result.stdout)
    markdown = payload.get('markdown')
    if not isinstance(markdown, str) or not markdown.strip():
        raise RuntimeError(f'Empty markdown for path {page_path!r}')
    return markdown


def build_link_markdown(page: GitBookPage) -> str:
    title = normalize_title(page.title.replace('г', ' г'))
    url = page.target_url or ''
    return (
        f'# {title}\n\n'
        f'Текст редакции договора публичной оферты доступен по ссылке:\n\n'
        f'[{title} (Google Drive)]({url})\n'
    )


def import_pages(
    *,
    token: str,
    structure_path: Path,
    ru_dir: Path,
    overwrite: bool,
) -> int:
    structure = json.loads(structure_path.read_text(encoding='utf-8'))
    pages = walk_pages(structure.get('pages', []))
    existing_files = {str(path.relative_to(ru_dir)) for path in ru_dir.rglob('*.md')}

    imported = 0
    skipped = 0
    for page in pages:
        target = resolve_target_path(page, existing_files)
        if not target:
            continue

        target_path = ru_dir / target
        if target_path.exists() and not overwrite:
            skipped += 1
            continue

        if page.kind == 'link':
            if not page.target_url:
                print(f'SKIP link without URL: {page.title}', file=sys.stderr)
                continue
            markdown = build_link_markdown(page)
        else:
            if not page.path:
                print(f'SKIP sheet without path: {page.title}', file=sys.stderr)
                continue
            try:
                markdown = fetch_markdown(page.path, token)
            except (subprocess.CalledProcessError, RuntimeError, json.JSONDecodeError) as exc:
                print(f'FAIL {page.path}: {exc}', file=sys.stderr)
                continue

        markdown, _stats = convert_text(markdown)
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(markdown, encoding='utf-8')
        existing_files.add(target)
        imported += 1
        print(f'IMPORT {target}')

    print(f'\nImported: {imported}, skipped existing: {skipped}')
    return 0 if imported or skipped else 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--token', default=os.environ.get('GITBOOK_TOKEN'))
    parser.add_argument('--structure', type=Path, default=DEFAULT_STRUCTURE)
    parser.add_argument('--ru-dir', type=Path, default=DEFAULT_RU)
    parser.add_argument('--overwrite', action='store_true')
    args = parser.parse_args()

    if not args.token:
        print('Set GITBOOK_TOKEN env var or pass --token', file=sys.stderr)
        return 1
    if not args.structure.exists():
        print(f'Structure file not found: {args.structure}', file=sys.stderr)
        return 1
    if not args.ru_dir.exists():
        print(f'RU directory not found: {args.ru_dir}', file=sys.stderr)
        return 1

    return import_pages(
        token=args.token,
        structure_path=args.structure,
        ru_dir=args.ru_dir,
        overwrite=args.overwrite,
    )


if __name__ == '__main__':
    raise SystemExit(main())
