def es_posible_colocar(sopa, palabra, x, y, dx, dy, n):
    for i in range(len(palabra)):
        nx, ny = x + i * dx, y + i * dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            return False
        if sopa[nx][ny] != ' ' and sopa[nx][ny] != palabra[i]:
            return False
    return True
