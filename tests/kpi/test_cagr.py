from src.analytics.cagr import *
def test1():
    assert revenue_cagr(100, 200, 5) == 14.87
def test2():
    assert revenue_cagr(100, -50, 5) == "DECLINE_TO_LOSS"
def test3():
    assert revenue_cagr(-100, 50, 5) == "TURNAROUND"
def test4():
    assert revenue_cagr(-100, -50, 5) == "BOTH_NEGATIVE"
def test5():
    assert revenue_cagr(0, 100, 5) == "ZERO_BASE"
def test6():
    assert pat_cagr(500, 1000, 5) == 14.87
def test7():
    assert eps_cagr(10, 20, 5) == 14.87
def test8():
    assert calculate_cagr(100, 200, 0) == None
def test9():
    assert pat_cagr(100, -20, 5) == "DECLINE_TO_LOSS"
def test10():
    assert eps_cagr(-10, 20, 5) == "TURNAROUND"