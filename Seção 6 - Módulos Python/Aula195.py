# secrets gera números aleatórios seguros 
import secrets
import string as s
from secrets import SystemRandom as Sr

# Geração de senha aleatória 

print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k = 5)))

random = secrets.SystemRandom()

# Funções:
# seed #Neste caso, ele não faz nada !!
#   -> Inicializa o gerador de random (por isso "números pseudoaletórios ")

random.seed() #O módulo random está sendo inicializado 


# random.randrange(início, fim, passo)

r_range = random.randrange(10,20,2)
print(r_range)

#   -> Gera um número inteiro aleatório dentre de um intervalo específico 
# random.randint(início,fim)

r_int = random.randint(10,20) #O último número do range vai ser incluido !!
print(r_int)

# random.uniform(início,fim)
#    -> Gera um número flutuante aleatório dentro de um intervalo "sem passo"

r_uniform = random.uniform(10,20)
print(r_uniform)

# random.shuffle(SequênciaMutável) -> Embraralha a lista original
nomes = ["Luiz","Maria","Helena","Joana"]
random.shuffle(nomes)
print(nomes)

# ramdom.sample(Iterável, k=N)
#  -> Escolhe elementos doiterável e retorna outro iterável (não repete)
novos_nomes = random.sample(nomes, k=2) #Neste caso estpou escolhendo apenas 2 elementos da lista 
print(nomes)
print(novos_nomes)

# random.choices (Iterável, k=N)
#    -> Escolhe elementos do iterável e retorna outro iterável (repete valores)

novos_nomes_2 = random.choices(nomes, k=3)
print(novos_nomes_2)

# random.choice(Iterável) -> Escolhe um elemento do iterável
print(random.choice(nomes))
