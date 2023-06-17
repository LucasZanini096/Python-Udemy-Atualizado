#Method vs @Classmethod vs @Staticmethod
#method - self, método de instância 
# @classmethod - cls, método de classe 
# @staticmethod - método estático (Xself, Xcls)


class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self,password):
        self.password = password
    
    @classmethod
    def create_with_auth(cls, user, password):
        #return cls(user,password)
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def log(msg):
        print("LOG:", msg)



#c1 = Conection()
c1 = Connection.create_with_auth("Luiz","1234")
#c1.set_user("Lucas")
#c1.set_password("123")
print (c1.user) #Os atributos são salvos na memória a partir da chamada de um método, como neste caso 
print(c1.password)
print(Connection.log("Essa é a mensagem de log"))

#Qualquer método que eu for utilizar self
#Ele será considerado um método de instância          
       