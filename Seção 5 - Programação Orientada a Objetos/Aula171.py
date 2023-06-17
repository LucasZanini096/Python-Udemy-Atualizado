# namedtuples - tuplas imutáveis com nomes para valores
# Usamos naedtuples para criar classes de objetos que são apenas um agrupamento de atributos
#como classes normais sem métodos, ou registros, ou registros de bases de dados, etc.
# As namedtuples são imutáevis assim como as tuplas 

from typing import NamedTuple
from collections import nametuple 

#Carta = nametuple(
#  "Carta", ["valor", "naipe"],
#  defaults = ["Valor", "Naipe"] #Estou declarando valores padrão
#)
#Estou instanciando o self com os atributos valor e naipe 
#Classe Carta

as_espadas = Carta("A")
print(as_espadas._asdict())
print(as_espadas)
print(as_espadas.naipe)
print(as_espadas.valor)
print(as_espadas[1])
print()
print(as_espadas._field)
print(as_espadas._field_defaults)

for valor in as_espadas:
  print(valor)




class Carta(NamedTuple): #DataClass
  valor: str = "VALOR"
  naipe: str = "NAIPE"

  