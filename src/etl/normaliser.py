import re
def normalize_year(year):
    year = str(year).strip()
    if year.isdigit():
        return int(year)
    if year.startswith("FY"):
        return int("20" + year[-2:])
    match = re.search(r'(\d{4})[-/](\d{2})', year)
    if match:
        return int("20" + match.group(2))
    raise ValueError("Invalid year format")
def normalize_ticker(ticker):
    ticker = str(ticker).upper().strip()
    ticker = ticker.replace(".NS", "")
    ticker = ticker.replace(" LTD", "")
    ticker = ticker.replace(" LIMITED", "")
    return ticker