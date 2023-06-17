class Ponto:
    def __init__(self, x, y):

        self.x = x
        self.y = y


    def __str__(self): #Chama unicamente uma str
        return f'({self.x}, {self.y})'

    def __repr__(self): #Mostra para o desenvolvedor como o objeto é montado 
        #O Fallback é o __repr__
        # class_name = self.__class__.__name__
        class_name = type(self).__name__
        return f'{class_name} (x={self.x!r}, y={self.y!r}, z={self.z!r})'
        #Neste caso, todas os tipos de objetos declarados como str's vão ser indicados com aspas simples 
     
    def __add__(self,other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y) #Fábrica de novos objetos 
    
    def __gt__(self,other):
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y
        return resultado_self > resultado_other 



p1 = Ponto(1,2)
p2 = Ponto(978,876)
p3 = p1 + p2
print("P1 é maior que P2", p1 > p2) 

