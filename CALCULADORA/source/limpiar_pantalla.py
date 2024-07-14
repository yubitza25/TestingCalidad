# limpiar_pantalla.py
import os

def limpiar_pantalla():
    # Determina el comando para limpiar la pantalla según el sistema operativo
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
