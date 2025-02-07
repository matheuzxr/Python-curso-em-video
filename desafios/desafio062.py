a1 = int(input('Informe o primeiro termo da P. A.: '))
r = int(input('Informe a razão da P. A.: '))
termo = a1
add = 10
while add != 0:
    an = 0
    while an < add:
        print(termo + r * an, end=' ')
        an += 1
    termo = termo + r * add
    add = int(input('Quantos outros termos da P. A. deseja visualizar? '))
print('Fim')
