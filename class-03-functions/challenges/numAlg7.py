# Fórmula
#* n => td => d1
#* a => a * x = ax
#* d = d1 + ax

import math

n = 681
m = 3

def find_td(n, m):
    td = 10 ** (round(math.log10(n)) - 1)
    while td % m != 0:
        td -= 1
    return td

d1 = find_td(n, m)

def count_d1(m, d1):
    multiplos = list(range(m, d1, m))  
    multiplos_str = ''.join(str(m1) for m1 in multiplos)
    return [len(multiplos_str), multiplos]

algCheck = count_d1(m, d1)[0]

a = n - (d1 - m)
def count_Alg(n):
    return len(str(n))

print (f"(n - td = a) a = {a}")
print (f"(td => d1) d1 = {d1}")
print (f"BruteForce = {algCheck}")
print (f"nd = {count_Alg(n)}")


x = count_Alg(n) / m
Form_D = count_d1(m, d1)[0] + (a * x)
print(f"The number of digits in the number {n} to multiple {m} is {Form_D}")