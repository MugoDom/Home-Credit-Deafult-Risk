from pathlib import Path
import pandas as pd
import numpy as np
import joblib


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CLEAN_DIR    = PROJECT_ROOT / "data" / "clean"
MODEL_DIR    = PROJECT_ROOT / "model"


# Load precomputed tables
bureau_agg    = pd.read_csv(CLEAN_DIR / "bureau_agg.csv")
behavior_agg  = pd.read_csv(CLEAN_DIR / "behavior_agg.csv")

# Load artifacts
preprocessor     = joblib.load(MODEL_DIR / "preprocessor.pkl")
feature_names    = joblib.load(MODEL_DIR / "feature_names.pkl")
raw_feature_cols = joblib.load(MODEL_DIR / "raw_feature_columns.pkl")


def _engineer_minimal_features(df):
    """ Reproduce the simple engineered features from Notebook 01. """
    out = df.copy()

    if "DAYS_EMPLOYED" in out.columns:
        out["DAYS_EMPLOYED_REPLACED"] = out["DAYS_EMPLOYED"].replace({365243: np.nan})

    # safe divisions
    def safe_div(a, b): 
        return a / np.where(b == 0, 1, b)

    if {"AMT_CREDIT","AMT_INCOME_TOTAL"}.issubset(out.columns):
        out["CREDIT_INCOME_PERCENT"] = out["AMT_CREDIT"] / out["AMT_INCOME_TOTAL"]

    if {"AMT_ANNUITY","AMT_INCOME_TOTAL"}.issubset(out.columns):
        out["ANNUITY_INCOME_PERCENT"] = out["AMT_ANNUITY"] / out["AMT_INCOME_TOTAL"]

    if {"AMT_CREDIT","AMT_ANNUITY"}.issubset(out.columns):
        out["CREDIT_ANNUITY_PERCENT"] = out["AMT_CREDIT"] / out["AMT_ANNUITY"]

    if {"AMT_CREDIT","AMT_GOODS_PRICE"}.issubset(out.columns):
        out["CREDIT_GOODS_DIFF"] = out["AMT_CREDIT"] - out["AMT_GOODS_PRICE"]

    if {"AMT_INCOME_TOTAL","CNT_FAM_MEMBERS"}.issubset(out.columns):
        out["FAMILY_CNT_INCOME_PERCENT"] = out["AMT_INCOME_TOTAL"] / out["CNT_FAM_MEMBERS"]

    return out


def build_full_raw_features(raw_input: dict) -> pd.DataFrame:
    """
    MAIN ENTRYPOINT:
    - User gives minimal fields
    - We build full raw features expected by Notebook 05
    - Missing values filled later by preprocessor
    """

    df = pd.DataFrame([raw_input])

    # 1) Minimal engineered features
    df = _engineer_minimal_features(df)

    # 2) Merge bureau_agg
    df = df.merge(bureau_agg, on="SK_ID_CURR", how="left")

    # 3) Merge behavior_agg
    df = df.merge(behavior_agg, on="SK_ID_CURR", how="left")

    # 4) Ensure all expected raw features exist
    df = df.reindex(columns=raw_feature_cols, fill_value=np.nan)

    return df


def prepare_features_for_model(raw_input: dict):
    """
    - Build full raw feature row
    - Preprocess (impute + OHE)
    - Sanitize
    - Reindex to training feature order
    """
    df_raw = build_full_raw_features(raw_input)

    # sklearn preprocessing
    X_arr = preprocessor.transform(df_raw)

    df_fe = pd.DataFrame(
        X_arr,
        columns=preprocessor.get_feature_names_out()
    )

    # sanitize columns
    def sanitize(c):
        return "".join(ch if ch.isalnum() or ch == "_" else "_" for ch in c)

    df_fe.columns = [sanitize(c) for c in df_fe.columns]

    # reorder to match LightGBM
    df_final = df_fe.reindex(columns=feature_names, fill_value=0)

    return df_final
