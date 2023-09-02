#

def logging_soma_ab(func):
    def inner(a,b):
        print(str(a) + " + " + str(b) + " = ", end= "")
        return func(a,b)    
    return inner

@logging_soma_ab
def soma_ab(a,b):
    soma = a + b
    return soma

if __name__ == "__main__":
    valor = soma_ab(5,3)
    quadrado = valor ** 2
    print(valor)
    print(quadrado)