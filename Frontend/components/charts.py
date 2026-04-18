import streamlit as st
import plotly.graph_objects as go
from config import CHART_HEIGHT

# ── Color Mapping ─────────────────────────────────────────────

VIBGYOR = {
    "violet": "#8A5CF6",
    "indigo": "#6366F1",
    "blue":   "#3B82F6",
    "green":  "#22C55E",
    "yellow": "#F59E0B",
    "orange": "#F97316",
    "red":    "#F43F5E",
}

def _demand_color(value, vmin, vmax):
    if vmax == vmin:
        ratio = 0.5
    else:
        ratio = max(0.0, min(1.0, (value - vmin) / (vmax - vmin)))

    spectrum = ["violet","indigo","blue","green","yellow","orange","red"]
    idx = min(int(ratio * len(spectrum)), len(spectrum) - 1)
    return VIBGYOR[spectrum[idx]]


# ── FIXED: Safe color generator ───────────────────────────────
def _demand_colors_for_series(values):
    if not values or len(values) == 0:
        return []
    try:
        vmin, vmax = min(values), max(values)
    except Exception:
        return []
    return [_demand_color(v, vmin, vmax) for v in values]


# ── Forecast Chart ────────────────────────────────────────────
def render_forecast_chart(forecast_data: dict, anomaly_data: dict = None):

    # ✅ FULL SAFETY CHECK
    if not forecast_data:
        st.warning("No forecast data available")
        return

    forecast = forecast_data.get("forecast", [])
    dates    = forecast_data.get("dates", [])
    lower    = forecast_data.get("lower", [])
    upper    = forecast_data.get("upper", [])
    sku      = forecast_data.get("sku", "")

    # ✅ Prevent empty crash
    if not forecast or len(forecast) == 0:
        st.warning("Forecast data is empty")
        return

    # ✅ Safe colors
    bar_colors = _demand_colors_for_series(forecast)

    fig = go.Figure()

    # ── Confidence band ──
    if lower and upper and len(lower) == len(upper):
        fig.add_trace(go.Scatter(
            x=dates + dates[::-1],
            y=upper + lower[::-1],
            fill="toself",
            fillcolor="rgba(139,92,246,0.1)",
            line=dict(color="rgba(0,0,0,0)"),
            name="Confidence",
            hoverinfo="skip",
        ))

    # ── Bars ──
    fig.add_trace(go.Bar(
        x=dates,
        y=forecast,
        marker_color=bar_colors if bar_colors else "#8A5CF6",
        name=f"{sku}",
    ))

    # ── Trend line ──
    fig.add_trace(go.Scatter(
        x=dates,
        y=forecast,
        mode="lines",
        line=dict(color="#8A5CF6", width=2),
        name="Trend",
    ))

    # ── Anomalies ──
    if anomaly_data and anomaly_data.get("anomalies"):
        anomalies = anomaly_data["anomalies"]

        fig.add_trace(go.Scatter(
            x=[a.get("date") for a in anomalies],
            y=[a.get("demand") for a in anomalies],
            mode="markers",
            marker=dict(color="red", size=10),
            name="Anomalies",
        ))

    fig.update_layout(
        height=CHART_HEIGHT,
        title=f"Demand Forecast — {sku}",
    )

    st.plotly_chart(fig, use_container_width=True)