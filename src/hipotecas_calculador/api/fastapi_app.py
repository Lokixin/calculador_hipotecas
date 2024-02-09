from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from hipotecas_calculador.api.models import DatosHipoteca
from hipotecas_calculador.api.services import calcular_detalles_hipoteca

app = FastAPI()


@app.get("/", include_in_schema=False)
def home():
    return RedirectResponse(url="/docs")


@app.get("/healthcheck", summary="Comprueba el estado del servidor", tags=["Utils"])
def healthcheck() -> dict[str, str]:
    return {"message": "ok"}


@app.get(
    "/api/calcular_hipoteca",
    summary="Calcula el valor de tu hipoteca",
    tags=["Hipoteca"],
    response_model=DatosHipoteca,
)
def calcular_hipoteca(
    precio_inmueble: float,
    years: int,
    interes_fijo: float,
    porcentaje_entrada: float,
    itp: float = 5,
) -> DatosHipoteca:
    return calcular_detalles_hipoteca(
        precio_inmueble=precio_inmueble,
        years=years,
        interes_fijo=interes_fijo,
        porcentaje_entrada=porcentaje_entrada,
        itp=itp,
    )
