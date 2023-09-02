def mostrar(func):
    def interno():
        print("O usuario atual é : ", end="")
        func()
    return interno

def quem():
    print("Alice")

myobj = mostrar(quem) 
myobj()       