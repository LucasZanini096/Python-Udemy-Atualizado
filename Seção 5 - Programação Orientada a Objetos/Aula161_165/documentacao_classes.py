
class Foo:
    def soma(self, x: int | float, y: int | float) -> int | float:
        #Vou descrever o funcionamento dessa função (um tipo)
        """
        Soma x e y

        :param x: Número 1
        :type x: int or float
        :param y: Número 2
        :type y: int or float

        :return: A soma entre x e y
        ;rtypr: int ou float
        """

        return x + y

    def multiplica(
            self,
            x: int | float,
            y: int | float,
            z: int | float | None = None        
    ) -> int | float:
        

        if z is None:
            return x * y
        return x * y * z
                
    """Multiplica x,y,z e/ou z

     Multiplica x e y. Se z for enviado, multiplica x,y,z. 
    """
        
        
    def bar(self) -> int:
        """O que ele faz

        :raises NotImplementedError: Se o método não for definido
        :raises ValueError: Se o método não for definido
        """
        raise NotImplementedError("Teste")


        

       

    variavel_2 = 2
    variavel_3 = 3
    variavel_4 = 4

