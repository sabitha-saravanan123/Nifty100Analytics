def calculate_cagr(start, end, years):
    if years <= 0:
        return None
    if start == 0:
        return "ZERO_BASE"
    if start > 0 and end > 0:
        cagr = (((end / start) ** (1 / years)) - 1) * 100
        return round(cagr, 2)
    if start > 0 and end < 0:
        return "DECLINE_TO_LOSS"
    if start < 0 and end > 0:
        return "TURNAROUND"
    if start < 0 and end < 0:
        return "BOTH_NEGATIVE"
    return "INSUFFICIENT"

def revenue_cagr(start_sales, end_sales, years):
    return calculate_cagr(start_sales, end_sales, years)
def pat_cagr(start_profit, end_profit, years):
    return calculate_cagr(start_profit, end_profit, years)
def eps_cagr(start_eps, end_eps, years):
    return calculate_cagr(start_eps, end_eps, years)