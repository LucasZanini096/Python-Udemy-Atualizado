#Criando arquivos com Python
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x(para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Contexto Manager - with (abre e fecha)
# Métodos úteis 
# write, read (escrever e ler)
# writelines (escrever Várias linhas)
# seek (move o cursor)
# readline (ler linha)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo 
# os.rename - troca ou move o arquivo 
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load 

caminho_arquivo =  "C:\\Users\\Administrador\\Desktop\\Arquivos Python\\"
caminho_arquivo = "arquivo_1.txt"

with open(caminho_arquivo,"w+") as arquivo: # "+" para adicionar a função de ler um arquivo também.

    arquivo.write("Linha 1\n") #O cursor do Python move dentro do arquivo
    arquivo.write("Linha 2\n") #O \n realiza a quebra de linha. Se não colocar, os dois textos ficaram juntos numa mesma linha 
    arquivo.writelines( 
         
    ("Linha 3\n", "Linha 4\n")  #Permite eu criar várias linhas com apenas esse método, por meio de uma tupla
    #Possui um iterador dentro desse método 

    )

    arquivo.seek(0,0) #Método que permite eu mover o cursor para qualquer posição do arquivo
    print(arquivo.read()) #Se eu não coloca-se o cursor no início do arquivo ele não liria nada, pois o cursor já está no fim do arquivo 
    print("Lendo")
    arquivo.seek(0,0)
    print(arquivo.readline(),end=" ") #Vai realizar a leitura de uma linha por vez no arquivo. Possui a função __next__ dentro dele
    print(arquivo.readline().strip()) #Ele já realiza por padrão a quebra de linha 
    print(arquivo.readline()) #Sugestão: colocar a palavra chave end="" ou aplicar o método 
    #O método .readlines() forma uma lista de linhas

    print("Lendo linhas")
    
    arquivo.seek(0,0)

    for linha in arquivo.readlines():
        print(linha)



#O modo "r" realiza apenas a leitura do arquivo 
with open(caminho_arquivo, 'r') as arquivo:
     print(arquivo.read()) 