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



#Eu tenho que indicar o caminho do arquivo, por meio do nome das pastas. Os nomes são separadas por dois traços invertidos, no Windows
 
caminho_arquivo = "C:\\Users\\Administrador\\Desktop\\curso_vscode\\"
caminho_arquivo += "aula113.txt"
print(caminho_arquivo)