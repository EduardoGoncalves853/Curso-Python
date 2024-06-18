# Fórmula
#* n => td => d1
#* a => a * x = ax
#* d = d1 + ax

import math

n = 1100
m = 2
array = []

# Olha se (d1) é divisor de (m) ↓
if n % m != 0:
  print("the number (n) have to be multiple of (m)")
  exit()

# Digits in (td)
def find_td(n, m):
    td = 10 ** math.floor(math.log10(n))-1 
    while td % m != 0:
        td -= 1
    return td
d1 = find_td(n, m)

# Conta os dígitos de td 
def countDigitsTd(d1, m):
    valor_maximo = d1 - (d1 % m)
    multiplos = [i for i in range(m, valor_maximo + 1, m)]
    multiplos_str = ''.join(str(multiplo) for multiplo in multiplos)
    return [valor_maximo, multiplos_str]
tdDigits = len(countDigitsTd(d1, m)[1])

#* (nd) número de dígitos
# Para (nd) ↓
def count_Alg(n):
    return len(str(n))

for i in array:
    dig = count_Alg(array[0])
    while dig != 2:
        array.append(find_td(array[i]))
        dig -= 1

# Adquirimos o (a)
a = n - d1

# Para ax ↓
ax = math.floor(a * count_Alg(n) / m)

# E por fim adquirimos (d) ↓
d = (ax + tdDigits)

# Formula ↓
print(f'''
    {n} => {d1} => {tdDigits}
    {a} * {count_Alg(n)}/{m} = {ax}
    {d} = {ax} + {tdDigits}
''')
