# Entendendo os seus próprios módulos Python 
# O primeiro módulo executado executado chama-se __main__
# Você pode importar outro módulo inteiro ou partes dele -> mas tem que estar na mesma pasta 
# O python conhece a pasta o __main__ está e as pastas abaixo dele
# Ele não reconhece pastas e módulos acima do __main__ por padrão 
# O python conhece todos os módulos e pacotes presentes nos caminhos de sys.path 

try: 
    import sys
    sys.path.append('/Users/luizotavio/Desktop/')
except ModuleNotFoundError:
    ... #ou pass

import Aula96_m  

print('Este módulo se chama', __name__) #O primeiro módulo excecutado pelo Python se chama __main__
print(*sys.path, sep='\n')

