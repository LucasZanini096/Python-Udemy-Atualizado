# dataclasses (syntax sugar) - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como


from dataclass import dataclass

@dataclass(frozen = True)
#Frozen -> não me permite setar coisas dentro dataclass. Isso é bom !!
#É mais correto configurar mais alguma coisa, em relação a modificar algo já existente
class Pessoa: 
  nome: str 
  sobrenome: str 

   

if __name__ == "main":
   p1 = Pessoa("Luiz", "Otávio")
   p2 = Pessoa("Luiz", 30)

print(p1==p2)


@dataclass(repr = True)
#Posso desativar o repr da minha classe
class Pessoa: 
  nome: str 
  sobrenome: str 

   

if __name__ == "main":
 lista = [Pessoa('A','Z'), Pessoa('B','Y'), Pessoa('C','X')]
 ordenadas = sorted(lista, reverse=False, key=lambda p: p.nome)
 print(ordenadas)