import sqlite3
import pandas as pd
conn = sqlite3.connect("db/nifty100.db")
df = pd.read_sql("SELECT * FROM peer_percentiles", conn)
conn.close()
with pd.ExcelWriter("output/peer_comparison.xlsx", engine="openpyxl") as writer:
    for group in df["peer_group"].unique():
        temp = df[df["peer_group"] == group].copy()
        summary = {
            "company_id": "Average",
            "year": "",
            "peer_group": group,
            "return_on_equity_pct": temp["return_on_equity_pct"].mean(),
            "return_on_capital_employed_pct": temp["return_on_capital_employed_pct"].mean(),
            "net_profit_margin_pct": temp["net_profit_margin_pct"].mean(),
            "debt_to_equity": temp["debt_to_equity"].mean(),
            "interest_coverage": temp["interest_coverage"].mean(),
            "asset_turnover": temp["asset_turnover"].mean()}
        temp = pd.concat([temp, pd.DataFrame([summary])], ignore_index=True)
        temp.to_excel(writer,sheet_name=group[:31],index=False)
print("Peer Comparison Report Generated Successfully.")