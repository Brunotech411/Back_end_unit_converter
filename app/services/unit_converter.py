from pint import UnitRegistry

ureg = UnitRegistry()

def convert_units(request):
    try:
        quantity = request.value * ureg(request.from_unit)
        result = quantity.to(request.to_unit)
        return {
            "original": f"{request.value} {request.from_unit}",
            "converted": f"{result.magnitude:.4f} {result.units}"
        }
    except Exception as e:
        return {"error": str(e)}
