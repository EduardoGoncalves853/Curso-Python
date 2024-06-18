def countAlg():
    vm = int(1896)
    razao = int(2)
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

# _______________________
#        2 have 106
#        3 have 1107
#        4 have 11096
#        5 have 111085
#        6 have 1111086
#        7 have 11111086
#        8 have 111111056
#        9 have 1111111101

# _______________________
#       98 have 94
#      998 have 1444
#     9998 have 19444
#    99998 have 244444
#   999998 have 2944444
#  9999998 have 34444444
# 99999998 have 394444444

# 1456
# 458

# 3 + 1/4
# 1 + 1/56 + 1/224




