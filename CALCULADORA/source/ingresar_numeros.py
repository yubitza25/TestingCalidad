def ingresar_numeros(mensaje):
    try:
        numero = float(input(mensaje))    
        return numero
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")
        return None, None
