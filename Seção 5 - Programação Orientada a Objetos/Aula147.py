# Criando Exceptions em Python Orientado a Objetos 
# Para criar uma Exeption em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception 

#Criando exceções (comum colocar Error ao final)
# Levantado (raise) / Lançando (throw) exceções
# Relançando exceções 
# Adicionando notas em exceções (3.11.0)

class MeuError(Exception):
    ...



def levantar():
    exception_ = MeuError('a','b','c')
    raise exception_

try:
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)