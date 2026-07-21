import sqlite3
import pandas as pd
conn = sqlite3.connect("db/nifty100.db")
print("="*50)
print("NIFTY100 ANALYTICS QA REPORT")
print("="*50)
tables = ["companies","financial_ratios"]
for table in tables:
    try:
        df = pd.read_sql(f"SELECT * FROM {table}", conn)
        print(f"\n{table}")
        print("Rows :", len(df))
        print("Columns :", len(df.columns))
    except:
        print(f"{table} NOT FOUND")
conn.close()
print("\nDatabase Check Completed")