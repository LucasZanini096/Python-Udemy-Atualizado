# isistance - para saber se objeto é de determinado tipo

lista = [
    'a', 1 , 1.1, [0,1,2], (1,2),
    {0,1}, {'nome': 'Luiz'},
]

set()
for item in lista:
    if isinstance(item,set):
        print("SET")
        item.add(5) #Só pode ações de set depois de 'isistance' configurado como set
        print(item, isinstance(item,set))
    
    elif isinstance(item,str):
        print("STR")
        print(item.upper(), isinstance(item,set))


    elif isinstance(item, (int,float)):
        print('NUM')
        print(item, item*2)
    else:
        print("OUTRO")
        print(item)    