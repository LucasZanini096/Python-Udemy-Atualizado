from dataclass import dataclass, field, fields


@dataclass
class Pessoa: 
  
  nome: str = field ( #Função que me permite configurar os campos de uma dataclasse
    defaut = "Missing"
  ) #Estou estabelecendo um valor padrão para a instância nome
  sobrenome: str 
  idade: int = 100 #Essa estrutura apenas funciona apenas com valores imutáveis !!
  enderecos: list[str] = field(defaut_factory=list)
  #Estou definindo o tipo lista em minha dataclass

   

if __name__ == "main":
  p1 = Pessoa()
  print(fields(p1)) #Me possibilita vizualizar os meta-dados da minha meta-classe 
  

  