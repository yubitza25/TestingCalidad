# calculadora.py
from limpiar_pantalla import limpiar_pantalla
from tiempo_segundos import pausar_segundos
from opcion import mostrar_menu
from sumar import sumar
from restar import restar
from multiplicar import multiplicar
from dividir import dividir
from ingresar_numeros import ingresar_numeros

while True:
    opcion = mostrar_menu()

    if opcion == 5:
        print("Saliendo de la calculadora...")
        break
    
    num1 = ingresar_numeros("Ingrese el primer número (no se permiten letras ni negativos): ")
    num2 = ingresar_numeros("Ingrese el segundo número (no se permiten letras ni negativos): ") 
    
    if num1 is None or num2 is None:
        pausar_segundos(2)  
        limpiar_pantalla()
        continue

    if opcion == 1:
        resultado = sumar(num1, num2)
        print(f"La suma entre {num1} y {num2} es {resultado}")
    elif opcion == 2:
        resultado = restar(num1, num2)
        print(f"La resta entre {num1} y {num2} es {resultado}")
    elif opcion == 3:
        resultado = multiplicar(num1, num2)
        print(f"La multiplicación entre {num1} y {num2} es {resultado}")
    elif opcion == 4:
        try:
            resultado = dividir(num1, num2)
            print(f"La división entre {num1} y {num2} es {resultado}")
        except ValueError as e:
            print(f"Error: {e}")

    pausar_segundos(3) 
    limpiar_pantalla()

print("Gracias por utilizar la calculadora.")
