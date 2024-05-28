

# Faça um programa
# que leia  5 valores númericos
valores = []
for i in range(1,6):
    valores.append(int(input(f"Digite o {i}º valor: ")))

# e guarde-os em uma lista
# No final mostre qual foi o menor e a maior
# valor digitado e as suas respectivas posições na lista

menor_valor = min(valores)
maior_valor = max(valores)

print(f"O maior valor: {maior_valor} e seu índex {valores.index(maior_valor)}")
print(f"O menor valor: {menor_valor} e seu índex {valores.index(menor_valor)}")
