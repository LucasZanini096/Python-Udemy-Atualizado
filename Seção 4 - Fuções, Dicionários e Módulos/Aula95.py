# Modulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import name_modulo
# Vantagens: você tem o namespace do módulo 
# Desvatagens: nomes grandes 

import sys
platform = "A MINHA"
print(sys.platform)
print(platform)


#partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos 
# Desvantagens: Sem o namespace do módulo 

#from sys import exit, platform #Cuidado: Eu posso sobrescrever sobre algum nome. Neste caso, estou sobrescrevendo o platform

print(platform)



# alias 1 - import nome_modulo as apelido
import sys as s
sys = 'alguma coisa'
print (s.platform)

# alias 2 - from nome_modulo import objeto as apelido 
from sys import exit as ex
from sys import platform as pf

print(sys.pf)

# Vantagens: você pode reservar nomes para seu código 
# Desvantagens : pode ficar fora do padrão da linguagem 

# Má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo 
# Desvantagens: importa tudo de um módulo 
from sys import * #Está importando todos os módulos do sys -> Algo ruim -> Deixa obscuro

print(platform)
exit()

