import random

# OOP
# Programação Orientada a Objetos

class Car:
    # Informações do carro ↓
    def __init__(self, brand, model, year, offer, fipe):
        self.brand = brand
        self.model = model
        self.year = year
        self.offer = offer
        self.fipe = fipe
    
    def info(self):
       return (self.brand, self.model, self.year)
    
    def sale(self):
       if self.offer >= self.fipe:
          print("Carro vendido!")
       else:
          print("Sai daí fi de chiquim!")

    # Funções do carro ↓
    def acelerar(self):
        print("                                            ")
        print(f'O {self.brand} {self.model} está acelerando.')

    def frear(self):
        print(f'O {self.brand} {self.model} está freando.')
    
    def esbagacando(self):
        print(f'O {self.brand} {self.model} está só a capa do batman\n')

# Seleciona um carro aleatório para o print
def RandomCar():
   Random = random.random()
   if Random >= 0.5:
    my_Car1 = Car('Toyota', 'Corolla','2020', "380000", "345000")
    return my_Car1
   else:
    my_Car2 = Car('Chevrolet', 'Celta', '2006', '20000', '15600')
    return my_Car2

# Acelerando o carro
RandomCar().acelerar()
# Freando o carro
RandomCar().frear()
# Acabando o carro
RandomCar().esbagacando()

# ↓ Informações de venda e mecânica do carro 
print(RandomCar().info())
print(RandomCar().sale())
