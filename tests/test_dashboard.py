import sqlite3
import pandas as pd
conn = sqlite3.connect("db/nifty100.db")
companies = pd.read_sql("SELECT * FROM companies", conn)
ratios = pd.read_sql("SELECT * FROM financial_ratios", conn)
conn.close()
assert len(companies) > 0
assert len(ratios) > 0
print("Dashboard Database Test Passed")