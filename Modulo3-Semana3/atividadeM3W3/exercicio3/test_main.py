import pytest 
from main import calcular_preco_volume, calcular_multiplicador_peso, calcular_frete, calcular_multiplicador_rota

def test_calculando_volume_menor_que_1000():
    assert calcular_preco_volume(800) == 10.0

def test_calculando_volume_entre_1000_e_10000():
    assert calcular_preco_volume(1200) == 20.0

def test_calculando_volume_entre_10000_e_30000():
    assert calcular_preco_volume(15000) == 30.0

def test_calculando_volume_entre_30000_e_100000():
    assert calcular_preco_volume(40000) == 20.0

def test_calculando_volume_maior_que_100000():
    assert calcular_preco_volume(110000) == 0.0

def test_pesando_objeto_menor_que_01():
    assert calcular_multiplicador_peso(0.09) == 1.0

def test_pesando_objeto_entre_01_e_1():
    assert calcular_multiplicador_peso(0.87) == 1.5

def test_pesando_objeto_entre_1_e_10():
    assert calcular_multiplicador_peso(9) == 2.0

def test_pesando_objeto_entre_10_e_30():
    assert calcular_multiplicador_peso(25) == 3.0

def test_pesando_objeto_maior_que_30():
    assert calcular_multiplicador_peso(40) == 0

def test_calculando_rota_1():
    assert calcular_multiplicador_rota('rs') == 1.0

def test_calculando_rota_2():
    assert calcular_multiplicador_rota('SB') == 1.2

def test_calculando_rota_3():
    assert calcular_multiplicador_rota('br') == 1.5

def test_calculando_frete():
    assert calcular_frete(1.000, 1.5, 1.0) == 1.500
