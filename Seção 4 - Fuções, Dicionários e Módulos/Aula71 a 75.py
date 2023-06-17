#Sets - Conjuntos em Pyhton (tipo set)
#Conjuntos são ensinados na matemática 
#Representamos graficamente pelo diagrama de Venn 
#Sets em Python são mutáveis, porém aceitam apenas 
#tipos imutáveis como valor interno 

#Criando um set 
#set(iterável) ou {1,2,3}
s1 = set() #vazio
s1 = {'Luiz',1, 2 ,3} #com dados
print(s1)

#Parecido com o dicionário, mas sem as chaves 
#Sets são eficientes para remover valores duplicados 
#de iteráveis
# - eles não tem indexes;
# - Não aceitam dados mutáveis (dicts, sets ou listas)
# - eles não garantem ordem; !!!
# - eles são iteráveis(for, in ,not in) 

s1 = {1,2,3,3,3,3,1}
print(s1) #printou apenas {1,2,3}
l1 = [1,2,3,3,3,3,1] 
s1 = set(l1)
l2 = list(s1)
print(l2)


s1 = {1,2,3}
# print(3 not in S1)
# for número in s1:
#     print(numero)


#Métodos úteis:
# add (só aceita a inserção de um valor por vez), update, clear, discard
s1 = set()
s1.add('Luiz')
s1.add(1)
s1.update(('Olá mundo', 1,2,3,4))
#s1.clear()
s1.discard("Olá Mundo")
s1.discard('Luiz')
print(s1)


#Operadores úteis:
#união | união (union) - Une
# interseção & (intersection) - Itens presentes em ambos 
# diferença - Itens presentes no set da esquerda 
# diferença simétrica ^ - Itens que não estão em ambos 
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
print(s3)
s3 = s1 & s2
print(s3)
s3 = s1 - s2
print(s3)
s3 = s1 ^ s2 #retorna aos itens exclusivos de cada set