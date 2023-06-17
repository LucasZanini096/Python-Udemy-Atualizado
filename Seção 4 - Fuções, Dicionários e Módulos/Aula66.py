#Dicionários em Python (tipo dict)
#Dicionários são estrturas de dados do tipo 
# par de "chave" e "valor"
#Chaves podem ser coniderados como "índice"
# que vimos na lista e podem ser de tipo imutáveis 
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário 
# Usamos chaves - {} - ou a classe dict para criar 
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#        'nome': Luiz Otávio',
#        'sobrenome': 'Miranda',
#        'idade': 18,
#        'altura': 1.8,
#        'endereços': [
#        {'rua': 'tal tal', 'número':123}
#        {'rua': 'outra rua', 'número': 321}

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número':123},
        {'rua': 'outra rua', 'número': 321},
    ],

}


# OU pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')

print(pessoa['nome'])
print(pessoa['sobrenome'])

print()

for chave in pessoa:
    print(chave,pessoa[chave])
    
      
