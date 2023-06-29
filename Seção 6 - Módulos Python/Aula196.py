# string.Template para substituir variáveis em textos 
# Métodos:
# substitute: substiui mas gera erros se faltar chaves 
# safe_substitute: substitui sem gerar erros 
# Você pode trocar o delimitador e outras coisas criando uma subclasse
# de template
import locale 
import string as s
from datetime import datetime
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / "aula196.txt"

locale.setlocale(locale.LC_ALL, '')


def converte_para_brl (numero: float|int) -> str:
    brl = "R$" + locale.currency(val=numero, sybol=False, grouping=True)
    #Esse método consegue converter valores numéricos em valores monetários
    return brl

data = datetime(2022,12,28)
dados = dict (
    nome='João',
    valor=converte_para_brl(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa="O. M.",
    telefone= "+55 (11) 7890-5432"
)

#Posso mudar meu Delimitador 
class MyTemplate(s.Template):
    delimiter = "%"



with open(CAMINHO_ARQUIVO, "r") as arquivo:
    texto = arquivo.read()
    template = s.Template(texto) #Transformando em STR 
    print(template.substitute(dados)) #Vou substituir todos os dados
    # em que aparecem no texto com o nome da variável + $ pelo valor de sua variável 
    # em STR.
