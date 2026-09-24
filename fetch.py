# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pandas",
#     "numpy",
# ]
# ///

import os
import pandas as pd
import numpy as np

os.makedirs("data", exist_ok=True)
data_file = "data/daily_temp_2026.csv"

# 自动生成 2026 年 8 月逐小时气温模拟数据
dates = pd.date_range(start="2026-08-01 00:00:00", end="2026-08-31 23:00:00", freq="h")
np.random.seed(42)

base_temp = 29.5
diurnal_variation = 3.0 * np.sin((dates.hour - 9) * np.pi / 12)
random_noise = np.random.normal(0, 0.8, len(dates))

df = pd.DataFrame({
    "Date": dates,
    "Mean Temp (°C)": np.round(base_temp + diurnal_variation + random_noise, 1)
})

df.to_csv(data_file, index=False)
print("Data generated successfully and saved to data/daily_temp_2026.csv!")