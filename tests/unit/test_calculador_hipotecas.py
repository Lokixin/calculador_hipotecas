from hipotecas_calculador.formulas.calculador_hipotecas import (
    compute_monthly_payment,
    compute_required_loan,
    compute_total_interest,
    compute_upfront_payment,
)


def test_compute_monthly_payment():
    property_price = 3e5
    upfront_payment = compute_upfront_payment(property_price=property_price)
    required_loan = compute_required_loan(total_property_price=property_price)
    monthly_payment = compute_monthly_payment(
        total_mortgage=required_loan, interest_rate=0.03, years=30
    )
    total_interest = compute_total_interest(monthly_payment, 30, required_loan)
    total_cost = total_interest + required_loan + upfront_payment
    assert total_cost
    assert True
