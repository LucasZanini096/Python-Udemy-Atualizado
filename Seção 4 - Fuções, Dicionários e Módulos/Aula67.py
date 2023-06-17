#Manipulando chaves e valores em dicionários 
pessoa = {}

##
##

pessoa['nome'] = 'Luiz Otávio'

print(pessoa)
#print(pessoa['nome1']) Vai dar erro -> Não existe 


chave = 'nome_completo'
pessoa[chave] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'

print(pessoa[chave])

pessoa[chave] = 'Maria'

del pessoa['sobrenome']

print(pessoa)
print(pessoa['nome'])

#print(pessoa.get('sobrenome')) #Vai verificar a existência de uma chave especificada 
#Neste caso vai retornar um None !!!
if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])
