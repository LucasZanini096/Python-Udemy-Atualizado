import os

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


caminho_arquivo = "arquivo_1.txt"


with open(caminho_arquivo,"w+", encoding="utf8") as arquivo: 

    arquivo.write("Atenção\n") 
    arquivo.write("Linha 1\n") 
    arquivo.write("Linha 2\n") 
    arquivo.writelines( 
         
    ("Linha 3\n", "Linha 4\n")  
     

    )

os.remove(caminho_arquivo) #Ele remove por inteiro o arquivo criado. Tenho que passar o caminho do arquino no parâmetro do método
#Pode ser os.unlink também 

os.rename(caminho_arquivo, "Arquivo_1_2.txt") #Permite eu renomear o nome de um arquivo, quanto para mover de lugar 
#Em seu parâmetro devo escrever o nome do arquivo e seu novo caminho/nome
