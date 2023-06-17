# filter é um filtro funcional
def print_iter(iterator):
    print(*list(iterator),sep='\n')
    print()

produtos = [
    {'nome': 'Produto 5', 'preço': 10.00},
    {'nome': 'Produto 1', 'preço': 22.32},
    {'nome': 'Produto 3', 'preço': 10.11},
    {'nome': 'Produto 2', 'preço': 105.87},
    {'nome': 'Produto 4', 'preço': 69.90},
]

#novos_produtos = [
#    p for p in produtos
#    if p['preço'] > 10
#]


def filter_preco(produto):
    return produto['preço'] > 100


novos_produtos = filter(
    #lambda p: p['preço'] > 10,
    filter_preco,
    produtos
)


print_iter(produtos)
print_iter(novos_produtos)