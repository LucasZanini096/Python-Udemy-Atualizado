import copy

produtos = [
    {'nome': 'Produto 5', 'preço': 10.00},
    {'nome': 'Produto 1', 'preço': 22.32},
    {'nome': 'Produto 3', 'preço': 10.11},
    {'nome': 'Produto 2', 'preço': 105.87},
    {'nome': 'Produto 4', 'preço': 69.90},
]


novos_produtos =[
    {**p, 'preço' : round(p['preço'] * 1.1,2)}      #Criação de um novo dicionário com base nos dicionários da lista produtos
    for p in copy.deepcopy(produtos)
]

produtos_em_ordem_decrescente = sorted(
    copy.deepcopy(produtos),
    key= lambda p : p['nome'], #Função lambda que realiza a leitura da lista produtos
    reverse = True #Reverse -> irá converter a ordem dos elementos da lista 

)

produtos_ordenados_por_preço = sorted(
    copy.deepcopy(produtos),
    key= lambda p : p['preço'], 
    reverse = True 

)

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep ='\n')
print(*produtos_em_ordem_decrescente, sep ='\n')
print()
print(*produtos_ordenados_por_preço)
