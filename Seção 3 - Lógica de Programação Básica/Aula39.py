"""texto = 'Python'

i = 0
tamanho_string = len(texto)

while i < tamanho_string:
    print(texto[i])

    i += 1
"""

#senha_salva = '123456'
#senha_digitada = ' '
#repeticoes = 0

#while senha_salva != senha_digitada:
#    senha_digitada = input(f'Sua senha ({repeticoes}x):')

#    repeticoes += 1
texto = 'Python'

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print (novo_texto + "*")

#Comentários:
# 01 - Quando "letra" foi colocado dentro do comando for 
# ele vai ser uma variável para cada caractere de 'texto' a cada repetição
