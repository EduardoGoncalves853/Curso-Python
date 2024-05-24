# Fatoração
n = int(input("Digite o número que deseja fatorar: "))

def fator(n):
  if n == 0 or n == 1:
   return 1
  else:   
   return n * fator(n - 1)
  
# colocar pontos a cada 3 casas decimais
f = fator(n)
def formatar_numero(f):
    return '{:,}'.format(f).replace(',', '.')

print(f"{n}! é igual a : {formatar_numero(f)}")
