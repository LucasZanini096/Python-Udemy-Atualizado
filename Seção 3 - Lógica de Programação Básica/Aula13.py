a = 'A'
b = 'B'
c = 1.1
string = 'a={} b={} c={:.2f}'
string1 = 'b ={1} a = {0} a = {0} a={0} c = {2:.2f}' 
formato = string.format(a,b,c) #Há a presença de índices (a = 0, b = 1, c = 2), mas nem sempre são confiveis!!
# (a,b,c) = Parâmetro nomeado 
# Parâmetro nomeado = dar nome as coisas que estão dentro da chamada da função 
formato1 = string1.format(a,b,c)

print (formato)
print (formato1)
string2 = 'b={nome2} a= {nome1} a={nome1} c={nome3:.2f}'
formato2 = string.format(nome1=a, nome2=b, nome3=c)
print (formato2)