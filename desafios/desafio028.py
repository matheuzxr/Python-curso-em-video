from random import randint
import time
user = int(input('Tente advinhar um número de 0 a 5: '))
pc = randint(0, 5)
print('PROCESSANDO...')
time.sleep(3)
if user == pc:
    print('Parabéns! Vc acertou!')
else:
    print(f'Vc errou! O número correto era {pc}')
