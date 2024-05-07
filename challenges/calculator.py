# Capture dois números do usuario
# Faça as operações de (+, -, *, /) e atribua a variáveis semânticas
# Imprima na tela o valor das variáveis com suas operações

num1 = float(input("digite um número: "))
num2 = float(input("digite o próximo: "))
#__________________
sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
#__________________
print(f'''
 {num1} + {num2} = {sum}
 {num1} - {num2} = {sub}
 {num1} * {num2} = {mul}
 {num1} / {num2} = {div}
''')
#__________________

