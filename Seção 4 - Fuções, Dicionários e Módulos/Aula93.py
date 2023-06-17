# Try, except, else e finally 
try:
    print('ABRIR ARQUIVO')
    #8/0 #Erro aqui

except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('DIVIDIU POR ZERO')

except IndexError as error:
    print(error.__class__.__name__)
    print(error)
    print('IndexError')

except (NameError, ImportError):
    print('NameError, ImportError')

else: 
    print('NÃO DEU ERRO')

finally: #Sempre vai ser executado, independetemente se ocorrer algum erro, ateriormente 
    print('FECHAR ARQUIVO')