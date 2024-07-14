def colocar_palabra(sopa, palabra, x, y, dx, dy):

    max_x = x + (len(palabra) - 1) * dx
    max_y = y + (len(palabra) - 1) * dy

    if max_x >= len(sopa) or max_y >= len(sopa[0]):
        raise IndexError("La palabra no cabe en la sopa en la direccion especificada")
    
    for i, letra in enumerate(palabra):
        sopa[x + i * dx][y + i * dy] = letra.upper()