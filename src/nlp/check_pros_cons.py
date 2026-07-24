import pandas as pd
df = pd.read_csv("output/pros_cons_generated.csv")
print(df.groupby("company_id")["type"].value_counts())