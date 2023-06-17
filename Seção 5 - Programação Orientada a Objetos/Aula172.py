# Implementando o protocolo do Iterator em Python 
# Essa é apenas uma aula para introduzir os protocolos de collections.abc no Python 
# Qualuqer outro protocolo poderá ser implementado seguindo a mesma estrutura usada nesta aula
# Iterator = objeto diferente 

from _collections_abc import Sequence


class Mylist(Sequence):
    def __init__(self):
        self._data = {}
        self._index = 0
        self._next_index = 0


    def append(self,*values):
        for value in values:
            self._data[self._index] = value
            self._index += 1

    def __len__(self) -> int:
        return self._index
    
    def __getitem__(self,index):
        return self._data[index]
    
    def __setitem__(self,index,value):
        self._data[index] = value
    
    def __iter__(self):
        return self
    
    def __next__(self): #Por padrão, o next vai até o último item da lista e não
        #volta para o índice 0

        if self._next_index >= self._index:

            self._next_index = 0 #Me permite fazer outro for 

            raise StopIteration
       
        value = self._data[self._next_index]
        self._next_index += 1
        return value


if __name__ == '__main__':
    lista = Mylist()
    lista.append("Maria", "Helena")
    lista.append("Luiz")
    print(lista._data)