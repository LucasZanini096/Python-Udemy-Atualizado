"""
CONSTANTE = "Variáveis" que não vão mudar -> variáveis com letras maiusculas nao vão mudar !! (Constante)
Mutas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
Obs: Complexidade e não clareza é ruim !!
"""

velocidade = 661 #velocidade atual do carro 
local_carro = 101 #local em que um carro está na estrada 

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # lcoal onde o radar 1 está 
RADAR_RANGE = 1 # A distância onde o radar pega 

vel_carro_pass_radar_1 = velocidade > RADAR_1
diferanca_Local_Radar = LOCAL_1 - RADAR_1
soma_Local_Radar = LOCAL_1 + RADAR_RANGE
carro_passou_radar_1 = local_carro >= diferanca_Local_Radar  and \
    local_carro <= soma_Local_Radar
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1



if vel_carro_pass_radar_1:
    print ('Velocidade passou do radar 1')

if carro_passou_radar_1:
    print ('Carro passou pelo radar 1')

if carro_multado_radar_1:
    print ('Carro multado em radar 1')
    


