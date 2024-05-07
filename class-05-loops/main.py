
from re import split


print("Start")

count = 0
while count < 1000:
  count += 1
  print(count)
print("End")

#__________________________
musigas = ["Time", "Bateu 20h", "Clocks", "Venina Veneno", "Morango do Nordeste"]

index_music = 0
while index_music < len(musigas):
  print(musigas[index_music])
  index_music += 1
#___________________________

musigas = ["Time", "Bateu 20h", "Clocks", "Venina Veneno", "Morango do Nordeste"]

for music in musigas:
  print(music)
#__________________________

#* array dentro de array?
letters = [
  ["A" ,"B", "C"],
  ["A" ,"B", "C"]
  ]
#* ↓ para cada array no conjunto
for array in letters:
#* ↓ agora iremos retirar uma letra do array
  for letter in array:
    print(letter)
#__________________________
d = 2
n = 40
divisores = [i for i in range(d, n) if n % i == 0 ]
print(divisores)

divisores_str = ''.join(map(str, divisores))
print(len(divisores_str))
