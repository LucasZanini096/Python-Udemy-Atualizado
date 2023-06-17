#Operadores Lógicos 
#Usado para inverter expressões 
# not True = False 
# not False = True 
#Obs: String Vazia é considerada False 
senha = input('Senha: ')

if senha != '123456':
    print ('Senha incorreta.')
else: 
    print ('Senha Correta')
if not senha:
    print ('Digitou não digitou nada')

