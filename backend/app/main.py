from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import forecast, optimize, simulate, kpi

app = FastAPI(
    title="AI Logistics Optimization System",
    description="Predict demand, optimize routes, and simulate disruptions",
    version="1.0.0"
)

# -----------------------------
# CORS (allow frontend access)
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all (good for hackathon)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Root Route
# -----------------------------
@app.get("/")
def root():
    return {"message": "Backend is running 🚀"}

# -----------------------------
# Include Routes
# -----------------------------
app.include_router(forecast.router, prefix="/forecast", tags=["Forecast"])
app.include_router(optimize.router, prefix="/optimize", tags=["Optimization"])
app.include_router(simulate.router, prefix="/simulate", tags=["Simulation"])
app.include_router(kpi.router, prefix="/kpi", tags=["KPI"])