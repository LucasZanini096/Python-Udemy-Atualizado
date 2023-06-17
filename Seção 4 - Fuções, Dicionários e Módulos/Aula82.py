#Mapeamento de dados em list comprehension 

import pprint

def p(v):
    pprint.pprint(novos_produtos, sort_dicts=False, width=40)

produtos = [
    {'nome': 'p1', 'preço': 20, },
    {'nome': 'p2', 'preço': 10, },
    {'nome': 'p3', 'preço': 30, },

]
novos_produtos = [
    produto['nome']
    for produto in produtos
]

print(novos_produtos)
print(*novos_produtos, sep='\n') #'\n' quebra de linha 

novos_produtos = [
    {**produto, 'preço': produto['preço'] *1.05}
    if produto ['preço'] > 20 else {**produto}
    for produto in produtos
]


#Comentários:
#01 -> Sort_dict -> Ordenamento de chave 
#02 ->  Width  -> Largura 
#o3 -> O Filtro sempre vem depois do for, quando a condição for verdadeira 

print(novos_produtos)
p(novos_produtos)

# Filtro de List Comprehension
lista = [n for n in range(10) if n < 5]
print(lista)

novos_produtos = [
    {**produto, 'preço': produto['preço'] *1.05}
    if produto ['preço'] > 20 else {**produto}
    for produto in produtos
    if (produto['preço'] >= 20 and produto['preço'] * 1.05) > 10

]

