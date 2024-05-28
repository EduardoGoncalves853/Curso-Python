
#? Exercício Python: 
# Faça um programa que leia 5 valores numéricos
# e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
# valor digitado e as suas respectivas posições na lista. 


listaNum = []
mai = 0
men = 0

# ler 5 valores numéricos
for c in range(0,5):
    # guarde-os em uma lista
    listaNum.append(int(input(f"Digite um valor para a posição {c}: ")))
    # verifica na primeira verificação 
    # que o menor e maior valor são iguais
    if c == 0:
        mai = men = listaNum[c]
    else:
        # verifica se o número na posição c 
        # de listaNum é maior que a variavel mai
        if listaNum[c] > mai:
            mai = listaNum[c]
        # verifica se o número na posição c 
        # de listaNum é menor que a variavel men
        if listaNum[c] < men:
            men = listaNum[c]

print(f"Voçê digitou os valores {listaNum}")

print(f"O maior valor digitado foi {mai} nas posições ", end='')
for i, v in enumerate(listaNum):
    if listaNum[i] == mai:
        print(f"{i}...", end='')

print(f"O menor valor digitado foi {men} nas posições ", end='')
for i, v in enumerate(listaNum):
    if listaNum[i] == men:
        print(f"{i}...", end='')



