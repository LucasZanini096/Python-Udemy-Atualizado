#Variaveis livres +  nonlocal (locals, globals)


print(globals()) #Nomeia todas as variaveis globais 
def fora(x):
    a = x #Variável livre -> não está definida dentro do escopo dentro 

    def dentro(): #Essa função não está definida na mesma função, mas sim dentro da função fora
        print(locals()) #Locals nomeia as variaveis livres dentro de um escopo -> o que pode ser acessado 
        print(dentro.__code__.co_freevars)
        return a
    return dentro 




dentro1 = fora(10)
dentro2 = fora(20)

print(dentro1())
print(dentro2())


def concatenar(string_inicial):
    valor_final = string_inicial #valor_final é do escopo concatenar e não de interna 
    
    def interna(valor_a_concatenar):
        nonlocal valor_final #Vai buscar a essa variável no escopo de cima - podendo alterar a variavel livre
        valor_final += valor_a_concatenar
        return valor_final
    return interna

c = concatenar('a')
print(c)
 