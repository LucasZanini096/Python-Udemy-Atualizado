# Funções decoradoras e decoradores(açucar sintático) com classes 

#Por Herança 

class MyReprMixin:

     def __repr__(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name} ({class_dict})'
        return class_repr

class SuperTime:
    pass

class Time(SuperTime, MyReprMixin):
    def __init__(self, nome):
        self.nome = nome

class Planeta(MyReprMixin):
    def __init__(self, nome):
        self.nome = nome


#Por composição (Utilização de funções decoradoras)

def adiciona_repr(cls):
    def meu_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name} ({class_dict})'
        return class_repr
    cls.__repr__ = meu_repr #To falando por Python que minha função meu_repr é a 
    # def __repr__(self):
    return cls 

@adiciona_repr #Açúcar Sintático 
class Time:
    def __init__(self,nome):
        self.nome = nome

@adiciona_repr #Função Decoradora 
class Planeta:
    def __init__(self, nome):
        self.nome = nome 

    def falar_nome(self):
        return f'O planeta é {self.nome}'

