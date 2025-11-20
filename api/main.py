# api/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.models import ApplicationInput
from api.inference import score_application

app = FastAPI(
    title="Home Credit Default Risk API",
    description="Predict default probability for loan applicants",
    version="1.0.0"
)
# 🚩 Allow React dev server to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Vite default
        "http://localhost:3000",  # CRA default
        "https://home-credit-ui.onrender.com", # Render url
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
