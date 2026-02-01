def requerido(texto, min_len=2):
    texto = (texto or "").strip()
    if len(texto) < min_len:
        raise ValueError("campo obligatorio")
    return texto

def entero_positivo(valor, nombre="valor"):
    v = int(valor)
    if v <= 0:
        raise ValueError(f"{nombre} debe ser > 0")
    return v

def numero_no_negativo(valor, nombre="valor"):
    v = float(valor)
    if v < 0:
        raise ValueError(f"{nombre} no puede ser negativo")
    return v
