# Crie um programa que receba duas notas do aluno
firstGrade = float(input("Digite a 1º nota: "))
SecGrade = float(input("Digite a 2º nota: "))

# Faça uma função que calcule a sua média
def calc_avg(firstGrade, SecGrade):
    return (firstGrade + SecGrade) / 2

avg = round(calc_avg(firstGrade, SecGrade), 1)
# Apresente na tela se o aluno foi aprovado (média = 7)
try:
    
 if avg >= 7:
   print(f"aprovado com {avg}")
 else:
   print(f"reprovado com {avg}")
except ValueError:
  print("Valor indefinido")
except:
  print("Erro na operação")
   