import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
os.makedirs("reports/radar_charts", exist_ok=True)
conn = sqlite3.connect("db/nifty100.db")
df = pd.read_sql("SELECT * FROM financial_ratios", conn)
conn.close()
df = df.fillna(0)
df["score"] = (df["return_on_equity_pct"] +df["return_on_capital_employed_pct"] +df["net_profit_margin_pct"] +df["asset_turnover"] * 10 +df["interest_coverage"] * 5)
top10 = df.sort_values("score", ascending=False).head(10)
metrics = ["return_on_equity_pct","return_on_capital_employed_pct","net_profit_margin_pct","debt_to_equity","interest_coverage","asset_turnover"]
labels = ["ROE","ROCE","NPM","D/E","ICR","ATO"]
angles = np.linspace(0, 2*np.pi, len(metrics), endpoint=False).tolist()
angles += angles[:1]
for _, row in top10.iterrows():
    values = [row[m] for m in metrics]
    values += values[:1]
    plt.figure(figsize=(6,6))
    ax = plt.subplot(111, polar=True)
    ax.plot(angles, values, linewidth=2)
    ax.fill(angles, values, alpha=0.25)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    plt.title(f"Company {int(row['company_id'])}")
    plt.savefig(f"reports/radar_charts/company_{int(row['company_id'])}.png")
    plt.close()
print("Radar charts generated successfully.")