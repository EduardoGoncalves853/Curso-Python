age = 18

if age > 18:
   print("Maior de idade"),
else:
   print("menor de idade")

# _____________________________

age = 18
cnh = True
if age >= 18 and cnh:
   print("Pode fazer vrum vrum😎"),
else:
   print("Não pode fazer vrum vrum😔")

# _____________________________
age = 18

if age >= 18 and age <= 70:
   print("Voto obrigatório"),
elif age < 16:
   print("Não pode votar")
else:
   print("Voto facultativo")

#______________________________

try:
  print(2/"a")
except ZeroDivisionError:
  print("Não pode dividir por zero")
except TypeError:
  print("Formato inválido")
except:
  print("Error!")
finally:
  print("Fim da requisição")

print("Running")

   