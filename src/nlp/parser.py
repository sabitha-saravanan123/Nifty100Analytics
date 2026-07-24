import pandas as pd
import re
import os
os.makedirs("output", exist_ok=True)
df = pd.read_excel("data/raw/analysis.xlsx")
pattern = r"(\d+)\s*Years?:?\s*([\d.]+)%"
parsed = []
failed = []
columns = ["compounded_sales_growth","compounded_profit_growth","stock_price_cagr","roe"]
for _, row in df.iterrows():
    company = row["company_id"]
    for col in columns:
        text = str(row[col])
        match = re.search(pattern, text)
        if match:
            parsed.append({"company_id": company,"metric_type": col,"period_years": int(match.group(1)),"value_pct": float(match.group(2))})
        else:
            failed.append({"company_id": company,"metric_type": col,"text": text})
parsed_df = pd.DataFrame(parsed)
failed_df = pd.DataFrame(failed)
parsed_df.to_csv("output/analysis_parsed.csv",index=False)
failed_df.to_csv("output/parse_failures.csv",index=False)
print("Parser Completed Successfully")