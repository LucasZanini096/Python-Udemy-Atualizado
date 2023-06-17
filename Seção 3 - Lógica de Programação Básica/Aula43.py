"""
Listas em Python 
Tipo list - Mutável 
Suporta vários valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento 
Metodos úteis: append, insert, pop, del, celar, extend, +
"""

#       +01234
#       -54321
string = 'ABCDE'
#lista = list() -> Método menos comum
# print(bool([])) -> Retorna Falso (necessita colocar objetos dentro dela)
#print (lista, type(lista)) 
#        0     1         2          3    4
#       -5     -4       -3         -2   -1
lista = [123, True, 'Luis Otávio', 1.2, []]

lista[2] = 'Maria'
print (lista)
print(lista[2].upper(), type(lista[2]))


