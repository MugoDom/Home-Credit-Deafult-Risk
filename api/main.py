# api/main.py
from fastapi import FastAPI
from api.models import ApplicationInput
from api.inference import score_application

app = FastAPI(
    title="Home Credit Default Risk API",
    description="Predict default probability for loan applicants",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict")
def predict(payload: ApplicationInput):
    """
    Accepts ALL raw columns from train_merged.csv,
    preprocesses them using preprocessor.pkl,
    sanitizes columns,
    and runs LightGBM prediction.
    """
    return score_application(payload.dict())
