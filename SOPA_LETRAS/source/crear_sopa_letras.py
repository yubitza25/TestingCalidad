import random
import string
from es_posible_colocar import es_posible_colocar
from colocar_palabra import colocar_palabra

def crear_sopa_letras(palabras, n=10):
    sopa = [[' ' for _ in range(n)] for _ in range(n)]

    direcciones = [
        (0, 1),   # horizontal derecha
        (0, -1),  # horizontal izquierda
        (1, 0),   # vertical abajo
        (-1, 0),  # vertical arriba
        (1, 1),   # diagonal derecha abajo
        (-1, -1), # diagonal izquierda arriba
        (1, -1),  # diagonal izquierda abajo
        (-1, 1)   # diagonal derecha arriba
    ]

    for palabra in palabras:
        colocada = False
        intentos = 0
        while not colocada and intentos < 100:
            x = random.randint(0, n - 1)
            y = random.randint(0, n - 1)
            dx, dy = random.choice(direcciones)

            if es_posible_colocar(sopa, palabra, x, y, dx, dy, n):
                colocar_palabra(sopa, palabra, x, y, dx, dy)
                colocada = True
            intentos += 1

        if not colocada:
            raise ValueError(f"No se pudo colocar la palabra '{palabra}' después de 100 intentos.")

    # Rellenar espacios vacíos con letras aleatorias
    for i in range(n):
        for j in range(n):
            if sopa[i][j] == ' ':
                sopa[i][j] = random.choice(string.ascii_uppercase)

    return sopa
