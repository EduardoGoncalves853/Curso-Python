
# código time ↓
import time

# Meu código ↓
start_time = time.time()

def countAlg():
    valor_maximo = int(99998)
    razao = int(2)
    multiplos = [i for i in range(razao, valor_maximo + 1, razao)]
    multiplos_str = ''.join(str(multiplo) for multiplo in multiplos)
    return [valor_maximo, multiplos_str, razao]
algCheck = countAlg()
# 31, 62, 93, 124
print("--- %s seconds ---" % (time.time() - start_time))

print(f"{algCheck[0]} tem {len(algCheck[1])} dígitos dentre os múltiplos de {algCheck[2]}")