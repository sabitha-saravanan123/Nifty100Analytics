from src.analytics.cashflow_kpis import *
def test1():
    assert free_cash_flow(5000, -2000) == 3000
def test2():
    assert cfo_quality(1000, 500) == "High Quality"
def test3():
    assert cfo_quality(300, 500) == "Moderate"
def test4():
    assert cfo_quality(100, 500) == "Accrual Risk"
def test5():
    assert capex_intensity(-200, 10000) == "Asset Light"
def test6():
    assert capex_intensity(-500, 10000) == "Moderate"
def test7():
    assert capex_intensity(-1500, 10000) == "Capital Intensive"
def test8():
    assert capital_pattern(1000, -500, -200) == "Reinvestor"