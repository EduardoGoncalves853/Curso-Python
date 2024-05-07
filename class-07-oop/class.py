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
   if Random >= 0.96:
        return Car('Toyota', 'Corolla', '2020', 'R$ 380.000,00', '345.000 km')
   elif Random >= 0.88:
        return Car('Honda', 'Civic', '2020', 'R$ 400.000,00', '320.000 km')
   elif Random >= 0.80:
        return Car('Ford', 'Focus', '2020', 'R$ 370.000,00', '350.000 km')
   elif Random >= 0.72:
        return Car('Chevrolet', 'Cruze', '2020', 'R$ 390.000,00', '330.000 km')
   elif Random >= 0.64:
        return Car('Nissan', 'Sentra', '2020', 'R$ 375.000,00', '340.000 km')
   elif Random >= 0.56:
        return Car('Volkswagen', 'Jetta', '2020', 'R$ 395.000,00', '325.000 km')
   elif Random >= 0.45:
        return Car('Hyundai', 'Elantra', '2020', 'R$ 385.000,00', '335.000 km')
   elif Random >= 0.40:
        return Car('Renault', 'Megane', '2020', 'R$ 365.000,00', '355.000 km')
   elif Random >= 0.32:
        return Car('Peugeot', '308', '2020', 'R$ 410.000,00', '315.000 km')
   elif Random >= 0.24:
        return Car('Kia', 'Cerato', '2020', 'R$ 400.000,00', '320.000 km')
   elif Random >= 0.16:
        return Car('Toyota', 'Corolla','2020', "380000", "345000")
   elif Random >= 0.08:
        return Car('Chevrolet', 'Celta', '2006', '20000', '15600')
   else:
    return Car('Toyota', 'Corolla', '2020', 'R$ 380.000,00', '345.000 km')
    

# Acelerando o carro
RandomCar().acelerar()
# Freando o carro
RandomCar().frear()
# Acabando o carro
RandomCar().esbagacando()

# ↓ Informações de venda e mecânica do carro 
print(RandomCar().info())
print(RandomCar().sale())
