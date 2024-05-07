
n = 7

def fator(n):
  if n == 0 or n == 1:
   return 1
  else:   
   return n * fator(n - 1)
  
f = fator(n)
def formatar_numero(f):
    return '{:,}'.format(f).replace(',', '.')

print(f"seu {n}! e {formatar_numero(f)}")

# 2,4,6,8,10