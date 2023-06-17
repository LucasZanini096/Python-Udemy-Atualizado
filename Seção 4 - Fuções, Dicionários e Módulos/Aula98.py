import importlib

import aula98_m


print(aula98_m.variavel)

#for i in range(10):
#    print(i)
#    import aula98_m  -> Só vai executar apenas 1 vez o import 

for i in range(10):
    importlib.reload(aula98_m)
    print(i)

print('Fim')
