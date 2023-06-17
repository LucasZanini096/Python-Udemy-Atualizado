# Abstração 
# Log
# Herança - é um 

from pathlib import Path

LOG_FILE = Path(__file__).parent


class Log:
    def _log(self,msg): #Assinatura do método 
        raise NotImplementedError("Implemente o método log")
    
    def log_error(self,msg):
        return self._log(f'Error: {msg}')

    def log_success(Log):
        def _log(self, msg):
            return self._log(f'Sucess: {msg}')

class LogFileMixin(Log): #Indicar ao desenvolvedor para adicionar funcioanlidades na sua herança múltipla
    #Sendo que essas funcionalidades podem ser provindas de outras classes que são da família do Log    
      def _log(self,msg):
          msg_formatada = f'{msg} ({self.__class__.__name__})'
          print('Slavando no log:', msg_formatada)
          with open(LOG_FILE, 'a') as arquivo:
              arquivo.write(msg_formatada)
              arquivo.write('\r\n')




      def _log(self, msg): #Se eu modificar a assinatura desse método 
        #Eu posso quebrar um princípio da programação, denominado de Leskov Substitution Principal
        print(msg)
           
class LogPrintMixin(Log):
    def _log(self, msg):
        print(msg)
        print(f'{msg} ({self.__class__.__name__})')



if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('qualquer coisa')
    lp.log_success('Que Legal')
    lp = LogFileMixin()
    lp.log_error('Qualquer coisa')
    lp.log_sucess("Que legal")
    







