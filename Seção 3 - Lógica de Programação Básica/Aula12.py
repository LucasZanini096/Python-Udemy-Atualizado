#formação de strings 
nome = "Lucas Zanini"
altura = 1.83
peso = 64
imc = peso/altura**2
linha1 = f'{nome} tem {altura:.2f} de altura' #f colocado na frente de uma string permite que haja variaveis dentro dela, sendo definidas a partir da presença de chaves 
#arredondamento {variavel:.nf} f = float 
linha2 = f'pesa{peso} quilos e seu imc é'
linha3 = f'{imc:.2f}'

print(linha1)
print(linha2)
print(linha3)
