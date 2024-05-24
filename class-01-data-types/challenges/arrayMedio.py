
#? Nivél Médio

#? Array de Quadrados
# Escreva uma função que receba um array de números e retorne um novo array contendo os quadrados de cada número.

n = [23, 1, 17, 14, 3, 29, 6, 12, 19, 7, 25, 16, 11, 28, 10, 5, 8, 18]
print(n)

n_sort = sorted(n)
print(n_sort)

nc = []
for i in n:
    j = i ** 2
    nc.append(j)
nc.sort()      
print(nc)
nc.pop()

#? Remover Duplicatas
# Escreva uma função que receba um array e retorne um novo array sem elementos duplicados.


