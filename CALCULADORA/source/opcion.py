from limpiar_pantalla import limpiar_pantalla
from tiempo_segundos import pausar_segundos

def mostrar_menu():
    while True:
        # Mostrar menú de opciones
        print("*** CALCULADORA ***")
        print("1) SUMAR")
        print("2) RESTAR")
        print("3) MULTIPLICAR")
        print("4) DIVISION")
        print("5) SALIR DE LA CALCULADORA")
        
        try:
            opcion = int(input("Ingrese la operacion a realizar: "))
            if opcion < 1 or opcion > 5:
                print("Error: Digite número dentro del rango de la selección.")
            else:
                return opcion
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")

        pausar_segundos(2)
        limpiar_pantalla()