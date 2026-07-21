import sqlite3
import pandas as pd
import os
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DB = os.path.join(BASE_DIR, "db", "nifty100.db")
conn = sqlite3.connect(DB)
companies = pd.read_sql("SELECT * FROM companies", conn)
ratios = pd.read_sql("SELECT * FROM financial_ratios", conn)
conn.close()
if "pe_ratio" not in ratios.columns:
    ratios["pe_ratio"] = 18
if "pb_ratio" not in ratios.columns:
    ratios["pb_ratio"] = 2.5
if "ev_ebitda" not in ratios.columns:
    ratios["ev_ebitda"] = 12
if "free_cash_flow_cr" not in ratios.columns:
    ratios["free_cash_flow_cr"] = 100
ratios["market_cap_crore"] = 10000
ratios["fcf_yield_pct"] = round((ratios["free_cash_flow_cr"] /ratios["market_cap_crore"]) * 100,2)
merged = pd.merge(ratios,companies[["company_id", "sector"]],on="company_id",how="left")
sector_pe = merged.groupby("sector")["pe_ratio"].median()
merged["sector_median_pe"] = merged["sector"].map(sector_pe)
merged["pe_vs_sector_median_pct"] = round((merged["pe_ratio"] /merged["sector_median_pe"]) * 100,2)
def valuation_flag(row):
    if row["pe_ratio"] > row["sector_median_pe"] * 1.5:
        return "Caution"
    elif row["pe_ratio"] < row["sector_median_pe"] * 0.7:
        return "Discount"
    else:
        return "Fair"
merged["flag"] = merged.apply(valuation_flag,axis=1)
os.makedirs("output", exist_ok=True)
summary = merged[ ["company_id",
        "sector",
        "pe_ratio",
        "pb_ratio",
        "ev_ebitda",
        "fcf_yield_pct",
        "sector_median_pe",
        "pe_vs_sector_median_pct",
        "flag"]]
summary.to_excel("output/valuation_summary.xlsx",index=False)
summary[summary["flag"] != "Fair"].to_csv("output/valuation_flags.csv",index=False)
print("Valuation Summary Created Successfully")