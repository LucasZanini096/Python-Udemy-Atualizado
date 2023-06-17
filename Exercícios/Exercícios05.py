"""
Daça uma lista de compras com listas 
O usuário deve ter a possibilidade de inserir,
apagar e listar valores de sua lista 
Não permita que o programa quebre com erros de índices inexistentes na lista
"""

#01 Listar uma lista inicial 


lista_de_compras = []
while True:

#02 - Inserir uma determinada ação 

 acao = input('Digite um dos comandos: [I]nserir, [E]liminar,[S]air').upper()

#03 - Verficação do comando digitado  
 if acao != "I" or acao != "E" or acao != "S":
 
  print("Digite um comando válido")
  continue
 
 elif acao == "S":
 
  print(f'Está é a sua lista final {lista_de_compras}')
  break

 elif acao == "I":
  produto_inserido = input("Digite um produto para inserir:") 
  lista_de_compras.append(produto_inserido)
  
  for indice, produto in enumerate(lista_de_compras):
   print(f'{indice}  {produto}')
 
 elif acao == "D":
  retirada_produto = input('Digite um produto para ser retirado da lista').capitalize()

  if retirada_produto in lista_de_compras:
   lista_de_compras.pop(retirada_produto)
  
   for indice, produto in enumerate(lista_de_compras):
    print (f'{indice}   {produto}')
  
  else:
   print("Digite novamente uma ação")
   continue
