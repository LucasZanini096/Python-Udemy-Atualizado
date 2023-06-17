"""
Repetições 
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim 
"""
contador = 0

while contador <= 10:
    contador += 1
    print(contador)


    if contador == 6:
        #print(f'Não vou mostrar o seis.')
        continue #Bate no continue e volta para o início do laço, ou seja, vai ignorar a contagem do 6 neste caso (PULOU DETERMINADO NÚMERO OU SEQUÊNCIA)

    if contador == 40:
        break #Sai do laço, termiando as repetições !!!

print ('Acabou')

#OBS: Os comandos Break e Continue funcionam apenas para o While/Laço mais próximo !!!