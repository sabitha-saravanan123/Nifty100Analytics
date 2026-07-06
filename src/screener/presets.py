import sqlite3
import pandas as pd
conn = sqlite3.connect("db/nifty100.db")
df = pd.read_sql("SELECT * FROM financial_ratios", conn)
quality = df[(df["return_on_equity_pct"] > 15) & (df["debt_to_equity"] < 1)]
value = df[(df["debt_to_equity"] < 2) & (df["asset_turnover"] > 1)]
growth = df[(df["return_on_capital_employed_pct"] > 15)]
dividend = df[(df["net_profit_margin_pct"] > 10)]
debtfree = df[(df["debt_to_equity"] == 0)]
turnaround = df[(df["return_on_assets_pct"] > 5)]
with pd.ExcelWriter("output/screener_output.xlsx") as writer:
    quality.to_excel(writer, sheet_name="Quality", index=False)
    value.to_excel(writer, sheet_name="Value", index=False)
    growth.to_excel(writer, sheet_name="Growth", index=False)
    dividend.to_excel(writer, sheet_name="Dividend", index=False)
    debtfree.to_excel(writer, sheet_name="DebtFree", index=False)
    turnaround.to_excel(writer, sheet_name="Turnaround", index=False)
print("Screener report created.")
conn.close()