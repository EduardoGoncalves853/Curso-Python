import math

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

# [9998, 998, 98, 8]
print(find_td(n, m))

