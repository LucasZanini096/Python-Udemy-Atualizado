##### While/Else ####
string = "Valor Qualquer"
i = 0
while i < len(string):
    letra = string [i]

    if letra == " ":
        break
    
    print (letra)
    i += 1
else:
    print ('O else foi executado.')
print('Fora do while.')

""" Comentários:
01 - Neste caso o else será executado após o fim while, mesmo ele estando associado a ele
02 - Se for aplicado o comando break, haverá a sáida do laço forçado, não havendo a execução do restante do while e else.
"""