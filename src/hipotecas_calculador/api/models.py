from pydantic import BaseModel, computed_field


class DatosHipoteca(BaseModel):
    precio_entrada: float
    prestamo_necesario: float
    pago_mensual: float
    interes_total: float
    coste_total: float

    @computed_field
    def descripcion_hipoteca(self) -> str:
        return (
            f"Tendrás que dar una entrada de {self.precio_entrada}\n"
            f"Necesitarás un préstamos de {self.prestamo_necesario}\n"
            f"Pagarás cada mes {self.pago_mensual}€\n"
            f"Y en total te costará {self.coste_total}\n"
        )
