"""
Closure e funções que retornam outras funções
"""

def criar_saudacao(saudacao): #Primeiro chama a função criar_saudação
    def saudar(nome): #Dentro de criar_saudação, há a chamada de outra função - > Saudar
        return f'{saudacao}, {nome}!'#Depois de chamar o closure, ai vai para o retrun de Saudar
    return saudar #De def Saudar, vai direto para o return de criar_saudacao (segue o caminho em direção ao return do primeiro def chamado)


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))
    

