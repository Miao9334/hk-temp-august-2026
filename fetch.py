# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "requests",
#     "pandas",
# ]
# ///

import os
import requests
import pandas as pd

# 1. Ensure data directory exists
os.makedirs("data", exist_ok=True)
output_path = "data/daily_temp_2026.csv"

# 2. Fetch real hourly weather data for Hong Kong with explicit timezone setting
# Open-Meteo URL using timezone=Asia%2FHong_Kong to ensure correct HKT local hours
url = (
    "https://archive-api.open-meteo.com/v1/archive?"
    "latitude=22.3193&longitude=114.1694&"
    "start_date=2026-08-01&end_date=2026-08-31&"
    "hourly=temperature_2m&"
    "timezone=Asia%2FHong_Kong"
)

print("Fetching Hong Kong local time weather data from Open-Meteo API...")
response = requests.get(url)
response.raise_for_status()

data = response.json()

# 3. Parse JSON into clean DataFrame
df = pd.DataFrame({
    "Date": data["hourly"]["time"],
    "Mean Temp (°C)": data["hourly"]["temperature_2m"]
})

# 4. Save to local CSV
df.to_csv(output_path, index=False)
print(f"Successfully saved Hong Kong local time dataset to {output_path}!")