from src.analytics.ratios import *
def test1():
    assert debt_to_equity(1000, 2000, 3000) == 0.2
def test2():
    assert debt_to_equity(0, 2000, 3000) == 0
def test3():
    assert high_leverage_flag(6, "IT") == True
def test4():
    assert high_leverage_flag(6, "Financials") == False
def test5():
    assert interest_coverage(500, 100, 200) == 3.0
def test6():
    assert interest_coverage(500, 100, 0) == None
def test7():
    assert icr_label(0) == "Debt Free"
def test8():
    assert asset_turnover(10000, 5000) == 2.0