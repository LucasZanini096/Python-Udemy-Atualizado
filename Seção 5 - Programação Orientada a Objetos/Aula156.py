def adiciona_repr(cls):
    def meu_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name} ({class_dict})'
        return class_repr
    cls.__repr__ = meu_repr 
    return cls 

@adiciona_repr  
class Time:
    def __init__(self,nome):
        self.nome = nome

def meu_planeta(metodo): #Método decorador 
    def interno(self,*args,**kwargs):
        resultado = metodo(self,*args,**kwargs)
    
        if "Terra" in resultado:
         return 'Você está em casa'
        return resultado
    return interno
 



@adiciona_repr  
class Planeta:
    def __init__(self, nome):
        self.nome = nome 

    def falar_nome(self):
        return f'O planeta é {self.nome}'
