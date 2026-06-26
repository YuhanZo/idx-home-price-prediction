# Project working rules

CRMLS housing-market analytics pipeline (IDX Exchange Data Analyst program).
Goal: raw monthly MLS Sold CSVs → clean dataset → Tableau dashboards + market report.
This is an **analytics/BI project, not machine learning** — no model training.

## 🔒 Data handling — strict

**Never commit data to git. Code only.** The MLS/CRMLS data is licensed and confidential.

- Everything under `data/` (raw, processed, metadata) stays local — it is gitignored.
- Never commit `*.csv`, `*.pdf`, `*.sql`, `*.xlsx`, `*.parquet`, `*.pkl`.
- Before committing a notebook, **clear its outputs** (Restart & Clear Output) so no
  real transaction rows get embedded in `.ipynb` JSON.
- Before any `git add`, verify nothing data-like is staged:
  `git diff --cached --name-only | grep -iE '\.(csv|pdf|sql|xlsx|pkl|parquet)$'`
  (should print nothing).

## Style

- No emoji, icons, or logos anywhere — in README, docs, code comments, or commit
  messages. Use plain text only (e.g. write "Done"/"Planned", not check marks).

## Conventions

- Paths come from `src/config.py` — don't hard-code file paths.
- Pipeline outputs: `sold_combined.csv` → `sold_filtered.csv` → `sold_clean.csv`
  (all in `data/processed/`, all local-only).
- Analysis target = `PropertyType == 'Residential'` only (exclude leases/land/commercial).
- Key fields: `ClosePrice`, `OriginalListPrice`, `ListPrice`, `LivingArea`, `CloseDate`,
  `DaysOnMarket`, `City`, `PostalCode`, `CountyOrParish`, `ListAgentFullName`,
  `ListOfficeName`, `Latitude`, `Longitude`.

## Pipeline stages (handbook curriculum)

1. Exploration · 2. Aggregate months · 3. Filter residential + validate ·
4. Clean (dates/types/nulls) · 5. Feature engineering (PPSF, sold-to-list, YrMo) ·
6. IQR outlier removal · 7. Tableau dashboards · 8. Market-intelligence report.
