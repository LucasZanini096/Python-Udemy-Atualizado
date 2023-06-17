"""
for in com listas
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

for nome in lista:
        print(nome)
    
#Exercício 

indices = range(len(lista))

for indice in indices:
        print(indice, lista[indice], type(lista[indice]))

