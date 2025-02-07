tupla = (int(input('Digite um número: ')), int(input('Outro: ')), int(input('Mais um: ')), int(input('Último: ')))
print(f'O número 9 foi digitado {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O número 3 aparece pela primeira vez na {tupla.index(3) + 1}º posição.')
print('Os números pares digitados foram: ', end='')
for i in tupla:
    if i % 2 == 0:
        print(i, end=' ')
