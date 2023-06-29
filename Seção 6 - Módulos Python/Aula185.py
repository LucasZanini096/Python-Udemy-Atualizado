# os + shutill - Mover, copiar e apagar arquivos
# Mover/Renomear -> shutill.move
# Mover/Renomear -> os.rename 
# Copiar -> shutill.copy 
# Apagar -> os.unlink
# Apagar diretório recursivamente -> shutil.rmtree

import os 
import shutil


HOME = os.path.expanduser('~') #Me devolve o caminho até a Home do usuário 
DESKTOP = os.path.join(HOME, "Desktop")
PASTA_ORIGINAL = os.path.join(DESKTOP, "EXEMPLO")
NOVA_PASTA = os.path.join(DESKTOP, "NOVA_PASTA")

os.makedirs(NOVA_PASTA, exist_ok=True) #Vou criar a nova pasta 
#Exist_ok me permite executar o programa sem erro, caso a pasta já exista

for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        caminho_novo_diretorio = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
        ) #Root é uma str, pois é aplicado o método replace !!!!
        os.makedirs(caminho_novo_diretorio, exist_ok=True) #Criando sub-diretórios na nova pasta
    
    
    for file in files:
        caminho_arquivo = os.path.join(root,file) #Adcionando o root e file no 
        caminho_novo_arquivo = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
        )
        shutil.copy(caminho_arquivo,caminho_novo_arquivo) #Fazendo a cópia de uma pasta para outra !!!
