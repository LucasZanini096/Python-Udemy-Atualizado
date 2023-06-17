# Polimorfismo em Python Orinetado a Objetos
# Polimorfismo é o princípio que permite que 
# classes derivadas de uma mesma superclasse 
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes 
# Assinatura do método = Mesmo nome e quantidade 
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Asssinatura do método: nome, parâmetros e retorno iguais 
# SO"L"ID
# Princípio da substituiçõa de Liskov 
# Objetos de uma superclasse devem ser substituíveis 
# por objetos de uma subclasse sem quebrar a aplicação 
# Sobrecarga de métodos (overload) 
# Sobreposisção de métodos (override) 

from abc import ABC, abstractmethod


class Notificacao: #Classes abstratas não podem instânciar objetos
    #Até o momento em que um método declarado como abstrato seja concreto em sua subclasse
    def __init__(self, mensagem):
        self.mensagem = mensagem 

    @abstractmethod
    def enviar(self) -> bool: ... #Type Anotattions -> defini o tipo de retorno
    #Indico para o meu desenvolvedor que esse método deve retornar um Boolean


class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print("E-mail: enviando", self.mensagem)
        return True

class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS: enviando - ', self.mensagem)
        return False 
    
    

def notificar(notificacao: Notificacao):   #Objeto polimórfico (Não sabe o objeto a ser declarado) 
    notificacao_envidada = notificacao.enviar()

    if notificacao_envidada:
        print('Notificação enviada')
    else:
        print('Notificação Não enviada')

