#Exercício 1
#01 - Declarar um valor 
num = input("Digite um valor:")
#02 - Verficar se ele é inteiro 
#OU - if num.isdigit(): -> verifica se a string digitada é número de fato!!
try:
    print("Int:", num)
    num_int = int(num)
    #03 - Se for um inteiro, verficar se ele é par ou ímpar
    if num_int % 2 == 0:
        print(f'O número {num_int} é par.')
    else: 
        print (f'O número {num_int} é ímpar.')
except:
    print (f'Isso não é um número inteiro.')

#Exerício 02
#01 Declarar o horário
horario = input("Digite um horário:") #no formato (21:35), por exemplo
#02 Separar a string em índices 
horario.split()
#02.1 Declarar horas 
horas = horario [0] + horario [1]
horas_int = int(horas)
#02.2 - Declaração minutos 
minutos = horario[3] + horario[4]
minutos_int = int(minutos)
#03 - Condição para a saudação apropriada 
if horas_int >= 0 and horas_int < 12:
    print ('Bom dia %d-%d' % (horas_int, minutos_int))
elif horas_int >= 12 and horas_int < 18:
    print ('Bom tarde %d-%d' % (horas_int, minutos_int))
else:
    print ('Boa noite %d-%d' % (horas_int, minutos_int))

#Exercício 3
#01 - Declarar o primeiro nome 
primeiro_nome = input("Digite seu primeiro nome:")
#02 - Condional para os diferentes prints 
if len(primeiro_nome) <= 4:
    print(f'Se nome é curto')
elif len(primeiro_nome) == 5 or len(primeiro_nome) == 6:
    print(f'Seu nome é normal')
else:
    print(f'Seu nome é muito grande')

