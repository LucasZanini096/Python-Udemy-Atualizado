class MyOpen:
    def __init__(self,caminho_arquivo,modo):
        self.caminho_arquivo = caminho_arquivo 
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('Abrindo Arquivo')
        self._arquivo = open(self.caminho_arquivo,self.modo, encoding="utf8")
        return self._arquivo
    
    def __exit__(self,class_exception,exception_,traceback_):
        print('FECHANDO ARQUIVO')
        self._arquivo.close()

        raise class_exception(*exception_.args).with_traceback(traceback_)

        #print(class_exception)
        # print(exception_)
        # #print(traceback_)
        # exception_.add_note('Minha nota') #Posso adicionar notas para exceptions



        return True #Tratei da Exceção / Quando há um raise, ele finaliza a função no raise, como o return

with MyOpen('aula152.txt',"w") as arquivo:
    arquivo.write("Linha 1\r\n")
    arquivo.write("Linha 2 \r\n")