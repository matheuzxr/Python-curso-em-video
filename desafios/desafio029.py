v = float(input('Informe a velocidade do veículo: '))
if v > 80:
    multa = (v - 80) * 7
    print(f'Veículo multado. Valor da multa R${multa:.2f}')
else:
    print('Velocidade regular. Não há multa.')
