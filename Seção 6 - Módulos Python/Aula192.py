# csv.reader e cvs.DictReader
# csv.reader lê o CSV em formato de lista 
# csv.DictReader lÊ o CSV em formato de dicionário

import csv
from pathlib import Path


CAMINHO_CSV = Path(__file__).parent / "aula1192.csv" #Vou obter o camingho do arquivo

with open(CAMINHO_CSV, "r") as arquivo:
    leitor = csv.DictReader(arquivo) #Abro o arquivo como um dicionário 

    for linha in leitor:
        print(linha['Nome'], linha["Idade"])

with open(CAMINHO_CSV, "r") as arquivo_2:
    leitor = csv.reader(arquivo) #abre o arquivo como uma lista 

    for linha in leitor:
        print(linha)

