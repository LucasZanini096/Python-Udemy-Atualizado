"""
Iterável -> str, range, etc (_iter_)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor 
iter -> me entregue seu iterador 
"""
texto = iter('Luiz')

print(next(texto)) #ou texto_next_()
print(next(texto))
print(next(texto))
print(next(texto))


# for letra in texto -> O que o comando for realiza!!
texto = 'Luiz'
iteratador = iter(texto) #iterador 

while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break

#Comentários:
#01 - Método -> adicionar alguma ação depois de um objeto, pro exemplo uma STR.
#Ex: texto.upper()
#02 - Iter -> interador de objetos -> vizualização desse mesmo objeto na memória do compuatdor 
#03 - Next -> chama o próximo valor de um objeto, de acordo com o interador 