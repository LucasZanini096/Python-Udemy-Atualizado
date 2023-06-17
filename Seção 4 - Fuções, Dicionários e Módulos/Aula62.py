"""
Retorno de valores das funções (return)
"""

def soma(x,y):

    if x > 10:
      #return x + y #Vai retornar alguma coisa, podendo utiliza-lo depois, como efetuar uma soma (acabar com a exceução da função, retornando um valor) 
      return 10 , 20 #Pode retornar listas ou Tuplas
    return x + y  #Apenas nas funções e nos métodos pode - se utilizar return/ A execução do código dentro da função acaba no return !!
                  #Uma função pode ter apenas um return 





#variavel = print('Luiz') #Print não possui valor, apenas é uma função, mas retorna None 
#variavel = None
#variavel = soma(1,2)
#variavel = int('1') #Função que rertorna um valor
#print(variavel)

soma1 = soma(2,2) #Assim como print, essa função não retorna nada (None)
soma2 = soma(3,3)
print (soma1 + soma2)
print (soma1)
print(soma2)
print (soma(11,55))
