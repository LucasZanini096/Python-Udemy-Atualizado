def soma(x,y):
    return x + y

def multiplica(x,y):
    return x * y

def criar_funcao(funcao, *args):
    return funcao(*args) #Neste caso vai chamar imediatamente a próxima função, havendo a não leitura do parâmetro 

multiplica_por_dez = criar_funcao(multiplica,10,5)
print(multiplica_por_dez)

#Solução 

def soma(x,y): #Essa linha se chama método ou assinatura da função
    return x + y

def multiplica(x,y):
    return x * y

def criar_funcao(funcao, *args):
    return funcao #não vou estar executando a função, porém perco o parâmetro 

multiplica_por_dez = criar_funcao(multiplica,10)
print(multiplica_por_dez)
print(multiplica_por_dez(1,10))

#Outra Solução 

def soma(x,y):
    return x + y

def multiplica(x,y):
    return x * y

def criar_funcao(funcao,*args):
    def interna(*args): #Pausa para a execução da função interna 
        return funcao(*args)
    return interna

soma_com_cinco = criar_funcao(soma,5)
multiplica_por_dez = criar_funcao(multiplica,10)
