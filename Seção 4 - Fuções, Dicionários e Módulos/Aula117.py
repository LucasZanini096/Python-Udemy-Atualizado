
import json

# JSON(JavaScript Object) => Suporta mais de uma linguagem de programação para a armazenagem de dados 
#No JSON eu posso armazenar apenas Dados, ou seja, eu não posso armazenar funções, clases, sets e entre outros elementos.
#Por padrão ele utiliza o sistema de codificação Asc

#pessoa = {
#
#    "nome" : "Lucas ",
#    "sobrenome" : "Zanini",
#    "endereços" : [
#        {"rua" : "R1", "numero" : 32},
#        {"rua" : "R2", "numero" : 55},
#    ],
#    "altura" : 1.8,
#    "numeros_preferidos" :(2,4,6,8,10),
#    "dev" : True,
#    "Nada" : None,


#}


#with open("arquivo_Json.json", "w+", encoding="utf8") as arquivo: 
    
#    json.dump(
#        pessoa, 
#        arquivo, ensure_ascii=False, #Palavra chave que permite eu não utilizar a codificação Asc
#        indent=2, #Palavra chave que permite formatar corretamente um determinado objeto 
    
#    ) #O método dump permite eu armazenar um determinado dados/objeto no Json
    #Existe o método .dumps, na qual transforma o objeto armazenado no Json em STR 


with open("arquivo_Json.json", "r", encoding="utf8") as arquivo:
    pessoa = json.load(arquivo) #O método .load carrega os objetos/dados de um arquivo Json
    print(pessoa["nome"])
    print(type(pessoa))


    


