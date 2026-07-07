import sqlite3
import pandas as pd
conn = sqlite3.connect("db/nifty100.db")
df = pd.read_sql("SELECT * FROM financial_ratios", conn)
df = df.fillna(0)
df["composite_quality_score"] = (
    df["return_on_equity_pct"] * 0.30 +
    df["return_on_capital_employed_pct"] * 0.25 +
    df["net_profit_margin_pct"] * 0.20 +
    df["asset_turnover"] * 10 +
    df["interest_coverage"] * 5)
df["composite_quality_score"] = df["composite_quality_score"].round(2)
df = df.sort_values(by="composite_quality_score",ascending=False)
df.to_excel("output/screener_output.xlsx",index=False)
print("Excel report created successfully.")
conn.close()