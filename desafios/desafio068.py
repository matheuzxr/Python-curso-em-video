from random import randint
cont = 0
while True:
    user = int(input('Jogue um número (0 a 100): '))
    opcao = ''
    while opcao != 'P' and opcao != 'I':
        opcao = input('Par ou Ímpar? [P/I]: ').upper()
    pc = randint(0, 100)
    soma = user + pc
    resultado = 'PAR' if soma % 2 == 0 else 'ÍMPAR'
    if opcao == 'P' and resultado == 'PAR' or opcao == 'I' and resultado == 'ÍMPAR':
        print(f'Você ganhou! Você jogou {user} e eu {pc}, somando {soma}. Vamos de novo!')
        cont += 1
    else:
        break
print(f'Você perdeu! Seu total de vitórias foi {cont}')
