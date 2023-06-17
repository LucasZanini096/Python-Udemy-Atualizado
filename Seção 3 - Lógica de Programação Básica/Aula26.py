"""
Introdução ao try/except
try -> tentar executar o código 
except -> ocorreu algum erro ao tentar executar 
"""

numero_str = input(
    'Vou dobrar o número que vc digitar:'
)

"""if numero_str.isdigit():
    numero_float = float(numero_str)
    print (f'O dobro de {numero_str} será {numero_float:.2f}')
else:
    print("Isso não é um número")
"""
try: 
    print ("STR:", numero_str)
    numero_float = float(numero_str) #Vai executar o código até que ele de erro e automaticamente vai cair no "except"/ FAIL FAST
    print ('Float:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float*2}')
except:
    print ("Isso não é um número")