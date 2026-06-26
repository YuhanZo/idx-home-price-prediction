"""Central path configuration so every script/notebook resolves files the same way."""
from pathlib import Path

# Project root = parent of the src/ folder
ROOT = Path(__file__).resolve().parents[1]

DATA = ROOT / "data"
RAW = DATA / "raw"
METADATA = DATA / "metadata"
PROCESSED = DATA / "processed"

OUTPUTS = ROOT / "outputs"
FIGURES = OUTPUTS / "figures"
REPORT = ROOT / "report"

# Processed dataset filenames (the handbook's three pipeline outputs)
SOLD_COMBINED = PROCESSED / "sold_combined.csv"   # Weeks 3-4: all months concatenated
SOLD_FILTERED = PROCESSED / "sold_filtered.csv"   # Week 5: residential + validated
SOLD_CLEAN = PROCESSED / "sold_clean.csv"         # Weeks 6-9: cleaned, engineered, outliers removed

# Ensure output dirs exist when imported
for _d in (PROCESSED, OUTPUTS, FIGURES, REPORT):
    _d.mkdir(parents=True, exist_ok=True)
