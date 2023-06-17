#Decoradores com parâmetros 
def decaradora(func):
    print ("Decoradora 1")

    def aninhada(*args, **kwargs): #Inerfunction/ Nestedfunction -> Pausa para a execução de uma outra função
        print("Aninhada")
        res = func(*args, **kwargs)
        return res
    return aninhada

def blablabla(a,b,c): #Vai executar como um decorador, ou seja, vai criar a função decoradora 
   print(a,b,c) 
   return decaradora

 #Executa a decorada para a soma
@blablabla 
def soma (x,y):
    return x + y

dez_mais_cinco = soma(10,5)
print(dez_mais_cinco)


def fabrica_de_decoradores(a = None,b = None, c =None):
    def fabrica_de_funcoes(func):
        print ("Decoradora 1")
        def aninhada(*args, **kwargs): #Inerfunction/ Nestedfunction
            print('Parâmetros do decorador, ', a,b,c)
            print("Aninhada")
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_decoradores
   


@fabrica_de_decoradores(1,2,3)
def soma (x,y):
    return x + y

decaradora_1 = fabrica_de_decoradores()
multiplica = decaradora_1(lambda x,y: x * y)

