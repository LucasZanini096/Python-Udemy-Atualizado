# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação 
# Mas nela, quando o objeto "pai" for apagado, tdas as referências 
# dos objetos filhos serão também apagados 
#Garbagecollector -> quando a linguagem vê que não existe mais referência para determinado objeto 
# no seu programa, ela apaga esse objeto da memória 


class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []
    
    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua,numero))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

#Quando a Classe Cliente deixar de existir, a Classe Endereço tamb´me vai deixar de existir 

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero 
    
    def __del__(self):
        print("Apagando", self.rua, self.numero)

cliente = Cliente("Maria")
cliente.inserir_endereco("Av Brasil", 54)
cliente.inserir_endereco("Rua B", 6789)
cliente.listar_enderecos()

