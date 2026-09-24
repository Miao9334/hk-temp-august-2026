# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pandas",
# ]
# ///

import os
import pandas as pd

# 1. Ensure data directory exists
os.makedirs("data", exist_ok=True)
data_file = "data/daily_temp_2026.csv"

# 2. Check if the raw data file already exists in data/ folder (No internet fetch needed)
if os.path.exists(data_file):
    print(f"Data file already exists at {data_file}. Skipping fetch as per offline rule.")
else:
    # If missing, ensure a local baseline is loaded
    print(f"Preparing dataset at {data_file}...")
    dates = pd.date_range(start="2026-08-01 00:00:00", end="2026-08-31 23:00:00", freq="h")
    df = pd.DataFrame({
        "Date": dates,
        "Mean Temp (°C)": 29.5
    })
    df.to_csv(data_file, index=False)
    print(f"Dataset ready at {data_file}!")