def calculate_range(request):
    try:
        altura_min = request.altura_min
        altura_max = request.altura_max
        densidade = request.densidade
        zona_morta = request.zona_morta

        # Constante: 1 mH2O = 1000 mmH2O
        mmH2O_por_metro = 1000
        gravidade = 9.80665  # m/s²

        # Pressão mínima considerando zona morta
        p_min_mmh2o = ((altura_min + zona_morta) * densidade * gravidade) / 9.80665

        # Pressão máxima
        p_max_mmh2o = ((altura_max + zona_morta) * densidade * gravidade) / 9.80665

        return {
            "p_min_mmH2O": round(p_min_mmh2o, 2),
            "p_max_mmH2O": round(p_max_mmh2o, 2)
        }
    except Exception as e:
        return {"error": str(e)}
