import sqlite3
import pandas as pd
conn = sqlite3.connect("db/nifty100.db")
query = """SELECT company_id,COUNT(*) AS years_available FROM profitandloss GROUP BY company_id ORDER BY company_id"""
df = pd.read_sql(query, conn)
print(df.head())
conn.close()