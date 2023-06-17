# Emcapsulamento (modificadores de acesso: public, protected, private )
# Python Não TEM modificações de acesso
# Mas podemos seguir as seguintes convenções 
#    (sem underline) = public
#        pode ser usado em qualquer lugar
# _  (um underline) = protected
#         Só DEVE ser usado fora da classe
#         ou suas subclasses 
# __ (dois underlines) = private
#         "name mangling" (desfiguração de nomes) em Python
#         só DEVE ser usado na classe em que foi 
#         declarado

class Foo:
    
    def __init__(self):
        self.public = 'isso é público'
        self._protected = "isso é protegido"
        self.__exemplo = 'isso é private'

    def metodo_publico(self):
        self._metodo_protected()
        print(self._protected)
        return "metodo_publico"
    
    def _metodo_protected(self):
        print("_metodo_protected")
        return '_metodo_protected'
    
    def __metodo_private(self): #Eu não posso usar fora da classe.
        #Neste caso o próprio Python impede o usuário de fazer isso
        #Vai ocorrer a sua desfiguração de nome, fora da classe
        print("__metodo_private")
        return '__metodo_private'
    


f = Foo()
print(f._protected) #Em outras linguagens de progaramação, isso não seria possível 
print(f.metodo_publico())
