# Para a atividade desta semana, você deverá criar um interator que irá iterar os dados da API (Application Interface) da tabela FIPE e retornar os carros de uma determinada marca de veículos (essa deverá ser passada para a classe que fará o papel de interator no momento da instanciação, neste caso use o ID de uma marca).
import requests

class TabelaFIPE():
    def __init__(self, marca):
        self.marca = marca
        self.url = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{self.marca}/modelos"
        self.modelos = requests.get(self.url).json()['modelos']
        self.cont = 0
 
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.cont >= len(self.modelos):
            print(f"Existem {self.cont} modelos da marca {self.marca}")
            print('Fim da Lista')
            raise StopIteration
        resultado = self.modelos[self.cont]
        self.cont += 1
        return f"Código: {resultado['codigo']} -> Nome: {resultado['nome']}"
    
for modelo in TabelaFIPE(7): #BMW
    print(modelo)
    
    


