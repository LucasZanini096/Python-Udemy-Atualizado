# Exercícios com funções 
#Exercício 01

def fatorial(*args):
    anterior = 1
    
    for num in args:
        multiplicacao = num * anterior
        anterior = multiplicacao

    return multiplicacao     

fatorial_5 = 1,2,3,4,5
print(fatorial(*fatorial_5))
 
#             OU

#fatorial_5 = fatorial(1,2,3,4,5)
#print(fatorial_5)    

#Exercício 02

def par_ou_impar(*args):

    while True:
        
        if len(args) > 1 or len(args) == 0:
            print('Digite apenas um número')
            break
        
        else: 
            num = args[0]
            if num % 2 == 0:
                print (f'O número {num} é par!')
                break
            
            else:
                print(f'O número {num} é impar!')
                break

par_ou_impar(13)


# OU

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'



  

