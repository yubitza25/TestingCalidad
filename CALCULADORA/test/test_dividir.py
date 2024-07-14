import pytest
from source.dividir import dividir

# Caso de prueba 1: Números positivos
def test_division_numeros_positivos():
    resultado = dividir(10, 2)
    assert resultado == 5

# Caso de prueba 2: Números negativos
def test_division_numeros_negativos():
    resultado = dividir(-10, -2)
    assert resultado == 5

# Caso de prueba 3: Números mixtos
def test_division_numeros_mixtos():
    resultado = dividir(10, -2.5)
    assert resultado == -4.0

# Caso de prueba 4: División por cero
def test_division_por_cero():
    with pytest.raises(ZeroDivisionError):
        dividir(5, 0)

# Casos de prueba parametrizados
@pytest.mark.parametrize("num1, num2, resultado", [
    (10, 2, 5),         # Caso de prueba 1: Números positivos
    (-10, -2, 5),       # Caso de prueba 2: Números negativos
    (10, -2.5, -4.0),   # Caso de prueba 3: Números mixtos
])
def test_division_parametrizado(num1, num2, resultado):
    assert dividir(num1, num2) == resultado
