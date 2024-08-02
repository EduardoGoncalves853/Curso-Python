

# Algoritmo para gerar números na sequência de fibonacci
n = 
array = [1,1]

while n - 2 > 0:
    array.append(array[-1] + array[-2])
    n -= 1

print(array)
print(sum(array))
#_________________________

