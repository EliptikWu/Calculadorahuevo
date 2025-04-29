def sumar_huevos(total, a_sumar):
    """Suma una cantidad de huevos al total."""
    try:
        return int(total) + int(a_sumar)
    except ValueError:
        return "Error: Ingresa números enteros válidos"