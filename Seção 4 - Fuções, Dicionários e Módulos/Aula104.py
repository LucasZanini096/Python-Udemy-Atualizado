# Ordem dos decoradores
def parametros_decorador(nome):
    def decorador(func):
        print('Decoardor', nome)

        def sua_nova_funcao (*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final 
        return sua_nova_funcao
    return decorador

@parametros_decorador(nome='terceiro') #Posso chamar quantas vezes eu quiser o parâmetro_decorador, neste caso 
@parametros_decorador(nome='segundo')  #A leitura vai ser de baixo para cima, neste caso em específico  
@parametros_decorador(nome='primeiro') #Há uma closure imbutida
def soma(x,y):
    return x + y

dez_mais_cinco = soma(10,5)
print(dez_mais_cinco)