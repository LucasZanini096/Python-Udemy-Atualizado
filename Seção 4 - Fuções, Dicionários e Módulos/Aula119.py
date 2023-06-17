#Controlando a quantidade de argumentos posicionais e nomeados 
#*args (ilimitado de argumentos posicionais)
#** kwargs (ilimitado de argumentos)
# Positional-only Parameters (/) - Tudo antes da barra deve ser
# ! apenas ! posicionais
# PEP 570 - Python Positional-onlt Parameters 
# https://peps.python.org/pep-0570/
# Keyword-Only Arguments(*) - *sozinho !não suga! valores.
# PEP 3102 - Keyword-Only Arguments
# https://peps.python.org/pep-3102/

def soma(a,b,/,x,y): #Estou declarando que antes da barra, não pode haver argumentos nomeados, apenas depois da barra.
    #Havendo a aplicação da regra de argumentos nomeados(Se eu declarar um parâmetro, devo declarar todos a sua direita)
    print(a + b + x + y)

soma(1,2,3,y=3)


def soma(a,b,*,c, **kwargs): #Tudo depois do asterico deve ser argumento nomeado, obrigatoriamente.
    print(kwargs)
    print (a,b,c)

soma(1,2,3, nome="teste")

