import sqlite3
import pandas as pd
conn = sqlite3.connect("db/nifty100.db")
files = {"companies": "data/processed/companies.csv","profitandloss": "data/processed/profitandloss.csv","balancesheet": "data/processed/balancesheet.csv","cashflow": "data/processed/cashflow.csv"}
for table, path in files.items():
    try:
        df = pd.read_csv(path)
        df.to_sql(table, conn, if_exists="append", index=False)
        print(f"{table} loaded successfully")
    except Exception as e:
        print(f"Error loading {table}: {e}")
conn.close()