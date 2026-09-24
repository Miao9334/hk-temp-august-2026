# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pandas",
#     "matplotlib",
#     "seaborn",
# ]
# ///

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Ensure output directory exists
os.makedirs("out", exist_ok=True)

# 2. Read generated CSV dataset
df = pd.read_csv("data/daily_temp_2026.csv")
df["Date"] = pd.to_datetime(df["Date"])

# 3. Extract Day and Hour for pivot table
df["Day"] = df["Date"].dt.day
df["Hour"] = df["Date"].dt.hour

pivot_df = df.pivot(index="Day", columns="Hour", values="Mean Temp (°C)")

# 4. Create heatmap plot
plt.figure(figsize=(12, 8))
sns.heatmap(
    pivot_df, 
    cmap="coolwarm", 
    cbar_kws={'label': 'Mean Temp (°C)'},
    linewidths=0.5
)

plt.title("Hong Kong Hourly Temperature - August 2026")
plt.xlabel("Hour of the day")
plt.ylabel("Day of the month")

# 5. Save output PNG image
output_path = "out/plot.png"
plt.tight_layout()
plt.savefig(output_path, dpi=300)
plt.close()

print(f"Heatmap successfully saved to {output_path}!")