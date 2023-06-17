# reduce - faz a redução de um iterável em um valor 
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preço': 10.00},
    {'nome': 'Produto 1', 'preço': 22.32},
    {'nome': 'Produto 3', 'preço': 10.11},
    {'nome': 'Produto 2', 'preço': 105.87},
    {'nome': 'Produto 4', 'preço': 69.90},
]

def funcao_do_reduce(acumulador,produto):
    print('acumulador', acumulador)
    print('produto', produto)
    print()
    return acumulador + produto['preço']

total = reduce(
    funcao_do_reduce,
    produtos, 
    0 #valor inicial do acumulador -> delimita o início de trabalho
    # Se não colocar zero, ele vai tentar somar dicionários neste csao 
)

#total = 0
#for p in produtos:
#    total += p['preço']

#print(total)

#print(sum([p['preço'] for p in produtos]))