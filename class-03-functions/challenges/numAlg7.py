# Fórmula
#* n => td => d1
#* a => a * x = ax
#* d = d1 + ax

import math

n = 998
m = 2

# Digits in (td)
def find_td(n, m):
    td = 10 ** math.floor(math.log10(n))-1 
    while td % m != 0:
        td -= 1
    return td

d1 = find_td(n, m)

# Adquirimos o (a)
a = n - d1

# Olha se (d1) é divisor de (m) ↓
if d1 % m != 0:
  print("the number (n) have to be multiple of (m)")
  exit()

def alg2dig(d1,m):

    if m <=9 and m >= 5:
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
        print("Only type numbers between 1 and 9 !!")
        exit()

# 2 dígitos
dig2 = alg2dig(d1,m)

# Para (nd) ↓
def count_Alg(n):
    return len(str(n))

x = count_Alg(n) / m
ax = a * x

# E por fim adquirimos (d) ↓
d = math.ceil(ax + dig2)

# Formula ↓
print(f'''
    {n} => {d1} => {dig2}
    {a} * {x} = {ax}
    {d} = {ax} + {dig2}
''')
