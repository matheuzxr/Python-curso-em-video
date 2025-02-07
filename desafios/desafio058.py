from random import randint
pc = randint(0, 100)
user = int(input('Advinhe o número de 0 a 100 que estou pensando: '))
tentativas = 1
acertou = False
while not acertou:
    if pc == user:
        acertou = True
    else:
        if pc > user:
            print('Incorreto! O valor é MAIOR.')
        else:
            print('Incorreto! O valor é MENOR.')
        user = int(input('Tente novamente: '))
        tentativas += 1
print(f'Parabéns, você acertou com {tentativas} tentativas!')
