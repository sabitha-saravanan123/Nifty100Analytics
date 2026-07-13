import pandas as pd
df = pd.read_excel("output/screener_output.xlsx")
print("Total Companies:", len(df))
print("\nTop 5 Companies")
print(df[["company_id","composite_quality_score"]].head())