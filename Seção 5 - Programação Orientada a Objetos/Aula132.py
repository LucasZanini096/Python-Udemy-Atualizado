# No Setter você quer passar por um método para configurar determinado atributo
# Pode evitar quebrar algumas coisas 
#Getter -> obter um valor 
#Métodos não salvam valores, apenas executam ações
#Atributos que começar com um ou dois underlines 
#não devem ser usados fora da classe



class Caneta:
    def __init__(self, cor):
        self._cor = cor
        self._cor_tampa = None
        #Refere-se a minha Property
        #Este atributo é protegido pela classe (interno). Não pode ser usado 

    @property
    def cor(self): #Pode usar isso
        print("PROPERTY")
        return self._cor #Não pode usar isso 
    
    @cor.setter #Permite restringir determinadas coisas que eu não quero que ocorra
    #Permitir atribuir um valor ao self (instância)
    def cor(self, valor):
        if valor == "Rosa":
            raise ValueError("Alcides não gosta de rosa - Pau no seu Código")

        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self,valor):
        self.cor_tampa = valor


def mostrar(caneta):
    return caneta.cor



caneta = Caneta('Azul')
caneta.cor = 'Rosa' #Está errado, pois Property é um método e não um atributo
#Porém depois da declaração do setter, está certo essa estrtura
print(caneta.cor)
print(caneta.cor_tampa)
