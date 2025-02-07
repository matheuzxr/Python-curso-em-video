from datetime import date
nasc = int(input('Informe o seu ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
if idade <= 9:
    print('Categoria MIRIM')
elif 9 < idade <= 14:
    print('Categoria INFANTIL')
elif 14 < idade <= 25:
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER')
