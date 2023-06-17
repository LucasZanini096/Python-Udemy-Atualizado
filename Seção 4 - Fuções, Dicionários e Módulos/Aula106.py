#Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa 
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations,product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]

camisetas = [
    ['preta', 'branca'],
    ['p','m','g'],
    ['masculino','feminino'],
    ['algodão','poliéster']
]

print_iter(combinations(pessoas,2)) #São iterators!
print_iter(permutations(pessoas,2)) 
print(product(camisetas)) #Vai retornar todas as possibilidades entre as listas, a partir do
#desepacotamento da lista camisas 


