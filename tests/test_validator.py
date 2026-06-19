import pandas as pd
from src.etl.validator import (check_duplicates,check_positive_sales,check_null_values)
def test_duplicates():
    df = pd.DataFrame({"company_id": [1, 2, 3]})
    assert check_duplicates(df, ["company_id"])
def test_positive_sales():
    df = pd.DataFrame({"sales": [100, 200, 300]})
    assert check_positive_sales(df)
def test_null_values():
    df = pd.DataFrame({"sales": [100, 200, 300]})
    assert check_null_values(df)