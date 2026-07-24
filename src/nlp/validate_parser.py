import pandas as pd
parsed = pd.read_csv("output/analysis_parsed.csv")
print(parsed.head())
print()
print("Total Parsed:", len(parsed))