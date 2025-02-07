valor = int(input('Informe o valor que deseja sacar: '))
nota50 = valor // 50
resto = valor - (50 * nota50)
nota20 = resto // 20
resto = resto - (20 * nota20)
nota10 = resto // 10
resto = resto - (10 * nota10)
nota1 = resto
print(f'Valor a sacar: R${valor:.2f} \nNotas de 50: {nota50} \nNotas de 20: {nota20} \nNotas de 10: {nota10} \nNotas de 1: {nota1}')
