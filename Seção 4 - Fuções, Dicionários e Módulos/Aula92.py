# Try, except, else e finally
try:
      a = 18
      b = 0
      print('Linha 1')
      c = a/b  #Neste caso estou silenciando um erro, mesmo ele existindo
      print('Linha 2')

except:
    print('Dividiu por zero.')

print('continuar')



#a = 18
#b = 0
#c = a/b
try:
      a = 18
      b = 0
      print('Linha 1')
      c = a/b  #Neste caso estou silenciando um erro, mesmo ele existindo, sendo não existindo divisão por zero 
      # Eu posso colocar a classe referente do erro no except, para quando der erro dentro do try, ele cai no except, explicitando o erro no código 
      #Exceções são clases
      print('Linha 2')

except ZeroDivisionError: #Estilo Pascal Case 
    print('Dividiu por zero.')

print('Continuar')


try:
      a = 18
      #b = 0
      print('Linha 1'[1000])
      c = a/b  
      print('Linha 2')

except ZeroDivisionError as e:
    print('Dividiu por zero.')
    print (e.__class__.__name__)
    print(e)
except NameError:
     print('Nome b não está definido')
except (TypeError, IndexError) as error: #Pode colocar uma tupla dentro do except/ 'as error' especifica a instância do erro 
     print('TypeError + IndexError')
     print('MSG', error)
     print('Nome', error.__class__.__name__)
except Exception: #Maior classe de erro no Python, abrange todos os erros dessa linguagem
     print('Erro desconhecido')

print('continuar')