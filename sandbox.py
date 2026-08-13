def promedio(valores):
    return sum(valores) / len(valores)


def primero_mayor_a(valores, umbral):
    coincidencias = [v for v in valores if v > umbral]
    return coincidencias[0]


def cargar_config(ruta):
    try:
        with open(ruta) as f:
            return f.read()
    except Exception:
        return None
