
# An precisa ser ínpar
#gauss
# Sn = ((A1 + An)N)/2
# 1 + 3 + 5 + 7 + 9

An = 7
A1 = 1
N = (An + 1)/2

def Gauss(An,A1):
  return ((A1 + An)*N)/2

print(Gauss(An,A1))




