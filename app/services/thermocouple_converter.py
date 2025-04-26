thermocouple_coefficients = {
    "K": 0.041,  # mV/°C
    "J": 0.055,  # mV/°C
    "T": 0.043,  # mV/°C
}

def convert_thermocouple(request):
    try:
        value = request.value
        thermocouple_type = request.thermocouple_type.upper()
        direction = request.direction.lower()

        if thermocouple_type not in thermocouple_coefficients:
            raise ValueError(f"Tipo de termopar '{thermocouple_type}' não suportado.")

        coeff = thermocouple_coefficients[thermocouple_type]

        if direction == "celsius_para_mv":
            result = value * coeff
            unit = "mV"
        elif direction == "mv_para_celsius":
            result = value / coeff
            unit = "°C"
        else:
            raise ValueError(f"Direção '{direction}' inválida.")

        return {
            "original": f"{value} {'°C' if direction == 'celsius_para_mv' else 'mV'}",
            "converted": f"{result:.3f} {unit}"
        }

    except Exception as e:
        return {"error": str(e)}
