adultos = homens = m20 = cont = 0
while True:
    idade = int(input(f'Idade da pessoa {cont}: '))
    sexo = ''
    while sexo not in ['M', 'F']:
        sexo = input(f'Sexo da pessoa {cont} [M/F]: ').upper()
    cont += 1
    if idade >= 18:
        adultos += 1
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        m20 += 1
    prosseguir = ''
    while prosseguir not in ['S', 'N']:
        prosseguir = input('Deseja cadastrar mais pessoas? [S/N]: ').upper()
    if prosseguir == 'N':
        break
print(f'Total de cadastrados: {cont} \nAdultos: {adultos} \nHomens: {homens} \nMulheres com menos de 20 anos: {m20}')
    