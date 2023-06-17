# raise - lançando exceções (erros) -> Reelançar as exceções
# Essa ferramenta permite eu criar e modificar erros (o texto em que aparece no terminal)

def nao_aceito_zero(d):

    if d == 0:
        raise ZeroDivisionError(f'Você está tentando dividir por zero') #Depois do raise devo escrever o tipo do erro e depois colocar uma str com um  texto meu
    return True 

def nao_aceito_str(n):

    tipo_n = type(n)
    
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser do tipo int ou float.'
            f'"{tipo_n.__name__}" enviado'

        )
    return True

def divide(n,d):
    nao_aceito_zero(d)
    nao_aceito_str(n)
    nao_aceito_str(d)
    return n / d

print(divide(8,"0"))
