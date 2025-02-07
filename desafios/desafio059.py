num1 = int(input('Entre o primeiro valor: '))
num2 = int(input('Agora o segundo: '))
print('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa')
menu = 0
while menu != 5:
    menu = int(input('Selecione uma opção do menu: '))
    if menu == 1:
        print(f'{num1} + {num2} = {num1 + num2}')
    elif menu == 2:
        print(f'{num1} x {num2} = {num1 * num2}')
    elif menu == 3:
        diferenca = num1 - num2
        if diferenca > 0:
            print(f'{num1} é maior que {num2}')
        elif diferenca < 0:
            print(f'{num2} é maior que {num1}')
        else:
            print('As duas entradas de valores são iguais.')
    elif menu == 4:
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo: '))
    else:
        continue
print('Fim.')