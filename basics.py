'''Classes allow us to 
logically group our data and functions 
in a way that is easy to reuse and also easy to build upon if need be.

método = função associada a classe

'''

'''
exemplo 1: classe cachorro
- Atributos: nome, idade
- Método: andar, comer, latir
'''

class Cachorro:
    #atributos
    def __init__(self):
        self.nome = None
        self.idade = None

    #metodos
    def andar(self, distancia):
        print("O cachorro andou " + str(distancia) + " metros")
    
    def comer(self):
        print("O cachorro comeu")
    
    def latir(self):
        print("Au Au..,")


dog = Cachorro()
dog.nome = "Claudin Sheik"
dog.idade = 5
print("O cachorro de nome " + dog.nome + "possui a idade de " + str(dog.idade) + "anos")
dog.andar(2)
dog.latir()
dog.comer()

meu_cachorro = Cachorro()
meu_cachorro.nome = "Somalia"
meu_cachorro.idade = 3
print("O cachorro de nome " + dog.nome + "possui a idade de " + str(dog.idade) + "anos")
meu_cachorro.andar(5)
meu_cachorro.latir()
meu_cachorro.comer()
