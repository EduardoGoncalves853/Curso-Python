import math

n = 200000000
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

# atribui td ao array
array.append(d1)

find_td(array[0], m)

for i in range(len(array)):
    dig = len(str(array[0]))
    
    while dig != 2:
        array.append(find_td(array[-1], m))
        dig -= 1
print(array)
