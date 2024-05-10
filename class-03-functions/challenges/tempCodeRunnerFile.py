nn = 262
td = str(nn),''.join(str(n) for n in nn)
print(td)

# 98 => d1
# 2 * 49
# 49 + 45 = 94

#* 262 => 98 => 94
#* 164 => 164 * 1.5 = 246
#* 340 = 94 + 246

nn = 262
m = 2
# 56900
# 9994
# 4 * 10 
# 4 * 100 / 2

def CalcAlg(nn,m):
    nd = contar_digitos(nn)
    td = (contar_digitos(nn) - 1) * 100 / m
    a = td 
    x = nd / m
    ax = a * x
    d = d1 + ax

print(CalcAlg(262, 2))

#! important
def contar_digitos(numero):
    numero_str = str(numero)
    return len(numero_str)

nn = 262
quantidade_digitos = contar_digitos(nn)
print(f"O número {nn} tem {quantidade_digitos} dígitos.")