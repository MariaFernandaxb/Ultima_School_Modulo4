import pytest
from main import desconto_produtos

def test_10_a_99():          
    assert desconto_produtos(10, 100) == (950, 1000)

def test_100_a_999():
    assert desconto_produtos(100, 100) == (9000, 10000)

def test_maior_que_1000():
    assert desconto_produtos(1000, 100 ) == (85000, 100000 )

