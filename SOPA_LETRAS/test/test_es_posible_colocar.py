import pytest
from source.es_posible_colocar import es_posible_colocar

@pytest.fixture
def sopa_vacia():
    return [
        [' ' for _ in range(5)]
        for _ in range(5)
    ]

@pytest.fixture
def sopa_con_palabras():
    return [
        ['H', ' ', ' ', ' ', ' '],
        ['O', ' ', ' ', ' ', ' '],
        ['L', ' ', ' ', ' ', ' '],
        ['A', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]

def test_es_posible_colocar_horizontal_vacio(sopa_vacia):
    assert es_posible_colocar(sopa_vacia, "HOLA", 0, 0, 0, 1, 5) == True

def test_es_posible_colocar_vertical_vacio(sopa_vacia):
    assert es_posible_colocar(sopa_vacia, "HOLA", 0, 0, 1, 0, 5) == True

def test_es_posible_colocar_fuera_limites(sopa_vacia):
    assert es_posible_colocar(sopa_vacia, "HOLA", 0, 3, 0, 1, 5) == False

def test_es_posible_colocar_solapado_correcto(sopa_con_palabras):
    assert es_posible_colocar(sopa_con_palabras, "HOLA", 0, 0, 1, 0, 5) == True

def test_es_posible_colocar_solapado_incorrecto(sopa_con_palabras):
    assert es_posible_colocar(sopa_con_palabras, "HALO", 0, 0, 1, 0, 5) == False

def test_es_posible_colocar_espacio_no_vacio(sopa_con_palabras):
    assert es_posible_colocar(sopa_con_palabras, "TEST", 0, 0, 0, 1, 5) == False

    
