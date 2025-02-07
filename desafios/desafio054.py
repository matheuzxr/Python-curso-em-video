maiores = 0
menores = 0
for i in range(0, 7):
    idade = int(input('Digite a idade: '))
    if idade >= 18:
        maiores = maiores + 1
    else:
        menores = menores + 1
print(f'Maiores de idade: {maiores} \nMenores de idade: {menores}')
