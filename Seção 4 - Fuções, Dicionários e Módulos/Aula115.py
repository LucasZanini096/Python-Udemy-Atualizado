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

#O modo "w" apaga todo o conteúdo do arquivo a cada execução do código em Python 
#Já o modo "a" não apaga nenhum conteúdo prévio escrito no arquivo, ele continua da última linha de texto do arquivo 
with open(caminho_arquivo,"w+", encoding="utf8") as arquivo: #Sempre tenho que passar como parâmetros: caminho do arquivo, modo e o seu endocoding

    arquivo.write("Atenção\n") #No arquivo vai aparecer alguns caracteres errados no Windows, pois o arquivo possui um sistema de codificação distinto do UTF8
    arquivo.write("Linha 1\n") #Esse problema é associado ao Endcoding
    arquivo.write("Linha 2\n") 
    arquivo.writelines( 
         
    ("Linha 3\n", "Linha 4\n")  
     

    )