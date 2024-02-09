from hipotecas_calculador.api.models import DatosHipoteca
from hipotecas_calculador.api.services import calcular_detalles_hipoteca


def test_calcular_detalles_hipoteca():
    precio_inmueble = 300000
    years = 30
    interes_fijo = 3
    porcentaje_entrada = 30
    itp = 10

    detalles_hipoteca = calcular_detalles_hipoteca(
        precio_inmueble=precio_inmueble,
        years=years,
        interes_fijo=interes_fijo,
        porcentaje_entrada=porcentaje_entrada,
        itp=itp,
    )

    detalles_hipoteca_esperados = {
        "precio_entrada": 90000,
        "prestamo_necesario": 240000,
        "pago_mensual": 1011.85,
        "interes_total": 124265.89,
        "coste_total": 454265.89,
        "descripcion_hipoteca": "Tendrás que dar una entrada de 90000.0\nNecesitarás un préstamos de 240000.0\nPagarás cada mes 1011.85€\nY en total te costará 454265.89\n",
    }
    detalles_hipoteca_esperados = DatosHipoteca(**detalles_hipoteca_esperados)
    assert detalles_hipoteca == detalles_hipoteca_esperados
