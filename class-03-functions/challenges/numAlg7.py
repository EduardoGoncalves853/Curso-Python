# Fórmula
#* n => td => d1
#* a => a * x = ax
#* d = d1 + ax

import math

n = 7
m = 2

# Olha se (d1) é divisor de (m) ↓
if n % m != 0:
  print("the number (n) have to be multiple of (m)")
  exit()

#* Para (td) e (a)

# Digits in (td)
def find_td(n, m):
    td = 10 ** math.floor(math.log10(n))-1 
    while td % m != 0:
        td -= 1
    return td
d1 = find_td(n, m)

# Adquirimos o (a)
a = n - d1

# Quando o número for 2 dígitos
def alg2dig(d1,m):

    if d1 == 0:
        return d1 + (d1 * -1)
    elif m <=9 and m >= 5:
        return d1/m + ((d1/m) - 1)
    elif m == 4:
        return d1/m + ((d1/m) - 2)
    elif m == 3:
        return d1/m + ((d1/m) - 3)
    elif m == 2:
        return d1/m + ((d1/m) - 4)
    elif m == 1:
        return d1/m + ((d1/m) - 9)
    
    else:
        return print("Only type numbers between 1 and 9 !!")
    
#* (nd) número de dígitos
# Para (nd) ↓
def count_Alg(n):
    return len(str(n))

# Para ax ↓
ax = math.floor(a * count_Alg(n) / m)

# E por fim adquirimos (d) ↓
d = (ax + alg2dig(d1, m))

# Formula ↓
print(f'''
    {n} => {d1} => {alg2dig(d1, m)}
    {a} * {ax} = {ax}
    {d} = {ax} + {alg2dig(d1, m)}
''')
