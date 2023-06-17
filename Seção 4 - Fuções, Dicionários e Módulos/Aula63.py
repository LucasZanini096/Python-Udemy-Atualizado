"""
args - Argumnetos não nomeados 
* - * args (empacotamento e desempacotamento)
"""
#lembre-se de desempacotamento 
x,y,*resto = 1,2,3,4 #tupla
print(x,y,resto)

#def soma (x,y):
#    return x + y

def soma(*args): #passar todos os argumentos não nomeados para a função
    total = 0
    for numero in args:
        total += numero
        print(f'Total: {numero} + {total} = {numero + total}', end = '/')
    return total     


#soma(1,2,3,4,5,6) #Essa tupla foi empacotada em 'args'!!
soma_1_2_3 = soma(1,2,3)
#print(soma_1_2_3)

soma_4_5_6 = soma(4,5,6)
outra_soma_0 = soma(1,2,3,63,56,98,65,47)
#print (outra_soma_0)

#print(sum(1,2,3,4,5,6,7,8,9,2365,98)) -> essa mesma função já própria do Python !!

numeros = 1,2,3,4,5,6,7,8
#print(numeros)
#print(soma(numeros)) #Assim vai dar erro, pois os "ARGS" vai empacotar uma tupla, ficando assim ((1,2,3,4,5,6,7,8),).
#Dessa maneira, há a necessidade de desempacotar os valores dessa tupla !!
#Solução 

numeros = 1,2,3,4,5,6,7,8
outra_soma_1 = soma(*numeros) # O * desempacota uma tupla. Assim, pode ser considerado um argumento, executando a função !!
print (outra_soma_1)


