from src.etl.normaliser import normalize_year, normalize_ticker
def test_year_2023():
    assert normalize_year("2023") == 2023
def test_year_fy23():
    assert normalize_year("FY23") == 2023
def test_year_2022_23():
    assert normalize_year("2022-23") == 2023
def test_ticker_tcs():
    assert normalize_ticker("tcs") == "TCS"
def test_ticker_ns():
    assert normalize_ticker("TCS.NS") == "TCS"
def test_ticker_ltd():
    assert normalize_ticker("TCS LTD") == "TCS"