a1 = int(input('Informe o primeiro termo da P. A.: '))
r = int(input('Informe a razão da P. A.: '))
an = 0
while an < 10:
    print(a1 + r * an, end=' - ')
    an += 1
print('fim')