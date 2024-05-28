# Faça um programa
# que leia 5 valores numéricos
valores = []

for i in range(1, 6):
    valor = int(input(f"Digite seu {i}º valor: "))
    valores.append(valor)

# e guarde-os em uma lista

# No final mostre qual foi o menor e a maior
# valor digitado e as suas respectivas posições na lista
menor = min(valores)
maior = max(valores)

print(f"O menor valor da lista é {menor} e sua posição é {valores.index(menor)}")
print(f"O maior valor da lista é {maior} e sua posição é {valores.index(maior)}")

    