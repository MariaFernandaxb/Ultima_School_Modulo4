#Exemplo: Mensurar tempo de execução do sistema

import time
from datetime import datetime

def time_exec(func):
    def interno(*args, **kwargs):
        inicio = time.time()
        result = func(*args,**kwargs)
        fim = time.time()
        print(func.__name__ + ' executado em ' + str((fim-inicio)*1000) + ' milisegundos ')
    return interno

@time_exec
def calc_quadrado(numeros):
    resultado = []
    for numero in numeros:
        resultado.append(numero*numero)
    return resultado 

@time_exec
def cal_cubo(numeros):
    resultado = []
    for numero in numeros:
        resultado.append(numero*numero*numero)
    return resultado

if __name__ == '__main__':
    lista_numeros = range(1,10000000)
    print(datetime.now())
    saida_quadrados = calc_quadrado(lista_numeros)
    saida_cubo = cal_cubo(lista_numeros)
    print(datetime.now())