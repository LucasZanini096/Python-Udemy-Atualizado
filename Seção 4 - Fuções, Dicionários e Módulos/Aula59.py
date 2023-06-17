"""
Argumentos nomeados e não nomeados em funções Python 
Argumento nomeado tem nome com sinal de igual 
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y, z):
    # Definição
    print (f'{x=}  y={y}  z ={z}', '|', 'x + y + z', x + y + z)



soma(1,2,3) #Argumentos posicionais -> dependem da ordem para x e y
soma (y = 2, z = 3, x = 1) #Argumento nomeado !!
soma (1,2, z=5) #Nao recomendado -> todos os parâmetros depois do nomeado, precisam ser nomeados !!

print(1,2,3, sep='/')


