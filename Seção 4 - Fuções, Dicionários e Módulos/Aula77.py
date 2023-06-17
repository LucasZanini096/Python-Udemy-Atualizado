# Função Lambda em Python 
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas 
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única 
# expressão 

# lista =  [
#      {'nome': 'Luiz', 'sobrenome':'miranda'},
#      {'nome': 'Maria', 'sobrenome':'Oliveira'},
#      {'nome': 'Daniel', 'sobrenome':'Silva'},
#      {'nome': 'Eduardo', 'sobrenome':'Moreira'},
#      {'nome': 'Aline', 'sobrenome':'Souza'},

lista = [4,32,1,34,5,6,6,21]
lista.sort(reverse=True) #Deixa em ordem decrescente os objetos 

# sorted(lista) -> Cria uma cópia rasa da lista em ordem 

lista =  [
    {'nome': 'Luiz', 'sobrenome':'miranda'},
    {'nome': 'Maria', 'sobrenome':'Oliveira'},
    {'nome': 'Daniel', 'sobrenome':'Silva'},
    {'nome': 'Eduardo', 'sobrenome':'Moreira'},
    {'nome': 'Aline', 'sobrenome':'Souza'},
]

def ordena(item):
    print(item)
    return item['nome'] #Ele vai ordenar através da chave de um dicionário

lista.sort(key=ordena) #Key -> chama uma função !! -> Por meio da função "ordena" que está dentro
#sort, vai ocorrer o ordenamento dos dicionários dentro da lista, de acordo com a ordem alfabética dos nomes  
print(lista)

for item in lista:
    print(item)

#Essa mesma estrtura pode ser utilizada através da função lambda
#Uma maneira mais simplificada de ordenamento
lista.sort(key= lambda item: item['nome']) 
print(lista)

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(key= lambda item: item['nome']) 
l2 = sorted(key= lambda item: item['sobrenome']) 

exibir(l1)
exibir(l2)

#Comentários:
#01 - Quando chamada a função lambda para ordenação, ela não necessita ser enumerada,
# apenas colocar o parâmetro direto 
#02 - Depois de ter colocado os dois pontos, coloca-se o vai ser retornado 



