   # programa para escolher opções ↓
waiting_menu = False
def opções():
    while True:
        if waiting_menu:
            input("\n Pressione Enter para continuar...")
        print("\033c", end="") # terminal clear
        waiting_menu = True
        print('''
    === Automated Teller Machine ===
        [1] Ver extrato
        [2] Fazer o depósito
        [3] fazer saque
        [4] sair
    =================================
    ''')
        extract = 10000
        saldo = 3548.9
        option = input('Escolha uma opção: ')
        
        if option != int:
            print("Por favor, digite apenas inteiros")
            opções()

        else:
            if option == 1:
                print(f'''
                    Você tem {extract} R$ de extrato
                    transitados na conta nesse mês
                    ''')
            elif option == 2:
                saque = float(input("digite o quanto quer sacar: "))
                saldo -= saque # Subtrai saque de saldo
                print(f'''
                    Voçê sacou {saque} R$
                    Voçê tem em seu saldo {saldo} R$
                    ''')
            elif option == 3:

                deposit = float(input("digite o quanto quer depositar: "))
                saldo += deposit # Adiciona o deposito ao saldo
                print(f'''
                    Voçê depositou {deposit} R$
                    Voçê tem em seu saldo {saldo} R$
                    ''')

            elif option == 4:
                print("Programa encerrado.")
                break

    return print("Opção inválida")
          