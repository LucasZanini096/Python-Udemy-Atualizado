"""
Interpolação básica de strings 
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Luiz'
preco = 1000.9854845612612
variavel = '%s, o preço é R$%.2f' % (nome, preco) #Ele arredondou a variavel preco !!
print (variavel)
print ('O hexadecimal de %d é %08x' % (1500,1500)) #D - representa os inteiros/ X - representa os hexadecimais (04 - quantidade de zeros a frente do número)
