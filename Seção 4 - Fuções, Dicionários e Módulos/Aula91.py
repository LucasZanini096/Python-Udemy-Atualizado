# Yield from

def gen1():
    print('COMEÇOU GEN1')
    yield 1
    yield 2
    yield 3
    print('TERMINOU GEN1')


def gen2(gen):
    print('COMEÇOU GEN2')
    yield from gen() #importa de outras funções os seus respectivos yields 
    yield 4
    yield 5
    yield 6
    print('TERMINOU GEN2')


def gen3():
    print('COMEÇOU GEN3')
    yield 50
    yield 60
    yield 70
    print('TERMINOU GEN3')

g = gen2(gen1)
for numero in g:
    print (numero)

g1 = gen2(gen3)
for numero in g1:
    print(numero)

