# api/inference.py
from pathlib import Path
import lightgbm as lgb
from typing import Dict

from src.fe_pipeline import prepare_features

PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = PROJECT_ROOT / "model" / "lightgbm_model.txt"

model = lgb.Booster(model_file=str(MODEL_PATH))

DEFAULT_THRESHOLD = 0.25  # adjust based on calibration


def score_application(raw_input: Dict) -> Dict:
    """
    Full inference pipeline:
    1. raw input
    2. preprocess using preprocessor.pkl (Notebook 05)
    3. sanitize columns (Notebook 06)
    4. reorder to feature_names.pkl
    5. predict with lightgbm_model.txt
    """

    X_ready = prepare_features(raw_input)
    prob = float(model.predict(X_ready)[0])

    decision = "REJECT" if prob >= DEFAULT_THRESHOLD else "APPROVE"

    return {
        "default_probability": prob,
        "decision": decision,
        "threshold": DEFAULT_THRESHOLD,
    }
