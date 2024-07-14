import pytest
from source.sumar import sumar

# Caso de prueba 1: Números positivos
def test_sumar_numeros_positivos():
    resultado = sumar(3, 5)
    assert resultado == 8

# Caso de prueba 2: Números negativos
def test_sumar_numeros_negativos():
    resultado = sumar(-3, -5)
    assert resultado == -8

# Caso de prueba 3: Números mixtos
def test_sumar_numeros_mixtos():
    resultado = sumar(2.5, 3.5)
    assert resultado == 6.0

# Caso de prueba 4: Suma de cero
def test_sumar_numeros_ceros():
    resultado = sumar(0, 0)
    assert resultado == 0

# Caso de prueba 5: Suma de entero y flotante
def test_sumar_numeros_enteros_flotantes():
    resultado = sumar(4, 2.5)
    assert resultado == 6.5

# Caso de prueba 6: Suma de números grandes
def test_sumar_numeros_grandes():
    resultado = sumar(1000000, 2000000)
    assert resultado == 3000000

# Casos de prueba: parametrize

@pytest.mark.parametrize("num1, num2, resultado", [
    (3, 2, 5), # Caso de prueba 1: Números positivos 
    (-10, -5, -15), # Caso de prueba 2: Números negativos
    (2.5, -3.5, -1.0), # Caso de prueba 3: Números mixtos
    (0, 0, 0), # Caso de prueba 4: Suma de cero
    (4, 2.5, 6.5), # Caso de prueba 5: Suma de entero y flotante
    (100000, 200000, 300000) # Caso de prueba 6: Suma de números grandes
])

def test_sumar_parametrizado(num1, num2, resultado):
    assert sumar(num1, num2) == resultado