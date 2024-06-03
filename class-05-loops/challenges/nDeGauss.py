from functools import reduce
n = 30

def Gauss(n):
    sum = 0

    while n > 0:
        sum += n
        n -= 1
    return sum
print(Gauss(n))

#* Processo array

array = []

for i in range(1, n + 1):
    array.append(Gauss(i))

print(array)


