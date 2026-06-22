import pandas as pd
import numpy as np
import os
os.makedirs("data/processed", exist_ok=True)
companies = pd.DataFrame({"company_id": range(1, 93),"company_name": [f"Company_{i}" for i in range(1, 93)],"sector": np.random.choice(["IT", "Banking", "Pharma", "Auto"], 92)})
records = []
for cid in range(1, 93):
    for year in range(2019, 2024):
        records.append({"company_id": cid,"year": year,"sales": np.random.randint(1000, 50000),"net_profit": np.random.randint(100, 5000)})
profitandloss = pd.DataFrame(records)
balancesheet = profitandloss[["company_id", "year"]].copy()
balancesheet["assets"] = np.random.randint(5000, 100000, len(balancesheet))
balancesheet["liabilities"] = np.random.randint(1000, 50000, len(balancesheet))
cashflow = profitandloss[["company_id", "year"]].copy()
cashflow["operating_cash_flow"] = np.random.randint(500, 10000, len(cashflow))
companies.to_csv("data/processed/companies.csv", index=False)
profitandloss.to_csv("data/processed/profitandloss.csv", index=False)
balancesheet.to_csv("data/processed/balancesheet.csv", index=False)
cashflow.to_csv("data/processed/cashflow.csv", index=False)
print("Sample datasets generated successfully.")