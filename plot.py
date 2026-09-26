# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pandas",
#     "seaborn",
#     "matplotlib",
# ]
# ///

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# 1. Load data
input_path = "data/daily_temp_2026.csv"
if not os.path.exists(input_path):
    print(f"Error: {input_path} not found. Please run fetch.py first.")
    exit(1)

df = pd.read_csv(input_path)

# 2. Data processing
df['Date'] = pd.to_datetime(df['Date'])
df['Day'] = df['Date'].dt.day
df['Hour'] = df['Date'].dt.hour

pivoted_data = df.pivot(index='Day', columns='Hour', values='Mean Temp (°C)')

# 3. Plotting
plt.figure(figsize=(16, 10))

# --- 按要求修改这里 ---
# 将 cmap 参数从发散色标（如 RdBu）改为单向橙红色标（如 OrRd, Reds, YlOrRd）
# OrRd: 橙色 -> 红色
# Reds: 浅红 -> 深红
# rocket (Seaborn default): 深紫色 -> 橙色 (很漂亮)

# 我们选择 OrRd (橙色到红色) 来实现低气温也是橙红色调
sns.heatmap(pivoted_data, cmap="OrRd", cbar_kws={'label': 'Mean Temp (°C)'},
            xticklabels=2, yticklabels=2, linewidths=0.05)
# --------------------

plt.title("Hong Kong Hourly Temperature - August 2026 (Warm Palette)")
plt.xlabel("Hour of the day")
plt.ylabel("Day of the month")

# 4. Save plot
os.makedirs("out", exist_ok=True)
output_path = "out/plot.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Updated plot saved to {output_path} with new color palette!")