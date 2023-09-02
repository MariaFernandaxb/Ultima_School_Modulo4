
def decorator_imprimir(func):
    def interador(capital, taxa, tempo):
        print(f'CAPITAL: {capital} | TAXA: {taxa} | TEMPO: {tempo}')
        resultado = func(capital, taxa, tempo)
        print(f'Resultado: {resultado}')
        return resultado
    return interador


@decorator_imprimir
def juros_simples(capital, taxa, tempo):
    return capital * (taxa/100) * tempo

juros_simples(100,5,6)


