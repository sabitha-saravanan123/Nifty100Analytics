import sqlite3
import pandas as pd
import yaml
with open("config/screener_config.yaml") as file:
    config = yaml.safe_load(file)
conn = sqlite3.connect("db/nifty100.db")
df = pd.read_sql("SELECT * FROM financial_ratios", conn)
filtered = df[
    (df["return_on_equity_pct"] >= config["roe_min"]) &
    (df["debt_to_equity"] <= config["de_max"]) &
    (df["asset_turnover"] >= config["asset_turnover_min"]) &
    (df["interest_coverage"] >= config["interest_coverage_min"])]
filtered["composite_quality_score"] = (
    filtered["return_on_equity_pct"] +
    filtered["return_on_capital_employed_pct"] +
    filtered["net_profit_margin_pct"]) / 3
filtered = filtered.sort_values(by="composite_quality_score",ascending=False)
filtered.to_excel("output/screener_output.xlsx",index=False)
print("Screener report created successfully.")
conn.close()