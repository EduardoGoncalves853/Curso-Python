
def my_Sum(num1, num2):
  max = num1 + num2
  return {
    "result": max,
    "num1": num1,
    "num2": num2
    }

print(f'''
 num1 + num2 = total
 {my_Sum(2, 6)["num1"]} + {my_Sum(2, 6)["num2"]} = {my_Sum(2, 6)}
''')

#______________________________

def my_Sub(num1, num2):
  min = num1 - num2
  return {
    "result": min,
    "num1": num1,
    "num2": num2
  }

print(f'''
 {my_Sub(8, 2)["num1"]} - {my_Sub(8, 2)["num1"]} = {my_Sub(8, 2)}
      ''')
#______________________________

def my_Sub(num1, num2, min):
  min = num1 - num2
  return [min, num1, num2]

print(f'''
 {my_Sub(8, 2)[0]} - {my_Sub(8, 2)[1]} = {my_Sub(8, 2)}
      ''')

#______________________________

def calc_avg(grade1, grade2):
  avg = (grade1 + grade2) / 2
  return avg

print(calc_avg(5.5, 8))

#______________________________
