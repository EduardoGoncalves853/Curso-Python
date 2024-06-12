def countAlg():
    vm = int(11111086)
    razao = int(7)
    valor_maximo = vm - (vm % razao)
    multiplos = [i for i in range(razao, valor_maximo + 1, razao)]
    multiplos_str = ''.join(str(multiplo) for multiplo in multiplos)
    return [valor_maximo, multiplos_str, razao]


algCheck = countAlg()
multiplos_in_valor_maximo = len(algCheck[1])
between = algCheck[0] / algCheck[2]

v1 = (multiplos_in_valor_maximo - algCheck[0] * algCheck[2])

v2 = algCheck[0] - v1

if(v2 % algCheck[2] != 0):
    v3 = False
else:
    v3 = True

print(f'''
 {algCheck[0]} have {multiplos_in_valor_maximo}
 digits among the multiples of {algCheck[2]}
 and {v1} , {v2} and {v3}
''')

# _________________
# 2 => 106
# 3 => 1107
# 4 => 11096
# 5 => 111085
# 6 => 1111086
# 7 => 11111086
# 8 => 111111056
# 9 => 1111111101

