import sqlite3
conn = sqlite3.connect("db/nifty100.db")
tables = [
    "companies",
    "profitandloss",
    "balancesheet",
    "cashflow"]
for table in tables:
    count = conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
    print(table, ":", count)
conn.close()