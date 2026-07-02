import sqlite3
conn = sqlite3.connect("db/nifty100.db")
cursor = conn.cursor()
cursor.execute("""
SELECT company_id,year,return_on_equity_pct,return_on_capital_employed_pct FROM financial_ratios""")
rows = cursor.fetchall()
log = open("output/ratio_edge_cases.log", "w")
for row in rows:
    company_id = row[0]
    year = row[1]
    roe = row[2]
    roce = row[3]
    if roe is None:
        log.write(f"Company {company_id} Year {year} : Missing ROE | Data Issue\n")
    if roce is None:
        log.write(f"Company {company_id} Year {year} : Missing ROCE | Data Issue\n")
log.close()
conn.close()
print("Validation completed.")
print("Log file created.")