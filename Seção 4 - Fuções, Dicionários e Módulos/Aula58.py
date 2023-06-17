"""
Introdução às funções (def) em Python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""
#def Print():
#    print ("Que legal!!")

#Print()    







#def imprimir(a,b,c): #a,b,c -> são váriáveis e ao mesmo tempo, são parâmetros
#    print (a,b,c) 
    
#imprimir (1,2,3) #Quando eu preencho os parâmetros com valores e excecuto a função, os mesmos valores viram argumentos
#imprimir (4,5,6)


def saudacao(nome= 'Sem nome'): #Se não colocar um argumento, irá executar o print do 'Sem nome'
    print(f'Olá, {nome}')

saudacao('Luis Otávio')
saudacao('Maria')
saudacao('Helena')
saudacao()