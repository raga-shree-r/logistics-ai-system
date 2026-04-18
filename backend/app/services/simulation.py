def run_simulation(disruption_type: str):
    # Modify behavior based on disruption
    if disruption_type == "port_closure":
        cost_increase = 20
    elif disruption_type == "delay":
        cost_increase = 10
    else:
        cost_increase = 0

    return {
        "new_routes": [
            {
                "warehouse_id": "W1",
                "customer_id": "C1",
                "distance_km": 12,
                "cost": 60 + cost_increase,
                "co2": 6
            }
        ],
        "impact": {
            "cost_increase": cost_increase
        }
    }