# S03 – eda_cli: мини-EDA для CSV

Небольшое CLI-приложение для базового анализа CSV-файлов.
Используется в рамках Семинара 03 курса «Инженерия ИИ».

## Требования

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) установлен в систему

## Инициализация проекта

В корне проекта (S03):

```bash
uv sync
```

Эта команда:

- создаст виртуальное окружение `.venv`;
- установит зависимости из `pyproject.toml`;
- установит сам проект `eda-cli` в окружение.

## Запуск CLI

### Краткий обзор

```bash
uv run eda-cli overview data/example.csv
```

Параметры:

- `--sep` – разделитель (по умолчанию `,`);
- `--encoding` – кодировка (по умолчанию `utf-8`).

### Полный EDA-отчёт

```bash
uv run eda-cli report data/example.csv --out-dir reports
```

Параметры:

- `--path` – Путь к CSV-файлу;
- `--out_dir` – Каталог для отчёта (по умолчанию `reports`);
- `--sep` – разделитель (по умолчанию `,`);
- `--max_hist_columns` – Максимум числовых колонок для гистограмм (по умолчанию `6`);
- `--top_k_categories` – Cколько top-значений выводить для категориальных признаков (по умолчанию `5`);
- `--min_missing_share` – орог доли пропусков (по умолчанию `0.5`);
- `--encoding` – кодировка (по умолчанию `utf-8`).

В результате в каталоге `reports/` появятся:

- `report.md` – основной отчёт в Markdown;
- `summary.csv` – таблица по колонкам;
- `missing.csv` – пропуски по колонкам;
- `correlation.csv` – корреляционная матрица (если есть числовые признаки);
- `top_categories/*.csv` – top-k категорий по строковым признакам;
- `hist_*.png` – гистограммы числовых колонок;
- `missing_matrix.png` – визуализация пропусков;
- `correlation_heatmap.png` – тепловая карта корреляций.
Пример вызова:
- `uv run eda-cli report data/example.csv --out-dir reports_example --min-missing-share 0.9 --top-k-categories 7`;

## Тесты

```bash
uv run pytest -q
```
