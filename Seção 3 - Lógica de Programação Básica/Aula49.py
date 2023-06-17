"""
Introdução ao desempacotamento 
"""

nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']
print(nome2)

nome1, nome2 = ['Maria', 'Helena', 'Luiz'] #Vai dar erro, falta de variaveis!!
nome1, nome2, nome3, nome4 = ['Maria', 'Helena', 'Luiz'] #Vai dar erro, falta de valores correspondente as varivaeis.

nome1, *resto = ['Maria', 'Helena', 'Luiz']
print(nome1) #Maria ['Helena', 'Luiz']

_,_, nome, *resto = ['Maria', 'Helena', 'Luiz']

#Comentários:
#01 - A restrição do desempacotamento ocorre a partir do acréscimo de uma virgula, * e o nome da variavel que vai armazenar o "resto" de uma lista em outra
#02 - nome1, *_ = ['Maria', 'Helena', 'Luiz'] -> underline mais usual para desenvolvedores