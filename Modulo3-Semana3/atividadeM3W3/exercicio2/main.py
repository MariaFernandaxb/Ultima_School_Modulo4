def cacular_total_pedido(codigos_pedidos):
    cardapio = {
        100: ("Cachorro Quente", 9.00),
        101: ("Cachorro Quente Duplo", 11.00),
        102: ("X-Egg", 12.00),
        103: ("X-Salada",12.00),
        104: ("X-Bacon", 14.00),
        105: ("X-Tudo", 17.00),
        200: ("Refrigerante Lata", 5.00),
        201: ("Chá Gelado", 4.00),
    }

    total = 0.0

    for codigo in codigos_pedidos:
        if codigo in cardapio:
            produto, valor = cardapio[codigo]
            print(f'Você pediu um {produto} no valor de {valor:.2f}')
            total += valor
        else:
            print('Opção inválida')

    return total


if __name__ == '__main__':
    cardapio = """
    *******************Cardápio*******************
    ----------------------------------------------
    | Código |        Descrição        |  Valor  |
    |   100  |     Cachorro Quente     |   9,00  |
    |   101  |  Cachorro Quente Duplo  |  11,00  |
    |   102  |           X-Egg         |  12,00  |
    |   103  |         X-Salada        |  12,00  |
    |   104  |          X-Bacon        |  14,00  |
    |   105  |           X-Tudo        |  17,00  |
    |   200  |    Refrigerente Lata    |   5,00  |
    |   201  |         Chá Gelado      |   4,00  |
    ----------------------------------------------
    """
    print(cardapio)

    codigos = []

    codigo = int(input('Entre com o código desejado: '))

    while True:
        if codigo in [100, 101, 102, 103, 104, 105,200, 201]:
            codigos.append(codigo)
        
        else:
            print('Opção Inválida')

        print('Deseja pedir mais alguma coisa?')
        print('1 - Sim')
        print('2 - Não')
        pedir_mais = int(input())

        if pedir_mais == 2:
            break

        codigo = int(input('Entre com o código desejado: '))

    total = cacular_total_pedido(codigos)
    print(f'O total a ser pago é: {total:.2f} R$')