"""
Cuidados com dados mutáveis 
= - copiado o valor 
= - aponta para o mesmo valor na memória (mutável)
"""

#nome = 'Luiz'
#nome[1] = "D" -> não funciona
#noutra_variavel = nome 
#nome = 'João'
#print(nome)
#print(noutra_variavel)

lista_a = ['Luiz', 'Maria', 1, True, 1.2]
#lista_b = lista_a #Mesmo valor na memória => quando modifico a lista a, modifico a lista b também (Valor Mutável) !!
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer valor'
print(lista_a)
print(lista_b)
