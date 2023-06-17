# dir, hasattr e getattr em Python 
string = 'Luiz'
metodo = 'upper'

print(string)

if hasattr(string, metodo): #Primeiro se coloca um determinado objeto e, logo após se coloca o nome do método (str) 
    print('Existe upper')
    print(string.metodo()) #Posso chamar o método indicado no hasattr, sendo renomeado 
    print(getattr(string,metodo)())
else:
    print('Não existe o método', metodo)
    
