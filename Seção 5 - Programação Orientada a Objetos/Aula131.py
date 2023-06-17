# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# modo pythônico - modo do Python de fazer coisas 
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um atributo
# Geralmente é usada nas seguintes situações:
# - como getter 
# p/ evitar quebrar código cliente 
# p/ habilitar setter 
# p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código


class Caneta:
    def __init__(self, cor):
        self.cor = cor
    

    def get_cor(self): #Getter -> Tipo um local de teste 
        print("Estou dentro do Getter")
        return self.cor #Estou protegendo meu atributo 
    #Isso me possibilita realizar modificações neste atributo, sem mudar muitas linhas de código
             

#########################################

caneta = Caneta("Azul")
print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())



class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor
    

    @property #É um decorator 
    #É um método que sem comporta como um atibuto
    #Tanto que o chamamos por meio da sintaxe de um atributo <objeto.nome_atributo>
    #Outra maneira de proteção
    def cor(self):
        print("PROPERTY")
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        return 123456
    

             

#########################################

print(caneta.cor)
print(caneta.cor)
print(caneta.cor_tampa)