
# Algoritmo para calcular o
# número de algarismos multiplos
# de algum número

#*  m = múltiplo
#*  n = Valor inicial
#*  d = dígitos

#? Para 2 dígitos (m) de 2
# n => 46 = 23 + 19
#* d = 42 dígitos


#? Para 3 dígitos (m) de 2
#  n => 998 => 98 => 94d 
#  a => 900 * 1.5  => 1.350d
#* d = 1.444 dígitos

#? Para 4 dígitos (m) de 2
#  n => 4004 => 998 => 1.444d
#  a => 3006 * 2 => 6012d
#* d = 7.456 dígitos

#? para 5 dígitos (m) de 2
#  n => 12456 => 9998 => 19.444d
#  a => 2458 * 2.5 => 6.145d
#* d = 25.589 dígitos

#? para 6 dígitos (m) de 2
#  n => 111.112 => 99998 => 244.444
#  a => 11114 * 3 => 33.342d
#* d = 277.786 dígitos

valor_maximo = int(999998)
razao = int(2)

multiplos = [i for i in range(razao, valor_maximo + 1, razao)]

multiplos_str = ''.join(str(multiplo) for multiplo in multiplos)

print(multiplos_str)
print("_____________________________")
print(f"{valor_maximo} tem {len(multiplos_str)} dígitos dentre os múltiplos de {razao}")

# 1000