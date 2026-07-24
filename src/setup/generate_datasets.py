import sqlite3
import pandas as pd
import os
import random
os.makedirs("data/raw", exist_ok=True)
conn = sqlite3.connect("db/nifty100.db")
companies = pd.read_sql("SELECT * FROM companies", conn)
companies.to_excel("data/raw/companies.xlsx",index=False)
print("companies.xlsx created")
ratios = pd.read_sql("SELECT * FROM financial_ratios",conn)
analysis = pd.DataFrame()
analysis["company_id"] = sorted(ratios["company_id"].unique())
analysis["compounded_sales_growth"] = [f"10 Years: {random.randint(8,25)}%"for _ in range(len(analysis))]
analysis["compounded_profit_growth"] = [f"10 Years: {random.randint(8,28)}%"for _ in range(len(analysis))]
analysis["stock_price_cagr"] = [f"10 Years: {random.randint(10,35)}%"for _ in range(len(analysis))]
analysis["roe"] = [f"10 Years: {random.randint(10,30)}%"for _ in range(len(analysis))]
analysis.to_excel("data/raw/analysis.xlsx",index=False)
print("analysis.xlsx created")
market = pd.DataFrame()
market["company_id"] = analysis["company_id"]
market["market_cap_crore"] = [random.randint(10000,1000000)for _ in range(len(market))]
market["pe_ratio"] = [round(random.uniform(8,45),2)for _ in range(len(market))]
market["pb_ratio"] = [round(random.uniform(0.5,10),2)for _ in range(len(market))]
market["ev_ebitda"] = [round(random.uniform(4,25),2)for _ in range(len(market))]
market.to_excel("data/raw/market_cap.xlsx",index=False)
print("market_cap.xlsx created")
groups = [
    "IT Services",
    "Banking",
    "Financial Services",
    "FMCG",
    "Healthcare",
    "Energy",
    "Auto",
    "Metals",
    "Pharma",
    "Telecom",
    "Consumer"]
peer = pd.DataFrame()
peer["company_id"] = analysis["company_id"]
peer["peer_group"] = [random.choice(groups)for _ in range(len(peer))]
peer.to_excel("data/raw/peer_groups.xlsx",index=False)
print("peer_groups.xlsx created")
conn.close()
print("\nAll datasets generated successfully.")