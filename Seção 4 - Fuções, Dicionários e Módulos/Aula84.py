# Dictionary Compreenhension e Set Comprehension
produto = {
    'nome' : 'caneta azul',
    'preco': 2.5,
    'categoria': "Escritório",
}


for chave, valor in produto.items():
    print (chave, valor)


dc = {
   chave: valor  #declara o modelo da chave !!! 
   if isinstance(valor, (int,float)) else valor.upper() #Pode utilizar uma tupla para colocar mais de uma condição 
   for chave, valor
   in produto.items()
   if chave != 'categoria'
}

#Transformando lista em dicionário (A lista tem que possuir uma estrtura semelhante a de um dicionário)
lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]

dc = {
    chave: valor
    for chave, valor in lista 
}
# OU
print(dict(lista))

#SET Comprehension 

s1 = {i ** 2 for i in range(10)}
print(s1)
