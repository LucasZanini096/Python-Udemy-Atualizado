# Classes abstratas - Abstract Base Class (abc)
# ABC's são usadas como contratos para a definição
# de novas classes. Elas podem forçar outras classes 
# a criarem métodos concretos. Também podem ter 
# métodos concretos por elas mesmas.

# @abstractmethods são métodos que não têm corpo
# As regras para classes abstratas com métodos 
# abstratos é que elas NÃO PODEM ser instânciadas diretamente

#Métodos abstratos DEVEM ser implementados 
# nas subclasses (@abstractmethod).
# Uma classe abstrata em Python tem sua metaclasse 
# sendo ABCMeta.

#É possível criar @property @setter @classmethod 
# @staticmethod e @method como abstratos, para isso 
# use @abstractmethod como decorator mais interno  


from abc import ABC,abstractmethod
#Classes abstratas não podem ser instânciadas diretamente

class Log(ABC): #Não deve ser instânciada, pois é abstrata
    @abstractmethod #Deve ser implementada !!!!
    def _log(self,msg): ...
    
    def log_error(self,msg):
        return self._log(f'Error: {msg}')

    def log_success(Log):
        def _log(self, msg):
            return self._log(f'Sucess: {msg}')

class LogPrintMixin(Log):
    def _log(self, msg): #Método abstrato -> definimos a classe/método abstrata apenas na sub-classe 
        print(msg)
        print(f'{msg} ({self.__class__.__name__})')

