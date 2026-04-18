import streamlit as st

st.set_page_config(
    page_title="CognixOps — Logistics AI",
    page_icon="◈",
    layout="wide",
)

# ── Imports ─────────────────────────────────────────────────────────────
from config import APP_TITLE, SKUS, DISRUPTION_OPTIONS
from components.scenario_controls import render_sidebar, render_playbook
from components.kpi_cards import render_kpi_cards, render_kpi_status_badge
from components.charts import render_forecast_chart
from services.api import (
    get_kpis, get_forecast, get_all_forecasts,
    get_optimization, get_simulation, get_anomalies,
)
from utils.helpers import empty_state

# ── Sidebar Controls ─────────────────────────────────────────────────────
controls = render_sidebar()

disruption     = controls["disruption"]
sku            = controls["sku"]
horizon        = controls["horizon"]
show_all_skus  = controls["show_all_skus"]
show_anomalies = controls["show_anomalies"]
sensitivity    = controls["sensitivity"]
run_clicked    = controls["run"]

# ── State ────────────────────────────────────────────────────────────────
if "results" not in st.session_state:
    st.session_state.results = {}

# ── Run Analysis ─────────────────────────────────────────────────────────
if run_clicked:
    with st.spinner("Running analysis..."):

        forecast_data = get_forecast(sku, horizon)
        kpi_data = get_kpis()

        st.session_state.results = {
            "kpis": kpi_data if isinstance(kpi_data, dict) else None,
            "forecast": forecast_data if isinstance(forecast_data, dict) else None,
            "all_forecasts": get_all_forecasts(SKUS, horizon) if show_all_skus else [],
            "optimization": get_optimization(disruption),
            "simulation": get_simulation(disruption) if disruption != "none" else None,
            "anomalies": get_anomalies(sku, sensitivity) if show_anomalies else None,
        }

results = st.session_state.results

# ── Header ───────────────────────────────────────────────────────────────
st.title("CognixOps")

# ── KPI Section ──────────────────────────────────────────────────────────
if results.get("kpis"):
    render_kpi_status_badge(results["kpis"])
    render_kpi_cards(results["kpis"])
else:
    empty_state("Click Run Analysis to load KPIs")

st.divider()

# ── Forecast Section ──────────────────────────────────────────────────────
st.subheader("Demand Forecast")
forecast_data = results.get("forecast")

if forecast_data and forecast_data.get("forecast"):
    render_forecast_chart(forecast_data)
else:
    st.warning("No forecast data available")

st.divider()

# ── Optimization Section ─────────────────────────────────────────────────
st.subheader("Route Optimization")

optimization = results.get("optimization")

if optimization:
    st.write("Total Cost:", optimization.get("total_cost", 0))
    st.write("Total CO₂:", optimization.get("total_co2", 0))
else:
    empty_state("Run analysis to compute routes")

st.divider()

# ── Simulation Section ───────────────────────────────────────────────────
st.subheader("Disruption Scenario")

simulation = results.get("simulation")

if disruption == "none":
    st.info("No disruption selected")
elif simulation:
    st.write("Severity:", simulation.get("severity"))
    st.write("Recommended Actions:", simulation.get("recommended_actions"))
else:
    empty_state("Run analysis to simulate disruption")

st.divider()

# ── Anomaly Section ──────────────────────────────────────────────────────
st.subheader("Anomaly Detection")

anomalies = results.get("anomalies")

if anomalies and anomalies.get("anomalies"):
    for a in anomalies["anomalies"]:
        st.write(a)
else:
    st.info("No anomalies detected or not enabled")