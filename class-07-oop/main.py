
# Abstraction ↓
class User: 
    def __init__(self, name, cpf):
        self.name = name
        self.__cpf = cpf # ← encapsulation

    def get_cpf(self):
        return self.__cpf
    
    def info(self):
        return (self.name, self.__cpf)

user = User("Francisco", "000.000.000-00")

print(user.name)
# user.cpf = "xxxx"
# print(user._cpf)
print(user.info())

# inheritance 
class Admin(User):
    def __init__(self, name, cpf):
        super().__init__(name, cpf)
        self.__status = "admin"

    def set_status(self, status):
        self.__status = status

    def get_status(self):
       return self.__status

    def info(self):
       return (self.name, self.get_cpf(), self.__status)
    
admin = Admin("Eduardo", "265.736.837-37")
print(admin.name)

# adquiri os dados ↓
print(admin.get_status())

# define/transforma os dados ↓
admin.set_status("gold")
print(admin.get_status())

# printa o conjunto dos dados ↓
print(admin.info())