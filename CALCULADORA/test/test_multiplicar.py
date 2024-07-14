import pytest
from source.multiplicar import multiplicar

# Caso de prueba 1: Números positivos
def test_multiplicacion_numeros_positivos():
    resultado = multiplicar(5, 3)
    assert resultado == 15

# Caso de prueba 2: Números negativos
def test_multiplicacion_numeros_negativos():
    resultado = multiplicar(-3, -5)
    assert resultado == 15

# Caso de prueba 3: Números mixtos
def test_multiplicacion_numeros_mixtos():
    resultado = multiplicar(-2.5, 3.5)
    assert resultado == -8.75

# Caso de prueba 4: Multiplicación por cero
def test_multiplicacion_numeros_cero():
    resultado = multiplicar(0, 5)
    assert resultado == 0

# Caso de prueba 5: Multiplicación de entero y flotante
def test_multiplicacion_numeros_enteros_flotantes():
    resultado = multiplicar(4, -2.5)
    assert resultado == -10.0

# Caso de prueba 6: Multiplicación de números grandes
def test_multiplicacion_numeros_grandes():
    resultado = multiplicar(-1000000, -2)
    assert resultado == 2000000

# Casos de prueba parametrizados
@pytest.mark.parametrize("num1, num2, resultado", [
    (3, 2, 6),      # Caso de prueba 1: Números positivos
    (-10, 5, -50),  # Caso de prueba 2: Números negativos
    (2.5, -3.5, -8.75),  # Caso de prueba 3: Números mixtos
    (0, 5, 0),      # Caso de prueba 4: Multiplicación por cero
    (-4, 2.5, -10.0),   # Caso de prueba 5: Multiplicación de entero y flotante
    (-100000, 2, -200000)   # Caso de prueba 6: Multiplicación de números grandes
])
def test_multiplicacion_parametrizado(num1, num2, resultado):
    assert multiplicar(num1, num2) == resultado
