import sqlite3
conn = sqlite3.connect("db/nifty100.db")
result = conn.execute("PRAGMA foreign_key_check;").fetchall()
if len(result) == 0:
    print("No foreign key errors")
else:
    print(result)
conn.close()