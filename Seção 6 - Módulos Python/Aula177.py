# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/stable/relativedelta.html
# https: //docs.python.org/3/library/datetime.html#timedelta-objects


from datetime import datetime, timedelta

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime("20/04/1987" "09:30:30", fmt)
data_fim = datetime.strptime('12/12/2022' "08:20:20", fmt)
print (data_fim > data_inicio)
delta = data_fim - data_inicio #Retorna um timedelta (um delta, de dias)
print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())
delta = timedelta(days=10, hours=2)
print(data_fim - delta)
