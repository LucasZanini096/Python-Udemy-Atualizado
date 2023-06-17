"""
split e join com list e str
split - divide uma string
join - une uma string
"""

frase = '    Olha só que   ,   coisa interessante  '
lista_frases_cruas = frase.split(',') #Posso separar uma str por determinado elemento presente nela, na qual não será incluido

lista_frases = [] 
for i, frase in enumerate(lista_frases_cruas): #índice i + variável frase dentro do comando for 
    lista_frases.append(lista_frases_cruas[i].strip()) #Comando strip corta os espaços do começo e do final de uma string (limpa os espaços)

print(lista_frases_cruas)
print(lista_frases)

frases_unidas = ''.join('abc')
print(frases_unidas)



#Comentários:
#01 - rstrip() -> Comando strip corta os espaços à direita de uma string
#02 - lstrip() -> Comando strip corta os espaços à esquerda de uma string
#03 - ''.join() -> na string quer vai ser colocado o separador/ dentro do parênteses vêm os interaveis (strs, listas e tuplas) !!
