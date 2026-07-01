import sqlite3
import pandas as pd
from src.analytics.ratios import (
    net_profit_margin,
    operating_profit_margin,
    return_on_equity,
    return_on_capital_employed,
    return_on_assets,
    debt_to_equity,
    interest_coverage,
    asset_turnover
)
conn = sqlite3.connect("db/nifty100.db")
query = """
SELECT
p.company_id,
p.year,
p.sales,
p.operating_profit,
p.other_income,
p.EBIT,
p.interest,
p.net_profit,
b.assets,
b.equity_capital,
b.reserves,
b.borrowings
FROM profitandloss p
JOIN balancesheet b
ON p.company_id=b.company_id
AND p.year=b.year
"""
df = pd.read_sql(query, conn)
records=[]
for _,row in df.iterrows():
    records.append({
        "company_id":row.company_id,
        "year":row.year,
        "net_profit_margin_pct":
        net_profit_margin(row.net_profit,row.sales),
        "operating_profit_margin_pct":
        operating_profit_margin(row.operating_profit,row.sales),
        "return_on_equity_pct":
        return_on_equity(row.net_profit,row.equity_capital,row.reserves),
        "return_on_capital_employed_pct":
        return_on_capital_employed(
            row.EBIT,
            row.equity_capital,
            row.reserves,
            row.borrowings ), "return_on_assets_pct": return_on_assets(row.net_profit,row.assets),"debt_to_equity":debt_to_equity( row.borrowings, row.equity_capital, row.reserves),"interest_coverage":interest_coverage( row.operating_profit,row.other_income,row.interest),"asset_turnover":asset_turnover(row.sales,row.assets)})
ratios=pd.DataFrame(records)
ratios.to_sql("financial_ratios",conn,if_exists="replace",index=False)
print(ratios.head())
print()
print("Rows inserted:",len(ratios))
conn.close()