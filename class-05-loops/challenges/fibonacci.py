

# Algoritmo para gerar números na sequência de fibonacci
array = [1,1]
n = 7

while n - 2 > 0:
    array.append(array[-1] + array[-2])
    n -= 1

print(array)
#_________________________

