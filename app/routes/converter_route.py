from fastapi import APIRouter
from app.services.unit_converter import convert_units
from app.services.temperature_converter import convert_temperature
from app.services.thermocouple_converter import convert_thermocouple
from pydantic import BaseModel

router = APIRouter()

# Modelos de dados
class ConversionRequest(BaseModel):
    value: float
    from_unit: str
    to_unit: str

class TemperatureConversionRequest(BaseModel):
    value: float
    from_unit: str
    to_unit: str

class ThermocoupleConversionRequest(BaseModel):
    value: float
    thermocouple_type: str
    direction: str  # 'celsius_para_mv' ou 'mv_para_celsius'

# Rotas
@router.post("/convert")
def convert_units_route(request: ConversionRequest):
    return convert_units(request)

@router.post("/convert-temperature")
def convert_temperature_route(request: TemperatureConversionRequest):
    return convert_temperature(request)

@router.post("/convert-thermocouple")
def convert_thermocouple_route(request: ThermocoupleConversionRequest):
    return convert_thermocouple(request)
