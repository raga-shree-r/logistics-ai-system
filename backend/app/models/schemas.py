from pydantic import BaseModel, Field
from typing import List, Dict, Optional


# -----------------------------
# 1. COMMON BASE RESPONSE
# -----------------------------
class BaseResponse(BaseModel):
    status: str = "success"
    message: Optional[str] = None


# -----------------------------
# 2. FORECASTING
# -----------------------------
class ForecastItem(BaseModel):
    customer_id: str
    predicted_demand: float


class ForecastResponse(BaseResponse):
    forecast: List[ForecastItem]


# -----------------------------
# 3. OPTIMIZATION
# -----------------------------
class Route(BaseModel):
    warehouse_id: str
    customer_id: str
    distance_km: float
    cost: float
    co2: float


class OptimizationResponse(BaseResponse):
    routes: List[Route]
    total_cost: float
    total_co2: float


# -----------------------------
# 4. SIMULATION
# -----------------------------
class SimulationRequest(BaseModel):
    disruption_type: str = Field(
        ...,
        description="Type of disruption (e.g., port_closure, delay)"
    )


class SimulationResponse(BaseResponse):
    scenario: str
    new_routes: List[Route]
    impact: Dict[str, float]  # e.g., {"cost_increase": 10}


# -----------------------------
# 5. KPI
# -----------------------------
class KPIResponse(BaseResponse):
    service_level: float
    total_cost: float
    total_co2: float


# -----------------------------
# 6. SAFETY STOCK (Optional)
# -----------------------------
class SafetyStockItem(BaseModel):
    customer_id: str
    safety_stock: float


class SafetyStockResponse(BaseResponse):
    safety_stock: List[SafetyStockItem]


# -----------------------------
# 7. HEALTH CHECK
# -----------------------------
class HealthResponse(BaseModel):
    message: str = "Backend is running"