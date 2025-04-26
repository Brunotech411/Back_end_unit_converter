from fastapi import APIRouter
from app.services.unit_converter import convert_units
from app.services.temperature_converter import convert_temperature
from app.services.thermocouple_converter import convert_thermocouple
from app.services.rtd_converter import convert_rtd
from app.services.level_transmitter_range import calculate_range
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

class RTDConversionRequest(BaseModel):
    resistance: float  #'convertes RTD'

class LevelRangeRequest(BaseModel):
    altura_min: float
    altura_max: float
    densidade: float
    zona_morta: float = 0.0

# Rotas
@router.post("/convert-pressure")
def convert_pressure_route(request: ConversionRequest):
    return convert_units(request)

@router.post("/convert-temperature")
def convert_temperature_route(request: TemperatureConversionRequest):
    return convert_temperature(request)

@router.post("/convert-thermocouple")
def convert_thermocouple_route(request: ThermocoupleConversionRequest):
    return convert_thermocouple(request)

@router.post("/convert-rtd")
def convert_rtd_route(request: RTDConversionRequest):
    return convert_rtd(request)

@router.post("/calculate-level-range")
def calculate_level_range_route(request: LevelRangeRequest):
    return calculate_range(request)
