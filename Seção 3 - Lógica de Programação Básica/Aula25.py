"""""
Fatiamneto de strings 
012345678
 Olá mundo 
-987654321
Fatiamento [i:f:p] [::]/ i: início/f: fim/ p: de quanto em quanto vai ler a string/ [::] -> Vai ler toda a string 
Obs: a função len retorna a quantidade de caracteres da str
Obs1: "Para saber se tem espaço em uma palavra, digite if ' ' in "alguma coisa"
"""""""""
#Exercício
nome = input("Digite seu nome:")
idade = input("Digite sua idade:")
if len(nome) != 0 and len(idade) != 0:
    print (f'Seu nome é {nome}.')

    print ('Sua idade é %s' % (idade)) #Obs: Quando for colocar % não pode haver f' (f-string), pois ele não vai reconhcer 
    if ' ' in nome:
        print ('Seu nome possui espaços')
    else:
        print ('Seu nome não possui espaços')
    
    print(f'Seu nome invertido será:', nome[::-1])

    print (f'Seu nome tem:', len(nome), 'letras.')

    print (f'A primeira letra de seu nome é:', nome[0])

    print (f'A última letra do seu nome é:', nome[len(nome)-1])

else:
    print ("Desculpe, você deixou algum dos campos vazios.")


