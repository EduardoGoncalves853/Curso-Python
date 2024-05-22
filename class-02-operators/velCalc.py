# Velocidade = Distância / Tempo

DistanceMkm = input(
    '''
    digite 'km' para Distância em km
    digite 'm' para Distância em m
    ''')

# Se a distância requerida for em metros
if DistanceMkm.lower() == 'm':
    distanceM = float(input("Agora digite a distância em metros: " ))
    Time = float(input("Agora digite o tempo em minutos: "))
    vel = distanceM / Time
    print(f'''
          v = {distanceM} / {Time}
          ''')
    
# Se a distância requerida for em kilômetros
elif DistanceMkm.lower() == 'km':
    distancekm = float(input("Agora digite a distância em kilômetros: "))
    Time = float(input("Agora digite o tempo em horas: "))
    vel = distancekm / Time
    print(f"A sua velocidade é de {vel}km/h")


