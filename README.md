# Smartbot Pro — документация (Diplodoc)

## GitHub Pages

1. Запушь репозиторий в GitHub (`master`).
2. **Settings → Pages → Build and deployment → Source: GitHub Actions** — включи один раз.
3. После push workflow `.github/workflows/build.yml` соберёт сайт (~2–5 мин).
4. URL: `https://<username>.github.io/<repo>/`

Пуш **не** включает Pages автоматически — без шага 2 сайт не появится.

## GitLab Pages

1. Создай проект на [GitLab](https://gitlab.com/dima0408059).
2. Запушь этот репозиторий:
   ```bash
   git remote add gitlab git@gitlab.com:dima0408059/smartbot-docs.git
   git push -u gitlab master
   ```
3. CI возьмёт `.gitlab-ci.yml` — job `pages` отдаст артефакт `public/`.
4. **Settings → Pages** — URL появится после успешного pipeline.
5. Обычно: `https://dima0408059.gitlab.io/<project-name>/`

## Локальный просмотр

```bash
rm -rf ./_site
npx -y @diplodoc/cli@latest build -i ./ -o ./_site --allow-custom-resources
npx -y http-server ./_site --port 5000
```

Открыть: http://localhost:5000/ru/Smartbot_Pro.html

## Структура

- `ru/` — markdown и `toc.yaml`
- `_assets/` — стили
- `scripts/` — утилиты импорта из GitBook (не нужны для деплоя)
- `build/`, `_site/`, `public/` — артефакты сборки (в git не коммитить)
