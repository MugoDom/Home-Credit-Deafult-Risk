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
    Accept raw application data (one applicant),
    run preprocessing + LightGBM model, return probability + decision.
    """
    result = score_application(payload.dict())
    return result
