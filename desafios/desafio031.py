d = float(input('De quantos km será a viagem? '))
if d <= 200:
    passagem = d * 0.5
    print(f'A passagem custará R${passagem:.2f}')
else:
    passagem = d * 0.45
    print(f'A passagem custará R${passagem:.2f}')
