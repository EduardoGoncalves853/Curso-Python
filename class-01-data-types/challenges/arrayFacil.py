

#? Nível Fácil

#? Somar Elementos do Array
# Escreva uma função que receba um array de números e retorne a soma de todos os elementos.

n = [5,8,3,6]
print(sum(n))

#? Elemento Máximo
# Escreva uma função que receba um array de números e retorne o maior elemento.

n = [5,8,3,6]
print(max(n))

#? Elemento Mínimo
# Escreva uma função que receba um array de números e retorne o menor elemento.

n = [5,8,3,6]
print(min(n))

#? Contar Elementos
# Escreva uma função que receba um array e retorne o número de elementos no array.

n = [5,8,3,6]
#* Usando Funções
print(len(n))

#* Usando for loop
count = 0
for i in n:
    count +=1
print(count)

#? Inverter Array
# Escreva uma função que receba um array e retorne o array invertido

n = [5,8,3,6]
n.sort(reverse=True)
print(n)

