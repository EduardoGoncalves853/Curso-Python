
import math
# Para achar td ↓
n = 368
m = 2
l = 10**(round(math.log10(n)))- 1

td = l
while td % m != 0:
    td -= 1
print(td)

# Fórmula
#* n => td => d1
#* a => a * x = ax
#* d = d1 + ax


# def calcAlg(n,td):
#     n = td 

#     return n
