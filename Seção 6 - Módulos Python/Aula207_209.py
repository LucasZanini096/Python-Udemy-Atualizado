# PyPDF2 - Para manipular arquivos PDF
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir 
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair textos e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2
# Link: https://pypdf2.readthedocs.io/en/3.0.0/

from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / "pdfs_originais"
PASTA_NOVA = PASTA_RAIZ / "arquivos_novos"

RELATORIO_BACEN = PASTA_ORIGINAIS / "R20230623.pdf"

PASTA_NOVA.mkdir(exist_ok=True) #Criando uma pasta nova 

reader = PdfReader(RELATORIO_BACEN) #Abrindo o PDF

#print(len(reader.pages))

#for page in reader.pages:
#    print(page)


page0 = reader.pages[0]



#print(page0.extract_text())
#print(len(page0.images))

#Extraindo em colocando uma imagem em numa nova pasta


#for i in range (len(page0.images)):
#    imagem = page0.images[i]

#    with open(PASTA_NOVA/ imagem.name, "wb") as fp:
#        fp.write(imagem.data)


#writer = PdfWriter()
#writer.add_page(page0)

#with open(PASTA_NOVA / 'page0.pdf', 'wb') as arquivo:
#    writer.write(arquivo)


#SEPARANDO PDFS

for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(PASTA_NOVA/ f'page{i}.pdf', "wb") as arquivo:
        writer.add_page(page)
        writer.write(arquivo)


merger = PdfMerger()

files = [
    PASTA_NOVA / 'page0.pdf',
    PASTA_NOVA / 'page1.pdf'
]

for file in files:
    merger.append(file)

merger.write(PASTA_NOVA / 'Merged.pdf')
merger.close()
