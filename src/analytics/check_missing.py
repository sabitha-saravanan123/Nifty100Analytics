import sqlite3
import pandas as pd
conn = sqlite3.connect("db/nifty100.db")
df = pd.read_sql("SELECT * FROM financial_ratios", conn)
conn.close()
print(df.isnull().sum())