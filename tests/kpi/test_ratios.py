from src.analytics.ratios import *
def test_net_profit_margin():
    assert net_profit_margin(100, 1000) == 10.0

def test_net_profit_margin_zero_sales():
    assert net_profit_margin(100, 0) is None

def test_operating_profit_margin():
    assert operating_profit_margin(250, 1000) == 25.0

def test_opm_cross_check():
    assert opm_cross_check(25.0, 25.5) is True

def test_opm_cross_check_fail():
    assert opm_cross_check(25.0, 30.0) is False

def test_return_on_equity():
    assert return_on_equity(500, 2000, 3000) == 10.0

def test_return_on_equity_negative():
    assert return_on_equity(500, -1000, 500) is None

def test_return_on_assets():
    assert return_on_assets(500, 10000) == 5.0

def test_return_on_assets_zero():
    assert return_on_assets(500, 0) is None

def test_return_on_capital_employed():
    assert return_on_capital_employed(1000, 2000, 3000, 5000) == 10.0

def test_return_on_capital_employed_zero():
    assert return_on_capital_employed(1000, 0, 0, 0) is None