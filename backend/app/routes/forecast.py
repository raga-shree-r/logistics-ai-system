from fastapi import APIRouter
from app.services.forecasting import run_forecast
from app.models.schemas import ForecastResponse

router = APIRouter()

@router.get("/", response_model=ForecastResponse)
def get_forecast():
    result = run_forecast()

    # ✅ FIX: extract values properly
    forecast_values = [item["predicted_demand"] for item in result]
    labels = [item["customer_id"] for item in result]

    return {
        "status": "success",
        "forecast": forecast_values,
        "dates": labels   # frontend will use this as x-axis
    }