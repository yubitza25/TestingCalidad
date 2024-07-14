from crear_sopa_letras import crear_sopa_letras
from imprimir_sopa import imprimir_sopa

# Obtener entrada del usuario
while True:
    n = int(input("Ingrese el número de palabras (N): "))
    if n <= 100:  # 100 es el número total de casillas en una sopa de 10x10
        break
    else:
        print("Error: El número de palabras no puede ser mayor que 100 (tamaño de la sopa 10x10).")

palabras = []
for i in range(n):
    while True:
        palabra = input(f"Ingrese la palabra {i+1}: ").strip().upper()
        if( len(palabra) ) <= 10:
            palabras.append(palabra)
            break
        else:
            print("Error: La palabra es menor a 10, ingrese una palabra mayor o igual a 10.")

# Verificar si el tamaño es suficiente para todas las palabras
if any(len(palabra) > 10 for palabra in palabras):
    print("Error: Una o más palabras son demasiado largas para una sopa de letras de 10x10.")
else:
    try:
        sopa_letras = crear_sopa_letras(palabras)
        print("\nSopa de letras 10x10 creada:")
        imprimir_sopa(sopa_letras)
    except ValueError as e:
        print(f"Error: {e}")
