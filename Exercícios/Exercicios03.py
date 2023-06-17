# Calculadora de quatro operações + - * / 
#01 - Declaração de valores e operador desejado

while True:
 
 x = input("Digite o primeiro valor:")
 y = input("Digite o segundo valor:")
 operador = input("Digite um operador válido:")
 numeros = None
 operador_verdadeiro = None

#02 - Verificação de digitação correta do usuário
#02.1 - Números 

 try:
    x_int = int(x)
    y_int = int(y)
    numeros = True
 except:
    print ("Você deve digitar números e não letras ou símbolos")
    continue
  
#02.2 - Operadores
  
 Operadores_validos = "+", "-", "*", "/"

 if operador in Operadores_validos:
   operador_verdadeiro = True 
 else:
   print ('Você deve digitar um operador válido')
   continue 
#03. Operações em si

 if operador_verdadeiro == True and numeros == True:
   if operador == "+":
    soma = x + y
    print (f'{x} + {y} = {soma}')
   elif operador == "-":
     sub = x - y
     print (f'{x} - {y} = {sub}')
   elif operador == "*":
     multi = x * y
     print (f'{x} * {y} = {multi}')
   elif operador == "/":
     div = x/y
     print (f'{x} / {y} = {div}')
   else:
     print ('Você não deveria estar aqui')

 print ("Você deseja sair da calculadora? Digite [S]im ou [N]ão")
 exist = input().upper()
 if exist == "Sim":
   break 
 
     
 

