from main import gerar_codigo, cadastrar_peca, imprimir_peca



def test_imprimir_peca(capsys):
    global pecas
    pecas = [{'codigo': 1, 'nome': 'Peça 1', 'fabricante': 'Fabricante 1', 'valor': 50.0}]
    imprimir_peca(pecas[0])
    out, _ = capsys.readouterr()
    assert 'Código: 001\n' in out
    assert 'Fabricante: Fabricante 1\n' in out
    assert 'Valor: 50.00 R$\n' in out