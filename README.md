# California Property Price Prediction

Predicting California residential property sale prices from CRMLS sold-listing data.

## ⚠️ Data Privacy — Read Before Committing

**Do NOT upload any raw SQL, CSV, or other data files to your public GitHub.**
Commit **only your code**.

- ❌ No raw data (`data/raw/`, `data/processed/`, `*.csv`)
- ❌ No SQL dumps or query exports (`*.sql`)
- ❌ No proprietary metadata (`data/metadata/`)
- ❌ No trained model binaries (`*.pkl`) or generated outputs
- ✅ Yes to source code (`src/`), notebooks (cleared of data/output), and docs

The CRMLS / Trestle data is licensed and may contain sensitive or proprietary
information. Sharing it publicly can violate the data license and privacy rules.
Keep it local, or store it in a **private** location only.

## Project Structure

```
California-Property-Price-Prediction/
├── data/
│   ├── raw/          # original CRMLS sold CSVs        (DO NOT COMMIT)
│   ├── metadata/     # Trestle property metadata PDF   (DO NOT COMMIT)
│   └── processed/    # cleaned / filtered datasets      (DO NOT COMMIT)
├── notebooks/        # exploration, preprocessing, modeling
├── src/              # reusable Python modules
├── models/           # trained model artifacts          (DO NOT COMMIT)
├── outputs/          # figures, metrics, predictions     (DO NOT COMMIT)
├── presentation/     # slides and demo material
├── report/           # written documentation
├── requirements.txt
└── README.md
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Workflow

1. Place raw CRMLS CSVs in `data/raw/` (kept local only).
2. Run the notebooks in order: `01_data_exploration` → `02_preprocessing` → `03_model`.
3. Or use the `src/` modules: `load_data` → `preprocess` → `feature_engineering` → `train` → `evaluate` → `predict`.

## Suggested `.gitignore`

Add this file before your first commit so data never leaves your machine:

```gitignore
# Data
data/raw/
data/processed/
data/metadata/
*.csv
*.sql

# Models & outputs
models/
*.pkl
outputs/

# Environments
.venv/
__pycache__/
*.pyc
.ipynb_checkpoints/
```
