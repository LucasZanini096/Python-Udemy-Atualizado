#Funções decoradoras e decoradores
#Decorar = Adcionar / Remover / Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções 
# Decoradores são usados para fazer o Python 
# usar as funções decoradoras em outras funções 
#Funções dentro de funções permite realizar pausas dentro da execução de funções!!!!

def criar_funcao(func): #Função decoradora - > receber uma função para criar uma função interna
    def interna(*args, **kwargs):
        print ('Vou te decorar')
        for arg in args:
            e_string(arg) #Daqui ele vai par o inverte_string
        resultado = func(*args, **kwargs) #Func = inverte_string / Args = 123
        print(f'O seu resultado foi {resultado}')
        print('Ok, agora você foi decorada')
        return resultado
    return interna

def inverte_string(string):
    return string[::-1] #Meio para inverter strings !!!

def e_string(param):
    if not isinstance(param, str):
        raise TypeError ("param deve ser uma str")


invertida = inverte_string('Luiz')
print(invertida)

inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string_checando_parametro('123')
print(invertida)
