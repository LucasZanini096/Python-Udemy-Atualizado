# count é um interador sem fim (itertools) -> Infinito

from itertools import count 

c1 = count(step=8,start=8) #Só posso passar o início
r1 = range (10) #Não é um iterator

print('c1', hasattr(c1, '__iter__')) #True
print('c1', hasattr(c1, '__next__')) #True
print('r1', hasattr(r1, "__iter__")) #True
print('r1', hasattr(r1,'__next__'))  #False

print("count")
for i in c1:
    if i >= 100:
        break
    print(i)
print()

print('range')
for i in r1:
    print(i)


#for i in c1:
#    ...