# dataclasses (syntax sugar) - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr()__, __eq__() (entre outros) em classes definidas pelo usuário
# Em resumo: dataclasses são syntax sugar para criar classes normais.

from dataclass import dataclass

@dataclass(init=False) #É uma função decoradora !!
class Pessoa: #Neste caso eu só preciso declarar os atributos
  nome: str #Declaro o tipo de objeto a ser instânciado 
  sobrenome: str 

  def __post_init__(self):
   self.nome_completo = f'{self.nome} {self.sobrenome}'  #Método que é chamado logo após o termino do __init__ da dataclass. Se eu declarar um __init__ próprio, ele não será chamado. 


  
  @property
  def nome_completo(self):
    return f'{self.nome} {self.sobrenome}'


  @nome_completo.setter
  def nome_completo(self,valor):
    nome,*sobrenome = valor.split()
    self.nome = nome
    self.sobrenome = "".join(sobrenome)
    
   

if __name__ == "main":
   p1 = Pessoa("Luiz", "Otávio")
   p2 = Pessoa("Luiz", 30)

print(p1==p2)