from fastapi import FastAPI
import joblib

from .schemas import PredictRequest, PredictResponse, HealthResponse
from src.predict import predict_rentals
from src.utils import get_project_root
from src.logger import logger

app = FastAPI(
    title="Bike Sharing Demand Predictor",
    description="Сервис прогнозирования спроса на аренду велосипедов",
    version="1.0.0"
)

PROJECT_ROOT = get_project_root()
MODEL_PATH = PROJECT_ROOT / "artifacts" / "final_model" / "final_model.pkl"

logger.info("Loading model from %s", MODEL_PATH)

model = joblib.load(MODEL_PATH)

logger.info("Model loaded successfully")


@app.get("/")
def root():
    return {
        "service": app.title,
        "version": app.version,
        "docs": "/docs",
        "health": "/health",
        "predict": "/predict"
    }


@app.get("/health", response_model=HealthResponse)
async def health():
    
    logger.info("Health check requested")
    
    return HealthResponse(
        status="OK" if model is not None else "ERROR",
        model_loaded=model is not None
    )
    
    
@app.post("/predict", response_model=PredictResponse)
async def predict(request: PredictRequest):
    
    logger.info(
        "Prediction requested for datetime=%s",
        request.datetime
    )
    
    prediction = predict_rentals(model, input_data=request.model_dump())
    
    logger.info(
        "Prediction completed: %s",
        prediction
    )
    
    return PredictResponse(predicted_demand=prediction)