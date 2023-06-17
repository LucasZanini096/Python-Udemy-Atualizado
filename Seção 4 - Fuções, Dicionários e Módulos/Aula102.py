#Funções decoradoras e decoradores
#Decorar = Adcionar / Remover / Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções 
# Decoradores são usados para fazer o Python 
# usar as funções decoradoras em outras funções 

def criar_funcao(func): #Função decoradora - > receber uma função para criar uma função interna
    def interna(*args, **kwargs):
        print ('Vou te decorar')
        for arg in args:
            e_string(arg) 
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}')
        print('Ok, agora você foi decorada')
        return resultado
    return interna

@criar_funcao #Usar a função criar_funcao dentro da função inverte_string -> Usando o decorador neste caso -> Vai realizar todo o processo 
def inverte_string(string):
    print(f'{inverte_string.__name__}') #A função printada neste caso vai ser interna 
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError ("param deve ser uma str")


invertida = inverte_string('Luiz')
print(invertida)


invertida = inverte_string("123")
print(invertida)

#Toda função é objeto no Python 
