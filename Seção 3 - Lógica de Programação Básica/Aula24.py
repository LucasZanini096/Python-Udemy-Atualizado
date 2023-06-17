"""
s - string
d - int
f - float 
.<número de dígitos>f
(Caractere) (><^)(quantidade)
> - Esquerda 
< - Direita 
^ - Centro
= - Força o número a aparecer antes de zeros 
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion Flags - !r !s !a
"""
variavel = "ABC"
print (f'{variavel}')
print (f'{variavel: >10}') #PED
print (f'{variavel: <10}.')
print (f'{variavel: ^10}')
print (f'{10000.54165184514:0=+10,.1f}')
print ("O hexadecimal de 1500 é {1500:08X}") #{num:0nX} => simboliza a presença de um hexadecimal 

