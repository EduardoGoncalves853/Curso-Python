# Nível Iniciante:
# Contagem regressiva: Crie um programa que conte de 10 até 1 e, em seguida, exiba “Fogo!”.

#* Primeira forma
for i in reversed(range(1 , 11)):
    print(i)
print("Fogo!!")

#* Segunda forma
for i in range(10, 0, -1):
    print(i)   
print("Fogo!")

# Nível Intermediário:
# Soma dos primeiros N números: Peça ao usuário um número inteiro positivo N e calcule a soma dos prim

n = 10
soma = 0
for i in range(1, n + 1):
    soma += i
print(soma)

# Nível Difícil:
# Fatorial: Peça ao usuário um número inteiro não negativo n e calcule o fatorial desse número.

#* Minha forma
i = int(input("Digite um número inteiro não negativo n para calcularmos seu fatorial"))
vezes = 1

for i in range(1, i + 1):
    vezes *= i
print(vezes)

# Nível Avançado:
# Tabuada: Peça ao usuário um número inteiro e exiba a tabuada desse número de 1 a 10.

#* Minha forma
times = 3
for i in range(0, 10):
    times * i
    i+=1
    timesX = times * i
    print(f"{times} * {i} = {timesX}")

# Nível Professor:
# Triângulo de Pascal: Crie um programa que gere as primeiras N linhas do Triângulo de Pascal.
#2
#4
#8
#16
#32

#Array

#input
input = 5
times = 0

while times != input:
    times += 1
    print(times)
print(times)




