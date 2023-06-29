#os.walk
#os.walk é uma função que permite percorrer uma estrtura de diretórios de
#maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).

#Modo recursivo: ele vai entrar em cada uma das pastas que tiver até chegar no último arquivo da
# última pasta que ele encontrar dentro de seu sistema

import os 
from itertools import count


caminho = os.path.join("C:\\Users", 'luizotavio', 'Desktop', 'EXEMPLO')

counter = count()

for root, dirs, files in os.walk(caminho): #vai percorrer por todo o conteúdo desse diretório
    the_counter = next(counter)
    print(" ",the_counter, "Pasta atual", root)

    for dir_ in dirs:
        print(' ', the_counter, "Dir", dir_)

    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_) #Vai declarar o caminho completo 
        print(' ', the_counter, 'FILE:', caminho_completo_arquivo)
        os.unlink(caminho_completo_arquivo) #Vai excluir todos os arquivos do diretório 
        #Não existe lixeira neste caso !!!!