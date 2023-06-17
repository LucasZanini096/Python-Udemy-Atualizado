#Desempacotamento em chamadas 
# de métodos e funções 
string = 'ABCD'
lista = ['Maria', 'Helena', 1,2,3,'Eduarda']
tupla = 'Python', 'é', 'legal'


#p, b ,*_, ap, u = lista
#print (p,u,ap)

for nome in lista:
    print (nome, end='', sep='')



print(*lista)
print(*string)
print(*tupla)




#Comentários 
#01 - Comando end -> quebra de linha, todos os objetos são colocados numa mesma linha
#02 - Comando sep -> entre os espaços dos objetos de determinado print, coloca-se algo entre eles
#03 - print(*) -> retorna a mesma saída do comando for nome in lista:
#  #print (nome, end='', sep='') -> separa cada um dos elementos de uma str, tupla ou lista, printando-os.