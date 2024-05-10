
# Algoritmo para calcular o
# número de algarismos multiplos
# de algum número

#*  m = múltiplos
#*  n = Valor inicial
#*  d = dígitos

# Fórmula
#* n => td => d1
#* a => a * x = ax
#* d = d1 + ax

# Uso dele
# x = nd / m
# >100 % 4

#* 262 => 98 => 94
#* 164 => 164 * 1.5 = 246
#* 340 = 94 + 246

# código time ↓
import time

# Meu código ↓
start_time = time.time()




def countAlg():
    valor_maximo = int(998)
    razao = int(2)
    multiplos = [i for i in range(razao, valor_maximo + 1, razao)]
    multiplos_str = ''.join(str(multiplo) for multiplo in multiplos)
    return [valor_maximo, multiplos_str, razao]
algCheck = countAlg()

print("--- %s seconds ---" % (time.time() - start_time))

print(f"{algCheck[0]} tem {len(algCheck[1])} dígitos dentre os múltiplos de {algCheck[2]}")
#! important
def contar_digitos(numero):
    numero_str = str(numero)
    return len(numero_str)

nn = 262
quantidade_digitos = contar_digitos(nn)
print(f"O número {nn} tem {quantidade_digitos} dígitos.")
