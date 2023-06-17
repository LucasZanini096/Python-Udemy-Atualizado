"""
Higher Order Functions 
Funções de primeira classe -> funções executando outras funções !!
"""
def saudacao(msg):
    return msg


def executa(funcao, texto):
    return funcao(texto)


#saudacao_2 = saudacao 
#print(saudacao('Bom dia')

#x = executa(saudacao_2) #Vai dar erro !!!
#v = executa(saudacao)

v = executa(saudacao, 'Bom dia')
print(v)


def saudacao(msg, nome):
    return  f'{msg}, {nome}'


def executa(funcao, *args):
    return funcao(*args)

v = executa(saudacao, 'Bom dia', 'Lucas')
print(v)

