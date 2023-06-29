#os.listdir para navegar em caminhos
# C:\Users\luizotavio\Desktop\EXEMPLO
#caminho = r'C:\\Users\\luizotavio\\Desktop\\Exemplo'

import os 

caminho = os.path.join("C:\\Users", 'luizotavio', 'Desktop', 'EXEMPLO')

for pasta in os.listdir(caminho): #Permite acessar um determinado diretório 
    caminho_completo_pasta = os.path.join(caminho,pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue

    for imagem in os.listdir(caminho_completo_pasta):
        print(imagem)

#Isso me permite listar os componentes de meu diretório 