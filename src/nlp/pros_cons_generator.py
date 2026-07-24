import sqlite3
import pandas as pd
import os
os.makedirs("output", exist_ok=True)
conn = sqlite3.connect("db/nifty100.db")
companies = pd.read_sql("SELECT * FROM companies", conn)
ratios = pd.read_sql("SELECT * FROM financial_ratios", conn)
conn.close()
df = pd.merge(companies, ratios, on="company_id")
results = []
for _, row in df.iterrows():
    company = row["company_id"]
    if row["return_on_equity_pct"] > 20:
        results.append([company,"Pro","P1",
        "High return on equity above 20%.",90])
    if row["return_on_capital_employed_pct"] > 18:
        results.append([company,"Pro","P2",
        "Strong return on capital employed.",85])
    if row["net_profit_margin_pct"] > 15:
        results.append([company,"Pro","P3",
        "Healthy net profit margin.",80])
    if row["debt_to_equity"] == 0:
        results.append([company,"Pro","P4",
        "Debt free company.",95])
    if row["interest_coverage"] > 10:
        results.append([company,"Pro","P5",
        "Excellent interest coverage.",90])
    if row["asset_turnover"] > 1:
        results.append([company,"Pro","P6",
        "Efficient asset utilization.",75])
    if row["return_on_equity_pct"] < 10:
        results.append([company,"Con","C1",
        "Low return on equity.",85])
    if row["return_on_capital_employed_pct"] < 10:
        results.append([company,"Con","C2",
        "Low return on capital employed.",85])
    if row["net_profit_margin_pct"] < 5:
        results.append([company,"Con","C3",
        "Weak profitability.",80])
    if row["debt_to_equity"] > 2:
        results.append([company,"Con","C4",
        "High debt level.",90])
    if row["interest_coverage"] < 2:
        results.append([company,"Con","C5",
        "Poor interest coverage.",90])
    if row["asset_turnover"] < 0.5:
        results.append([company,"Con","C6",
        "Low asset utilization.",75])
output = pd.DataFrame(results,
columns=["company_id","type","rule_id","text","confidence_pct"])
output.to_csv("output/pros_cons_generated.csv",index=False)
print("Pros & Cons Generated Successfully")