"""Load raw CRMLS Sold monthly CSVs (Weeks 1-4)."""
from pathlib import Path
import pandas as pd

try:
    from .config import RAW
except ImportError:  # allow running as a plain script
    from config import RAW


def list_sold_files(raw_dir: Path = RAW):
    """Return sorted list of monthly Sold CSV paths."""
    return sorted(raw_dir.glob("CRMLSSold*.csv"))


def load_month(path: Path) -> pd.DataFrame:
    """Load one monthly Sold file, tagging it with the source month (YYYYMM)."""
    df = pd.read_csv(path, low_memory=False)
    # Filename pattern: CRMLSSoldYYYYMM.csv -> grab the YYYYMM
    yyyymm = path.stem.replace("CRMLSSold", "")
    df["SourceMonth"] = yyyymm
    return df


def load_all(raw_dir: Path = RAW) -> pd.DataFrame:
    """Concatenate every monthly Sold file into one DataFrame (Weeks 3-4)."""
    files = list_sold_files(raw_dir)
    if not files:
        raise FileNotFoundError(f"No CRMLSSold*.csv files found in {raw_dir}")
    frames = [load_month(f) for f in files]
    return pd.concat(frames, ignore_index=True)


if __name__ == "__main__":
    files = list_sold_files()
    print(f"Found {len(files)} monthly files:")
    for f in files:
        print("  ", f.name)
    df = load_all()
    print(f"\nCombined shape: {df.shape}")
