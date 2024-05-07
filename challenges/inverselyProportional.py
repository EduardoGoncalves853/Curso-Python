import math

# velocidade
vel1 = 70
vel2 = 20
# tempo
time1 = 3 #*horas
# time2 = x #*horas

def dPtoTime2(vel1, vel2, time1):
  return (vel1 * time1) / vel2

dPtimeRES = dPtoTime2(vel1, vel2, time1) # inteiro.decimal
print(f"{dPtimeRES} horas")

num_truc = math.trunc(dPtoTime2(vel1, vel2, time1))
timeMin = (dPtimeRES - num_truc) *100 # minutos

print(f"time2 vai chegar em casa em {dPtimeRES} horas e {timeMin} minutos")
# _________________________________________