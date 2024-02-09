def compute_monthly_payment(
    total_mortgage: float,
    interest_rate: float,
    years: int,
) -> float:
    r = interest_rate / 12
    n = years * 12
    return total_mortgage * (r * (1 + r) ** n) / ((1 + r) ** n - 1)


def compute_upfront_payment(
    property_price: float,
    upfront_percentage: float = 0.3,
) -> float:
    return property_price * upfront_percentage


def compute_total_interest(monthly_payment: float, years: int, total_loan) -> float:
    return monthly_payment * years * 12 - total_loan


def compute_required_loan(
    total_property_price: float,
    upfront_percentage: float = 0.3,
    itp: float = 0.1,
) -> float:
    return total_property_price * (1 + itp - upfront_percentage)
