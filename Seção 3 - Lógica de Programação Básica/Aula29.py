""""
Flag (bandeira) - Marcar um local 
Nome = não valor/ nada 
is e is not = é ou não é (tipo, valor, identidade)
id = identidade 
"""
condicao = False 
passou_no_if = None 

if condicao:
    passou_no_if = True #SEMPRE DECLARAR VARIÁVEIS ANTES DE BLOCOS, COMO DO IF! SE NÃO O CÓDIGO FICA RUIM!!
    print ('Faça algo')
else:
    print ('Não faça algo')

print (passou_no_if, passou_no_if is None) #O operador is é semelhante a uma igualdade (==), porém é utilizado junto com None 
print (passou_no_if, passou_no_if is not None) 

if passou_no_if is None:
    print('Não passou no if')
else:
    print ('Passou no if')
    