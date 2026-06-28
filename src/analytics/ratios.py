def net_profit_margin(net_profit, sales):
    if sales == 0:
        return None
    return round((net_profit / sales) * 100, 2)
def operating_profit_margin(operating_profit, sales):
    if sales == 0:
        return None
    return round((operating_profit / sales) * 100, 2)
def opm_cross_check(calculated_opm, stored_opm):
    if calculated_opm is None or stored_opm is None:
        return False
    difference = abs(calculated_opm - stored_opm)
    return difference <= 1
def return_on_equity(net_profit, equity_capital, reserves):
    equity = equity_capital + reserves
    if equity <= 0:
        return None
    return round((net_profit / equity) * 100, 2)
def return_on_capital_employed(ebit,equity_capital,reserves,borrowings):
    capital = equity_capital + reserves + borrowings
    if capital <= 0:
        return None
    return round((ebit / capital) * 100, 2)
def return_on_assets(net_profit, total_assets):
    if total_assets == 0:
        return None
    return round((net_profit / total_assets) * 100, 2)
def profitability_summary(sales,operating_profit,stored_opm,net_profit,equity_capital,reserves,borrowings,total_assets,ebit,):
    npm = net_profit_margin(net_profit, sales)
    opm = operating_profit_margin(operating_profit,sales)
    roe = return_on_equity(net_profit,equity_capital,reserves)
    roce = return_on_capital_employed(ebit,equity_capital,reserves,borrowings)
    roa = return_on_assets(net_profit,total_assets)
    opm_match = opm_cross_check(opm,stored_opm)
    return {"Net Profit Margin (%)": npm,"Operating Profit Margin (%)": opm,"OPM Match": opm_match,"ROE (%)": roe,"ROCE (%)": roce,"ROA (%)": roa}
if __name__ == "__main__":
    result = profitability_summary(sales=10000,operating_profit=2500,stored_opm=25,net_profit=1800,equity_capital=2000,reserves=6000, borrowings=1500,total_assets=18000,ebit=2700)
    print("\nProfitability Ratios\n")
    for key, value in result.items():
        print(f"{key}: {value}")

        
def debt_to_equity(borrowings, equity_capital, reserves):
    equity = equity_capital + reserves
    if borrowings == 0:
        return 0
    if equity <= 0:
        return None
    return round(borrowings / equity, 2)
def high_leverage_flag(de_ratio, sector):
    if sector != "Financials" and de_ratio is not None and de_ratio > 5:
        return True
    return False
def interest_coverage(operating_profit, other_income, interest):
    if interest == 0:
        return None
    return round((operating_profit + other_income) / interest, 2)
def icr_label(interest):
    if interest == 0:
        return "Debt Free"
    return "Normal"
def icr_warning(icr):
    if icr is None:
        return False
    return icr < 1.5
def net_debt(borrowings, investments):
    return borrowings - investments
def asset_turnover(sales, total_assets):
    if total_assets == 0:
        return None
    return round(sales / total_assets, 2)