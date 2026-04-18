🚀 Cognix — AI Logistics Intelligence Platform
An end-to-end AI-powered logistics system that helps businesses predict demand, optimize delivery routes, simulate disruptions, detect anomalies, and monitor performance in real time.

📌 Overview
CognixOps acts like a smart control tower for supply chains.

It helps answer key questions:

📈 What will future demand look like?

🚚 What is the best delivery route?

⚠️ What happens if disruptions occur?

📊 How is the system performing?

🧠 Core Features
🔮 Demand Forecasting
Predicts future demand using historical data.

Benefits:

Avoid stockouts

Reduce excess inventory

🚚 Route Optimization
Finds the most efficient route based on:

Cost 💰

Speed ⏱️

Environmental impact 🌱

⚠️ Disruption Simulation
Simulates real-world supply chain issues:

Weather disruptions

Supplier delays

Transport failures

Outputs:

Delay impact

Cost increase

Service level drop

🚨 Anomaly Detection
Detects unusual demand spikes using statistical analysis.

📊 KPI Dashboard
Displays key performance metrics:

Service Level

Lead Time

Total Cost

CO₂ Emissions

Delivery Performance

🏗️ Architecture
Frontend (Streamlit UI)
        ↓
Backend (FastAPI)
        ↓
Data Layer (CSV + ML Models)
📂 Project Structure
CognixOps/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── models/
│   │   ├── routes/
│   │   ├── services/
│   │   └── data/
│   └── requirements.txt
│
└── frontend/
    ├── app.py
    ├── config.py
    ├── components/
    ├── services/
    └── utils/
🧪 Tech Stack
Layer	Technology
Frontend	Streamlit
Backend	FastAPI
Data Processing	Pandas
Machine Learning	scikit-learn
Optimization	SciPy
Visualization	Plotly
Maps	Folium
▶️ Getting Started
✅ Prerequisites
Python 3.10+

pip

⚙️ Backend Setup
cd backend
pip install -r requirements.txt

# Generate datasets
python app/data/generate_datasets.py

# Run backend server
uvicorn app.main:app --reload --port 8000
Backend runs at:
👉 http://localhost:8000

🖥️ Frontend Setup
cd frontend
pip install -r requirements.txt

# Run frontend
streamlit run app.py
Frontend runs at:
👉 http://localhost:8501

🔌 API Endpoints
Endpoint	Description
/forecast	Predict demand
/optimize	Optimize delivery routes
/simulate	Simulate disruptions
/kpi	Fetch KPI metrics
/anomaly	Detect anomalies
/health	API health check
📊 Data Used
demand_history.csv → Historical demand data

route_options.csv → Transport routes

kpi_snapshots.csv → KPI baseline data

✨ Key Highlights
Combines Machine Learning + Optimization + Analytics

Designed for real-world logistics problems

Modular and scalable architecture

Interactive dashboard for easy decision-making

🆕 Version 2.0 Updates
Improved demand forecasting (seasonality + ML)

Advanced optimization (LP + MIP + Network Flow)

Realistic disruption simulations

New anomaly detection module

Enhanced dashboard UI

🎯 One-Line Summary
CognixOps is an AI-powered platform that helps optimize supply chain decisions through forecasting, routing, simulation, and real-time analytics.

📜 License
This project is proprietary. All rights reserv
