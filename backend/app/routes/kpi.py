from fastapi import APIRouter
from app.services.kpi import calculate_kpis
from app.models.schemas import KPIResponse

router = APIRouter()

@router.get("/", response_model=KPIResponse)
def get_kpis():
    result = calculate_kpis()

    return {
        "status": "success",
        **result
    }