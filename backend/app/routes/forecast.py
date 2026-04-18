from fastapi import APIRouter
from app.services.forecasting import run_forecast
from app.models.schemas import ForecastResponse

router = APIRouter()

@router.get("/", response_model=ForecastResponse)
def get_forecast():
    result = run_forecast()

    return {
        "status": "success",
        "forecast": result
    }