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