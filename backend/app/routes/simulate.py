from fastapi import APIRouter
from app.services.simulation import run_simulation
from app.models.schemas import SimulationRequest, SimulationResponse

router = APIRouter()

@router.post("/", response_model=SimulationResponse)
def simulate(request: SimulationRequest):
    result = run_simulation(request.disruption_type)

    return {
        "status": "success",
        "scenario": request.disruption_type,
        **result
    }