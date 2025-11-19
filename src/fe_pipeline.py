# src/fe_pipeline.py
from pathlib import Path
import pandas as pd
import joblib
import numpy as np
from typing import Dict

# Optional: your sanitize_columns function (lightgbm-safe names)
import re

def sanitize_columns(df, mapping=None):
    """
    Reproduce the sanitize logic used in Training Notebook (06_model_training).
    Ensures column names are identical between train/test/inference.
    """
    df = df.copy()
    if mapping is None:
        mapping = {}
        for c in df.columns:
            clean = re.sub(r"[^0-9a-zA-Z_]", "_", c)
            base = clean
            k = 1
            while clean in mapping.values():
                clean = f"{base}_{k}"
                k += 1
            mapping[c] = clean

    new_cols = []
    for c in df.columns:
        if c in mapping:
            new_cols.append(mapping[c])
        else:
            clean = re.sub(r"[^0-9a-zA-Z_]", "_", c)
            new_cols.append(clean)
    df.columns = new_cols
    return df, mapping


# Load artifacts
PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODEL_DIR = PROJECT_ROOT / "model"

preprocessor = joblib.load(MODEL_DIR / "preprocessor.pkl")
feature_names = joblib.load(MODEL_DIR / "feature_names.pkl")  # sanitized names


def prepare_features(raw_input: Dict) -> pd.DataFrame:
    """
    Convert raw dictionary input into a model-ready row with:
    - same preprocessing used during training
    - same column sanitization
    - same feature ordering
    """
    # 1. Convert to DataFrame
    df_raw = pd.DataFrame([raw_input])

    # 2. Preprocessing (impute + OHE)
    X_arr = preprocessor.transform(df_raw)

    df_fe = pd.DataFrame(X_arr, columns=preprocessor.get_feature_names_out())

    # 3. Sanitize columns (same as training)
    df_fe, _ = sanitize_columns(df_fe, mapping=None)

    # 4. Reindex to match training feature order
    df_final = df_fe.reindex(columns=feature_names, fill_value=0)

    return df_final
