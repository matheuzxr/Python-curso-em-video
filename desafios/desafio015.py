dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos quilômetros foram rodados com o carro? '))
preco = (dias * 60) + (km * 0.15)
print('Valor a pagar: R${:.2f}' .format(preco))
