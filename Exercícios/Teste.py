"""
import random

cpf_aleatorio = ''
for i in range (11):
    cpf_aleatorio += str(random.randint(0,9))

print (cpf_aleatorio)



tupla = ''
print(len(tupla))



def soma(numero1,numero2):
    soma_total = numero1 + numero2
    return soma_total

def execute(funcao,*args):
    return funcao(*args)

x = execute(soma, 2,6)
print(x)

produtos = [
    {'nome': 'p1', 'preço': 20, },
    {'nome': 'p2', 'preço': 10, },
    {'nome': 'p3', 'preço': 30, },

]

novos_produtos =[

    {**produto, 'preço' : produto['preço'] * 1.30}
    if produto['preço'] > 15 else {**produto} 
    for produto in produtos 
]

print(*novos_produtos, sep='\n') #Tem que desempacotar
print()

"""


"""
#List Compreehention
lista =  [
    {'nome': 'Luiz', 'sobrenome':'Miranda'},
    {'nome': 'Maria', 'sobrenome':'Oliveira'},
    {'nome': 'Daniel', 'sobrenome':'Silva'},
    {'nome': 'Eduardo', 'sobrenome':'Moreira'},
    {'nome': 'Aline', 'sobrenome':'Souza'},
]


# .sort(é um método)
# sort é uma função !!

lista_ordenada = sorted(lista, key = lambda lista: lista["nome"])

for pessoa in lista_ordenada:
    print(pessoa)

print()
lista_ordenada_2 = sorted(lista, key = lambda lista: lista["sobrenome"])

for pessoa_2 in lista_ordenada_2:
    print(pessoa_2)
"""

str_ = "Lucas"

lista_valores = [
 [(x,y) for x in range (10)]
 for y in str_ #Eu posso formar matrizes com esse as lists compreehentions 
]

for lista in lista_valores:
    print(*lista)


"""
#Dictionary Compreehension 

produto = {
    'nome' : 'caneta azul',
    'preco': 2.5,
    'categoria': "escritório",
}


dc = {
    chave: valor 
    if isinstance(valor,(int, float)) else valor.upper()
    for chave, valor in produto.items()
    if chave != "nome"    
}
print(dc, end='\n')
"""


