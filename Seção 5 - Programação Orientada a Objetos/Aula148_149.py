#Python Dunder Methods __repr__ e __str__
# Dunder = Duble Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __it__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self < other
# __neg__(self,) - -self
# __str__(self,) - str
# __repr__(self,) - str #Tipo de representação no Python

class Ponto:
    def __init__(self, x, y, z ="Qualquer coisa"):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self): #Chama unicamente uma str
        return f'({self.x}, {self.y})'

    def __repr__(self): #Mostra para o desenvolvedor como o objeto é montado 
        #O Fallback é o __repr__
        # class_name = self.__class__.__name__
        class_name = type(self).__name__
        return f'{class_name} (x={self.x!r}, y={self.y!r}, z={self.z!r})'
        #Neste caso, todas os tipos de objetos declarados como str's vão ser indicados com aspas simples 

p1 = Ponto(1,2)
p2 = Ponto(978,876)
print(p1)
print(repr(p2))
print(f'{p2!r}') #Estou chamando o __repr__ e não a str !!

