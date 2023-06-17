# if/ elif ....../ else 
# se / se não se/ se não 
entrada = input('Você quer "entrar" ou "sair"?')

if entrada == 'entrar':
    print ('Você entrou no sistema.')

elif entrada == 'sair':
    print ('Você saiu do sistema.')

else:
    print('Você não digitou nem entrar e nem sair.')

print ('Fora dos Blocos')
#Na hora de digitar a reposta de um input no terminal, NÃO pode colocar espaço, se não ele não reconhece as condições impostas (sempre cai no else)
    