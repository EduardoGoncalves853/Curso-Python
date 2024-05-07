import math

num1 = 9
num2 = 2
# arithmetic

print(f"num  + num2  = {num1 + num2}")
print(f"num1 - num2  = {num1 - num2}")
print(f"num1 * num2  = {num1 * num2}")
print(f"num1 / num2  = {num1 / num2}")
print(f"num1 ** num2 = {num1 ** num2}")
print(f"num1 % num2  = {num1 % num2}")

print(pow(num1, num2))
print(round(num1, num2))
print(math.ceil(1.1))
print(math.floor(1.9))

# assignment
num = 2
num = num + 3
print(f"num agora é igual a {num}")
num += 1
num -= 1
num *= 1
num /= 1
num **= 1
num %= 1
print(num)

# comparison

print(2 == 2)
print(2 != 2)
print(3 > 2)
print(3 < 2)
print(2 <= 3)
print(3 >= 3)

# Logical

#? and
print(True and True) #* V
print(True and False) #* F
print(False and True) #* F
print(False and False) #* F
#? or
print(True or True) #* V
print(True or False) #* V
print(False or True) #* V
print(False or False) #* F
#? not
print(not True)
print(not False)
#? and
print(2 == 2 and 3 == 3)
print(2 != 2 and 3 != 3)
print(2 != 2 and 3 == 3)
#? or
print(2 != 2 or 3 == 3)
print(2 != 2 or 3 != 3)