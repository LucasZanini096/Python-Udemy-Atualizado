#Tipos built-in, documentação, tipo imutáveis, métodos de strings
"""
https://docs.python,org/pt-br/3/library/stdtypes.html
Imutaveis que vimos: str, int, float, bool -> Não pode mudar o valor desses tipos de dados
"""
string = 'Luiz Otávio'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
#print (string)
#print (outra_variavel)

print (string.capitalize())
#Capitalize -> Retorna apenas a primeira letra da str em maiúsculo
print (string.zfill(10))
#Zfill -> Coloca "x" zeros a esquerda de uma string
