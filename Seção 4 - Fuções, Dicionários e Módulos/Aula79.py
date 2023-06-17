#Empacotamento e desempacotamento de dicionários 
a,b = 1,2
a,b = b,a
print(a,b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

a,b = pessoa.values()
print(a,b)

a,b = pessoa.items()
print(a,b)

(a1,a2), (b1,b2) = pessoa.items()
print(a1,a2)
print(b1,b2)

for chave, valor in pessoa.items():
    print(chave,valor)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,

}

pessoa_completa = {**pessoa, 'chave' : 1}
#Os dois asteriscos extrai um dicionário por inteiro para ser colocado em outro, 
# empacotando-o
pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)


def monstro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave,valor in kwargs.items():
        print(chave,valor)

monstro_argumentos_nomeados(nome='Joana', qlq=123)
monstro_argumentos_nomeados(**pessoa_completa)




