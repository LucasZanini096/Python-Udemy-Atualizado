# Generator expressions, Iterables e Iterators em Python 

import sys

iterable = ['Eu','Tenho', '_iter_']
iterator = iter(iterable)

lista = [n for n in range(100000)] #Problema: vai ser salva por interia na memória 
#print(generator)

#Solução 
generator = (n for n in range(100000)) #Parênteses já indica uma generator expression


print(sys.getsizeof(lista)) #Getsizeof -> quantidade de objetos de uma variável 
print(sys.getsizeof(generator))


for n in generator:
    print(n)




#Comentários
# 01 - Generator (Iter + Next) -> São funções que sabem pausar em determinada ocasião, em que entrega apenas 1 número por vez, salvando - o na memória 
# 02 - Iterator  -> Classe que possui que possui os métodos iter e next, na qual trabalha com iteravél (como uma lista ou str)
# 03 -> Iterator não é Generator
