import math

# velocidade
vel1 = 60
vel2 = 30
# tempo
time1 = 3
# time2 = x

def dPtoTime2(vel1, vel2, time1):
  return (vel1 * time1) / vel2
time2H = dPtoTime2(vel1, vel2, time1)

print(f"time2 vai chegar em seu destino em {time2H} horas")
# _________________________________________


def extrair_parte_fracionaria(numero):
    _, parte_fracionaria = math.modf(numero)
    return parte_fracionaria

# Testando a função
print(extrair_parte_fracionaria(10.78))  # Deve imprimir 0.78


timeMin = time2H - math.trunc()
