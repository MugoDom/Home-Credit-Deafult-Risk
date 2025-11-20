# api/inference.py
from pathlib import Path
import lightgbm as lgb
from typing import Dict

# from src.fe_pipeline import prepare_features
from src.fe_engineering_light import prepare_features_for_model


PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = PROJECT_ROOT / "model" / "lightgbm_model.txt"

model = lgb.Booster(model_file=str(MODEL_PATH))

DEFAULT_THRESHOLD = 0.25  # Theoretical


def score_application(raw_input):
    X_ready = prepare_features_for_model(raw_input)
    prob = float(model.predict(X_ready)[0])
    decision = "REJECT" if prob >= DEFAULT_THRESHOLD else "APPROVE"

    return {
        "default_probability": prob,
        "decision": decision,
        "threshold": DEFAULT_THRESHOLD,
    }

