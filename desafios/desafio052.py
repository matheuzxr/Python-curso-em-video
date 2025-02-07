num = int(input('Digite um número: '))
divisores = 0
print(f'Divisores de {num}: ')
for i in range(1, num+1):
    if num % i == 0:
        divisores += 1
        print(i, end=' ')
if divisores == 2:
    print(f'\n{num} é um número primo')
else:
    print(f'\n{num} não é primo. Ele possui {divisores} divisores.')
