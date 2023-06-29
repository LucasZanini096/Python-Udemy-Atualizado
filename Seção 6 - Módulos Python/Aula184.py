# os.path.getsize e os.start para dados dos arquivos

import math
import os 
from itertools import count


def formata_tamanho(tamanho_em_bytes: int, base:int = 1000) -> str:
    #Formata um tamanho, de bytes para o tamanho apropriado


    #Se o tamanho for menor ou igual a 0, 0B:

    if tamanho_em_bytes <=0:
        return "0B"
    
    #Tupla com tamanhos 
    #                      0    1     2     3     4     5      
    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"
    #math.log vai retornar o logaritmo de tamanho_em_bytes
    #com a base (1000 por padrão), isso deve bater
    #com o nosso índice na abreviação dos tamanhos
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))
    # Por quanto nosso tamanho deve ser dividido para
    # gerar o tamanho correto 
    potencia = base ** indice_abreviacao_tamanhos
    #Nosso tamanho final 
    tamanho_final = tamanho_em_bytes / potencia
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f"{tamanho_final:.2f} {abreviacao_tamanho}"

caminho = os.path.join("C:\\Users", 'luizotavio', 'Desktop', 'EXEMPLO')

counter = count()

for root, dirs, files in os.walk(caminho): #vai percorrer por todo o conteúdo desse diretório
    the_counter = next(counter)
    print(" ",the_counter, "Pasta atual", root)

    for dir_ in dirs:
        print(' ', the_counter, "Dir", dir_)

    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_) #Vai declarar o caminho completo 
        #tamanho = os.path.getsize(caminho_completo_arquivo) #Obtém o tamanho de um arquivo
        stats = os.stat(caminho_completo_arquivo) #Vou pegar os todos os dados do arquivo
        tamanho = stats.st_size #Vou pegar o tamanho do arquivo
        print(' ', the_counter, 'FILE:', file_, formata_tamanho(tamanho))
        #os.unlink(caminho_completo_arquivo) #Vai excluir todos os arquivos do diretório 
        #Não existe lixeira neste caso !!!!