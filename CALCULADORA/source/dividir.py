def dividir(numero1, numero2):
    if numero2 == 0:
        raise ValueError("No se puede dividir entre cero.")
    return numero1 / numero2
