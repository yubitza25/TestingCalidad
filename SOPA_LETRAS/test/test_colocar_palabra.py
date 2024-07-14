import pytest
from source.colocar_palabra import colocar_palabra

@pytest.fixture
def sopa_vacia():
    return [
        [' ' for _ in range(5)]
        for _ in range(5)
    ]

def test_colocar_palabra_horizontal_inicio(sopa_vacia):
    sopa = sopa_vacia
    colocar_palabra(sopa, "HOLA", 0, 0, 0, 1)
    assert ''.join(sopa[0][:4]) == "HOLA"

def test_colocar_palabra_vertical_inicio(sopa_vacia):
    sopa = sopa_vacia
    colocar_palabra(sopa, "HOLA", 0, 0, 1, 0)
    assert ''.join(sopa[i][0] for i in range(4)) == "HOLA"

def test_colocar_palabra_horizontal_posicion(sopa_vacia):
    sopa = sopa_vacia
    colocar_palabra(sopa, "HOLA", 0, 1, 0, 1)
    assert ''.join(sopa[0][1:5]) == "HOLA"

def test_colocar_palabra_vertical_posicion(sopa_vacia):
    sopa = sopa_vacia
    colocar_palabra(sopa, "HOLA", 0, 1, 1, 0)
    assert ''.join(sopa[i][1] for i in range(4)) == "HOLA"

def test_colocar_palabra_horizontal_medio(sopa_vacia):
    sopa = sopa_vacia
    colocar_palabra(sopa, "HOLA", 2, 0, 0, 1)
    assert ''.join(sopa[2][:4]) == "HOLA"

def test_colocar_palabra_vertical_columna(sopa_vacia):
    sopa = sopa_vacia
    colocar_palabra(sopa, "HOLA", 1, 3, 1, 0)
    assert ''.join(sopa[i + 1][3] for i in range(4)) == "HOLA"

def test_colocar_palabra_corta_horizontal(sopa_vacia):
    sopa = sopa_vacia
    colocar_palabra(sopa, "HI", 0, 0, 0, 1)
    assert ''.join(sopa[0][:2]) == "HI"

def test_colocar_palabra_corta_vertical(sopa_vacia):
    sopa = sopa_vacia
    colocar_palabra(sopa, "HI", 0, 0, 1, 0)
    assert ''.join(sopa[i][0] for i in range(2)) == "HI" #ERROR 

def test_colocar_palabra_no_cabe_horizontal(sopa_vacia):
    sopa = sopa_vacia
    with pytest.raises(IndexError):
        colocar_palabra(sopa, "HOLA", 0, 3, 0, 1)  #ERROR 

def test_colocar_palabra_no_cabe_vertical(sopa_vacia):
    sopa = sopa_vacia
    with pytest.raises(IndexError):
        colocar_palabra(sopa, "HOLA", 3, 0, 1, 0)

@pytest.mark.parametrize("palabra, x, y, dx, dy, resultado", [
    ("HOLA", 0, 0, 0, 1, ["HOLA ", "     ", "     ", "     ", "     "]),     
    ("HOLA", 0, 0, 1, 0, ["H    ", "O    ", "L    ", "A    ", "     "]),     
    ("HOLA", 0, 1, 0, 1, [" HOLA", "     ", "     ", "     ", "     "]),     
    ("HOLA", 0, 1, 1, 0, [" H   ", " O   ", " L   ", " A   ", "     "]),     
    ("HOLA", 2, 0, 0, 1, ["     ", "     ", "HOLA ", "     ", "     "]),     
    ("HOLA", 1, 3, 1, 0, ["     ", "   H ", "   O ", "   L ", "   A "]),     
    ("HI", 0, 0, 0, 1, ["HI   ", "     ", "     ", "     ", "     "]),       
    ("HI", 0, 0, 1, 0, ["H    ", "I    ", "     ", "     ", "     "]),       
])
def test_colocar_palabra_parametrizado(sopa_vacia, palabra, x, y, dx, dy, resultado):
    sopa = sopa_vacia
    colocar_palabra(sopa, palabra, x, y, dx, dy)
    assert [''.join(fila) for fila in sopa] == resultado

@pytest.mark.parametrize("palabra, x, y, dx, dy", [
    ("HOLA", 0, 3, 0, 1),  # No cabe horizontalmente desde (0, 3)
    ("HOLA", 3, 0, 1, 0),  # No cabe verticalmente desde (3, 0)
])
def test_colocar_palabra_no_cabe(sopa_vacia, palabra, x, y, dx, dy):
    sopa = sopa_vacia
    with pytest.raises(IndexError):
        colocar_palabra(sopa, palabra, x, y, dx, dy)
