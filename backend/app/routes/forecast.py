from fastapi import APIRouter
from app.services.forecasting import run_forecast
from app.models.schemas import ForecastResponse

router = APIRouter()

@router.get("/")
def get_forecast():
    result = run_forecast()

    forecast_values = [item["predicted_demand"] for item in result]
    labels = [item["customer_id"] for item in result]

    return {
        "status": "success",
        "forecast": forecast_values,
        "dates": labels
    }
