n = int(input('Digite um número inteiro qualquer: '))
b = int(input('Para qual base você deseja converter?' +
              '\n0 para binário' +
              '\n1 para octal' +
              '\n2 para hexadecimal: '))
if b == 0:
    bin = bin(n)[2:]
    print(f'{n} em binário: {bin}')
elif b == 1:
    oct = oct(n)[2:]
    print(f'{n} em octal: {oct}')
elif b == 2:
    hex = hex(n).upper()[2:]
    print(f'{n} em hexadecimal: {hex}')
else:
    print('Tente novamente.')
