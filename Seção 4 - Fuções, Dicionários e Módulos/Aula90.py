# introdução às Generator functions em Python 
# generator = (n for n in range(100000))

def generator(n=0):
    yield 1 #O yield simboliza uma pausa dentro da função, em relação ao next repsectivo
    print ('Continuando...')
    yield 2 #Pausar novamente 
    print("Mais uma...")
    yield 3
    print('Vou terminar')
    return 'Acabou ' #O return neste caso acaba no stop interation, ou seja, 
#quando é chamado mais de um next para a função generator além do yield máximo.

gen = generator(n=0)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

#OU
gen = generator(n = 5, maximum=8) #O comando for possui o next em sua composição. Por isso não há necessidade de declarar esse mesmo método.
for n in gen:
    print(n)


def generator(n=0, maximum = 10): 
    while True: #obs: O input dentro de um while True pode ser considerado uma pausa 
        yield n
        n += 1

        if n > maximum:
            return

gen = generator(n=5, maximum=8) #Vai criar um range implicitamente 
for n in gen:
    print(n)


    
