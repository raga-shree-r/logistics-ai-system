import pandas as pd
import numpy as np
import os

DATA_PATH = "data"

def generate_data():
    os.makedirs(DATA_PATH, exist_ok=True)

    # Demand
    dates = pd.date_range(end=pd.Timestamp.today(), periods=90)
    demand = pd.DataFrame({
        "date": np.tile(dates, 3),
        "sku": np.repeat(["SKU1", "SKU2", "SKU3"], 90),
        "demand": np.random.randint(50, 150, 270)
    })
    demand.to_csv(f"{DATA_PATH}/demand.csv", index=False)

    # Shipments
    shipments = pd.DataFrame({
        "shipment_id": range(200),
        "on_time": np.random.choice([0,1], 200, p=[0.2,0.8]),
        "lead_time": np.random.uniform(2, 8, 200)
    })
    shipments.to_csv(f"{DATA_PATH}/shipments.csv", index=False)

    # Disruptions
    disruptions = pd.DataFrame({
        "type": np.random.choice(["delay","weather","strike"], 30),
        "severity": np.random.randint(1, 5, 30)
    })
    disruptions.to_csv(f"{DATA_PATH}/disruptions.csv", index=False)

    # Inventory
    inventory = pd.DataFrame({
        "sku": [f"SKU{i}" for i in range(1,26)],
        "stock": np.random.randint(0, 200, 25),
        "reorder_point": np.random.randint(20, 80, 25)
    })
    inventory.to_csv(f"{DATA_PATH}/inventory.csv", index=False)

    # Routes
    routes = pd.DataFrame({
        "route": ["A-B-C", "A-D-C", "A-E-C"],
        "cost": [100, 80, 120],
        "time": [5, 7, 4],
        "co2": [50, 40, 60]
    })
    routes.to_csv(f"{DATA_PATH}/routes.csv", index=False)

    print("Data generated")