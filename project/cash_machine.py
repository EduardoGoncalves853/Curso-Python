
class Bank_account:
    def __init__(self, balance = 0):
        self.__balance = balance
        self.__file = "project/files/transactions.txt"

    def deposit(self, amount):
        self.__balance += amount

        try:
            with open(self.__file, "a") as file:
                file.write(f"deposito (+), {amount}\n")
        except:
            print("Algo deu errado em abrir o arquivo!")
            pass


account = Bank_account()
waiting_menu = False
while True:
    if waiting_menu == True:
        input("\n Pressione Enter para continuar...")

    print("\033c", end="") # terminal clear
    waiting_menu = True
    print(
    '''
 === Automated Teller Machine ===
      [1] Ver extrato
      [2] Fazer o depósito
      [3] fazer saque
      [4] sair
=================================
    ''')

    option = input("\nEscolha uma opção ")
     
    if option == "1":
        print("Extrato")

    elif option == "2":
        amount = float(input("digite o quanto quer depositar: "))
        account.deposit(amount)

        print("Depósito")  
    elif option == "3":
        print("Saque")

    elif option == "4":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida")