import math
from functools import reduce

n = 9998
m = 2
div = n / m

def find_td(n, m):
    array= [n]
    count = len(str(array[0]))

    while count != 1:
        last_Array = 10 ** math.floor(math.log10(array[-1]))-1

        while last_Array % m != 0:
            last_Array -= 1 
        
        array.append(last_Array)
        count -= 1

    return array

array = find_td(n,m)


def alg_calc(array):
    al = []
    for i in array:
       al.append((i - 10 ** (len(str(i))) - 1) len(str(i)))

    return al


print(find_td(n, m))
print(alg_calc(array))