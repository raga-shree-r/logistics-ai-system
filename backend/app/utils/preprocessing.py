import os
from app.utils.data_generator import generate_data

def ensure_data():
    if not os.path.exists("data/demand.csv"):
        generate_data()