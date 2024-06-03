
# Algoritmo para gerar números na sequência de fibonacci
num = 10

array = [1,1]

while (num - 2) > 0:
    array.append(array[-1] + array[-2])
    num -= 1

print(array)