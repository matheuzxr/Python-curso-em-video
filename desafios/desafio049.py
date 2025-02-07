n = int(input('Digite um número: '))
print(f'Tabuada do {n}')
for i in range(1, 11):
    print('{} x {:>2} = {}'.format(n, i, n*i))