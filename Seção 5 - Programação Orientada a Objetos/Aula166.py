#Enum -> Enumerações (permite criar um grupo de coisas pré-definidas de um tipo)
#Enumerações na programação, são usadas em ocassões onde temos 
#um determinado número de coisas para escolher.
#Enums têm membros e seus valores são constantes.
#Ele é uma classe, porém não se comporta como uma classe normal, pois possui uma metaclasse distinta
# Enums em Python:
# -são um conjunto de nomes simbólicos (membros) ligados a valores únicos
# -podem ser iterados para retornar seus membros canônicos na ordem de definição
#
# enum.Enum é a superclasse para a suas enumeraçãoes. Mas tamb´me pode ser considerada 
# diretamente (mesmo assim, Enums não são classes normais em Python)
# Você poderá usar seu Enum com type annotations, com isistance
# outras coisas relacioandas com tipo.
# Para obter os dados:
# Para obter o membro -> membro = Classe(valor), Classe['chave']
# chave = Chave.chave.name
# valor = Classe.chave.value

import enum

#Direcoes = enum.Enum("Direcoes", ['ESQUERDA', 'DIREITA']) #Dentro de enum estou declarando o tipo de direção
# Direcoes é uma classe !!!

#Para conferir tipagem nesta classe, eu devo fazer o seguinte;

class Direcoes(enum.Enum): #Minha metaclasse é enum.Enum 
    ESQUERDA = enum.auto()  
    DIREITA = enum.auto()
    BAIXO = enum.auto()
    CIMA = enum.auto()


print(Direcoes(1), Direcoes["Esquerda"], ['ESQUERDA', 'DIREITA'])
print(Direcoes(1).name, Direcoes.ESQUERDA.value)

def mover(direcao): #Não há tipagem por padrão !!

    if not isinstance(direcao, Direcoes):
        raise ValueError("Direção não encontrada") #Joga o erro na tela, a fim de evitar bugs ao longo do programa

    print(f'Movendo para {direcao.name} - ({direcao.value})')


mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover("lado")
