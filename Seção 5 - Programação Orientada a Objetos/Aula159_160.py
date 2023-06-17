#Metaclasses são o tipo das classes
# Em PYTHON, TUDO É UM OBJETO (CLASSES TAMBÉM)
# Então, qual é o tipo de uma classe? (type)
# Seu objeto é uma instância da sua classe 
# Sua classe é uma instância de type (type é uma metaclasse)
# type ("Name", (Bases), __dict__)
#
#Ao criar uma classe, coisas ocorrem por padrão nessa ordem:
# __new__ da metaclass é chamado e cria a nova classe
# __call__ da metaclass é chamado com os argumentos e chama:
# __new__ da class com os argumentos (cria a instância)
# __init__ da class com os argumentos 
# __call__ da metaclass termina a execução 
#
# Métodos importantes da metaclass
# __new__(mcs,name,bases(heranças),dct) (Cria a classe)
# __call__(cls, *args, **kwargs) (Cria e inicializa a instância)

# "Metaclasses são mágias mais profundas do que 99% dos usuários"
# deveriam se preocupar. SE você quer saber se precisa delas, 
# não precisa (As pessoas que relamente precisam delas sabem)
# com ctz que precisam delas e não precisam de uma explicação
# sobre o porquê)."
# - Tim Peters (CPython Core Developer)


from typing import Any


def meu_repr(self):
    return f'{type(self).__name__} ({self.__dict__})'


class Meta(type): #Cria a classe
    #Não consigo usar self de uma metaclasse, pois estou instanciando uma classe
    def __new__(mcs, name, bases, dct):
        print ("MetaClass New")
        cls = super().__new__(mcs, name, bases, dct)
        cls.attr = 1234 #Esse atributo vai ser herdado !!
        cls.__repr__ =  meu_repr

        if "falar" not in cls.__dict__ or not callable(cls.__dict__['falar']):
            raise NotADirectoryError("Você não implementou o método falar")


        return cls
    
    def __call__(self, *args ,**kwds): #Permite a criação e o retorno da Instância
        return super().__call__(*args, **kwds) #Estou permitindo isso Pessoa("Luiz")

#Estou executando a criação da classe por meio da MetaClasse
#Então posso criar coisas antes da criação da classe

#Toda metaclasse precisa herdar de type
class Pessoa(object, metaclass=Meta): #Por padrão !!
    #A classe Pessoa é uma instância de Meta, mas herda de Object
    def __new__(cls, *args, **kwargs):
        print("Meu New")
        instancia = super().__new__(cls) #Criando a instância
        return instancia
    
    def __init__(self, nome): #Inicializando a instância
        print("Meu Init")
        self.nome = nome

    def falar(self):
        print("Falando...")

p1 = Pessoa('Luiz')
