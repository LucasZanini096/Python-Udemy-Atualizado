from abc import ABC, abstractmethod

class AbstractFoo(ABC): #Abstrato não é para ser usado
    def __init__(self,name):
        self.name = name
        


    @property
    @abstractmethod #Deve vir o mais interno possível !!!
    def name(self): ...
        

#Classes concretas são utilizadas !!!
class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        #print("Sou inútil")
    
    @property
    def name(self):
        return self._name  

    @name.setter
    def name(self,name):
        self._name = name 

foo = Foo('Bar')
print(foo.name)

# ***************************************************************

from abc import ABC, abstractmethod

class AbstractFoo(ABC):
    def __init__(self,name):
        self._name = None
        self.name = name
        


    @property 
    def name(self): 
        return self._name
    
    @name.setter
    @abstractmethod
    def name(self,name): ...

        

#Classes concretas são utilizadas !!!
class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        #print("Sou inútil")
    
    @property
    def name(self):
        return self._name  

    @AbstractFoo.name.setter
    def name(self,name):
        self._name = name 

foo = Foo('Bar')
print(foo.name)
