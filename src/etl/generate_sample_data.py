import pandas as pd
import numpy as np
import os
os.makedirs("data/processed", exist_ok=True)
companies = pd.DataFrame({"company_id": range(1, 93),"company_name": [f"Company_{i}" for i in range(1, 93)],"sector": np.random.choice(["IT", "Banking", "Pharma", "Auto"],92)})
companies.to_csv("data/processed/companies.csv",index=False)
pl_records = []
for company in range(1, 93):
    for year in range(2019, 2024):
        sales = np.random.randint(5000, 50000)
        operating_profit = np.random.randint(int(sales * 0.15),int(sales * 0.35))
        other_income = np.random.randint(100, 3000)
        ebit = operating_profit + other_income
        interest = np.random.randint(50, 1500)
        net_profit = np.random.randint( int(sales * 0.08), int(sales * 0.20))
        eps = round(np.random.uniform(5, 80), 2)
        dividend = round(np.random.uniform(0, eps * 2), 2)
        pl_records.append({"company_id": company,"year": year,"sales": sales,"operating_profit": operating_profit,"other_income": other_income,"EBIT": ebit,"interest": interest,"net_profit": net_profit,"earnings_per_share": eps,"dividend": dividend})
profitandloss = pd.DataFrame(pl_records)
profitandloss.to_csv( "data/processed/profitandloss.csv", index=False)
bs_records = []
for company in range(1, 93):
    for year in range(2019, 2024):
        assets = np.random.randint(30000, 150000)
        liabilities = np.random.randint(10000, 50000)
        equity = np.random.randint(5000, 30000)
        reserves = np.random.randint(5000, 40000)
        borrowings = np.random.randint(0, 25000)
        investments = np.random.randint(0, 15000)
        bs_records.append({"company_id": company,"year": year,"assets": assets,"liabilities": liabilities,"equity_capital": equity,"reserves": reserves,"borrowings": borrowings,"investments": investments})
balancesheet = pd.DataFrame(bs_records)
balancesheet.to_csv("data/processed/balancesheet.csv",index=False)
cf_records = []
for company in range(1, 93):
    for year in range(2019, 2024):
        operating = np.random.randint(3000, 25000)
        investing = -np.random.randint(500, 15000)
        financing = np.random.randint(-10000, 10000)
        cf_records.append({"company_id": company,"year": year,"operating_activity": operating,"investing_activity": investing,"financing_activity": financing})
cashflow = pd.DataFrame(cf_records)
cashflow.to_csv( "data/processed/cashflow.csv",index=False)
print("Sample datasets generated successfully.")