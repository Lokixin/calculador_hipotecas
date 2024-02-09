from hipotecas_calculador.api.models import DatosHipoteca
from hipotecas_calculador.formulas.calculador_hipotecas import (
    compute_monthly_payment,
    compute_required_loan,
    compute_total_interest,
    compute_upfront_payment,
)


def calcular_detalles_hipoteca(
    precio_inmueble: float,
    years: int,
    interes_fijo: float,
    porcentaje_entrada: float,
    itp: float = 5,
) -> DatosHipoteca:
    porcentaje_entrada = porcentaje_entrada / 100
    itp = itp / 100
    interes_fijo = interes_fijo / 100

    precio_entrada = compute_upfront_payment(
        property_price=precio_inmueble,
        upfront_percentage=porcentaje_entrada,
    )
    prestamos_necesario = compute_required_loan(
        total_property_price=precio_inmueble,
        upfront_percentage=porcentaje_entrada,
        itp=itp,
    )
    pago_mensual = compute_monthly_payment(
        total_mortgage=prestamos_necesario, interest_rate=interes_fijo, years=years
    )
    interes_total = compute_total_interest(
        monthly_payment=pago_mensual, years=years, total_loan=prestamos_necesario
    )
    coste_total = interes_total + prestamos_necesario + precio_entrada

    return DatosHipoteca(
        precio_entrada=round(precio_entrada, 2),
        prestamo_necesario=round(prestamos_necesario, 2),
        pago_mensual=round(pago_mensual, 2),
        interes_total=round(interes_total, 2),
        coste_total=round(coste_total, 2),
    )
