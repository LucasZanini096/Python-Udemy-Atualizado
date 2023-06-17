"""
enumerate - enumera iteráveis (índices) -> Itens de uma lista 
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

#lista_enumerada = enumerate(lista)

for indice, nome in enumerate(lista):
    print(indice, nome)

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)

for tupla_enumerada in enumerate(lista):
    print('FOR da Tupla:')
    for valor in tupla_enumerada:
        print(f'\t{valor}')


#Comentários:
#01 - Enumerate -> interador !!
#02 - Ele sempre rertorna uma tupla !!
#03 - Start - Começa num índice proposto 

