import pandas as pd
df = pd.read_excel("output/peer_comparison.xlsx", sheet_name=0)
print(df.head())
print("\nVerification Completed.")