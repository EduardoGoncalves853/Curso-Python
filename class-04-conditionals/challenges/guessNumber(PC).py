

# Adivinhe o Número (Computador):
# O computador escolhe um número aleatório e o usuário tenta adivinhar qual é. O programa deve fornecer dicas se o palpite do usuário for muito alto ou muito baixo.

import math, random

print('''  
      Vamos jogar um jogo, a máquina escolhe um
      número aleatório de 0 á 10 e voçê tem que
      adivinhar.

      Voçê tem 5 tentativas

      Não se preocupe jogador! caso voçê erre, o computador irá te dar dicas sobre o número!
      ''')

# Atribuição das variáveis
n = math.ceil(random.random()) * 10
tentativas = 5

# Primeira tentativa do player
player = int(input("Digite seu número inteiro não nulo, se for capaz... muahahahaha: "))

# Verificações
if player == n:
      print(f'''
             O Player acertou o número!

            impossível que eu fui derrotado de primeeeiiiraaaa!!!
            Resposta : {print(f'{n:.0f}')}
            ''')
else:
      tentativas -= 1
      print(f"Voçê tem {tentativas} tentativas")


# Verificação while
while player != n or tentativas != 0:
      if player == n:
            print(f'''
                  O Player acertou o número!

                  Nãaaaaaaao eu fui derrotadoooo!!!
                  Resposta : {print(f'{n:.0f}')}
                  ''')
      elif player > n:
            print('''
                  número maior que n

                  Talvez na próxima...voçê acerte! muahahaahahah
                  ''')
      elif player < n:
            print('''
                  número menor que n
                  
                  Não tão fácil assim usuário...
                  ''')
      else:

            print('''
                  Por favor digite um número inteiro não nulo
                  
                  i alá cara tá tentando roubar num jogo de terminal kkkkk muito burro
                  ''')
            
      print(f'Número de tentativas: {tentativas}')
      tentativas -= 1
      if tentativas == 0:
            print("Voçê perdeu o jogo!! agora pague com sua alma kkkkkk")
            exit()
            
      player = int(input("Digite seu número inteiro não nulo, de novo: "))

    
