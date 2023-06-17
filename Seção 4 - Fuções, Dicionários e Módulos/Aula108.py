from functools import partial #É uma função que recebe uma outra função 


# map - para mapear dados 
def print_iter(iterator):
    print(*list(iterator),sep= '\n')
    print()
produtos = [
    {'nome': 'Produto 5', 'preço': 10.00},
    {'nome': 'Produto 1', 'preço': 22.32},
    {'nome': 'Produto 3', 'preço': 10.11},
    {'nome': 'Produto 2', 'preço': 105.87},
    {'nome': 'Produto 4', 'preço': 69.90},
]



def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem,2)


aumentar_dez_porcento = partial( #Já possui um closure em sua raiz 
    aumentar_porcentagem,
    porcentagem=1.1
)




def muda_preco_de_produtos(produto):
    return {
        **produto, 
        'preco': aumentar_dez_porcento(
        produto['preço']
        )
    }

novos_produtos = list(map( #map deixa de ser um iterator 
muda_preco_de_produtos,
    produtos
))




#novos_produtos = [
#    {**p, 
#     'preço': aumentar_porcentagem((p['preço']),1.1)} 
#     for p in produtos
#]

print_iter(produtos)
print_iter(novos_produtos)
print(hasattr(novos_produtos, '__iter__'))
print(hasattr(novos_produtos, '__iter__'))


print(
    list(map(
        lambda x : x *3
        [1,2,3,4]
    ))
)