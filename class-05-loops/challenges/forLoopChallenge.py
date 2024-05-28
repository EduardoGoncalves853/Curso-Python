
# Nível Iniciante:
# Contagem regressiva: Crie um programa que conte de 10 até 1 e, em seguida, exiba “Fogo!”.
import time

#* Primeira forma
for i in range(10, 0, -1):
    time.sleep(1)
    print(i)
    
time.sleep(1)
print("Fogo!!")

#* Segunda forma
i = 10
print(i)

#loop while
while i > 1:
    time.sleep(1)
    i -= 1
    print(i)

time.sleep(1)
print("Fogo!")

# Nível Intermediário:
# Soma dos primeiros N números: Peça ao usuário um número inteiro positivo N e calcule a soma dos prim

#* Primeira forma
n = 10
soma = 0
for i in range(1, n + 1):
    soma += i
print(soma)

#* Segunda Forma
n = 10
soma = 0

while n > 0:
    soma += n
    n -= 1
print(soma)

# Nível Difícil:
# Fatorial: Peça ao usuário um número inteiro não negativo n e calcule o fatorial desse número.

#* Primeira forma
from functools import reduce

n = list([5])
count = 1

for i in n:
    while count < n[0]:
        i -= 1
        n.append(i)
        count += 1

result = reduce(lambda x,y: x * y, n)
print(result)

#* Segunda Forma
n = 5
count = n

while count > 1:
    count -= 1
    n *= count
    print(n)

# # Nível Avançado:
# # Tabuada: Peça ao usuário um número inteiro e exiba a tabuada desse número de 1 a 10.

#* Primeira forma
n = 8
for i in range(1, 11):
    ar = n * i
    print(f'{n} * {i} = {ar}')
    
#* Segunda forma
n = 8
t = 10

while t >= 1:
    n1 = n * t
    print(f'{n} * {t} = {n1}')
    t -= 1



