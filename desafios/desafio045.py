from random import randint
print('=*' *15, 'JOKENPO ', '=*' *15)
print('1 - Pedra',
      '\t2 - Papel',
      '\t3 - Tesoura')
user = int(input('Jogue: '))
if user == 1 or user == 2 or user == 3:
    comp = randint(1, 3)
    print('Computador: {}' .format(comp))
    if user == 1 and comp == 2:
        print('VOCÊ PERDEU!')
    elif user == 1 and comp == 3:
        print('VOCÊ VENCEU!')
    elif user == 2 and comp == 1:
        print('VOCE VENCEU!')
    elif user == 2 and comp == 3:
        print('VOCÊ PERDEU!')
    if user == 3 and comp == 1:
        print('VOCÊ PERDEU!')
    if user == 3 and comp == 2:
        print('VOCE VENCEU!')
    else:
        print('Empate. Jogue novamente!')
else:
    print('Jogada inválida. Tente novamente.')
