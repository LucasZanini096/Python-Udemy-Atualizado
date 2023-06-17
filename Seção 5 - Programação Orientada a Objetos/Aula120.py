# class - Classes são moldes para criar novos objetos 
# As classes geram novos objetos (instâncias) que 
# que podem ter seus próprios atributos e métodos
# Os objetos gerados pela classe podem ser udar seus dados 
# internos para realizar várias ações
#Por convenção, usamos PasvcalCase para nomes de classes.
#PascalCase -> Coloca e separa toda palavra com a letra maiúscula
#Há o CamelCase, mas não existe no Python. Nele ele separa toda a palavra com a letra Maiúscula

string = "Luiz"
print(string.upper())
print(isinstance(string,str))

#Função class permite eu criar uma classe em Python 

class Pessoa: #PascalCase sendo utilizado
    ...

p1 = Pessoa() #Esse elemento está sendo associado à Classe Pessoa 
print(p1)

p1.nome = "Luiz" #Declaração de um atributo -> Relacionando com um dado/valor distinto 
p1.sobrenome = "Otávio"

print(p1.nome)
print(p1.sobrenome)
