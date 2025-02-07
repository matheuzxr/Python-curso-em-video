p = float(input('Informe seu peso (kg): '))
a = float(input('Informe a sua altura (m): '))
imc = p / a ** 2
print(f'{imc:.2f}')
if imc < 18.5:
    print('Abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Peso ideal.')
elif 25 <= imc < 30:
    print('Sobrepeso.')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida.')
