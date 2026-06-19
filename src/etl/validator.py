import pandas as pd
def check_duplicates(df, columns):
    duplicates = df[df.duplicated(subset=columns)]
    return len(duplicates) == 0
def check_positive_sales(df):
    return (df["sales"] > 0).all()
def check_null_values(df):
    return not df.isnull().values.any()
if __name__ == "__main__":
    print("Validator ready")