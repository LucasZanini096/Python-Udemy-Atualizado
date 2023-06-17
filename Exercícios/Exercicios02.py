"""
Iterando strings com while
"""    #012345678910
#nome = "Luiz Otávio"

#tamanho_nome = len(nome)
#print (nome)
#print(tamanho_nome)
#print(nome[3])

#nova_string = '*L*u*i*Z* *O*t*á*v*i*o'
#Exercício 
nome = input("Digite seu nome:")
nome.split()
tamanho_nome = len(nome)
cont = 0
ind = 0
palavra_final = ''
while cont <= tamanho_nome: #Repetição da ação
    while ind < tamanho_nome: #Índice + *
        letra = nome[ind]
        simbolo = "*"
        letra_final = simbolo + letra
        palavra_final += letra_final
        ind += 1
    cont += 1
print (palavra_final)

