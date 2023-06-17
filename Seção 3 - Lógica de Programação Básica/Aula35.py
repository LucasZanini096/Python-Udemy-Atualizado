"""
Repetições 
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim 
"""

qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
   coluna = 1
   while coluna <= qtd_colunas:
        print(f'{linha},{coluna}')
        coluna +=1
        linha += 1


print ('acabou')

#Comentários :
# 01 - Quando se formata um string, pode ser dessa maneira print(f'{linha=},{coluna=}')
# o sinal de igual depois da variável terá como resultado linha = 1 coluna = 1 e, assim por diante!!