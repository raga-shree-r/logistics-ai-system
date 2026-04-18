"""
API Service Layer — CognixOps Frontend (FIXED)
Handles all HTTP calls to the FastAPI backend.
"""

import requests
import streamlit as st
from config import API_BASE

_TIMEOUT = 15


# ── Helpers ────────────────────────────────────────────────────────────────

def _get(path: str, params: dict = None) -> dict | None:
    url = f"{API_BASE}{path}"
    try:
        r = requests.get(url, params=params, timeout=_TIMEOUT)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.ConnectionError:
        st.error(f"Cannot reach backend at {API_BASE}")
        return None
    except requests.exceptions.Timeout:
        st.error(f"Request to {url} timed out")
        return None
    except requests.exceptions.HTTPError as e:
        st.error(f"Backend error {e.response.status_code}: {e.response.text}")
        return None
    except Exception as e:
        st.error(f"Unexpected error: {e}")
        return None


def _post(path: str, payload: dict) -> dict | None:
    url = f"{API_BASE}{path}"
    try:
        r = requests.post(url, json=payload, timeout=_TIMEOUT)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.ConnectionError:
        st.error(f"Cannot reach backend at {API_BASE}")
        return None
    except requests.exceptions.Timeout:
        st.error(f"Request to {url} timed out")
        return None
    except requests.exceptions.HTTPError as e:
        st.error(f"Backend error {e.response.status_code}: {e.response.text}")
        return None
    except Exception as e:
        st.error(f"Unexpected error: {e}")
        return None


# ── Health ────────────────────────────────────────────────────────────────

def health_check() -> bool:
    try:
        r = requests.get(f"{API_BASE}/health", timeout=4)
        return r.status_code == 200
    except Exception:
        return False


# ── Forecast (FIXED → GET) ────────────────────────────────────────────────

def get_forecast(sku: str, horizon_days: int = 7) -> dict | None:
    raw = _get("/forecast", {
        "sku": sku,
        "horizon": horizon_days
    })
    if raw is None:
        return None

    return {
        "sku": raw.get("sku"),
        "dates": raw.get("dates", []),
        "forecast": raw.get("forecast", []),
        "lower": raw.get("lower", []),
        "upper": raw.get("upper", []),
        "model_mae": raw.get("model_mae", 0),
        "baseline_mae": raw.get("baseline_mae", 0),
    }


def get_all_forecasts(skus: list[str], horizon_days: int = 7) -> list[dict]:
    return [d for sku in skus if (d := get_forecast(sku, horizon_days))]


# ── KPI (SAFE) ────────────────────────────────────────────────────────────

def get_kpis() -> dict | None:
    raw = _get("/kpi")
    if raw is None:
        return None

    return {
        "service_level": raw.get("service_level", 0),
        "total_cost": raw.get("total_cost", 0),
        "co2_kg": raw.get("co2_kg", 0),
        "on_time_delivery": raw.get("on_time_delivery", 0),
        "inventory_turnover": raw.get("inventory_turnover", 0),
    }


# ── Optimization (FIXED) ──────────────────────────────────────────────────

def get_optimization(disruption_type: str = "none") -> dict | None:
    raw = _post("/optimize", {
        "disruption_type": disruption_type
    })
    if raw is None:
        return None

    return {
        "routes": raw.get("routes", []),
        "total_cost": raw.get("total_cost", 0),
        "total_co2": raw.get("total_co2", 0),
        "service_level": raw.get("service_level", 0),
    }


# ── Simulation (FIXED) ────────────────────────────────────────────────────

def get_simulation(disruption_type: str) -> dict | None:
    if disruption_type == "none":
        return None

    raw = _post("/simulate", {
        "disruption_type": disruption_type
    })
    if raw is None:
        return None

    return {
        "kpi_before": raw.get("kpi_before", {}),
        "kpi_after": raw.get("kpi_after", {}),
        "recommended_actions": raw.get("recommended_actions", []),
        "severity": raw.get("severity", "low"),
    }


# ── Anomaly Detection (FIXED) ─────────────────────────────────────────────

def get_anomalies(sku: str, sensitivity: float = 2.0) -> dict | None:
    raw = _post("/anomaly", {
        "product_id": sku,
        "sensitivity": sensitivity
    })
    return raw