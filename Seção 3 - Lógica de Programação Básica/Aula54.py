"""
Listas de listas e seus índices 
"""
salas = [
    # 0
    ['Maria', 'Helena' , ], #0
    # 0
    ['Elaine', ], # 1
    # 0       1      2
    ['Luiz', 'Joao', 'Eduarda', (0,10,20,30,40)], #2
]

print(salas)
print(salas[1])
print(salas[1][0]) #Cada lista interna a lista salas, possui um ínidce próprio, assim como os objetos dentro dessas listas 
print(salas[2][2])
print(salas[2][3][2])

for sala in salas:
    print (f'A sala é {sala}')
    for aluno in sala:
        print (aluno)


