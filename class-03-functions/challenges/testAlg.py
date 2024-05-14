# código para nd Igual a 2

import math

n = 27
m = 9

if n % m != 0:
  print("the number (n) have to be multiple of (m)")
  exit()

def alg2dig(n,m):

    if m <=9 and m >= 5:
        return n/m + ((n/m) - 1)
    elif m == 4:
        return n/m + ((n/m) - 2)
    elif m == 3:
        return n/m + ((n/m) - 3)
    elif m == 2:
        return n/m + ((n/m) - 4)
    elif m == 1:
        return n/m + ((n/m) - 9)
    
    else:
        print("Only type numbers between 1 and 9 !!")
        exit()

print(f"The number of digits in the number {n} to multiple {m} is {alg2dig(n,m)}")