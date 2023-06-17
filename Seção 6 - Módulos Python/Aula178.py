

import calendar

print(calendar.calendar(2022)) #Recebo todo o calendário do ano declarado no parâmetro
print(calendar.month(2022,12)) #Primeiro passo o ano e depois e mês 

print(calendar.monthrange(2022,12)) #Assim como calendar.month(), 
#eu tenho que passar o ano e o mês, para saber qual é o último dia do mês.

#Saída : (3,31)
#Primeiro valor: número que representa o dia da semana 
#Segundo valor: número que representa o último dia do mês

print(list(enumerate(calendar.day_name)))
#Retorna uma lista com os dias da semana (0-segunda | 6-domingo)


numero_primeiro_dia, ultimo_dia = calendar.monthrange(2022,12) #Retorna uma tupla com o primeiro e último dia do mês
print(calendar.day_name[numero_primeiro_dia]) #Retorna o dia da semana de determinada data
print(calendar.day_name[calendar.weekday(2022,12,ultimo_dia)])

#calendar.weekday() -> Retorna o dia do mês


for week in calendar.monthcalendar(2022,12): #Retorna todos as semanas do mês, em forma de lista
    print(list(enumerate(week)))

for week in calendar.monthcalendar(2022,12):
    for day in week:
        if day == 0:
            continue
        print(day)

