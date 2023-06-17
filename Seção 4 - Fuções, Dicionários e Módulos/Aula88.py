# Generetor expression, Iterables e Iterators em Python
iterable = ['Eu','Tenho', '_iter_']
iterator = iter(iterable)
print(next(iterator)) #Retorna apenas o próximo item do iterador !!!
print(next(iterator)) #lembre-se que o for também possui um iterator
print(next(iterator))