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

print(pessoa['nome'])
print(pessoa.get('nome','Não existe'))

nome = pessoa.pop('nome')
#print(nome)
#print(pessoa)

ultima_chave = pessoa.popitem()
print(ultima_chave)
print(pessoa)


pessoa.update({
    'nome': 'novo valor',
     'idade': 30,

})

pessoa.update(nome='novo valor', idade=30)
tupla = ('nome', 'novo valor'), ('idade', 30)
lista = [['nome', 'novo valor'], ['idade', 30]]
pessoa.update(tupla)
print(pessoa)