"""""
Operadores de comparação (relacionais)
OP       Significado        Exemplo (True)
>        Maior              2 > 1
>=       Maior ou Igual     2 >= 2
<        Menor              1 < 2
<=       Menor ou Igual     2 <= 2
==       Igual              'a' == 'a'
!=       Diferente          'a' != 'b'
"""""""""
maior = 2 > 1
maior_ou_igual = 2>= 2
menor = 1 < 2
menor_ou_igual = 2 <= 2
igual = 2 == 2
diferente = 4 != 5
print (diferente)

#Exemplo:
primeiro_valor = int(input("Digite um valor:"))
segundo_valor = int(input('Digite outro número:'))
if primeiro_valor >= segundo_valor:
    print (f'{primeiro_valor} é maior que {segundo_valor}')
    #ou print ("{} é maior que {}".format(primeiro_valor,segundo_valor))
else:
    print (f'{segundo_valor} é maior que {primeiro_valor}')
    #ou print ("{} é maior que {}".format(segundo_valor,primeiro_valor))