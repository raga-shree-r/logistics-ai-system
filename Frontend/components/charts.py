import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from config import CHART_HEIGHT

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


# ✅ FIXED (handles empty values)
def _demand_colors_for_series(values):
    if not values:
        return []
    vmin, vmax = min(values), max(values)
    return [_demand_color(v, vmin, vmax) for v in values]


def render_forecast_chart(forecast_data: dict, anomaly_data: dict = None):
    
    # ✅ SAFETY CHECK (prevents crash)
    if not forecast_data or not forecast_data.get("forecast"):
        st.warning("No forecast data available")
        return

    dates    = forecast_data.get("dates", [])
    forecast = forecast_data.get("forecast", [])
    lower    = forecast_data.get("lower", [])
    upper    = forecast_data.get("upper", [])
    sku      = forecast_data.get("sku", "")

    # ✅ SAFE color generation
    bar_colors = _demand_colors_for_series(forecast)

    fig = go.Figure()

    # Confidence band
    if lower and upper:
        fig.add_trace(go.Scatter(
            x=dates + dates[::-1],
            y=upper + lower[::-1],
            fill="toself",
            fillcolor="rgba(139,92,246,0.1)",
            line=dict(color="rgba(0,0,0,0)"),
            name="Confidence",
            hoverinfo="skip",
        ))

    # Bars
    fig.add_trace(go.Bar(
        x=dates,
        y=forecast,
        marker_color=bar_colors,
        name=f"{sku}",
    ))

    # Line
    fig.add_trace(go.Scatter(
        x=dates,
        y=forecast,
        mode="lines",
        line=dict(color="#8A5CF6"),
        name="Trend",
    ))

    # Anomalies
    if anomaly_data and anomaly_data.get("anomalies"):
        anomalies = anomaly_data["anomalies"]

        fig.add_trace(go.Scatter(
            x=[a["date"] for a in anomalies],
            y=[a["demand"] for a in anomalies],
            mode="markers",
            marker=dict(color="red", size=10),
            name="Anomalies",
        ))

    fig.update_layout(
        height=CHART_HEIGHT,
        title=f"Demand Forecast — {sku}",
    )

    st.plotly_chart(fig, use_container_width=True)