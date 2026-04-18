# CognixOps — AI Logistics Intelligence Platform

CognixOps is an AI-powered logistics system that enables demand forecasting, route optimization, disruption simulation, anomaly detection, and real-time performance monitoring.

---

## Overview

CognixOps acts as a centralized decision-support system for supply chains, helping users predict demand, optimize operations, and evaluate system performance.

---

## Core Features

* Demand Forecasting predicts future demand using historical data to improve inventory planning.
* Route Optimization identifies the most efficient delivery routes based on cost, time, and environmental impact.
* Disruption Simulation models real-world supply chain issues to estimate delays, cost changes, and service impact.
* Anomaly Detection detects unusual demand patterns using statistical techniques.
* KPI Dashboard provides real-time metrics such as service level, cost, and delivery performance.

---

## Architecture

```text
Frontend (Streamlit)
        ↓
Backend (FastAPI)
        ↓
Data Layer (CSV + Models)
```

---

## Project Structure

```text
CognixOps/
├── backend/
│   └── app/
│       ├── routes/
│       ├── services/
│       ├── models/
│       └── data/
└── frontend/
    ├── app.py
    ├── components/
    ├── services/
    └── utils/
```

---

## Tech Stack

| Layer         | Technology   |
| ------------- | ------------ |
| Frontend      | Streamlit    |
| Backend       | FastAPI      |
| Data          | Pandas       |
| ML            | scikit-learn |
| Optimization  | SciPy        |
| Visualization | Plotly       |
| Maps          | Folium       |

---

## Setup

### Backend

```bash
cd backend
pip install -r requirements.txt
python app/data/generate_datasets.py
uvicorn app.main:app --reload --port 8000
```

Runs at: [http://localhost:8000](http://localhost:8000)

---

### Frontend

```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

Runs at: [http://localhost:8501](http://localhost:8501)

---

## API Endpoints

* /forecast returns predicted demand values.
* /optimize computes optimal delivery routes.
* /simulate evaluates disruption scenarios.
* /kpi provides performance metrics.
* /anomaly detects demand anomalies.
* /health checks API status.

---

## Data

* demand_history.csv contains historical demand data.
* route_options.csv stores route information.
* kpi_snapshots.csv provides baseline metrics.

---

## Highlights

* Combines machine learning, optimization, and analytics in one system.
* Uses a modular backend design for scalability.
* Provides an interactive dashboard for decision-making.

---

## Summary

CognixOps is an AI-based platform that improves supply chain efficiency through predictive analytics and optimization.

---

## License

This project is proprietary and all rights are reserved.
