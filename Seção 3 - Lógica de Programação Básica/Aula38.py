frase = "O Python é uma linguagem de programação "\
     "multiparadigma. "\
     "Python foi criado por Guildo van Rossum."

print(frase.lower().count('python'))
#Comentários:
#01 - .lower() -> transforma toda a str em minúscula
#02 - .upper() -> tranforma toda a str em maiúscula 
#03 - .cont() -> conta quantas vezes houve a presença de determinada str

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual  = frase[i]

    if letra_atual == ' ':
        i += 1
        continue
    qtd_apareceu_mais_vezes_atual= frase.count(letra_atual)
    if qtd_apareceu_mais_vezes <= qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1


print(
    'A letra que mais apareceu mais vezes foi o '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)

    