def convert_rtd(request):
    try:
        resistance = request.resistance
        # Fórmula simplificada para RTD PT100 (0°C = 100 Ω, 0.385 Ω/°C)
        temperature = (resistance - 100) / 0.385
        return {
            "original": f"{resistance:.2f} Ω",
            "converted": f"{temperature:.2f} °C"
        }
    except Exception as e:
        return {"error": str(e)}
