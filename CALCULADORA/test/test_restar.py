import pytest
from source.restar import restar

# Caso de prueba 1: Números positivos
def test_resta_numeros_positivos():
    resultado = restar(5, 3)
    assert resultado == 2

# Caso de prueba 2: Números negativos
def test_resta_numeros_negativos():
    resultado = restar(-3, -5)
    assert resultado == 2

# Caso de prueba 3: Números mixtos
def test_resta_numeros_mixtos():
    resultado = restar(-2.5, 3.5)
    assert resultado == -6.0

# Caso de prueba 4: Suma de cero
def test_resta_numeros_ceros():
    resultado = restar(0, 0)
    assert resultado == 0

# Caso de prueba 5: Suma de entero y flotante
def test_resta_numeros_enteros_flotantes():
    resultado = restar(4, -2.5)
    assert resultado == 6.5

# Caso de prueba 6: Suma de números grandes
def test_resta_numeros_grandes():
    resultado = restar(-1000000, -2000000)
    assert resultado == 1000000

# Casos de prueba: parametrize

@pytest.mark.parametrize("num1, num2, resultado", [
    (-3, 2, -5), # Caso de prueba 1: Números negativos
    (-10, 5, -15), # Caso de prueba 2: Números negativos
    (2.5, -3.5, 6.0), # Caso de prueba 3: Números mixtos
    (0, 0, 0), # Caso de prueba 4: Restar de cero
    (-4, 2.5, -6.5), # Caso de prueba 5: Restar de entero y flotante
    (-100000, 200000, -300000) # Caso de prueba 6: Restar de números grandes
])

def test_resta_parametrizado(num1, num2, resultado):
    assert restar(num1, num2) == resultado