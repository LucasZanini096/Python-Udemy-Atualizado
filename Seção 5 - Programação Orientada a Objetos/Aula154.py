# Context Manager com função - Criando e Usando gerenciados de contexto

from contextlib import contextmanager

@contextmanager #Função Decoradora que funcoina como um Context Manager 
def my_open(caminho_arquivo, modo):
    
    try: 
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding="utf8")
        yield arquivo    
    
    except Exception as e: #Estou tratando o erro

        print("Ocorreu erro," ,e)
    
    finally:
        print("Fechando arquivo")
        arquivo.close()

with my_open('aula150.txt', "w") as arquivo:
    arquivo.write("Linha 1\r\n")
    arquivo.write("Linha 1\r\n")
    arquivo.write("Linha 1\r\n")
