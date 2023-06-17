# Métodos úteis dos dicionários 
# len - quantas chaves 
# keys - iterável com as chaves 
# values - iterável com os valores 
# items - iterável com chaves e valores
# setdefaut - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave 
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado 
# update - Atualiza um dicionário com outro
 
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',

}


pessoa.setdefault('idade', 50) #Não existe essa chave em meu dicionário. Mas caso já exista, o Python irá ignorar esse comando
print(pessoa['idade'])
#print(pessoa.__len__())
print(len(pessoa))
#Repetição de chaves contabiliza apenas a última !!

print(list(pessoa.keys())) #retorna as chaves !!
print(list(pessoa.values()))
print(list(pessoa.items()))

for chave, valor in pessoa.items(): #retorna algo semelhante a função enumerate
    print(chave,valor)
