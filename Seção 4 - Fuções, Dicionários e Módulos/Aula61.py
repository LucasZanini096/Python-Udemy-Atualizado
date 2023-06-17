"""
Escopo de funções em Python 
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local 
podem ser alcançados.
"""
x = 1 # Posso definir o x fora da função, assim eu posso executa-lá, caso ela esteje declarada antes da chamada da função 


def escopo():
    global x #Vai associar o valor de x declarado internamente e externamente, manipulando-o
    x = 10 #Mas se eu declarar um novo x dentro de uma funçao, se eu chamar ela, ela vai considerar a variavel x dentro da função e a de fora 
    
    def outra_funcao():
        global x 
        x = 11 #Mais um 'novo' x -> esta situação lembra  mecanismo das bonecas russas 
        y = 2
        print (x,y)

    outra_funcao()
    print(x)


print(x)
escopo()
print(x)
