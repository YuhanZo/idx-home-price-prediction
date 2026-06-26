# CRMLS Housing Market Analytics

End-to-end analytics pipeline that turns monthly **California Regional MLS (CRMLS)**
sold-transaction data into housing-market insights and interactive **Tableau** dashboards.

Built as part of the IDX Exchange Data Analyst program: ingest raw MLS exports →
clean & validate → engineer market metrics → visualize → report.

## What it does

- **Ingests** monthly `CRMLSSold` CSV exports (Dec 2025 – May 2026, ~124K transactions).
- **Filters & validates** to residential sale records (~83K rows) with data-quality checks.
- **Engineers market metrics** used across the dashboards:
  - **Price per Sq Ft** — `ClosePrice / LivingArea`
  - **Sold-to-List Ratio** — `ClosePrice / OriginalListPrice` (negotiation strength)
  - **Days on Market** — time-to-sell
  - **Year / Month / YrMo** — time-series dimensions from `CloseDate`
- **Removes outliers** with the IQR method so medians/averages stay representative.
- **Visualizes** four Tableau dashboards: Market Trends, Market Activity,
  Competitive Intelligence (agents & brokerages), and Geographic Analysis.

## Tech stack

`Python` · `pandas` · `Jupyter` · `Tableau Public`

## Project structure

```
.
├── data/                 # local only — never committed (see CLAUDE.md)
│   ├── raw/              # monthly CRMLSSold CSV exports
│   ├── metadata/         # Trestle field metadata
│   └── processed/        # cleaned/engineered datasets
├── notebooks/
│   └── 01_data_exploration.ipynb
├── src/
│   ├── config.py         # central path configuration
│   └── load_data.py      # load + concatenate monthly files
├── outputs/              # figures (local only)
├── report/               # market-intelligence report
├── requirements.txt
└── README.md
```

## Getting started

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Place the monthly `CRMLSSold*.csv` files in `data/raw/`, then run the notebook
or use the `src/` modules:

```python
from src.load_data import load_all
sold = load_all()          # all months concatenated, tagged with SourceMonth
```

## Pipeline status

| Stage | Status |
|-------|--------|
| Dataset exploration | Done |
| Monthly aggregation | Planned |
| Structuring & validation | Planned |
| Cleaning | Planned |
| Feature engineering | Planned |
| Outlier detection (IQR) | Planned |
| Tableau dashboards | Planned |
| Market-intelligence report | Planned |

## Data note

The underlying MLS data is licensed and confidential, so **no data files are
included in this repository** — only code. See `CLAUDE.md` for the data-handling
rules this project follows.
