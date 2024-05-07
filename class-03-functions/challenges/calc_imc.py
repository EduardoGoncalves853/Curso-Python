#  crie uma função que receba como parâmetros altura e peso e retorne o IMC
#  IMC = peso/(altura x altura)

peso = float(80.4)
altura = float(170)

def calc_imc(peso, altura):
    if altura > 5:
     imc = peso / ((altura * altura)/ 10000)
    else: 
     imc = peso / (altura * altura)
    return imc

print(f"{calc_imc(peso, altura):0.2f}kg/m²")