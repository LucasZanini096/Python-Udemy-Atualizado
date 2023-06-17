"""
Listas em Python 
Tipo list - Mutável 
Suporta vários valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento 
Métodos uteis:
      append, insert, pop, del, clear, extend, +
Create Read Update       Delete 
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#         0   1   2   3
lista = [10, 20, 30, 40]
lista [2] = 300
del lista [2]
print(lista)
print(lista[2])

lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop() #Atribuição de valor
print(lista, 'Removido', ultimo_valor)


#Comentários:
#01 - Retirar e adicionar elementos apenas no final da lista (mais interessante)
#02 - A função del retira determinado elemento de uma lista, sendo que o índice do objeto posterior será do objeto retirado
#03 - A função pop retira o ultimo elemento de uma lista -> pode atribuir um índice a ele 


