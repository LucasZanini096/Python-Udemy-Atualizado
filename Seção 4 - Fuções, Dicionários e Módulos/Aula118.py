#Problema dos parâmetros mutáveis em funções Python 

def adiciona_clientes(nome, lista=[]): #Lista vazia como parâmetro padrão da função
    lista.append(nome)
    return lista

clientes_1 = adiciona_clientes('luiz')
adiciona_clientes("Joana", clientes_1)
print(clientes_1)

clientes_2 = adiciona_clientes("Helena")
adiciona_clientes("Maria", clientes_2)
print(clientes_2)

#O print vai sair como uma única lista, ou seja, com os elementos de clientes 1 e de clientes 2
#Isso ocorre, pois no parâmetro da função foi declarado uma lista vazia, sendo um objeto mutável. 
#Neste caso, ela vai adicionando novos dados a lista a cada nova chamada da função, independente de uma associação a uma variável distinta 
#Para corrigir devo declarar uma lista fora função da função e colocar como argumento na chamada da função 
#OU

def adiciona_clientes(nome, lista=None): #Lista vazia como parâmetro padrão da função
    if lista ==  None:
        lista = [] #Dessa maneira, a cada chamada da função em que a lista não é declarada como argumento, vai ser criada uma nova lista 

    lista.append(nome)
    return lista

clientes_1 = adiciona_clientes('luiz')
adiciona_clientes("Joana", clientes_1)
print(clientes_1)

clientes_2 = adiciona_clientes("Helena")
adiciona_clientes("Maria", clientes_2)
print(clientes_2)

