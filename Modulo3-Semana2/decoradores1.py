def ola(func):
    def inner():
        print("Olá ")
        func()
        print("Tudo bem ? ")
    return inner

def nome():
    print("Alice")


# variavel_func = ola(nome)
# variavel_func()

def maiusculo(texto):
    return texto.upper()

print(maiusculo('adimir'))
variavel_aluno = maiusculo('jeferson')
print(variavel_aluno)