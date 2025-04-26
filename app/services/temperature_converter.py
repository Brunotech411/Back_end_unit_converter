def convert_temperature(request):
    try:
        value = request.value
        from_unit = request.from_unit.upper()
        to_unit = request.to_unit.upper()

        if from_unit == to_unit:
            return {"original": f"{value} {from_unit}", "converted": f"{value:.2f} {to_unit}"}

        if from_unit == "C":
            if to_unit == "F":
                result = (value * 9/5) + 32
            elif to_unit == "K":
                result = value + 273.15
            else:
                raise ValueError
        elif from_unit == "F":
            if to_unit == "C":
                result = (value - 32) * 5/9
            elif to_unit == "K":
                result = (value - 32) * 5/9 + 273.15
            else:
                raise ValueError
        elif from_unit == "K":
            if to_unit == "C":
                result = value - 273.15
            elif to_unit == "F":
                result = (value - 273.15) * 9/5 + 32
            else:
                raise ValueError
        else:
            raise ValueError

        return {
            "original": f"{value} {from_unit}",
            "converted": f"{result:.2f} {to_unit}"
        }

    except ValueError:
        return {"error": f"Conversão de {request.from_unit} para {request.to_unit} não suportada."}
