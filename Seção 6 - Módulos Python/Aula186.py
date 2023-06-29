# os + shutill - Mover, copiar e apagar arquivos
# Mover/Renomear -> shutill.move
# Mover/Renomear -> os.rename 
# Copiar -> shutill.copy 
# Apagar Árvore recursivamente -> shutill.rmtree
# Copiar Árvore recursivamente -> shutill.copytree
# Apagar arquivos -> os.unlink


import os 
import shutil


HOME = os.path.expanduser('~') #Me devolve o caminho até a Home do usuário 
DESKTOP = os.path.join(HOME, "Desktop")
PASTA_ORIGINAL = os.path.join(DESKTOP, "EXEMPLO")
NOVA_PASTA = os.path.join(DESKTOP, "NOVA_PASTA")

#os.unlink(NOVA_PASTA) #Quero apagar uma pasta que esteja vazia
#Porém se eu queiser apagar uma pasta de maneira recursiva, eu devo usar este método:
shutil.rmtree(NOVA_PASTA, ignore_errors=True)


shutil.copytree(PASTA_ORIGINAL,NOVA_PASTA) #Posso copiar os arquivos de uma pasta para outra 
#, sendo que esta última não existe !!! Apenas devo informar caminho de ambas as pastas

shutil.move(NOVA_PASTA, NOVA_PASTA + "_EITA" ) #stou renomeando meu arquivo 