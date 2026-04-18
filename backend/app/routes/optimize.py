from fastapi import APIRouter
from app.services.optimization import run_optimization
from app.models.schemas import OptimizationResponse

router = APIRouter()

@router.get("/", response_model=OptimizationResponse)
def optimize_routes():
    result = run_optimization()

    return {
        "status": "success",
        **result
    }