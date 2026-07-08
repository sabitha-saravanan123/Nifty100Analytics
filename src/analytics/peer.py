import sqlite3
import pandas as pd
conn = sqlite3.connect("db/nifty100.db")
df = pd.read_sql("SELECT * FROM financial_ratios", conn)
groups = ["IT Services","Banking","Pharma","FMCG","Auto"]
df["peer_group"] = [groups[i % len(groups)] for i in range(len(df))]
metrics = ["return_on_equity_pct","return_on_capital_employed_pct","net_profit_margin_pct","asset_turnover","interest_coverage"]
result = []
for group in df["peer_group"].unique():
    temp = df[df["peer_group"] == group].copy()
    for metric in metrics:
        temp[metric + "_rank"] = temp[metric].rank(pct=True) * 100
    result.append(temp)
peer = pd.concat(result)
peer.to_sql("peer_percentiles",conn,if_exists="replace",index=False)
peer.to_excel("output/peer_comparison.xlsx",index=False)
print("Peer comparison completed.")
conn.close()