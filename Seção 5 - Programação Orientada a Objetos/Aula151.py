# __new__  e __init__ em classes Python 
# ___new__ é o método responsável por criar e 
# retornar o novo objeto. Por isso, new recebe cls
# __new__ !Deve retornar o novo objeto!
# __init__ é o método responsável por inicializar 
# a instância. Por isso, init recebe self.
# __init__ !Não Deve retirnar nada (None) !
# object é a super classe de uma classe 

#__new__ não recebe self, pois ele cria a instância/self !!
#Ele é chamado antes do __init__


class A:

     def __new__(cls,x): #New precisa ter a mesma assinatura do init 
            print("Antes de criar a inst")
            instancia = super().__new__(cls) #Tô criando a instância 
            print('Depois')
            instancia.x = 213
            return instancia

     def __init__(self,x):
           self.x = x
           print("Sou o init")
     
     def __repr__(self):
           return 'A()'

a = A(123)
print(a.x)