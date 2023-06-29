from threading import Thread
from time import sleep


class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
    
    def comprar(self,quantidade):
        if self.estoque < quantidade:
            print("Não temos ingressos suficientes")
            return 

        sleep(1)    

        self.estoque -= quantidade 
        print(f'Você comprou {quantidade} ingresso(s).'
              f'Ainda temos {self.estoque} em estoque.')
        
if __name__ == "__main__":
    ingressos = Ingressos(10) #Instanciando a classe

    for i in range (1,20):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()
