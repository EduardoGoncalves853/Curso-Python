
# Meu código ↓

def countAlg():
    valor_maximo = int(10)
    razao = int(2)
    multiplos = [i for i in range(razao, valor_maximo + 1, razao)]
    multiplos_str = ''.join(str(multiplo) for multiplo in multiplos)
    return [valor_maximo, multiplos_str, razao]

algCheck = countAlg()
between = algCheck[0] / algCheck[2]
multiplos_in_valor_maximo = len(algCheck[1])
print(f"{algCheck[0]} have {multiplos_in_valor_maximo} digits among the multiples of {algCheck[2]}")
print(f"[{algCheck[2]}...{between:.0f}...{multiplos_in_valor_maximo}]")