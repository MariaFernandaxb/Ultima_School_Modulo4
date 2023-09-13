import pytest 
from main import cacular_total_pedido

def test_calcular_total_um_produto():
    assert cacular_total_pedido([100]) == 9.0

def test_calcular_total_varios_produtos():
    assert cacular_total_pedido([100, 101, 105, 201]) == 41.0

def test_calcular_total_pedido_produto_invalido():
    assert cacular_total_pedido([200, 300, 104]) == 19.0

def test_calcular_total_pedido_sem_produto():
    assert cacular_total_pedido([]) == 0.0

def test_calcular_total_pedido_produtos_repetidos():
    assert cacular_total_pedido([100, 100, 105, 200, 201, 201]) == 48.0

def test_calcular_total_pedido_todos_produtos():
    assert cacular_total_pedido([100, 101, 102, 104, 105, 200, 201]) == 72.0

def test_calcular_total_pedido_inexistente():
    assert cacular_total_pedido([300]) == 0.0
