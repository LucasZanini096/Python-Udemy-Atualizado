"""
Valores padrão para parâmetros 
Ao definir uma função, os parâmetros ter valores padrão. 
Caso o valor não seja 
enviado para o parâmetro, o valor padrão será 
usado.
Refatorar: editar o seu código.
"""
#OBS: Valor 0 é considerado FALSE 

def soma (x,y,z = None):  #Toda vez que eu declarar um parâmetro como padrão, terei que nomear todos após ele como padrão
    if z is not None:
        print(f' {x=} {y=} {z=}', x + y + z)
    else:
        print (f'{x=} {y=}', x + y)



soma(1,2)
soma(3,5)
soma(100,200)
soma(7,9,0)
soma (y = 9, z = 0, x = 7)